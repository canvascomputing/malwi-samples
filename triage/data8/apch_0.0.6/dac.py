import numpy as np

def calculate_dac(branch, account_number, wallet, our_number):
    """
    Should return the DAC 
    If DAC calc division be 0 result should be 0

    >>> calculate_dac("0057", "12345-7", "110", "12345678")
    8
    """
    calc_string = f"{branch.zfill(4)}{account_number.zfill(5).split('-')[0]}{wallet.zfill(3)}{our_number.zfill(8)}"
    
    user_calc_vector = list(int(char) for char in calc_string.replace(".", "").replace("-", "").replace("/", ""))
    dac_calc_vector = [1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2]

    vector_multiplication_result_list = list(np.multiply(user_calc_vector, dac_calc_vector))

    # the bank documentation ask to sum any number > 10. Eg. 13 = 1+3 = 4
    list_with_every_number_higher_than_10_recalculated = []
    for number in vector_multiplication_result_list:
        if number >= 10:
            n_number = sum(list(int(char) for char in str(number)))
        else:
            n_number = number
        list_with_every_number_higher_than_10_recalculated.append(n_number)

    calc_sum_result = sum(list_with_every_number_higher_than_10_recalculated)

    dac_remaining = calc_sum_result % 10
    if dac_remaining != 0:
        return 10 - dac_remaining
    return 0
