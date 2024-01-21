import socket
from cryptography.fernet import Fernet


def receive_data():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8080))
    server_socket.listen(1)

    print("Waiting for a connection...")
    conn, addr = server_socket.accept()
    print(f"Connection from {addr}")

    with open("received.txt", "wb") as file:
        data = conn.recv(1024)
        while data:
            file.write(data)
            data = conn.recv(1024)

    print("Data received successfully!")

    key = b'5tlOpu2Bvib0m_yllgmzfhYVmonJNUR7bKCcdNh827Y='
    cipher = Fernet(key)

    with open("received.txt", "rb") as file:
        content = file.read()

    decrypted_content = cipher.decrypt(content)

    with open("decrypted_received.txt", "wb") as decrypted_file:
        decrypted_file.write(decrypted_content)

    conn.close()
    server_socket.close()


if __name__ == "__main__":
    receive_data()
