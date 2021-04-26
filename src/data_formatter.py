# |-------------------------------------------------------------------------------------------------------------------------------
# | By: Christian Toro |
# |-------------------------------------------------------------------------------------------------------------------------------

import re
import string
import logging

#---------------------------------------------------------------------------------------------------------------------
# Function that formats the author name by removing comma or period at the end of name
def author_format(data, index_one, index_two):
    try:
        if data[index_one][index_two] is None:
            return ''
        data_string = str(data[index_one][index_two])
        data_string = string.capwords(data_string)
        data_length = len(data_string)
        if ',' == data_string[data_length - 1] or '.' == data_string[data_length - 1]:
            data_string = data_string[:(data_length-1)]
        if ' :' in data_string:
            semicolon_index = data_string.index(':')
            data_string = data_string[:(semicolon_index - 1)] + data_string[semicolon_index:]
    except:
        logging.error('Author key not found in response json.')
        return ''
    return data_string

#---------------------------------------------------------------------------------------------------------------------
# Function to return call number
# Checks for a case in given api where the call number is CD-291 but is supposed to be SDA 55980
# Source for error: https://catalog.loc.gov/vwebv/holdingsInfo?&bibId=5653611&searchId=27497&recPointer=0&recCount=25
def call_number_format(data, index_one, index_two):
    try:
        if data[index_one][index_two] is None:
            return ''
        data_string = str(data[index_one][index_two])
        if 'CD-291' == data_string:
            return 'SDA 55980'
    except:
        logging.error('Call Number key not found in response json.')
        return ''
    return data_string

#---------------------------------------------------------------------------------------------------------------------
# Formats the 4 digit year date presented in the data
def date_format(data, index_one, index_two):
    date = number_format(data, index_one, index_two)
    return date

#---------------------------------------------------------------------------------------------------------------------
# Formats the ISBN number presented in the data and checks to ensure 
# the number contains either 10 or 13 digits as per ISBN standards
def isbn_format(data, index_one, index_two):
    isbn = number_format(data, index_one, index_two)
    if len(isbn) != 10 and len(isbn) != 13:
        return ''
    if len(isbn) == 13:
        if '978' not in isbn[0:3] or '979' not in isbn[0:3]:
            return ''
    return isbn

#---------------------------------------------------------------------------------------------------------------------
# Formats any data that is supposed to be number only by using regex to remove
# any non-numerical values from the string.
def number_format(data, index_one, index_two):
    try:
        if data[index_one][index_two] is None:
            return ''
    except Exception:
        logging.error('Date or ISBN key not found in response json.')
        return ''
    
    return re.sub(r'\D', '', data[index_one][index_two])

#---------------------------------------------------------------------------------------------------------------------
# Formats the title by capitalizing every word, removing / or . at end of title, and
# if there is a colon, will remove the white space before it.
def title_format(data, index_one, index_two):
    try:
        if data[index_one][index_two] is None:
            return ''
        data_string = str(data[index_one][index_two])
        data_string = string.capwords(data_string)
        data_length = len(data_string)
        if '/' == data_string[data_length - 1] or '.' == data_string[data_length - 1]:
            data_string = data_string[:(data_length-1)]
        if ' :' in data_string:
            semicolon_index = data_string.index(':')
            data_string = data_string[:(semicolon_index - 1)] + data_string[semicolon_index:]
    except:
        logging.error('Title key not found in response json.')
        return ''
    return data_string
