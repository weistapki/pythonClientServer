import socket
from cryptography.fernet import Fernet


def send_data():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    with open('secret.txt', 'rb') as file:
        content = file.read()

    key = b'5tlOpu2Bvib0m_yllgmzfhYVmonJNUR7bKCcdNh827Y='
    cipher = Fernet(key)

    encrypted_content = cipher.encrypt(content)

    try:
        server_address = ('localhost', 8080)
        client_socket.connect(server_address)

        client_socket.sendall(encrypted_content)
        print("Data sent successfully!")
    finally:
        client_socket.close()


if __name__ == "__main__":
    send_data()
