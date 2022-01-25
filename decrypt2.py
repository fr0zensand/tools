#!/usr/bin/env python
# coding: utf-8

import re
import os

def decryption(py_doc):
    py_doc = re.sub('==31=','a',py_doc)
    py_doc = re.sub('==45=','b',py_doc)
    py_doc = re.sub('==14=','c',py_doc)
    py_doc = re.sub('==47=','d',py_doc)
    py_doc = re.sub('==18=','e',py_doc)
    py_doc = re.sub('==41=','f',py_doc)
    py_doc = re.sub('==00=','g',py_doc)
    py_doc = re.sub('==24=','h',py_doc)
    py_doc = re.sub('==67=','i',py_doc)
    py_doc = re.sub('==52=','j',py_doc)
    py_doc = re.sub('==23=','k',py_doc)
    py_doc = re.sub('==20=','l',py_doc)
    py_doc = re.sub('==77=','m',py_doc)
    py_doc = re.sub('==85=','n',py_doc)
    py_doc = re.sub('==46=','o',py_doc)
    py_doc = re.sub('==84=','p',py_doc)
    py_doc = re.sub('==64=','q',py_doc)
    py_doc = re.sub('==98=','r',py_doc)
    py_doc = re.sub('==08=','s',py_doc)
    py_doc = re.sub('==92=','t',py_doc)
    py_doc = re.sub('==33=','u',py_doc)
    py_doc = re.sub('==10=','v',py_doc)
    py_doc = re.sub('==11=','w',py_doc)
    py_doc = re.sub('==97=','x',py_doc)
    py_doc = re.sub('==80=','y',py_doc)
    py_doc = re.sub('==42=','z',py_doc)
    py_doc = re.sub('==07=','A',py_doc)
    py_doc = re.sub('==19=','B',py_doc)
    py_doc = re.sub('==78=','C',py_doc)
    py_doc = re.sub('==96=','D',py_doc)
    py_doc = re.sub('==94=','E',py_doc)
    py_doc = re.sub('==28=','F',py_doc)
    py_doc = re.sub('==25=','G',py_doc)
    py_doc = re.sub('==61=','H',py_doc)
    py_doc = re.sub('==95=','I',py_doc)
    py_doc = re.sub('==91=','J',py_doc)
    py_doc = re.sub('==65=','K',py_doc)
    py_doc = re.sub('==89=','L',py_doc)
    py_doc = re.sub('==30=','M',py_doc)
    py_doc = re.sub('==88=','N',py_doc)
    py_doc = re.sub('==57=','O',py_doc)
    py_doc = re.sub('==39=','P',py_doc)
    py_doc = re.sub('==02=','Q',py_doc)
    py_doc = re.sub('==83=','R',py_doc)
    py_doc = re.sub('==15=','S',py_doc)
    py_doc = re.sub('==60=','T',py_doc)
    py_doc = re.sub('==03=','U',py_doc)
    py_doc = re.sub('==59=','V',py_doc)
    py_doc = re.sub('==71=','W',py_doc)
    py_doc = re.sub('==50=','X',py_doc)
    py_doc = re.sub('==66=','Y',py_doc)
    py_doc = re.sub('==05=','Z',py_doc)

    return py_doc
    
if __name__ == "__main__":
    for filename in os.listdir(os.getcwd()):
        infile = open(filename, 'r')
        py_doc = infile.read()
        py_doc = decryption(py_doc)
        print(py_doc,file = open("dcrpt_"+filename[5:],"w"))