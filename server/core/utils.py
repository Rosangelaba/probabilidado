import random

# import uuid
# uuid.uuid4().hex[:6].upper()
# hex

def int_to_5bit(n):
    code = []
    for i in range(0, 66, 5):
        s = (n >> i)
        if s == 0:
            break
        c = s & 0b11111
        if c < 10:
            code.append(str(c))
        else:
            code.append(chr(55 + c))
    code.reverse()
    return ''.join(code)

def gen_code(idx):
    salt = random.randrange(0, 255)
    return int_to_5bit(idx << 8 + salt)
    #~ return int_to_5bit(idx << 8 + (salt & 0b11111111))


#~ for n in [0,1,5,9,10,11,20,30,60,90,128, 512, 1023, 1024, 1025, 2**30 + 2**27 + 2**23 + 2**19 + 2**17 + 2**11 + 507]:
    #~ print(n, int_to_5bit(n))
