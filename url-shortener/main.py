import string

ENCODE_CHAR = string.ascii_letters + string.digits
COUNTER = 0

def calcRemainers(num, base):
    if num == 0:
        return [0]
    digits = []
    while num > 0:
        remainer = num % base
        digits.append(remainer)
        num = num // base
    return reversed(digits)

def charDigitEncode(num):
    enc = ""
    for pos in calcRemainers(num, len(ENCODE_CHAR)):
        enc += ENCODE_CHAR[pos]
    return enc

if __name__ == "__main__":
    import time
    
    while True:
        print(COUNTER, charDigitEncode(COUNTER))
        COUNTER += 8
        time.sleep(1)