def jogar_forca():

    print("*************************************")
    print("Bem vindo ao jogo da forca!\n")

    # definindo a palavra secreta e atribuido à uma vaiável
    palavra_secreta = "banana".upper()

    # definindo a lista de letras que foram acertadas

    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    # definindo valores booleanos para as variaveis que finalizam o jogo

    enforcou = False
    acertou = False
    erros = 0

    # imprimindo a palavra_secreta em branco

    print(letras_acertadas)

    # enquanto não FALSE e não False, repetir o laço
    # enquanto TRUE e TRUE, repetir o laço
    # enquanto for TRUE, repetir o laço
    
    while(not enforcou and not acertou):

        # definindo o valor a ser digitado na variável 'chute'

        chute = input("Digite uma letra: ")
        chute = chute.strip().upper()

        # definindo index igual a zero
        
        # a função 'for' vai fazer um loop em cada letra da minha 'palavra_secreta'.
        # caso ela ache a letra ela irá ser impressa no print abaixo junto com o index
        # da letra na 'palavra-secreta'
        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):  # NESSA LINHA, se a letra 'digitada' for igual a letra da 'palavra_secreta'
                    letras_acertadas[index] = letra  # ENTÃO, a letra da 'palavra_secreta' entra na lista, e preenche a sua posição na lista
                index += 1
        else:
            erros += 1

        # fazendo teste para o número máximo de tentativas ser de até 6 vezes

        enforcou = erros == 6

        # fazendo teste para ver se todas as letras foram preenchidas

        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if(acertou):
        print("Parabéns você salvou uma vida!")
    else:
        print("Você condenou uma vida :/")

    print("Fim do jogo")


# -- FIM DO SCRIPT --

if(__name__ == "__main__"):
    jogar_forca()