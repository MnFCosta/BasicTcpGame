import socket

HOST = '127.0.0.1'  # The IP address or hostname of the remote computer
PORT = 5000  # The port number to use

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the remote computer
s.connect((HOST, PORT))

# Receive the number from the server
number = int(s.recv(1024).decode())

# Loop until the correct number is guessed
while True:
    print("Iniciando o jogo!")
    # Get a guess from the user
    guess = input('Guess a number between 1 and 100: ')

    # Send the guess to the server
    s.send(guess.encode())

    # Receive a response from the server
    response = s.recv(1024).decode()

    # Check if the guess was correct
    if response == 'correct':
        print('Congratulations, you guessed the number!')
        break
    elif response == 'higher':
        print('The number is higher than your guess. Try again.')
    elif response == 'lower':
        print('The number is lower than your guess. Try again.')