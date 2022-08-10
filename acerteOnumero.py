import random
 
def aleatorio(x):
    randow_numero = random.randint(1, x)
    aleatorio = 0
    while aleatorio!= randow_numero:
        aleatorio = int(input(f'adivinhe um numero aleatorio entre 1 e {x}: '))
        if aleatorio < randow_numero:
            print("desculpe, adivinhe novamente, muito baixo ")
        elif aleatorio > randow_numero:
            print("desculpe, adivinhe novamente, muito alto ")
        
    print(f"parabens, voce acertou o numero {randow_numero} e correto")
    
aleatorio(10)
