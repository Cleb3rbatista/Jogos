import random
from tkinter import N
def play():
    user=input("Qual e sua escolha? 'R' para pedra, 'P' para papel e 'T' para tesoura"/N)
    computer=random.choice(['r''p''t'])
        if user==computer:
            return 'tie'
        if ()
def is_win(jogador,computer_oponente):
    if(jogador=='r' and computer_oponente=='t') or (jogador=='p' and computer_oponente=='r') or (jogador=='t' and computer_oponente=='p'):
        return True