class caeser:
    print('=========Calculator Cypher==============')

    text = input('Enter the text to be Encrypted or Decrypted: ').upper()
    key = int(input('type the key (> 0; < 26): '))
    mode = input('Choose E to encrypt or D to decrypt: ').upper()

    CHARACTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    converted = ''

    for character in text:
        if character in CHARACTERS:
            num = CHARACTERS.find(character)

            if mode == 'E':
                num += key
            elif mode == 'D': 
                num -= key
        
            if num >= len(CHARACTERS):
                num -= len(CHARACTERS)
            elif num < 0:
                num += len(CHARACTERS)
            
            converted += CHARACTERS[num]

        else:
            converted += character

    if mode == 'E':
        print(f'Encrypted text is {converted}')
    elif mode == 'D':
        print(f'decrypted text is {converted}')
