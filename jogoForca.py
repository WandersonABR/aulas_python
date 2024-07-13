import random
import os

lista_palavras = ['python', 'programação', 'computador', 'notebook', 'software', 'openai', 'algoritmos', 'computador']

palavra = random.choice(lista_palavras) # Escolher palavra aleatória da lista
letras_corretas = []
letras_erradas = []
tentativas = 6

while True:
    palavra_escondia = ''
    for letra in palavra:
        if letra in letras_corretas:
            palavra_escondia += letra
        else:
            palavra_escondia += '_'
    os.system('cls')
    print('Palavra: ', palavra_escondia)
    print('Letras erradas: ', letras_erradas)
    print('Tentativas restante: ', tentativas)

    if palavra_escondia == palavra:
        print('Você acertou!')
        break
    elif tentativas == 0:
        print('Você perdeu! A palavra era: ', palavra)

    letra_usuario = input("Digite uma letra: ").lower()

    #Verificando a letra digitada
    if letra_usuario in palavra:
        print("Letra correta!")
        letras_corretas.append(letra_usuario)
    else:
        print("Letra incorreta!")
        letras_erradas.append(letra_usuario)
        tentativas -= 1