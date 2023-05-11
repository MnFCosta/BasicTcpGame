data_dict = {'Statusp1': {'Vida': 3, 'Arma': 'Lança', 'Ação': 'Escolha de arma'}, 'Statusp2': {'Vida': 3, 'Arma': 'Espada', 'Ação': 'Escolha de arma'}}

primeira_key= next(iter(data_dict))  # Get the first key

valores_primeira_key = data_dict[primeira_key].values()  # Retrieve the values of the first key

print(list(valores_primeira_key)[0]) 
