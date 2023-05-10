import socket

def run_client():
    host = '127.0.0.1'
    port = 9999

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print("Connected to the server.")

    while True:
        choice = input("Enter your choice (Rock, Paper, or Scissors): ")
        client_socket.send(choice.encode())

        result = client_socket.recv(1024).decode()
        print(result)

        if result != "Draw":
            break

    client_socket.close()

if __name__ == '__main__':
    run_client()