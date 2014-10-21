#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
# ------------------------------------------------------------------------- #
  Objetivo:  Ler xml com problema de caracter e gravar em forma binaria do codigo unicode - legivel no navegador
    Script:  SetRightUnicode.py
   Chamada:  python SetRightUnicode.py
# ------------------------------------------------------------------------- #
#   DATA    Responsaveis      Comentarios
# 20110201  Fabio Brito       Edicao original

OBJETIVO: deixar os caracteres que ficarao em ISIS e que nao se consegue a visualizacao adequada no navegador,
na FORMA BINARIA DO CODIGO UNICODE


# Os caracteres são armazenados em XML e HTML na forma binária do código Unicode (desde que a codificação em uso suporte o código). Alternativamente, pode-se armazená-los como referências numéricas baseadas no seu respectivo código, seguindo o formato &#valor; (no qual "valor" é o código em notação decimal) ou &#xvalor; (código em notação hexadecimal; note o "x" antes do 
valor);

# Por exemplo, as referências &#916;, &#1049;, &#1511;, &#1605;, &#3671;, &#12354;, &#21494;, &#33865; e &#45307; são visualizadas nos navegadores respectivamente como Δ, Й, ק, م, ๗, あ, 叶, 葉 e 냻. Se as fontes apropriadas existem, tais símbolos aparecem respectivamente como a letra maiúscula grega "delta", a letra maiúscula cirílica "I curta", a letra árabe "Meem", a letra hebraica "Qof", o numeral tailandês 7, o hiragana japonês "A", a letra do chinês simplificado "folha", a letra do chinês tradicional "folha" e a sílaba hangul "Nyaelh".


Links para referencia
http://pt.wikipedia.org/wiki/Unicode#World_Wide_Web

http://www.python.org.br/wiki/TudoSobrePythoneUnicode


'''


import glob, os
from xml.etree.ElementTree import ElementTree

# definicao dos path's
path_arquivos_originais = '/home/xmls/*.xml'
diretorio_convertidos = '/home/xmls/convertidos'

# verifica a existencia do diretorio, cria se nao existir
if not os.path.exists(diretorio_convertidos):
    os.makedirs(diretorio_convertidos)

# lista arquivos para processamento
lista_arquivos = glob.glob(path_arquivos_originais)

# Funcao para resgatar nome do arquivo sem extencao
def trazNome(arquivo):
    list_PathArquivo = os.path.split(arquivo)
    nameArquivoComExtencao = list_PathArquivo[-1]
    list_nameArquivoComExtencao = nameArquivoComExtencao.split('.')
    nameArquivo = list_nameArquivoComExtencao[-2]
    output = diretorio_convertidos + "/" + nameArquivo + "_output.xml"
    return output


# processamento
for arquivo in lista_arquivos:
    print 'Convertendo arquivo', arquivo
    tree = ElementTree(file=arquivo)
    output = trazNome(arquivo)
    print '  => Criando: ',output
    tree.write(output)

print 'Termino'

