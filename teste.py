escolha_arma = None

while escolha_arma not in ['1', '2', '3']:
    escolha_arma = input('\n 1 - Lança \n 2 - Machado \n 3 - Espada \n Escolha a arma de seu gladiador: ')
    
    if escolha_arma == '1':
        escolha_arma = "Lança"
        break
    elif escolha_arma == '2':
        escolha_arma = "Machado"
        break
    elif escolha_arma == '3':
        escolha_arma = "Espada"
        break
    else:
        print("Escolha inválida!")
        

print("Arma escolhida:", escolha_arma)