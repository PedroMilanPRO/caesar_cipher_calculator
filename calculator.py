class caeser:
    print('=========Calculator Cypher==============')

    texto = input('Enter the text to be Encrypted or Decrypted: ').upper()
    chave = int(input('type the key (> 0; < 26): '))
    modo = input('Choose E to encrypt or D to decrypt: ')

    CHARACTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    converted = ''

    for character in texto:
        if character in CHARACTERS:
            num = CHARACTERS.find(character)

            if modo == 'E':
                num = num + chave
            elif modo == 'D': 
                num = num - chave
            
            if num >= len(CHARACTERS):
                num = num - len(CHARACTERS)
            elif num < 0:
                num = num + len(CHARACTERS)
            
            converted = converted + CHARACTERS[num]


    if modo == 'E':
        print(f'Encrypted text is {converted}')
    elif modo == 'D':
        print(f'decrypted text is {converted}')









