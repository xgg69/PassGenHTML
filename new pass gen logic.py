#exam join code: P9RSNLDS

import random
import string

lowercase = True
uppercase = True
numbers = True
symbols = False

passLength = 6

def generate(length = int(), lowerc = bool(), upperc = bool(), num = bool(), sym = bool()):
    currentChars = ""
    password = ""
    if(lowerc):
        currentChars = currentChars + string.ascii_lowercase
    if(upperc):
        currentChars = currentChars + string.ascii_uppercase
    if(num):
        currentChars = currentChars + string.digits
    if(sym):
        currentChars = currentChars + string.punctuation
    for i in range(length):
        password = password + currentChars[random.randint(0, len(currentChars)-1)]
    return(password)

print(generate(passLength, lowercase, uppercase, numbers, symbols))