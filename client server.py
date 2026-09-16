import socket
import sys


def run_server():
    # Define host and port
    HOST = '127.0.0.1'  # Localhost
    PORT = 65432  # Arbitrary non-privileged port

    # Create a TCP socket
    # AF_INET specifies IPv4, SOCK_STREAM specifies TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Allow immediate reuse of the port after stopping the server
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        # Bind the socket to the address and port
        server_socket.bind((HOST, PORT))
        # Listen for incoming connections (max backlog of 1)
        server_socket.listen(1)
        print(f"[SERVER] Listening on {HOST}:{PORT}...")

        # Accept a connection (blocks until a client connects)
        client_socket, client_address = server_socket.accept()
        print(f"[SERVER] Accepted connection from {client_address}")

        try:
            # Receive data from the client (buffer size 1024 bytes)
            data = client_socket.recv(1024)
            if not data:
                print("[SERVER] Client disconnected before sending data.")
            else:
                # Decode the bytes into a string
                message = data.decode('utf-8')
                print(f"[SERVER] Received message: '{message}'")

        except socket.error as e:
            print(f"[SERVER] Network error while receiving data: {e}")
        finally:
            # Clean up the client connection
            client_socket.close()
            print("[SERVER] Client socket closed.")

    except socket.error as e:
        print(f"[SERVER] Socket error: {e}")
        sys.exit(1)
    finally:
        # Clean up the server listening socket
        server_socket.close()
        print("[SERVER] Server socket closed.")


if __name__ == "__main__":
    run_server()
