# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 10:22:01 2020

@author: weltonaraujo
"""

import pdftotext

import nltk

from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

from nltk.corpus import stopwords

from string import punctuation


base = ['Resultado', 'Eritrócitos', 'Hemoglobina', 'Hematócrito', 'V.C.M', 'H.C.M', 
        'C.H.C.M', 'RDW', 'Leucócitos', 'Mielócitos', 'Metamielócitos', 'Bastonetes', 
        'Segmentados', 'Eosinófilos', 'Basófilos', 'Linfócitos', 'Monócitos', 'Contagem']



def extractInfoPDF(path):
    with open(path, "rb") as f:
        pdf = pdftotext.PDF(f)
    return "\n\n".join(pdf)

def phrases(pdf):
    txtPdf = sent_tokenize(pdf, "portuguese")
    listPDF = []
    for i in range(len(txtPdf)):
        phrasesPDF = txtPdf[i].split('\n')
        for j in range(len(phrasesPDF)):
            listPDF.append(phrasesPDF[j])
    print(listPDF)

    resultPharse(listPDF)
       
def resultPharse(pharsespdf):
    resultVet = []
    for i in range(len(pharsespdf)-1):
        textoLinha = word_tokenize(pharsespdf[i], "portuguese")
        for j in range(len(textoLinha)-1):
            for x in base:
                if(textoLinha[j] == x):
                    resultVet.append(textoLinha)
    print(resultVet)
    print(len(resultVet))
    valueResult(resultVet)
    
def valueResult(resultVet):
    for j in range(len(resultVet)):
        print('------------------------')
        for i in range(len(resultVet[j])-1):
            testeAqui = resultVet[j][i].replace(",", ".")
            try:
                print(type(testeAqui), ": ",float(testeAqui))
            except:
                continue 

pdfStr = extractInfoPDF("C:\\Users\\weltonaraujo\\Desktop\\pdf\\20202718122718.pdf")

phrases(pdfStr)






for i in range(len(resultVet[1])-1):
    testeAqui = resultVet[1][i].replace(",", ".")
    try:
        print(type(testeAqui), ": ",float(testeAqui))
    except:
        continue

var1='2112'
print( type(var1) )
var2 = int(var1)
print( type(var2) )
teste = resultVet[0][2].replace(",", ".")
print(type(float(teste)))

'''           
print(len(resultVet))  
print(resultVet)
print(resultVet[0][2])

resultado = []
for i in range(len(resultVet)):
    tam = len(resultVet[i])
    for j in range(tam):
        if(resultVet[i][j] == ":"):
            resultado.append(resultVet[i][j+1])
print(resultado)

for page in pdf:
    print(page)
      
with open('C:\\Users\\weltonaraujo\\Desktop\\pdf\\ResultadoCreatinina.txt', 'w') as f:
    f.write("\n\n".join(pdf))
    
pdfTxt = open('C:\\Users\\weltonaraujo\\Desktop\\pdf\\ResultadoCreatinina.txt')
print(type(pdfTxt))
linhas = pdfTxt.readlines()
totalLinhas = len(linhas)
#print(linhas)
#print(len(linhas))
print(len(linhas))'''

for i in range(totalLinhas-1):
    textoLinha = word_tokenize(linhas[i], "portuguese")
    for j in range(len(textoLinha)-1):
        if(textoLinha[j] == "Resultado"):
            print(textoLinha)
    
