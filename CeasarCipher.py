alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

print(logo) 

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))    

def caesar(plain_text, shift_amount, direction):
    cipher_text = ""
    counter = 0
    if(direction == "encode"):
        for letter in plain_text:
            index = alphabet.index(letter)
            for i in range(1, shift_amount + 1):
                if(index == 25):
                    index = 0
                else:
                    index += 1

            new_index = index 
            new_letter = alphabet[new_index]
            cipher_text += new_letter
            counter += 1
    
        print(f"The encoded text is {cipher_text}")
    
    else:
        for letter in plain_text:
            index = alphabet.index(letter)
            for i in range(1, shift_amount + 1):
                if(index == 0):
                    index = 25
                else:
                    index -= 1
            new_index = index 
            new_letter = alphabet[new_index]
            cipher_text += new_letter
            counter += 1
        print(f"The decoded text is {cipher_text}")

caesar(plain_text=text, shift_amount=shift, direction=direction)

