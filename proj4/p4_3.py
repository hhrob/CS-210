def encrypt(msg: str) -> str:
    '''
    Encrypts message using ROT-13 cipher. Accepts non-alphanumeric characters, as well as white space.
    All strings returned in lowercase.

    Parameters:
        msg (str)

    Return Values:
        ciph_msg (str)

    
    >>> encrypt('Ahoy, there!')
    nubl, gurer!

    >>> encrypt('Forever, and ever!')
    sberire, naq rire!

    >>> encrypt('1234')
    1234
    '''
    msg = msg.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    ciph_alpha = 'nopqrstuvwxyzabcdefghijklm'

    ciph_msg = ""
    ciph_char = ""
    
    for char in msg:
        ct = 0
        if not char.isalpha():
            ciph_msg += char


        for i in alphabet:
            if char == i:
                ciph_char = ciph_alpha[ct]
                ciph_msg += ciph_char
            ct += 1
    
    return ciph_msg

def decrypt(msg: str) -> str:
    '''
    Decrypts message ciphered with ROT-13. Accepts non-alphanumeric characters.
    Returns lowercase string.

    Parameters:
        msg (str)

    Return values:
        orig_msg (str)

    >>> decrypt('nubl, gurer!')
    ahoy, there!
    
    >>> decrypt('sbreire, naq rire!')
    forever, and ever!

    >>> decrypt('1234')
    1234
    '''
    msg = msg.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    ciph_alpha = 'nopqrstuvwxyzabcdefghijklm'

    orig_msg = ""
    ciph_char = ""
    
    for char in msg:
        ct = 0
        if not char.isalpha():
            orig_msg += char


        for i in alphabet:
            if char == i:
                ciph_char = ciph_alpha[ct]
                orig_msg += ciph_char
            ct += 1
    
    return orig_msg
