import random
def jogo_acerta_palavra():
    mylist = ["amarelo", "banana", "piso", "precioso", "hunched" , "dado", \
                "Rabino", "agudo", "antro", "anunciar", "bebida", "enfermeira",\
                "urso", "chefe", "sangrar", "ombros", "barco", "senhora", "escrita"]
    palavra_aleatoria=random.choice(mylist)
    palavra_secreta = palavra_aleatoria.upper()
    letras_acertadas = ''
    entrar_sair = input("Jogo de acerta a palavra secreta [E]ntrar e [S]air\n").upper()
    contador_tentativas = 0
    if entrar_sair == 'E':
        while contador_tentativas >= 0:
            letra_dig= input("Digite uma letra: ").upper()
            if len(letra_dig) > 1:
                print("Digite apenas uma letra")
                contador_tentativas += 1
                print(palavra_formada)
                continue
            if letras_acertadas.count(letra_dig) != 0:
                print("Voce ja digitou essa letra antes")
                contador_tentativas += 1
                print(palavra_formada)
                continue
            if palavra_secreta.count(letra_dig) != 0:
                print("A letra pertence a palavra secreta")
                contador_tentativas += 1
                if letra_dig in palavra_secreta:
                    letras_acertadas += letra_dig  
                palavra_formada = ''            
                for letras_secreta in palavra_secreta:
                    if letras_secreta in letras_acertadas:
                        palavra_formada +=letras_secreta
                    else:
                        palavra_formada += "*"   
                print(palavra_formada)
                if palavra_formada == palavra_secreta:
                    print("PARABENS!!, VOCE GANHOU" 
                        " voce ganhou em " , contador_tentativas , "tentativas",
                        "a palavra certa e ", palavra_formada)
                    jogar_novamente = input("Deseja jogar novamente ? [S]im ou [N]ão?\n ").upper()
                    while True:    
                        if jogar_novamente == "S":
                            contador_tentativas= 0
                            letras_acertadas = ''
                            jogo_acerta_palavra()
                        elif jogar_novamente == "N":
                            print("Saindo...")
                            break
                        else:
                            print("opção invalida!")
                            continue
            elif palavra_secreta.count(letra_dig) == 0:
                print(" A letra digitada não pertence a palavra secreta")
                contador_tentativas += 1 
                print(palavra_formada)       
    elif entrar_sair == "S":
        print ("Saindo...");
    else:
        print("Valor digitado invalido")
        
jogo_acerta_palavra()