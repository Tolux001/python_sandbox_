# Example of a custom module to be imported

import re


def validate_email(email):
    if len(email) > 14:
        return bool(re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email))

def nameValidator(name1, name2):
    if name1 == name2:
        answer = 'Matching Names'
    else:
        answer = 'Seriously Bro, just write the same name that all: Check typo or casing'
    return answer