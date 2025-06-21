from socket import *

def receive(client):
    response = client.recv(1024).decode("utf-8")
    print("\nServer:", response)
    return response

client = socket(AF_INET, SOCK_STREAM)
client.connect(('localhost', 55555))

try:
    msg = receive(client)
    client.send("102 Konnichiwa doradora.com".encode('utf-8'))
    print("Client: 102 Konnichiwa doradora.com")

    if "welcome" in msg.lower():
        msg1 = receive(client)
        client.send("102 ok".encode('utf-8'))
        print("Client: 102 ok")
        while True:
            msg = receive(client)
            if "thank you" in msg.lower():
                break
            elif "ques" in msg.lower():                
                answer = input("Client: ANSR ")
                msg = "ANSR " + answer
                client.send(msg.encode("utf-8"))
                continue
            elif "gess" in msg.lower():
                answer = input("Client: ANSR ")
                msg = "ANSR " + answer
                client.send(msg.encode("utf-8"))
            elif "yayy" in msg.lower():
                file = open('char.png', "wb")
                msg1=receive(client)
                client.send("102 Ready to receive".encode("utf-8"))
                print("Client: 102 Ready to receive")
                
                file_size= int(client.recv(1024).decode('utf-8'))  # Receive file size
                client.send("102 ok".encode("utf-8"))
                received_size = 0
                try:
                    while received_size < file_size:
                        image_chunk = client.recv(2048)  # Receive image data
                        file.write(image_chunk)
                        received_size += len(image_chunk)
                finally:
                    file.close()  # Ensure file is closed even if an error occurs
                client.send("102 ok".encode("utf-8"))
                msg1=receive(client)
                client.send("102 Image received".encode("utf-8"))
                print("Client: 102 Image received")
                break
            else:
                break

    response = client.recv(1024).decode("utf-8")
    print("\nServer:", response)
    client.send('QUIT'.encode("utf-8"))
    print("Client: QUIT")
    response = client.recv(1024).decode("utf-8")
    print("\nServer:", response)

except Exception as e:
    print("An error occurred:", e)

client.close()
