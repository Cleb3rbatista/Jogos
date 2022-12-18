from ast import Break
from random import*
import os, sys

tabuleiro=[["-" for var in range(20)] for var in range(20)]
bombas=[[randint(0,19) for var in range(2)] for var in range(40)]
for i in range(len(bombas)):
    z=0
    for j in range(len(bombas)):
        if bombas[i][0]==bombas[j][0] and bombas[j][1]==bombas[i][1]:
            z+=1
        if z==2:
            bombas=[[randint(0,19) for var in range(2)] for var in range(40)]
            
cont=(-1)
fim = False

def inicio():
    start=int(input("deseja começar o jogo ?\n"+"1-iniciar\n"+"0-sair\n"))
    if start == 1:
        print(tabuleiro)
    elif start == 0:
        print("saindo...")
        Break
    else:
        print("opção invalida!")
        
    os.system("pause")
    tabuleiro(None,None)
    

def tabuleiro(var,var2):
    fim = False
    global cont
    contador = 0
    os.system('csl')
    for c in (range(len(bombas))):
        if bombas[c][0] == var and bombas[c][1] == var2:
            for e in range(len(bombas)):
                if bombas[e][0] == "X":
                    fim = True
        else:
            if var > 0 and var2 > 0 and var < 19 and var2 < 19:
                       
        
    
    