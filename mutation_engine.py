from time import sleep
from random import shuffle
from collections import OrderedDict
import os
import subprocess

encrypt_key = {'b': 'i', 'G': 'h', 'E': '<', 'A': 'g', 'K': 'b', '+': '7', '1': '#', 'g': 'J', '"': '5', 'Q': 'v', '9': 'S', '0': 'P', '2': 'A', 'x': 'y', '(': '8', '4': 'm', '5': 'f', 'i': '%', 'f': '>', 'X': '?', 'k': '6', 'c': 'p', 's': 'C', '3': 'q', 't': 'D', 'z': 'X', 'r': 'V', ')': ',', '#': '4', 'C': 'T', 'u': 'Q', 'U': '1', 'w': 'U', '.': '(', ',': '*', '<': ' ', 'd': '"', 'T': 'c', 'v': '=', 'o': 'F', '6': '-', 'Y': 's', 'Z': 'a', ':': 'w', 'e': 'N', 'F': 'O', '8': '.', 'V': 't', 'R': 'u', '\\': '\\', 'q': ')', 'M': 'j', ' ': 'M', 'I': 'o', 'n': 'z', 'p': 'e', 'y': 'L', '?': 'n', 'O': 'x', 'H': '9', '7': 'K', '!': '!', 'l': 'Y', 'L': 'l', 'J': 'k', 'S': 'r', '*': ':', '=': 'G', '>': '+', 'P': "'", 'D': 'I', 'h': 'Z', '%': 'H', 'j': 'B', 'W': '3', '-': 'E', "'": '0', 'B': 'W', 'N': 'R', 'm': 'd', 'a': '2'}

decrypt_key = {v: k for k, v in encrypt_key.items()}
unencrypted_code = []
encrypted_code = []

def polymorphic(filename):
    global encrypt_key
    global encrypted_code
    global decrypt_key
    global unencrypted_code
    lines = open(filename, 'r').readlines()
    for i in lines:
        for x in i:
            if x == '\n':
                unencrypted_code.append('\n')
            else:
                unencrypted_code.append(decrypt_key[x])

    with open(filename,'w') as file:
        for line in unencrypted_code:
            file.write(line)
        print(unencrypted_code)

    file.close()

    subprocess.call('python ' + filename,shell=True)

    lines = open(filename, 'r').readlines()
    for i in lines:
        for x in i:
            if x == '\n':
                encrypted_code.append('\n')
            else:
                encrypted_code.append(encrypt_key[x])

    with open(filename,'w') as file:
        encrypted_code = encrypted_code[int(len(encrypted_code)/2):]
        for line in encrypted_code:
            file.write(line)
        print(encrypted_code)
    file.close()

    print('[+] Polymorphic code ran successfully')

def encrypt(filename):
    global encrypt_key
    global encrypted_code
    global decrypt_key
    global unencrypted_code
    lines = open(filename, 'r').readlines()
    for i in lines:
        for x in i:
            if x == '\n':
                encrypted_code.append('\n')
            else:
                encrypted_code.append(encrypt_key[x])

    with open(filename, 'w') as file:
        for line in encrypted_code:
            file.write(line)

    print('[+] Encrypted')

def decrypt(filename):
    global encrypt_key
    global encrypted_code
    global decrypt_key
    global unencrypted_code
    lines = open(filename, 'r').readlines()
    for i in lines:
        for x in i:
            if x == '\n':
                unencrypted_code.append('\n')
            else:
                unencrypted_code.append(decrypt_key[x])

    with open(filename, 'w') as file:
        for line in unencrypted_code:
            file.write(line)

    print('[+] Decrypted')

def dict_shuffle():
    global encrypt_key
    keys = list(encrypt_key.keys())
    shuffle(keys)
    encrypt_key = dict(OrderedDict(zip(keys, encrypt_key.values())))

    file = open('mutation_engine.py', 'r')
    data = file.readlines()

    data[6] = 'encrypt_key = ' + str(encrypt_key) + '\n'

    file2 = open('mutation_engine.py', 'w')
    file2.writelines(data)

def controlPanel():
    isDone = False
    while isDone == False:
        result = int(input("Choose an option:\n1. Encrypt a code file\n2. Decrypt a code file\n3. Execute encrypted code as polymorphic code\n4. End Program\n>>> "))
        if result == 4:
            print('[+] Quitting...')
            isDone = True
        else:
            filename = input('Input the name of your file (If your file is not in the current workind directory, input the path of the file): ')
            if result == 1:
                try:
                    encrypt(filename)
                except:
                    print('[-] Invalid filename or path')
            elif result == 2:
                try:
                    decrypt(filename)
                except:
                    print('[-] Invalid filename or path')
            elif result == 3:
                try:
                    polymorphic(filename)
                except:
                    print('[-] Invalid filename or path')
            else:
                print('[-] Invalid input')

    dict_shuffle()

if __name__ == "__main__":
    controlPanel()
