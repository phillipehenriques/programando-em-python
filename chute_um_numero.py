import random

numero_secreto= random.randrange(1,101)
total_tentativas = 0

print("*************************************")
print("Bem vindo ao jogo de chutes!\n")

print("Qual o nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil \n")

nivel = int(input("Defina o nível: "))

if(nivel == 1):
    total_tentativas = 20
elif(nivel ==2):
    total_tentativas = 10
elif(nivel ==3):
    total_tentativas = 5

for rodada in range(1, total_tentativas + 1):
    print("Tentiva {} de {}".format(rodada, total_tentativas))
    chute_str = input("Digite um número entre 1 e 100: ")
    print(f"Você digitou {chute_str}")
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100! Tente novamente.")
        continue
    
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("você acertou!")
        break
    else:
        if(maior):
            print("Você errou! O número secreto é menor que seu chute.")
        elif(menor):
            print("Você errou! O número secreto é maior que seu chute.")

print("Fim de jogo. Obrigado por jogar!")