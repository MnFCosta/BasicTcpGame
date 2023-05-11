stat1 = {'Vida': 10,
         'Arma': 'Espada',
         'Ação': 'Ataque',
         'Vantagem': '',}

stat2 = {'Vida': 10,
         'Arma': 'Lança',
         'Ação': 'Ataque',
         'Vantagem': '',}

def mudar_status(stat_p1, stat_p2):
    #Quando Início do round
    if (stat_p1['Ação'] == 'Escolha de arma' and stat_p2['Ação'] == 'Escolha de arma'):
        pass
    
    #checar vantagem
    elif (stat_p1['Vantagem'] == '' and stat_p2['Vantagem'] == ''):
        vantagem_dict = {
            ('Lança', 'Espada'): ('Sim', 'Não'),
            ('Espada', 'Machado'): ('Sim', 'Não'),
            ('Machado', 'Lança'): ('Sim', 'Não'),
            }

        # Usando as armas dos jogadores para procurar no dicionario "vantagem_dict" o valor correspondente de vantagem
        vantagem = vantagem_dict.get((stat_p1['Arma'], stat_p2['Arma']))

        #caso vantagem existir, reduza o hp dos jogadores
        if vantagem:
            stat_p1['Vantagem'] = vantagem[0]
            stat_p2['Vantagem'] = vantagem[1]
        elif stat_p1['Arma'] == stat_p2['Arma']:
            stat_p1['Vantagem'] = 'Não'
            stat_p2['Vantagem'] = 'Não'
        else:
            stat_p1['Vantagem'] = 'Não'
            stat_p2['Vantagem'] = 'Sim'

    """ #Quando defendido
    elif (stat_p1['Ação'] == 'Defesa' and stat_p2['Ação'] == 'Defesa'):
        pass
    elif (stat_p1['Ação'] == 'Ataque' and stat_p2['Ação'] == 'Defesa'):
        pass
    elif(stat_p2['Ação'] == 'Ataque' and stat_p1['Ação'] == 'Defesa'):
        pass
    elif(stat_p1['Ação'] == 'Ataque Forte' and stat_p2['Ação'] == 'Defesa'):
        pass
    elif(stat_p2['Ação'] == 'Ataque Forte' and stat_p1['Ação'] == 'Defesa'):
        pass """
    
    #tabela de açoes com as possíveis combinações de escolhas e valores para redução de vida
    acoes = {
        ('Ataque', 'Ataque'): (2, 2),
        ('Ataque Forte', 'Ataque Forte'): (4, 4),
        ('Ataque', 'Ataque Forte'): (4, 1),
        ('Ataque Forte', 'Ataque'): (1, 4),
        }

    # Usando as acoes dos jogadores para procurar no dicionario "acoes" o valor correspondente  de reducao
    reducao = acoes.get((stat_p1['Ação'], stat_p2['Ação']))

    #caso reducao existir, reduza o hp dos jogadores
    if reducao:
        if(stat_p1['Vantagem'] == 'Sim'):
            stat_p1['Vida'] -= reducao[0] 
            stat_p2['Vida'] -= reducao[1] + 1
        elif(stat_p1['Vantagem'] == stat_p2['Vantagem']):
            stat_p1['Vida'] -= reducao[0] 
            stat_p2['Vida'] -= reducao[1] 
        else:
            stat_p1['Vida'] -= reducao[0] + 1 
            stat_p2['Vida'] -= reducao[1] 


print(stat1)
print(stat2)
mudar_status(stat1,stat2)
print(stat1)
print(stat2)


