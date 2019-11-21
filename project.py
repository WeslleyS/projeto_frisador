# coding: utf-8
import numpy as np
import cv2
import sys
  
def rotaciona(imagemOriginal, angulo):
    imagem = imagemOriginal.copy()
    (alt, lar) = imagem.shape[:2] #captura altura e largura
    centro = (lar / 2, alt / 2) #acha o centro
    rotacao = cv2.getRotationMatrix2D(centro, angulo, 1.0) #180
    return cv2.warpAffine(imagem, rotacao, (lar, alt))
    
def branco(imagemOriginal):
    imagem = imagemOriginal.copy()
    for y in range(0, imagem.shape[0]):
         for x in range(0, imagem.shape[1]):
             imagem[y, x] = (255,255,255)
    return imagem

def translacao(imagem,imagem2):
    return np.concatenate((imagem, imagem2), axis=1)

def concatenaVertical(imagem,imagem2):
    return np.concatenate((imagem, imagem2), axis=0)

def salva(imagem):
    cv2.imwrite('saida.png', imagem)

def reflexaoHorizontal(imagem):
    return imagem[::-1,:]

def reflexaoVertical(imagem):
    return imagem[:,::-1]
    
def reflexaoHV(imagem):
    return imagem[::-1,::-1]
    
def friso1EU(imagem):
    resultado = imagem.copy()
    for i in range(0,6):
        resultado = translacao(resultado,imagem)
    #cv2.imshow("F1", resultado)
    cv2.imwrite('FRISO1.png', resultado)
    
def friso2EU(imagem):
	imgBranca = branco(imagem)
	x1 = translacao(imagem, imgBranca)
	for i in range(0,2):
		x1 = translacao(x1,x1)
	imagemInv = reflexaoHorizontal(imagem)
	x2 = translacao(imgBranca, imagemInv)
	for i in range(0,2):
		x2 = translacao(x2,x2)
	resultado = concatenaVertical(x1, x2)
	#cv2.imshow("F2", resultado)
	cv2.imwrite('FRISO2.png', resultado)
	
def friso3EU(imagem):
    imagem_refletida = reflexaoVertical(imagem)
    resultado = translacao(imagem_refletida,imagem)

    for i in range(0,2):
            resultado = translacao(resultado,resultado)
    #cv2.imshow("F3", resultado)
    cv2.imwrite('FRISO3.png', resultado)
	 
def friso4EU(imagem):
	x1 = imagem
	x2 = reflexaoHorizontal(imagem)
	
	for i in range(0,3):
		x1 = translacao(x1,x1)
		x2 = translacao(x2,x2)
	resultado = concatenaVertical(x1,x2)
	#cv2.imshow("F4", resultado)
	cv2.imwrite('FRISO4.png', resultado)
	
def friso5EU(imagem):
	imgBranca = branco(imagem)
	x1 = translacao(imagem, imgBranca)
	for i in range(0,2):
		x1 = translacao(x1,x1)
	imagemInv = reflexaoVertical(imagem)
	x2 = translacao(imgBranca, imagemInv)
	for i in range(0,2):
		x2 = translacao(x2,x2)
	resultado = concatenaVertical(x1, x2)
	#cv2.imshow("F5", resultado)
	cv2.imwrite('FRISO5.png', resultado)	
		
def friso6EU(imagem):
	imagem_refletida = reflexaoVertical(imagem)
	partedecima = translacao(imagem_refletida,imagem)
	imgBranca = branco(partedecima)
	partedebaixo = reflexaoHorizontal(partedecima)
	
	partedecima = translacao(partedecima, imgBranca)
	partedebaixo = translacao(imgBranca, partedebaixo)
	for i in range(1):
		partedecima = translacao(partedecima, partedecima)
		partedebaixo = translacao(partedebaixo, partedebaixo)
	
	resultado = concatenaVertical(partedecima, partedebaixo)
	#cv2.imshow("F6", resultado)
	cv2.imwrite('FRISO6.png', resultado)	
		
def friso7EU(imagem):
	imagem_refletida = reflexaoVertical(imagem)
	partedecima = translacao(imagem_refletida,imagem)
	partedebaixo = reflexaoHorizontal(partedecima)
	for i in range(2):
		partedecima = translacao(partedecima, partedecima)
		partedebaixo = translacao(partedebaixo, partedebaixo)
	resultado = concatenaVertical(partedecima, partedebaixo)
	#cv2.imshow("F7", resultado)
	cv2.imwrite('FRISO7.png', resultado)	

foto = sys.argv[1]
diretorio_output = sys.argv[2]

imagem = cv2.imread(foto, 1)


friso1EU(imagem)
friso2EU(imagem)
friso3EU(imagem)
friso4EU(imagem)
friso5EU(imagem)
friso6EU(imagem)
friso7EU(imagem)

#cv2.waitKey(0)





