import asyncio
import time
from solana.rpc.types import TokenAccountOpts
from solders.pubkey import Pubkey
from solana.rpc.commitment import Commitment, Confirmed, Finalized
from solana.rpc.api import RPCException
from solders.compute_budget import set_compute_unit_price, set_compute_unit_limit
from spl.token.instructions import create_associated_token_account, get_associated_token_address, close_account, CloseAccountParams
from raydium.utils.create_close_account import fetch_pool_keys, make_swap_instruction, sell_get_token_account
from spl.token.client import Token
from spl.token.core import _TokenCore
from spl.token.constants import WRAPPED_SOL_MINT
from solana.transaction import Transaction

LAMPORTS_PER_SOL = 1000000000
MAX_RETRIES = 5
RETRY_DELAY = 3

async def get_token_account(ctx, owner: Pubkey.from_string, mint: Pubkey.from_string):
    try:
        account_data = await ctx.get_token_accounts_by_owner(owner, TokenAccountOpts(mint))
        return account_data.value[0].pubkey, None
    except:
        swap_associated_token_address = get_associated_token_address(owner, mint)
        swap_token_account_Instructions = create_associated_token_account(owner, owner, mint)
        return swap_associated_token_address, swap_token_account_Instructions

async def buy(solana_client, async_solana_client, token, keypair, amount, compute_unit_price, compute_unit_limit, debug):
    retry_count = 0
    while retry_count < MAX_RETRIES:
        try:
            mint = Pubkey.from_string(token)
            pool_keys = fetch_pool_keys(str(mint))
            amount_in = int(amount * LAMPORTS_PER_SOL)
            accountProgramId = solana_client.get_account_info_json_parsed(mint)
            TOKEN_PROGRAM_ID = accountProgramId.value.owner

            balance_needed = Token.get_min_balance_rent_for_exempt_for_account(solana_client)
            swap_associated_token_address, swap_token_account_Instructions = await get_token_account(async_solana_client,keypair.pubkey(),mint)
            WSOL_token_account, swap_tx, keypair, Wsol_account_keyPair, opts, = _TokenCore._create_wrapped_native_account_args(
                TOKEN_PROGRAM_ID, keypair.pubkey(), keypair, amount_in,
                False, balance_needed, Commitment("confirmed"))

            if debug:
                print("Creating swap instructions...")
            instructions_swap = make_swap_instruction(amount_in,
                WSOL_token_account,
                swap_associated_token_address,
                pool_keys,
                mint,
                solana_client,
                keypair
            )
            params = CloseAccountParams(account=WSOL_token_account, dest=keypair.pubkey(), owner=keypair.pubkey(),
                                        program_id=TOKEN_PROGRAM_ID)
            closeAcc = (close_account(params))
            if swap_token_account_Instructions != None:
                swap_tx.add(swap_token_account_Instructions)

            swap_tx.add(instructions_swap,set_compute_unit_price(compute_unit_price),set_compute_unit_limit(compute_unit_limit),closeAcc)
            txn = solana_client.send_transaction(swap_tx, keypair,Wsol_account_keyPair)
            txid_string_sig = txn.value
            if txid_string_sig:
                if debug:
                    print("Transaction sent!")
                    print("Awaiting confirmations...")

            confirmation_resp = solana_client.confirm_transaction(
                txid_string_sig,
                commitment=Confirmed,
                sleep_seconds=0.5,
            )

            if confirmation_resp.value[0].err == None and str(
                    confirmation_resp.value[0].confirmation_status) == "TransactionConfirmationStatus.Confirmed":
                if debug:
                    print("Transaction confirmed!")
                    print(f"View your transaction at: https://solscan.io/tx/{txid_string_sig}")
                return txid_string_sig

            else:
                if debug:
                    print("Transaction not yet confirmed.")
                return False


        except asyncio.TimeoutError:
            if debug:
                print("Transaction confirmation timed out. Retrying...")
            retry_count += 1
            time.sleep(RETRY_DELAY)
        except RPCException as e:
            if debug:
                print(f"RPC Error: [{e.args[0]}]... Retrying...")
            retry_count += 1
            time.sleep(RETRY_DELAY)
        except Exception as e:
            if "block height exceeded" in str(e):
                if debug:
                    print("Transaction has expired due to block height exceeded. Retrying...")
                retry_count += 1
                await asyncio.sleep(RETRY_DELAY)
            else:
                if debug:
                    print(f"Unhandled exception: {e}. Retrying...")
                retry_count += 1
                await asyncio.sleep(RETRY_DELAY)
    
    if debug:
        print("Failed to confirm transaction after maximum retries.")
    return False

async def sell(solana_client, async_solana_client, token, keypair, amount, compute_unit_price, compute_unit_limit, debug):
    retry_count = 0
    while retry_count < MAX_RETRIES:
        try:
            mint = Pubkey.from_string(token)
            sol= WRAPPED_SOL_MINT
            TOKEN_PROGRAM_ID = solana_client.get_account_info_json_parsed(mint).value.owner
            pool_keys = fetch_pool_keys(str(mint))
            accountProgramId = solana_client.get_account_info_json_parsed(mint)
            programid_of_token = accountProgramId.value.owner
            accounts = solana_client.get_token_accounts_by_owner_json_parsed(keypair.pubkey(), TokenAccountOpts(
                program_id=programid_of_token)).value
            for account in accounts:
                mint_in_acc = account.account.data.parsed['info']['mint']
                if mint_in_acc == str(mint):
                    amount_in = int(account.account.data.parsed['info']['tokenAmount']['amount'])
                    if debug:
                        print("Your token balance is:", amount_in)
                    break

            swap_token_account = sell_get_token_account(solana_client, keypair.pubkey(), mint)
            WSOL_token_account, WSOL_token_account_Instructions = await get_token_account(solana_client, keypair.pubkey(), sol)

            if debug:
                print("Creating swap instructions...")
            if amount is not None:
                amount_in = amount
            instructions_swap = make_swap_instruction(amount_in,
                swap_token_account,
                WSOL_token_account,
                pool_keys,
                mint,
                solana_client,
                keypair
            )
            params = CloseAccountParams(account=WSOL_token_account, dest=keypair.pubkey(), owner=keypair.pubkey(),
                                        program_id=TOKEN_PROGRAM_ID)
            closeAcc = (close_account(params))
            swap_tx = Transaction()
            if WSOL_token_account_Instructions != None:
                recent_blockhash = solana_client.get_latest_blockhash(commitment="confirmed")
                swap_tx.recent_blockhash = recent_blockhash.value.blockhash
                swap_tx.add(WSOL_token_account_Instructions)

            swap_tx.add(instructions_swap,set_compute_unit_price(compute_unit_price),set_compute_unit_limit(compute_unit_limit))
            swap_tx.add(closeAcc)
            
            txn = solana_client.send_transaction(swap_tx, keypair)
            txid_string_sig = txn.value
            if txid_string_sig:
                if debug:
                    print("Transaction sent!")
                    print("Awaiting confirmations...")

            confirmation_resp = solana_client.confirm_transaction(
                txid_string_sig,
                commitment=Confirmed,
                sleep_seconds=0.5,
            )

            if confirmation_resp.value[0].err == None and str(
                    confirmation_resp.value[0].confirmation_status) == "TransactionConfirmationStatus.Confirmed":
                if debug:
                    print("Transaction confirmed!")
                    print(f"View your transaction at: https://solscan.io/tx/{txid_string_sig}")
                return txid_string_sig

            else:
                if debug:
                    print("Transaction not yet confirmed.")
                return False

        except asyncio.TimeoutError:
            if debug:
                print("Transaction confirmation timed out. Retrying...")
            retry_count += 1
            time.sleep(RETRY_DELAY)
        except RPCException as e:
            if debug:
                print(f"RPC Error: [{e.args[0].message}]... Retrying...")
            retry_count += 1
            time.sleep(RETRY_DELAY)
        except Exception as e:
            if "block height exceeded" in str(e):
                if debug:
                    print("Transaction has expired due to block height exceeded. Retrying...",e.args[0])
                retry_count += 1
                await asyncio.sleep(RETRY_DELAY)
            else:
                if debug:
                    print(f"Unhandled exception: {e}. Retrying...")
                retry_count += 1
                await asyncio.sleep(RETRY_DELAY)
    if debug:
        print("Failed to confirm transaction after maximum retries.")
    return False

def buy_token(solana_client, async_solana_client, token, keypair, amount, compute_unit_price=25_232, compute_unit_limit=200_337, debug=False):
    return asyncio.run(buy(solana_client, async_solana_client, token, keypair, 0.01, compute_unit_price, compute_unit_limit, debug))

def sell_token(solana_client, async_solana_client, token, keypair, amount=None, compute_unit_price=25_232, compute_unit_limit=200_337, debug=False):
    return asyncio.run(sell(solana_client, async_solana_client, token, keypair, amount, compute_unit_price, compute_unit_limit, debug))