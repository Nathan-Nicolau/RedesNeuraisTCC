import os
import cv2
from PIL import Image

caminhoImagens = 'C:\\Users\\Gamer\\Documents\\Datasets\\Cromossomos\\Data\\Classes\\'
caminhoRedimensionadas = 'C:\\Users\\Gamer\\Documents\\Datasets\\Redimensionadas\\'
# Vetor que armazena todas as classes de cromossomos identificados
vetorClasses = ['A1', 'A2', 'A3', 'B4', 'B5', 'C6', 'C7', 'C8', 'C9', 'C10', 'C11',
                'C12', 'D13', 'D14', 'D15', 'E16', 'E17', 'E18', 'F19', 'F20', 'G21', 'G22', 'X', 'Y']

vetorTotal = [0]*24
vetorQuantidadeImagens = [0]*24
vetorTamanhos = [0]*24


def realizarContagemImagens():

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

    # print(vetorQuantidadeImagens)
    # print(' ')

    contador = 0
    for i in vetorClasses:
        for j in vetorQuantidadeImagens:
            if contador == 24:
                break
        print('Classe ' + str(i) + ' tem: ' +
              str(vetorQuantidadeImagens[contador]) + ' imagens')
        contador += 1


def lerImagensClasse(classe='', tamanho=0):
    contador = 0
    contadorAuxiliar = 0
    maior = 0
    nome = ''
    largura = 0
    altura = 0
    path = str(caminhoImagens + '\\' + classe + '\\')
    vetorAuxiliar = [0]*1

    for arquivo in os.listdir(path=path):
        if contador == tamanho:
            break
        img = Image.open(path + arquivo)
        valorTamanho = img.width + img.height

        if valorTamanho > maior:
            maior = valorTamanho
            nome = arquivo
            largura = img.width
            altura = img.height

        vetorAuxiliar[0] = 'Imagem ' + \
            str(nome) + ' Largura ' + str(largura) + \
            ' Altura: ' + str(altura)
        contador += 1
    return vetorAuxiliar


def redimensionarImagens(caminho=''):
    img = Image.open(caminho)
    width = img.width + 100
    height = img.height + 100
    img_resized = img.resize((width, height))
    Image._show(img)
    img_resized.save(caminhoRedimensionadas + 'Imagem1.jpg')


if __name__ == '__main__':
    realizarContagemImagens()
    contador = 0
    for i in vetorClasses:
        for j in vetorQuantidadeImagens:
            if contador == 24:
                break
            vetorTotal[contador] == lerImagensClasse(i, j)
        contador += 1
