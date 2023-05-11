import socket
import json

def run_client():
    host = '127.0.0.1'
    port = 5000

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print("Connectado ao servidor.")

    escolha_arma = ''
    acao = ''
    bloqueios_restante = 2
    ataques_fortes = 1
    

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
                      'Arma': escolha_arma,
                      'Ação': 'Escolha de arma',}
            status = json.dumps(status)
            client_socket.sendall(status.encode())
        else:
            print(resposta)
            primeira_key= next(iter(resposta))  # Get the first key
            valores_primeira_key = resposta[primeira_key].values() 
            acao = []
            while acao not in ['1', '2', '3']:
                acao = input('\n 1 - Ataque \n 2 - Ataque Forte  \n 3 - Defender \n Escolha uma ação: ')
                
                if acao == '1':
                    acao = "Ataque"
                    break
                elif acao == '2' and ataques_fortes > 0:
                    acao = "Ataque Forte"
                    ataques_fortes -= 1
                    break
                elif acao == '3' and bloqueios_restante > 0:
                    acao = "Defender"
                    bloqueios_restante -= 1
                    break
                else:
                    print("\nEscolha inválida, tente novamente.")

            vida_value = list(valores_primeira_key)[0]
            
            status = {'Vida': vida_value,
                      'Arma': escolha_arma,
                      'Ação': acao,}
            status = json.dumps(status)
            client_socket.sendall(status.encode())
        
        resposta = json.loads((client_socket.recv(1024).decode()))


    client_socket.close()
                                               

if __name__ == '__main__':
    run_client()