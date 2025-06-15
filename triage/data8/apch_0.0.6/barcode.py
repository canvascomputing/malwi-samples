def generate_codebar_from_bank_slip_digitable_line(digitable_line):
    """
    Generate barcode from digitable line if it is not present 

    >>> generate_codebar_from_bank_slip_digitable_line("00190500954014481606906809350314337370000000100")
    '00193373700000001000500940144816060680935031'

    >>> generate_codebar_from_bank_slip_digitable_line("34191090080000016200809185950004683650000000100")
    '34196836500000001001090000000162000918595000'
    """
    field_1 = digitable_line[:9]
    field_2 = digitable_line[10:21]
    field_3 = digitable_line[21:32]
    field_4 = digitable_line[32:33]
    field_5 = digitable_line[33:47]

    line = f"{field_1[:4]}{field_4}{field_5}{field_1[4:]}{field_2[:6]}{field_2[6:10]}{field_3[:-1]}"
    return line


def generate_codebar_from_utility_slip_digitable_line(digitable_line):
    """
    Generate barcode from digitable line if it is not present 
    >>> generate_codebar_from_utility_slip_digitable_line("836500000168185600481005093838009319001859138966")
    '8365000001618560048100093838009310018591'

    >>> generate_codebar_from_utility_slip_digitable_line("846500000027665900820895995557764819112990559992")
    '8465000000266590082089995557764811129905'

    >>> generate_codebar_from_utility_slip_digitable_line("836200000005874800577213003029174004000722823606")
    '8362000000087480057721003029174000007228'
    """
    line = f"{digitable_line[:11]}{digitable_line[12:23]}{digitable_line[24:35]}{digitable_line[36:43]}"
    return line
