import os
import cv2
import xml.etree.ElementTree as Et

xmlFolder = 'C:\\Users\\Gamer\\Documents\\Datasets\\Cromossomos\\Data\\24_chromosomes_object\\annotations\\'
jpgFolder = 'C:\\Users\\Gamer\\Documents\\Datasets\\Cromossomos\\Data\\24_chromosomes_object\\JPEG\\'
classFolder = 'C:\\Users\\Gamer\\Documents\\Datasets\\Cromossomos\\Data\\Classes\\'


contador = 0
for xmlFile in os.listdir(path=xmlFolder):
    contador = contador + 1
    print(contador, '-', xmlFile)

    imgFile = xmlFile.replace('.xml', '.jpg')
    image = cv2.imread(filename=jpgFolder + imgFile)

    # Lendo o xml como lista/json
    tree = Et.parse(xmlFolder + xmlFile)
    root = tree.getroot()

    # Acessando informações do XML
    contadorPares = 0
    for obj in root.findall('object'):
        contadorPares += 1

        # Nome da classe(A1,A2...)
        name = obj.find('name').text

        # Se a pasta da classe nao existe, então ela é criada
        if os.path.exists(path=classFolder + '\\' + name) is False:
            os.mkdir(path=classFolder + '\\' + name)

        # Pega as informações da localização de onde está localizado o cromossomo
        bndBox = obj.find('bndbox')
        xMin = int(bndBox.find('xmin').text)
        xMax = int(bndBox.find('xmax').text)
        yMin = int(bndBox.find('ymin').text)
        yMax = int(bndBox.find('ymax').text)

        # recorte da  Imagem original
        imagemCrop = image[yMin:yMax, xMin:xMax]

        # Se quiser observa as imagens sendo salvas:
        # cv2.imshow('Image',imageCrop)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        # Salvando a imagem na pasta da sua respectiva classe
        cv2.imwrite(
            f'{classFolder}\\{name}\\{xmlFile.replace(".xml","")}-Cromossomo-{name}-{contadorPares}.jpg', imagemCrop)

        if contadorPares == 2:
            contadorPares = 0
