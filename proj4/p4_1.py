def encrypt(msg:str) -> str:
    '''
    Returns encrypted message using simple Transposition cipher.

    >>> encrypt('It was a dark and stormy night')
    twsadr n tryngtI a  akadsom ih

    >>> encrypt('I am going to miss the train')
    mgigt istetanIa on oms h ri

    >>> encrypt('Doctest')
    otsDcet
    '''

    even_chars = ""
    odd_chars = ""
    ch_ct = 0
    for ch in msg:
        if ch_ct % 2 == 0:
            even_chars = even_chars + ch
        else:
            odd_chars = odd_chars + ch
        ch_ct+= 1
    trans_cipher = odd_chars + even_chars

    return trans_cipher

print(encrypt('Doctest'))

def decrypt(msg:str) -> str:
    '''
    Returns decrypted transposition cipher text. Offsets encrypt().

    >>> decrypt('twsadr n tryngtI a  akadsom ih')
    It was a dark and stormy night

    >>> decrypt('mgigt istetanIa on oms h ri')

    >>> decrypt('otsDcet')
    Doctest
    '''
    half_length = len(msg) // 2
    even_chars = msg[half_length:]
    odd_chars = msg[:half_length]
    decrypted_msg = ""

    for i in range(half_length):
        decrypted_msg = decrypted_msg + even_chars[i]
        decrypted_msg = decrypted_msg + odd_chars[i]

    if len(odd_chars) < len(even_chars):
        decrypted_msg = decrypted_msg + even_chars[-1]

    return decrypted_msg
