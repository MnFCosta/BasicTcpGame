import socket
import json

def run_server():
    host = '127.0.0.1'
    port = 9999

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(2)
    print("Esperando por jogadores...")

    player1, addr1 = server_socket.accept()
    print("Jogador 1 conectado!", addr1)

    player2, addr2 = server_socket.accept()
    print("Jogador 2 conectado!", addr2)

    while True:
        status_j1 = json.loads(player1.recv(1024).decode())
        status_j2 = json.loads(player2.recv(1024).decode())

        """ result = determine_winner(player1_choice, player2_choice) """ 
        print(status_j1)
        print(status_j2)
        """ player1.send(status_j2.encode())
        player2.send(status_j1.encode())  """

        """ if result == "Draw":
            print("It's a draw!")
        else:
            print("Player 1:", player1_choice)
            print("Player 2:", player2_choice)
            print("Result:", result)
            break """

        """ player1.close()
        player2.close() """

""" def determine_winner(choice1, choice2):
    if choice1 == choice2:
        return "Draw"

    if (choice1 == "Rock" and choice2 == "Scissors") or \
       (choice1 == "Paper" and choice2 == "Rock") or \
       (choice1 == "Scissors" and choice2 == "Paper"):
        return "Player 1 wins!"

    return "Player 2 wins!" """

if __name__ == '__main__':
    run_server()