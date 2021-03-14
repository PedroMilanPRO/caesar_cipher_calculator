# caesar_cipher_calculator
##### Caesar's Principles:

- Encrypt a text
       - shift to the right (value)
- Decrypt a text
       - Shift to the left (value)
    
##### Example:

Let's attack to the north (offset = 3)

I = L
r = u
e = h

To decrypt, just do the reverse, with the key in your hands

And so on...

##### Explaining a little about the code...

---
```python
class caeser:
    print('=========Calculator Cypher==============')

    # Entrada de dados
    text = input('Enter the text to be Encrypted or Decrypted: ').upper()
    key = int(input('type the key (> 0; < 26): '))
    mode = input('Choose E to encrypt or D to decrypt: ')

    # Alfabeto e uma variavel que será o texto convertido
    CHARACTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    converted = ''

    # Laço for, iterando cara caratere do texto
    for character in text:
        # Verificando se possui o caratere no alfabeto
        if character in CHARACTERS:
            # Retornar a posição do caractere dentro da constante 
            num = CHARACTERS.find(character)
            # Verificar qual o modo 
            if modo == 'E':
                num = num + key
            elif modo == 'D': 
                num = num - key
            
            # Caso o numero for maior/menor do que o alfabeto, sera subtraido/adicionado
            # o valor do comprimento do alfabeto
            # Caso sendo maior que 0, e menor que 26, sera simplesmente concatenado
            if num >= len(CHARACTERS):
                num = num - len(CHARACTERS)
            elif num < 0:
                num = num + len(CHARACTERS)
            
            converted = converted + CHARACTERS[num]
            
        else:
            converted = converted + character

    #Resultado Final
    if mode == 'E':
        print(f'Encrypted text is {converted}')
    elif mode == 'D':
        print(f'decrypted text is {converted}')
```
---
If something is wrong, let me know so I can fix it, I am always willing to improve.

![](Hello_Bye.gif)