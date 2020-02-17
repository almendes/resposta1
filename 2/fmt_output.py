#!/usr/bin/env python

import sys
import argparse

# se passar parametros pode-se mudar os nomes dos arquivos de entrada e saida
parser = argparse.ArgumentParser(description='Executa a formatacao de saida do arquivo /tmp/output_1.txt')
parser.add_argument('-i', '--input', default='/tmp/output_1.txt', help='Nome do arquivo de entrada')
parser.add_argument('-o', '--output', default='/tmp/output_2.txt', help='Nome do arquivo de saida')
args = parser.parse_args()

# Trata o arquivo
# Linha de print comentadas podem ser habilitadas para imprimir na tela
#
with open(args.input) as entrada: 
 with open(args.output,"w+") as saida:  
   linhas = entrada.readlines()
   # Manipula linha a linha
   for linha in linhas:
     word = linha.split()
     # identifica linhas em branco
     if len(word) == 0:
       # print
       saida.write('') 
       continue
     # identifica linhas diferentes
     if word[0] == "#" or word[0] == "\n" or word[0] == "":
        # print linha  
        saida.write(linha)
     else:
        # Formata as linhas conforme a necessidade
        for i in range(len(word)):
          if i == 0:
            # print (word[i].ljust(17," ")),
            saida.write(word[i].ljust(18," "))
          elif i == 1:
            # print (word[i].ljust(10," ")),
            saida.write(word[i].ljust(11," "))
          elif i == 6:
            # print ("{}  ".format(word[i].ljust(7," "))),
            saida.write("{}  ".format(word[i].ljust(8," ")))
	  else:
            # print ("{}  ".format(word[i])),
            saida.write("{}   ".format(word[i])) 
     #print 
     saida.write("\n")
 saida.close()
entrada.close()
