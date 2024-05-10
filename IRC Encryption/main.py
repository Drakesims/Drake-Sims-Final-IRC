import string
import math
from Enigma import *

public_key = None  #Public key used in RSA
private_key = None  #Private Key used in RSA
n = None #modulus used
enigma = Enigma() #calls enigma class

#function for encrypting using Caesar Cipher
def caesarEncrypt(message, shift):
    chars = " " + string.punctuation + string.digits + string.ascii_letters
    shiftChars = chars[shift:] + chars[:shift]
    key = str.maketrans(chars, shiftChars)
    return message.translate(key)

#function for decrypting using Caesar Cipher
def caesarDecrpyt(cipherText, shiftValue):
    chars = " " + string.punctuation + string.digits + string.ascii_letters
    shiftChars = chars[shiftValue:] + chars[:shiftValue]
    key = str.maketrans(shiftChars, chars)
    return cipherText.translate(key)

#sets public and private keys. https://www.geeksforgeeks.org/rsa-algorithm-cryptography/# was used as a guide for this function
def setkeys():
    global public_key, private_key, n
    prime1 = 7  
    prime2 = 19 
 
    n = prime1 * prime2
    fi = (prime1 - 1) * (prime2 - 1)
 
    e = 2
    while True:
        if math.gcd(e, fi) == 1:
            break
        e += 1
 
    # d = (k*Φ(n) + 1) / e for some integer k
    public_key = e
 
    d = 2
    while True:
        if (d * e) % fi == 1:
            break
        d += 1
 
    private_key = d
 
#Encrypts the message using the RSA algorithm
def RSAencrypt(message):
    public_key, n
    e = public_key
    RSAencrypted = message**e % n
    return RSAencrypted
 
#decrypts the encrypted message by using the RSA algorithm for decrypting
def RSAdecrypt(RSAencrypted):
    private_key, n
    d = private_key
    RSAdecrypted = RSAencrypted**d % n
    return RSAdecrypted
 
# Creates an empty list, and then appends the integer to each letter in the message and returns the list. https://www.geeksforgeeks.org/rsa-algorithm-cryptography/# was used as a guide for this function
def RSAencoder(message):
    encoded = []
    # Calling the encrypting function in encoding function
    for letter in message:
        encoded.append((RSAencrypt(ord(letter))))
    return encoded
 
#Creates an empty string, and then runs the RSAdecrypt function and appends to the decoded string. https://www.geeksforgeeks.org/rsa-algorithm-cryptography/# was used as a guide for this function.
def RSAdecoder(encoded):
    decoded = ''
    # Calling the RSAdecrypt function
    for num in encoded:
        decoded += chr(RSAdecrypt(num))
    return decoded
 
#Allows users to pick if they would like to encrypt or RSAdecrypt
while True:
    encryptDecrypt = int(input("[1] Encyrpt a message\n[2] Decrypt a Message\nType your choice in using the corresponding number.\n"))
    #Gives the user what options they have to encrpyt with
    if encryptDecrypt == 1:
        print("What method would you like to use to encrypt? \n [1] Caesar Cipher \n [2] Enigma Machine  \n [3] RSA")
        encryptChoice = int(input("Type your choice in using the corresponding number.\n"))
        #This option allows the user to encrypt using the caesar cipher. It gets values from the user and plugs those inputs into the caesarEncrypt function
        if encryptChoice == 1:
            shift = int(input("How many characters would you like to shift? "))
            caesarMessage = input("Type the message you would like to encrypt. ")
            encryptedMessage = caesarEncrypt(caesarMessage,shift)
            print("Your Encrypted Message: ", encryptedMessage)
            break
        #This option allows the user to encrypt using the caesar cipher. It gets values from the user and plugs those inputs into the caesarEncrypt function
        if encryptChoice == 2:
            message = input("Enter the message you would like encrypted.\n")
            encryptedText = enigma.encrypt_text(message)
            print("Your encrypted message is: ", encryptedText)
            break
        if encryptChoice == 3:
            setkeys()
            message = input("Enter the message you would like encrypted.\n")
            finalmessage = RSAencoder(message)
            print("Your encrypted message is: ",finalmessage)
            break
    #This option is called if the user wants to decrypt a already encrypted message
    if encryptDecrypt == 2:
        print("What method would you like to use to decrypt? \n [1] Caesar Cipher \n [2] Enigma Machine \n [3] RSA")
        #User is given the option of what method they'd liek to use to RSAdecrypt
        decryptChoice = int(input("Type your choice in using the coresponding number!\n"))
        #This option allows a user to decrypt a message using the Caesar Cipher. This called the caesarDecrypt function
        if decryptChoice == 1:
            cipherText = input("What message would you like to decrypt?\n")
            shiftValue = int(input("What shift value was used to encrypt this message?\n"))
            RSAdecryptedMessage = caesarDecrpyt(cipherText, shiftValue)
            print("Your decrypted Message: ", RSAdecryptedMessage)
            break
        if decryptChoice == 2:
            message = input("Enter the message you would like decrypted.\n")
            decryptedText = enigma.encrypt_text(message)
            print("Your decrypted message is: ", decryptedText)
            break
        if decryptChoice == 3:
            setkeys()
            encryptedMessage = input("Enter the message you would like decrypted. Please seperate integers using commas!\n")
            encodedMessage = [int(num) for num in encryptedMessage.split(',')]
            finalmessage = RSAdecoder(encodedMessage)
            print("Your decrypted message is: ",finalmessage)
            break
    else:
        print("That is not a valid choice. Please try again")
