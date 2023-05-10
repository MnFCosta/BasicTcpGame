import socket

HOST = '127.0.0.1'  # The IP address or hostname of the remote computer
PORT = 5001  # The port number to use

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the remote computer
s.connect((HOST, PORT))

# Receive the number from the server
number = int(s.recv(1024).decode())

# Loop until the correct number is guessed
while True:
    print("Iniciando o jogo!")
    # Input para selecionar o tipo de arma escolhida para a rodada
    personagem = input('\n 1 - Lança \n 2 - Machado \n 3 - Espada \n Escolha a arma de seu gladiador: ')

    # Manda o input da arma para o server
    s.send(personagem.encode())

    # Recebe resposta do server
    response = s.recv(1024).decode()

    # Check if the guess was correct
    print(f'{response}')
    break
    """ if response == 'correct':
        print('Congratulations, you guessed the number!')
        break
    elif response == 'higher':
        print('The number is higher than your guess. Try again.')
    elif response == 'lower':
        print('The number is lower than your guess. Try again.') """