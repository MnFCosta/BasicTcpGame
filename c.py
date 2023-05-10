import socket
import json

def run_client():
    host = '127.0.0.1'
    port = 9999

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print("Connectado ao servidor.")

    escolha_arma = ''
    acao = ''
    

    while True:
        if escolha_arma == '':
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
                    print("\nEscolha inválida, tente novamente.")
                    
            status = {'Vida': 10,
                      'Arma': escolha_arma}
            status = json.dumps(status)
            client_socket.sendall(status.encode())
        else:
            acao = input('\n 1 - Ataque \n 2 - Ataque Forte  \n 3 - Defender \n Escolha uma ação: ')
        
        """ client_socket.send(choice.encode()) """

        result = client_socket.recv(1024).decode()

        if result != "Draw":
            break

    client_socket.close()

if __name__ == '__main__':
    run_client()