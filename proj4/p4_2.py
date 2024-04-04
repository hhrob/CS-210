def encrypt(msg:str) -> str:
    '''
    Returns an encrypted message using a 3-Rail Cipher, wherein the message is broken by each character's place within the
    string.

    Parameters:
        msg (str)
    Return Values:
        encrypted_msg (str)
    >>> encrypt()
    '''
    rail_1 = msg[::3]
    rail_2 = msg[1::3]
    rail_3 = msg[2::3]

    encrypted_msg = rail_1 + rail_2 + rail_3

    return encrypted_msg

def decrypt(msg: str) -> str:
    '''
    Returns a decrypted message of a ciphered string, ciphered using 3-rail method.

    Parameters:
        msg (str)
    Return Values:
        decrypted_msg (str)

    >>> decrypt()
    '''
    decrypted = ""
    rail_1_len = 0
    rail_2_len = 0
    rail_3_len = 0
    ct = 0
    length = len(msg)

    for char in msg:
        if ct == 0:
            rail_1_len += 1
        elif ct == 1:
            rail_2_len += 1
        elif ct == 2:
            rail_3_len += 1
            ct = -1
        ct += 1

    len_ct = 0

    while (len_ct < length):
        if len_ct < rail_1_len:
            decrypted = decrypted + msg[len_ct]
        if len_ct < rail_2_len:
            decrypted = decrypted + msg[rail_1_len + len_ct]
        if len_ct < rail_3_len:
            decrypted = decrypted + msg[rail_1_len + rail_2_len + len_ct]

        len_ct += 1

    return(decrypted)

