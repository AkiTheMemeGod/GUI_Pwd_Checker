alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
             'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
             'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
             'y', 'z', ' ', 'A', 'B', 'C', 'D', 'E',
             'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z', '1', '2', '3',
             '4', '5', '6', '7', '8', '9', '0', '/',
             '@', '<', '-', '=', '*', '.', '_', '#',
             '`', '~', ',', ':', ';', '[', ']', '{',
             '$', '!', '%', '&', '(', ')', '\n', '?',
             '"', '>', '|', '+', "'"]

'''print(len(alphabets))
'''

def key(bits):
    import secrets as st
    keys = st.token_hex(bits)
    return keys


def get_key():
    with open("assets/key.txt", 'r') as file:
        keys = file.read()
    key_list = [keys[i:i + 64] for i in range(0, len(keys), 64)]
    # print(len(key_list))
    return key_list


def put_key(the_key):
    with open("assets/key.txt", 'w') as file:
        file.write(the_key)


def new_key():
    i = 1
    dec_key = ""
    while i <= 93:
        x = key(32)
        dec_key = dec_key + x
        i += 1

    put_key(dec_key)


def show_key():
    x = ""
    alpha = get_key()
    for i in alpha:
        i = i.strip("\n")
        x += i
    print(x)


def encrypt(message):
    encrypted_message = ""
    x = get_key()
    for i in message:
        # i = i.lower()
        ind = alphabets.index(i)
        encrypted_message += x[ind]

    return encrypted_message


def decrypt(message):
    decrypted_message = ""
    x = get_key()
    substrings = [message[i:i + 64] for i in range(0, len(message), 64)]
    for i in substrings:
        # i = i.lower()
        ind = x.index(i)
        decrypted_message += alphabets[ind]

    return decrypted_message


def decrypt_file(filename):
    with open(filename, 'r') as enc_passes:
        passes = enc_passes.read()
    dec_pass = decrypt(passes)

    with open(filename, 'w') as passes:
        passes.write(dec_pass)


def encrypt_file(filename):
    with open(filename, 'r') as passes:
        passes = passes.read()
    m = get_key()
    for i in m:
        if i in passes:
            print(f"Error the file -> {filename} <- is already encrypted")
            return None
    enc_pass = encrypt(passes)
    with open(filename, 'w') as enc_passes:
        enc_passes.write(enc_pass)


def encrypt_folder(folder):
    import os
    for filename in os.listdir(folder):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder, filename)
            try:
                encrypt_file(file_path)
            except Exception as e:
                print(f'Error encrypting --> {filename}:', e)


def decrypt_folder(folder):
    import os
    for filename in os.listdir(folder):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder, filename)
            try:
                decrypt_file(file_path)
            except Exception:
                print(f'Error decrypting --> {filename}: ')


# decrypt_folder('pg_chk_fls')