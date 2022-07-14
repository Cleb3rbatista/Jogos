from calendar import c


tabuleiro = [[0 for i in range(3)]for j in range(3)]
def menu():
    continuar=1
    while continuar:
        continuar = int(input("0. sair\n" + "1. continuar\n"))
        if continuar:
            jogo()
        else:
            print("saindo...")
            
def jogo():
    jogada = 0
    
    while ganhou() == 0:
        print("n\Jogador", jogada%2 + 1 )
        exibir()
        linha= int(input("\nlinha:"))
        coluna= int(input("\ncoluna:"))
        
        if tabuleiro [linha-1][coluna-1] == 0:
            if(jogada%2+1)==1:
                tabuleiro[linha-1][coluna-1] = 1
            else:
                tabuleiro[linha-1][coluna-1] = -1
        else:
            print("não esta vazio")
            jogada = -1
            
        if ganhou():
            print("jogador", jogada%2+1,"ganhou após", jogada+1 ,"rodadas" )

        jogada += 1
def ganhou():
    for i in range(3):
        soma = tabuleiro[i][0]+tabuleiro[i][1]+tabuleiro[i][2]
        if soma==3 or soma==-3:
            return 1
        
    for i in range(3):
        soma = tabuleiro[0][i]+tabuleiro[1][i]+tabuleiro[2][i]
        if soma==3 or soma==-3:
            return 1
    
    diagonal1 = tabuleiro[0][0]+tabuleiro[1][1]+tabuleiro[2][2]
    diagonal2   = tabuleiro[0][2]+tabuleiro[1][1]+tabuleiro[2][0]
    if diagonal1==3 or diagonal1==-3 or diagonal2==3 or diagonal2==-3:  
        return 1
    
    return 0

def exibir():
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j]== 0:
                print(" __",end=' ')
            elif tabuleiro[i][j]== 1:
                print(" X ",end=' ')
            elif tabuleiro[i][j]==-1:
                print(" O ",end=' ')
                
        print()
        
tabuleiro = [ [0,0,0],
              [0,0,0],
              [0,0,0] ]

menu()