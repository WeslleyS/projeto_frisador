#!/bin/bash
echo "Instalando bibliotecas utilizadas no projeto..."
sudo apt-get install python-pip
pip install numpy
pip install opencv-python
echo "Instalação concluida."
