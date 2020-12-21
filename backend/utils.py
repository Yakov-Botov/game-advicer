

def get_only_int_from_str(extractable_str):
    # extractable_str =  '48984 products'
    product_count_int_list = [x for x in extractable_str if x.isdigit()]  # ['4', '8', '9', '8', '4']
    result = ''.join(product_count_int_list)  # '48984'
    return result
