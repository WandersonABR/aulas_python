import random

numero_secreto = random.randint(1,20)

tentativas = 0
max_tentativas = 5
acertou = False

print("Bem-vindo ao python Games!")
print(f'Você possui {max_tentativas} tentativas para adivinhar o numero secreto entre 1 e 5')

while tentativas < max_tentativas:
    palpite = input("Digite um numero inteiro: ")
    palpite = int(palpite)
    tentativas += 1

    if palpite == numero_secreto:
        acertou = True
        break
    elif palpite < numero_secreto:
        print("Tente um numero maior")
    else:
        print("Tente um numero menor")

if acertou:
    print(f'Parabéns! Você acertou o número secreto que é {numero_secreto} em {tentativas} tentativas')
else:
    print(f'Que pena! Você não conseguiu adivinhar o número secreto que era {numero_secreto}')