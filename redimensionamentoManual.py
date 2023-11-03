import os
import cv2
from PIL import Image

caminhoImagens = 'C:\\Users\\Gamer\\Documents\\Datasets\\Cromossomos\\Data\\Classes\\'
caminhoRedimensionadasMaior = 'C:\\Users\\Gamer\\Documents\\Datasets\\CromossomosAjustados_317_x_212\\'
caminhoRedimensionadasMenor = 'C:\\Users\\Gamer\\Documents\\Datasets\\CromossososAjustados_52_x_52\\'

# Vetor que armazena todas as classes de cromossomos identificados
vetorClasses = ['A1', 'A2', 'A3', 'B4', 'B5', 'C6', 'C7', 'C8', 'C9', 'C10', 'C11',
                'C12', 'D13', 'D14', 'D15', 'E16', 'E17', 'E18', 'F19', 'F20', 'G21', 'G22', 'X', 'Y']


tamanhoMaximoRedimensionamento = [317, 212]
tamanhoMinimoRedimensionamento = [100, 100]

vetorTotal = [0]*24
vetorQuantidadeImagens = [0]*24
vetorTamanhos = [0]*24


def redimensionarImagensMaior(caminho='', classe=''):
    contador = 0
    caminhoSalvamento = caminhoRedimensionadasMaior + classe
    for arquivo in os.listdir(path=caminho + classe):
        # Possível limite de imagens estabelecido para testes
        if contador == 200:
            break
        img = Image.open(caminho + classe + '\\' + arquivo)
        img_resized = img.resize(
            (tamanhoMaximoRedimensionamento[0], tamanhoMaximoRedimensionamento[1]))
        if os.path.exists(path=caminhoSalvamento) is False:
            os.mkdir(path=caminhoSalvamento)
        img_resized.save(caminhoSalvamento + '\\' + arquivo)
        contador += 1


def redimensionarImagensMenor(caminho='', classe=''):
    contador = 0
    if os.path.exists(path=caminhoRedimensionadasMenor) is False:
        os.mkdir(path=caminhoRedimensionadasMenor)

    caminhoSalvamento = caminhoRedimensionadasMenor + classe
    for arquivo in os.listdir(path=caminho + classe):
        if contador == 200:
            break
        img = Image.open(caminho + classe + '\\' + arquivo)
        img_resized = img.resize(
            (tamanhoMinimoRedimensionamento[0], tamanhoMinimoRedimensionamento[1]))
        if os.path.exists(path=caminhoSalvamento) is False:
            os.mkdir(path=caminhoSalvamento)
        img_resized.save(caminhoSalvamento + '\\' + arquivo)
        contador += 1


def redimensionarUmaClasse(caminho='', classe='', tamanho=0):
    contador = 0
    caminhoSalvamento = caminhoRedimensionadasMaior + classe + '\\'
    for arquivo in os.listdir(path=caminho + classe):
        img = Image.open(caminho + classe + '\\' + arquivo)
        img_resized = img.resize(
            (tamanhoMaximoRedimensionamento[0], tamanhoMaximoRedimensionamento[1]))
        if os.path.exists(path=caminhoSalvamento) is False:
            os.mkdir(path=caminhoSalvamento)
        img_resized.save(caminhoSalvamento + arquivo)
        contador += 1


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


if __name__ == '__main__':
    realizarContagemImagens()
    # contador = 0
    # for i in vetorClasses:
    #    if contador == 24:
    #        break
    #    redimensionarImagensMaior(caminhoImagens, i)
    #    contador += 1
    #
    contador = 0
    for i in vetorClasses:
        if contador == 24:
            break
        redimensionarImagensMenor(caminhoImagens, i)
        contador += 1
