# this was one of the learning projects
# i've found useful for understanding concepts of changing models
# and for understanding Morse Code itself
# NB-NOTE: THE ORIGINAL PROJECT
# CAN BE FOUND IN THE FOLLOWING ADDRESS:
# https://www.geeksforgeeks.org/morse-code-translator-python


# This Project is redesigned and updated in a more understandable way
# by me! (/https://github.com/AmirHosseinRnj1)
# If you have any problem running or understanding this project,
# feel free to make contact with me...


# Dictionary representing the morse code chart
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

# Fucntion to encrypt from English text to Morse Code

###############
### ENCRYPT ###
###############

def encrypt(message):
    cipher = ""
    for letter in message:
        if letter != " ":
            cipher += MORSE_CODE_DICT[letter]
        else:
            cipher += " "
    return cipher

###############
### DECRYPT ###
###############

def decrypt(message):
    i = 0
    decipher = ""
    citext = ""
    for letter in message:
        if letter != " ":
            i = 0

            citext += letter
        else:
            i += 1

            if i == 2:
                decipher += " "

            else:
                # accessing keys with values!
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                citext = ""

    return decipher

############
### MAIN ###
############
    # if you don't want to use Tkinter app,
    # uncomment below code and run this file again
    # p.s: Tkinter app will be updated soon...

"""
def main():
    print("What do You wish to do now? ")
    cmd = str(input("Give \"enc\" for Encryption and \"dec\"for Decryption... "))
    if cmd == "enc":
        message = str(input("Give the text You Want to Encrypt: ")).upper()
        enc = encrypt(message)
        return enc
    elif cmd == "dec":
        message = str(input("Give the text You Want to Decrypt: "))
        dec = decrypt(message)
        return dec
    else:
        print("Wrong Input! plz Try again with an Normal English or Morse.. \n Existing...")
        sys.exit()

if __name__ == '__main__':
    print(main())
"""