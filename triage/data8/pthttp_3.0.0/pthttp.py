"""this is pthttp.py module to print a list recursively"""
def print_lol(the_list):
    for item in the_list:
        if isinstance(item, list):
            print_lol(item)
        else:
            print(item)
            
