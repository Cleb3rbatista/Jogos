import random
def play():
    user=input("Qual e sua escolha? 'R' para pedra, 'P' para papel e 'T' para tesoura\n")
    computer = random.choice(['r','p','t'])
    
    if user == computer:
        return "empate"
        
    if is_win (user,computer):
        return "Parabens, você venceu!"
    
    return"lamento, você perdeu!"
        
def is_win(jogador,computer_oponente):
    if(jogador=='r' and computer_oponente=='t') or (jogador=='p' and computer_oponente=='r') or (jogador=='t' and computer_oponente=='p'):
        return True
print (play())

