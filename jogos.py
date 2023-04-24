import chute_um_numero
import jogo_da_forca

def escolha_o_jogo():
    print("*************************************")
    print("Bem vindo a seleção de jogos!\n")

    jogo = int(input("Qual jogo você quer jogar? "))
    print("(1) Forca \n(2) Chute um número \n")

    if(jogo == 1):
        jogo_da_forca.jogar_forca()
    elif(jogo ==2):
        chute_um_numero.jogar_chute()

if(__name__ == "__main__"):
    escolha_o_jogo()