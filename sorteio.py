import random
import os


lista = []
lista_sorteados = []
lista_temp = []
lista_removidos = []

while True:
    nome = input("Digite os nomes que serão sorteados ")
    if nome != '':
        lista.append(nome) # Adiciona o nome na lista, função append(parametro)
    else:
        break

lista_temp = lista.copy()
while True:
    if lista_temp:
        os.system('cls')
        premiado = random.choice(lista_temp)
        lista_sorteados.append(premiado)
        lista_temp.remove(premiado)

        print(f'O premiado da vez é o {premiado}')
        

        opcao = input("Deseja realizar um novo sorteio? (s/n)").lower()
        os.system('cls')

        if opcao != 's':
            break
    else:
        print("Não existe nomes para serem sorteados")
print("Sistema finalizado!")
print(f'Lista do sorteio:  {lista}')
print(f'Listas de sorteados: {lista_sorteados}')


