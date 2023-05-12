import socket
import json

def run_server():
    host = '127.0.0.1'
    port = 5001

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(2)
    print("Esperando por jogadores...")

    player1, addr1 = server_socket.accept()
    print("Jogador 1 conectado!", addr1)

    player2, addr2 = server_socket.accept()
    print("Jogador 2 conectado!", addr2)

    p1_status = {}
    p2_status = {}

    try:
        while True:
            p1_data = player1.recv(1024).decode()
            p2_data = player2.recv(1024).decode()
            try:
                p1_status = json.loads(p1_data)
                p2_status = json.loads(p2_data)
            except:
                pass

            mudar_status(p1_status,p2_status)
            resultado = resultado_jogo(p1_status, p2_status) 
            

            if resultado == "Continua":
                status_dict = {"Você": p1_status,
                            "Inimigo": p2_status}
                
                status_dict2 = {"Você": p2_status,
                            "Inimigo": p1_status}
            

                updated_status_p1 = json.dumps(status_dict)
                updated_status_p2 = json.dumps(status_dict2)


                player1.sendall(updated_status_p1.encode())
                player2.sendall(updated_status_p2.encode())
            else:
                if resultado == "Empate":
                    player1.send(resultado.encode())
                    player2.send(resultado.encode())
                elif resultado == "Jogador 2 ganhou!":
                    player1.send(resultado.encode())
                    player2.send(resultado.encode())
                else:
                    player1.send(resultado.encode())
                    player2.send(resultado.encode())
    except BrokenPipeError:
        print("Todos os clientes conectados não quiseram jogar novamente, fim de jogo!")
        server_socket.close()


def mudar_status(stat_p1, stat_p2):
    #Quando Início do round
    if (stat_p1['Ação'] == 'Escolha de arma' and stat_p2['Ação'] == 'Escolha de arma'):
        #checar vantagem
        if (stat_p1['Vantagem'] == '' and stat_p2['Vantagem'] == ''):
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
    
    #tabela de açoes com as possíveis combinações de escolhas e valores para redução de vida
    acoes = {
        ('Ataque', 'Ataque'): (2, 2),
        ('Ataque Forte', 'Ataque Forte'): (4, 4),
        ('Ataque', 'Ataque Forte'): (4, 2),
        ('Ataque Forte', 'Ataque'): (2, 4),
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
            
def resultado_jogo(stat_p1, stat_p2):
    
    if stat_p1['Vida']  <= 0 and stat_p2['Vida'] <= 0:
        return "Empate!"
    
    elif(stat_p1['Vida'] <= 0):
        return "Jogador 2 ganhou!"
    
    elif(stat_p2['Vida'] <= 0):
        return "Jogador 1 ganhou!"
    else:
        return f"Continua"
    
if __name__ == '__main__':
    run_server()