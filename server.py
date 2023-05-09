import socket
import random

HOST = ''  # Listen on all available interfaces
PORT = 5000  # The port number to use

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific interface and port
s.bind((HOST, PORT))

# Listen for incoming connections
s.listen()

# Generate a random number between 1 and 100
number = random.randint(1, 10)

# Accept an incoming connection
conn, addr = s.accept()

# Send the number to the client
conn.send(str(number).encode())

# Loop until the correct number is guessed
while True:
    print("Servidor esperando cliente")
    # Receive a guess from the client
    guess = int(conn.recv(1024).decode())

    # Check if the guess is correct, too high, or too low
    if guess == number:
        response = 'correct'
    elif guess > number:
        response = 'lower'
    else:
        response = 'higher'

    # Send the response back to the client
    conn.send(response.encode())