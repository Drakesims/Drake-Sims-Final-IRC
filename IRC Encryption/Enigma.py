#https://medium.com/analytics-vidhya/how-to-build-an-enigma-machine-virtualisation-in-python-b5476a1fd922 was used as a guide to create this enigma machine
from string import ascii_lowercase

class Enigma:
    def __init__(self):
        #Create the alphabet including a space
        self.alphabet = list(ascii_lowercase) + [' ']

        #Fixed rotor positions
        self.alpha = 6
        self.beta = 5
        self.charlie = 4
        self.delta = 3
        self.echo = 2

        #Reflector used in the enigma machine
        self.reflector = list("yruhqsldpxngokmiebfzcwvjat ")

    #Permutates the alphabet depending on rotor positions and direction
    def permutate(self, rotor, direction):
        new_alphabet = self.alphabet[:]
        for _ in range(rotor):
            if direction == 'forward':
                new_alphabet.append(new_alphabet.pop(0))
            if direction == 'backward':
                new_alphabet.insert(0, new_alphabet.pop(-1))
        return new_alphabet
    
    #Method used to encrypt the text given to it after being called, works to decrypt as well
    def encrypt_text(self, text):
        encrypted_text = []
        text = text.lower()
        for letter in text:
            temp_letter = self.permutate(self.alpha, 'forward')[self.alphabet.index(letter)]
            temp_letter = self.permutate(self.beta, 'forward')[self.alphabet.index(temp_letter)]
            temp_letter = self.permutate(self.charlie, 'forward')[self.alphabet.index(temp_letter)]
            temp_letter = self.permutate(self.delta, 'forward')[self.alphabet.index(temp_letter)]
            temp_letter = self.permutate(self.echo, 'forward')[self.alphabet.index(temp_letter)]

            temp_letter = self.reflector[self.alphabet.index(temp_letter)]

            temp_letter = self.permutate(self.echo, 'backward')[self.alphabet.index(temp_letter)]
            temp_letter = self.permutate(self.delta, 'backward')[self.alphabet.index(temp_letter)]
            temp_letter = self.permutate(self.charlie, 'backward')[self.alphabet.index(temp_letter)]
            temp_letter = self.permutate(self.beta, 'backward')[self.alphabet.index(temp_letter)]
            temp_letter = self.permutate(self.alpha, 'backward')[self.alphabet.index(temp_letter)]

            encrypted_text.append(temp_letter)
            #turning the rotors
            self.alpha += 1
            if self.alpha % 26 == 0:
                self.beta += 1
                self.alpha = 0
            if self.beta % 26 == 0 and self.alpha % 26 != 0 and self.beta >= 25:
                self.charlie += 1
                self.beta = 1
            if self.charlie % 26 == 0 and self.beta % 26 != 0 and self.charlie >= 25:
                self.delta += 1
                self.charlie = 1
            if self.delta % 26 == 0 and self.charlie % 26 != 0 and self.delta >= 25:
                self.echo += 1
                self.delta = 1


        return ''.join(encrypted_text)