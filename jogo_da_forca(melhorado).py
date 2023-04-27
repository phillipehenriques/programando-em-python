import random

def jogar_forca():

    intro()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0   

    while(not enforcou and not acertou):
            
        chute = pede_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if(acertou):
        mensagem_ganhador()
    else:
        mensagem_perdedor(palavra_secreta)

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

        print(" |            ")
        print("_|___         ")
        print()

# -- FUNÇÕES DO JOGO -- 

def intro():
        print("*************************************")
        print("Bem vindo ao jogo da forca!\n")

def carrega_palavra_secreta():
        arquivo = open("palavras.txt", "r")
        palavras = []
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

        arquivo. close()

        numero = random.randrange(0, len(palavras))      
        palavra_secreta = palavras[numero].upper()

        return palavra_secreta
        
def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
            chute = input("Digite uma letra: ")
            chute = chute.strip().upper()
            return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):  
            letras_acertadas[index] = letra  
        index += 1

def mensagem_ganhador():
     print("Parabéns você salvou uma vida!")

def mensagem_perdedor(palavra_secreta):
     print("Que pena, você enforcou uma pessoa :(")
     print("A palavra secreta era {}".format(palavra_secreta))

# -- FIM DO SCRIPT --

if(__name__ == "__main__"):
    jogar_forca()
