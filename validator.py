# Example of a custom module to be imported

import re


def validate_email(email):
    if len(email) > 14:
        return bool(re.match("^.+@(\\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email))





def dataTypeValidator(name1):
    if type(name1) == int:
        answer = f'{name1} is the correct data type'
    else:
        answer = 'Wrong data type'
    return answer

def matching_number(num1, num2):
    if num1 == num2:
        result = f'{num1} is a perfect match with {num2}' 
    else:
        result = f'{num1} is not a perfect match with {num2}'
    return result