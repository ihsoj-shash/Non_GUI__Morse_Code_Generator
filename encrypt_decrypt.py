import data


def encrypt_a_msg(msg):
    encrypted_msg = ''
    for letter in msg.upper():
        if letter != ' ':
            encrypted_msg += data.MORSE_CODE_DICT[letter] + ' '
        else:
            encrypted_msg += ' '

    return encrypted_msg


def decrypt_a_msg(msg):
    msg += ' '
    decrypted_msg = ''
    citext = ''
    for letter in msg:
        if letter != ' ':
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2:
                decrypted_msg += ' '
            else:
                decrypted_msg += list(data.MORSE_CODE_DICT.keys())[list(data.MORSE_CODE_DICT.values()).index(citext)]
                citext = ''
    return decrypted_msg
