import os
import cv2


def realizarContagemImagens():
    caminhoImagens = 'C:\\Users\\Gamer\\Documents\\Datasets\\Cromossomos\\Data\\Classes\\'
    # Vetor que armazena todas as classes de cromossomos identificados
    vetorClasses = ['A1', 'A2', 'A3', 'B4', 'B5', 'C6', 'C7', 'C8', 'C9', 'C10', 'C11',
                    'C12', 'D13', 'D14', 'D15', 'E16', 'E17', 'E18', 'F19', 'F20', 'G21', 'G22', 'X', 'Y']

    vetorQuantidadeImagens = [0]*24
    contadorImagensClasse = 0
    contadorAuxiliar = 0

    # Leitura da classe
    for i in vetorClasses:
        for j in os.listdir(path=caminhoImagens + '\\' + i):
            if contadorAuxiliar == 24:
                break
            contadorImagensClasse += 1
        vetorQuantidadeImagens[contadorAuxiliar] = contadorImagensClasse
        contadorImagensClasse = 0
        contadorAuxiliar += 1

    print(vetorQuantidadeImagens)
    print(' ')

    contador = 0
    for i in vetorClasses:
        for j in vetorQuantidadeImagens:
            if contador == 24:
                break
        print('Classe ' + str(i) + ' tem: ' +
              str(vetorQuantidadeImagens[contador]) + ' imagens')
        contador += 1


def redimensionarImagens():
    vetorImagens = []


if __name__ == '__main__':
    realizarContagemImagens()
