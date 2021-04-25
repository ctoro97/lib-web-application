import re

def isbn_format(data, index_one, index_two):
    print('')

# Remove the backslash and period at the end of the title
# Caps the first letter of each word in title


# function
def number_format(data, index_one, index_two):
    if data[index_one][index_two] is None:
        return ''
    
    return re.sub(r'\D', '', data[index_one][index_two])



# function
def data_value(data, index_one, index_two):
    if data[index_one][index_two] is None:
        return ''
    
    return data[index_one][index_two]

def title_format(data, index_one, index_two):
    data_string = str(data[index_one][index_two])
    data_length = len(data_string)
    if '/' == data_string[data_length - 1] or '.' == data_string[data_length - 1]:
        return data_string[:(data_length-1)]
    print(f'Length: {data_length} and {data_string.index("/")}')
    return data[index_one][index_two]