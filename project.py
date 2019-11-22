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
    
def friso1(imagem):
    resultado = imagem.copy()
    for i in range(0,6):
        resultado = translacao(resultado,imagem)

    cv2.imwrite('%s/FRISO1.png' %diretorio_output, resultado)
    
def friso2(imagem):
	imgBranca = branco(imagem)
	x1 = translacao(imagem, imgBranca)
	for i in range(0,2):
		x1 = translacao(x1,x1)
	imagemInv = reflexaoHorizontal(imagem)
	x2 = translacao(imgBranca, imagemInv)
	for i in range(0,2):
		x2 = translacao(x2,x2)
	resultado = concatenaVertical(x1, x2)
	
	cv2.imwrite('%s/FRISO2.png' %diretorio_output, resultado)
	
def friso3(imagem):
    imagem_refletida = reflexaoVertical(imagem)
    resultado = translacao(imagem_refletida,imagem)

    for i in range(0,2):
            resultado = translacao(resultado,resultado)
   
    cv2.imwrite('%s/FRISO3.png' %diretorio_output, resultado)
	 
def friso4(imagem):
	x1 = imagem
	x2 = reflexaoHorizontal(imagem)
	
	for i in range(0,3):
		x1 = translacao(x1,x1)
		x2 = translacao(x2,x2)
	resultado = concatenaVertical(x1,x2)
	
	cv2.imwrite('%s/FRISO4.png' %diretorio_output, resultado)
	
def friso5(imagem):
	imgBranca = branco(imagem)
	x1 = translacao(imagem, imgBranca)
	for i in range(0,2):
		x1 = translacao(x1,x1)
	imagemInv = reflexaoVertical(imagem)
	x2 = translacao(imgBranca, imagemInv)
	for i in range(0,2):
		x2 = translacao(x2,x2)
	resultado = concatenaVertical(x1, x2)
	
	cv2.imwrite('%s/FRISO5.png' %diretorio_output, resultado)	
		
def friso6(imagem):
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
	
	cv2.imwrite('%s/FRISO6.png' %diretorio_output, resultado)	
		
def friso7(imagem):
	imagem_refletida = reflexaoVertical(imagem)
	partedecima = translacao(imagem_refletida,imagem)
	partedebaixo = reflexaoHorizontal(partedecima)
	for i in range(2):
		partedecima = translacao(partedecima, partedecima)
		partedebaixo = translacao(partedebaixo, partedebaixo)
	resultado = concatenaVertical(partedecima, partedebaixo)
	
	cv2.imwrite('%s/FRISO7.png' %diretorio_output, resultado)	


foto = sys.argv[1]
diretorio_output = sys.argv[2]

imagem = cv2.imread(foto, 1)

friso1(imagem)
friso2(imagem)
friso3(imagem)
friso4(imagem)
friso5(imagem)
friso6(imagem)
friso7(imagem)






