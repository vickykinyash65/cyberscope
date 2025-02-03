from cryptography.fernet import Fernet
import socket

class CyberScope:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)

    def encrypt_message(self, message: str) -> bytes:
        """Encrypts a message using Fernet symmetric encryption."""
        encoded_message = message.encode()
        encrypted_message = self.cipher_suite.encrypt(encoded_message)
        return encrypted_message

    def decrypt_message(self, encrypted_message: bytes) -> str:
        """Decrypts a message using Fernet symmetric encryption."""
        decrypted_message = self.cipher_suite.decrypt(encrypted_message)
        return decrypted_message.decode()

    def start_server(self, host: str, port: int):
        """Starts a server to receive encrypted messages."""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((host, port))
            s.listen()
            print(f"Server listening on {host}:{port}")
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    decrypted_data = self.decrypt_message(data)
                    print(f"Received encrypted data: {data}")
                    print(f"Decrypted message: {decrypted_data}")

    def send_message(self, host: str, port: int, message: str):
        """Sends an encrypted message to a specified host and port."""
        encrypted_message = self.encrypt_message(message)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            s.sendall(encrypted_message)
            print(f"Sent encrypted message: {encrypted_message}")

if __name__ == "__main__":
    cyber_scope = CyberScope()
    # Example usage:
    # To start the server:
    # cyber_scope.start_server('127.0.0.1', 65432)
    
    # To send a message:
    # cyber_scope.send_message('127.0.0.1', 65432, "Hello, World!")