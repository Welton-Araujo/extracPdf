# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 10:22:01 2020

@author: weltonaraujo
"""
from tkinter import *

import pdftotext

import nltk

from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

from nltk.corpus import stopwords

from string import punctuation

import glob

base = ['Resultado', 'Eritrócitos', 'Hemoglobina', 'Hematócrito', 'V.C.M', 'H.C.M', 
        'C.H.C.M', 'RDW', 'Leucócitos', 'Mielócitos', 'Metamielócitos', 'Bastonetes', 
        'Segmentados', 'Eosinófilos', 'Basófilos', 'Linfócitos', 'Monócitos', 'Plaquetas']


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
    #print("Lista de PDF: \n" + listPDF)

    resultPharse(listPDF)
       
def resultPharse(pharsespdf):
    resultVet = []
    for i in range(len(pharsespdf)-1):
        textoLinha = word_tokenize(pharsespdf[i], "portuguese")
        for j in range(len(textoLinha)-1):
            for x in base:
                if(textoLinha[j] == x):
                    resultVet.append(textoLinha)
    #print("resultVet: \n" + resultVet)
    #print(len(resultVet))
    valueResult(resultVet)
    
def valueResult(resultVet):
    for j in range(len(resultVet)):
        counter = 0;
        listaInd = []
        for i in range(len(resultVet[j])-1):
            #print(resultVet)
            altDec = resultVet[j][i].replace(",", ".")
            try:
                #print(type(altDec), ": ",float(altDec))
                listaInd.append(float(altDec))
                counter += 1
            except:
                continue 
        verificaInd(listaInd, counter, resultVet[j][0])

def verificaInd(lista, count, name):
    if(count == 2):
            if(lista[0] <= lista[1]):
                print("O valor de(a) " + name +  " está dentro do padrão")
            else:
                print("O valor de(a) " + name +  " está fora do padrão")
    if(count == 3):
            if(lista[1] <= lista[0] <= lista[2]):
                print("O valor de(a) " + name +  " está dentro do padrão")
            else:
                print("O valor de(a) " + name +  " está fora do padrão")
    if(count == 4):
            if((lista[0] == lista[2]) and (lista[1] == lista[3])):
                print("O valor de(a) " + name +  " está dentro do padrão")
            else:
                print("O valor de(a) " + name +  " está fora do padrão")
    if(count == 6):
            if((lista[2] <= lista[0] <= lista[3]) and (lista[4] <= lista[1] <= lista[5])):
                print("O valor de(a) " + name +  " está dentro do padrão")
            else:
                print("O valor de(a) " + name +  " está fora do padrão")

for x in glob.glob("C:\\Users\\weltonaraujo\\Desktop\\pdf\\*.pdf"):
    print("----------------------------------------")
    pdfStr = extractInfoPDF(x)
    phrases(pdfStr)
    print("----------------------------------------")


