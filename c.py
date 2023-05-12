import socket
import json

def run_client():
    host = '127.0.0.1'
    port = 5001

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print("Conectado ao servidor.")


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
                      'Ação': 'Escolha de arma',
                      'Vantagem': '',}
            status = json.dumps(status)
            client_socket.sendall(status.encode())
        else:
            resposta = json.loads(resposta)
            print(resposta)
            primeira_key= next(iter(resposta))  # Get the first key
            valores_primeira_key = resposta[primeira_key].values() 
            acao = []
            while acao not in ['1', '2', '3']:
                acao = input('\n 1 - Ataque \n 2 - Ataque Forte  \n 3 - Defender \n Escolha uma ação: ')
                
                if acao == '3' and bloqueios_restante < 1:
                    print("\nVocê não pode mais se defender!.")
                    acao = 4
                
                elif acao == '2' and ataques_fortes < 1:
                    print("\nVocê não pode mais usar ataques fortes!.")
                    acao = 4

                elif acao == '1':
                    acao = "Ataque"
                    break
                elif acao == '2':
                    acao = "Ataque Forte"
                    ataques_fortes -= 1
                    break
                elif acao == '3':
                    acao = "Defender"
                    bloqueios_restante -= 1
                    break
                else:
                    print("\nEscolha invalida, tente novamente!.")
                

            vida_value = list(valores_primeira_key)[0]
            vantagem_value = list(valores_primeira_key)[3]
            
            status = {'Vida': vida_value,
                      'Arma': escolha_arma,
                      'Ação': acao,
                      'Vantagem': vantagem_value,}
            status = json.dumps(status)
            client_socket.sendall(status.encode())
        
        resposta = client_socket.recv(1024).decode()
        
        if resposta == "Empate!":
            print(f"\n{resposta}")
            jogar_denovo = int(input("\n1 - Sim\n 2 - Não\n Deseja jogar o jogo novamente?: "))
            if jogar_denovo == 1:
                escolha_arma = ''
            else:
                break
        elif resposta == "Jogador 1 ganhou!":
            print(f"\n{resposta}")
            jogar_denovo = int(input("\n1 - Sim\n 2 - Não\n Deseja jogar o jogo novamente?: "))
            if jogar_denovo == 1:
                escolha_arma = ''
            else:
                client_socket.close()
                break
        elif resposta == "Jogador 2 ganhou!":
            print(f"\n{resposta}")
            jogar_denovo = int(input("\n1 - Sim\n 2 - Não\n Deseja jogar o jogo novamente?: "))
            if jogar_denovo == 1:
                escolha_arma = ''
            else:
                client_socket.close()
                break
        else:
            pass
    

if __name__ == '__main__':
    run_client()