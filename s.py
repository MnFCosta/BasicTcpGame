import socket
import json

def run_server():
    host = '127.0.0.1'
    port = 5000

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

    while True:
        p1_status = json.loads(player1.recv(1024).decode())
        p2_status = json.loads(player2.recv(1024).decode())

        print(p1_status)
        print(p2_status)
        """ result = determine_winner(player1_choice, player2_choice) """ 

        mudar_status(p1_status,p2_status)

        status_dict = {"Você": p1_status,
                       "Inimigo": p2_status}
        
        status_dict2 = {"Você": p2_status,
                       "Inimigo": p1_status}
        
        updated_status_p1 = json.dumps(status_dict)
        updated_status_p2 = json.dumps(status_dict2)

        player1.sendall(updated_status_p1.encode())
        player2.sendall(updated_status_p2.encode())


        """ if result == "Draw":
            print("It's a draw!")
        else:
            print("Player 1:", player1_choice)
            print("Player 2:", player2_choice)
            print("Result:", result)
            break """

        """ player1.close()
        player2.close() """

def mudar_status(stat_p1, stat_p2):
    #Quando Início do round
    if (stat_p1['Ação'] == 'Escolha de arma' and stat_p2['Ação'] == 'Escolha de arma'):
        pass
    #Quando defendido
    if (stat_p1['Ação'] == 'Ataque' and stat_p2['Ação'] == 'Defesa'):
        pass
    elif(stat_p2['Ação'] == 'Ataque' and stat_p1['Ação'] == 'Defesa'):
        pass
    elif(stat_p1['Ação'] == 'Ataque Forte' and stat_p2['Ação'] == 'Defesa'):
        pass
    elif(stat_p2['Ação'] == 'Ataque Forte' and stat_p1['Ação'] == 'Defesa'):
        pass
    #Ataque vs ataque
    elif(stat_p1['Ação'] == 'Ataque' and stat_p2['Ação'] == 'Ataque'):
        stat_p1['Vida'] -= 2
        stat_p2['Vida'] -= 2
    #Ataque forte vs Ataque Forte
    elif(stat_p1['Ação'] == 'Ataque Forte' and stat_p2['Ação'] == 'Ataque Forte'):
        stat_p1['Vida'] -= 6
        stat_p2['Vida'] -= 6
    #Ataque forte vs Ataque
    elif(stat_p1['Ação'] == 'Ataque' and stat_p2['Ação'] == 'Ataque Forte'):
        stat_p1['Vida'] -= 6
        stat_p2['Vida'] -= 2

    elif(stat_p2['Ação'] == 'Ataque' and stat_p1['Ação'] == 'Ataque Forte'):
        stat_p1['Vida'] -= 2
        stat_p2['Vida'] -= 6

""" def resultado_jogo(stat_p1, stat_p2):
    
    if stat_p1[0] & stat_p2[0]== '0':
        return "Empate!"
    
    if(stat_p1[0] == 0):
        return "Jogador 2 ganhou!"
    
    if(stat_p2[0] == 0):
        return "Jogador 1 venceu!" """
    

if __name__ == '__main__':
    run_server()