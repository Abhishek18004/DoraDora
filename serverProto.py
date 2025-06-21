from socket import *

# Message Codes
WELCOME_MESSAGE = "161 Welcome to Doraemon message server"
READY_TO_PLAY_MESSAGE = "165 Hello {} are you ready to play"
CLOSING_MESSAGE = "482 Doraemon server closing connection"

def send_receive(client, message):
    try:
        client.send(message.encode("utf-8"))
        response = client.recv(1024).decode("utf-8")
        return response
    except (ConnectionError, socket.error) as e:
        print("Error during communication:", e)
        return ""

server = socket(AF_INET, SOCK_STREAM)
server.bind(('localhost', 55555))
server.listen(1)
print("610 Server is waiting for a player...\n")
client_accepted = False

try:
    client, addr = server.accept()
    addr = str(addr)
    print("121 Client connected: @", addr)
    print("The game is in progress")
    client_accepted = True
    # Conversation initiation
    msg = send_receive(client, WELCOME_MESSAGE)
    response = send_receive(client, READY_TO_PLAY_MESSAGE.format(addr))

    while True:
        msg = send_receive(client, "QUES Is your character a girl.")
        if "yes" in msg.lower():
            # Jaiko, Shizuka, Doraemi
            msg = send_receive(client, "QUES Is she human")
            if "yes" in msg.lower():
                # Jaiko, Shizuka
                msg1 = send_receive(client, "QUES Is she strong")
                msg2 = send_receive(client, "QUES Is she an artist")
                if "yes" in msg1.lower() and "yes" in msg2.lower():
                    # Jaiko
                    msg1 = send_receive(client, "QUES Does she have short hair")
                    msg2 = send_receive(client, "QUES Does she like drawing comic books")
                    if "yes" in msg1.lower() and "yes" in msg2.lower():
                        msg = send_receive(client, "GESS Is your character JAIKO GODA?")
                        if "yes" in msg.lower():
                            client.send("102 Yayy I guessed it right".encode("utf-8"))
                            #file_path = r'D:\GITAM\Sem 4\CN\Protocol Project\characters\Jaiko.png'
                            file_path = r'C:\Users\HP\Documents\Projects\DoraDora\character\Jaiko.png'
                            
                            with open(file_path, 'rb') as file:
                                send_receive(client, "102 Preparing to send image")

                                image_data = file.read()
                                file_size = len(image_data)
                                client.send(str(file_size).encode("utf-8"))  # Send the file size first
                                response = client.recv(1024).decode("utf-8")                               
                                if 'ok' in response.lower():
                                    client.send(image_data)  # Send the image data
                                    response = client.recv(1024).decode("utf-8")
                                    break

                else:
                    # Shizuka
                    msg1 = send_receive(client, "QUES Does your char like baking cookies")
                    msg2 = send_receive(client, "QUES what colour does she wear")
                    if "yes" in msg1.lower() and "pink" in msg2.lower():
                        msg = send_receive(client, "GESS Is your character SHIZUKA MINAMOTO?")
                        if "yes" in msg.lower():
                            client.send("102 Yayy I guessed it right".encode("utf-8"))
                            #file_path = r'D:\GITAM\Sem 4\CN\Protocol Project\characters\Jaiko.png'
                            file_path = r'C:\Users\HP\Documents\Projects\DoraDora\character\Shizuka.png'
                            with open(file_path, 'rb') as file:
                                send_receive(client, "102 Preparing to send image")

                                image_data = file.read()
                                file_size = len(image_data)
                                client.send(str(file_size).encode("utf-8"))  # Send the file size first
                                response = client.recv(1024).decode("utf-8")                               
                                if 'ok' in response.lower():
                                    client.send(image_data)  # Send the image data
                                    response = client.recv(1024).decode("utf-8")
                                    break

            else:
                # Doremi
                msg1 = send_receive(client, "QUES Is she a robot")
                if "yes" in msg1.lower():
                    msg2 = send_receive(client, "QUES Is she strong")
                    if "no" in msg2.lower():
                        msg1 = send_receive(client, "QUES Does she have a bow")
                        msg2 = send_receive(client, "QUES Does she belong to the 22nd century")
                        if "yes" in msg1.lower() and "yes" in msg2.lower():
                            msg = send_receive(client, "GESS Is your character DOREMI?")
                            if "yes" in msg.lower():
                                client.send("102 Yayy I guessed it right".encode("utf-8"))
                                #file_path = r'D:\GITAM\Sem 4\CN\Protocol Project\characters\Jaiko.png'
                                file_path = r'C:\Users\HP\Documents\Projects\DoraDora\character\Doremi.png'
                                with open(file_path, 'rb') as file:
                                    send_receive(client, "102 Preparing to send image")

                                    image_data = file.read()
                                    file_size = len(image_data)
                                    client.send(str(file_size).encode("utf-8"))  # Send the file size first
                                    response = client.recv(1024).decode("utf-8")                               
                                    if 'ok' in response.lower():
                                        client.send(image_data)  # Send the image data
                                        response = client.recv(1024).decode("utf-8")
                                        break

        else:
            # Gian, Nobita, Dekisugi, Suneo, Doraemon
            msg1 = send_receive(client, "QUES Is your character a boy.")
            if "yes" in msg1.lower():
                msg2 = send_receive(client, "QUES Is he human")
                if "yes" in msg2.lower():
                    msg1 = send_receive(client, "QUES Is he strong")
                    if "yes" in msg1.lower():
                        # Gian
                        msg1 = send_receive(client, "QUES Does he like singing")
                        msg2 = send_receive(client, "QUES what colour does he wear")
                        if "yes" in msg1.lower() and "orange" in msg2.lower():
                            msg = send_receive(client, "GESS Is your character TAKESHI GODA (Gian)?")
                            if "yes" in msg.lower():
                                client.send("102 Yayy I guessed it right".encode("utf-8"))
                                #file_path = r'D:\GITAM\Sem 4\CN\Protocol Project\characters\Jaiko.png'
                                file_path = r'C:\Users\HP\Documents\Projects\DoraDora\character\Takeshi.png'
                                with open(file_path, 'rb') as file:
                                    send_receive(client, "102 Preparing to send image")

                                    image_data = file.read()
                                    file_size = len(image_data)
                                    client.send(str(file_size).encode("utf-8"))  # Send the file size first
                                    response = client.recv(1024).decode("utf-8")                               
                                    if 'ok' in response.lower():
                                        client.send(image_data)  # Send the image data
                                        response = client.recv(1024).decode("utf-8")
                                        break

                    else:
                        # Nobita, Dekisugi, Suneo
                        msg1 = send_receive(client, "QUES Does he wear glasses")
                        msg2 = send_receive(client, "QUES Is he rich")
                        msg3 = send_receive(client, "QUES Is he intelligent")
                        if "yes" in msg1.lower():
                            # Nobita
                            msg = send_receive(client, "QUES what colour does he wear")
                            if "yellow" in msg.lower():
                                msg = send_receive(client, "GESS Is your character NOBITA NOBI?")
                                if "yes" in msg.lower():
                                    client.send("102 Yayy I guessed it right".encode("utf-8"))
                                    #file_path = r'D:\GITAM\Sem 4\CN\Protocol Project\characters\Jaiko.png'
                                    file_path = r'C:\Users\HP\Documents\Projects\DoraDora\character\Nobita.png'
                                    with open(file_path, 'rb') as file:
                                        send_receive(client, "102 Preparing to send image")

                                        image_data = file.read()
                                        file_size = len(image_data)
                                        client.send(str(file_size).encode("utf-8"))  # Send the file size first
                                        response = client.recv(1024).decode("utf-8")                               
                                        if 'ok' in response.lower():
                                            client.send(image_data)  # Send the image data
                                            response = client.recv(1024).decode("utf-8")
                                            break

                        elif "yes" in msg2.lower():
                            # Suneo
                            msg = send_receive(client, "QUES what colour does he wear")
                            if "green" in msg.lower():
                                msg = send_receive(client, "GESS Is your character SUNEO HONEKAWA?")
                                if "yes" in msg.lower():
                                    client.send("102 Yayy I guessed it right".encode("utf-8"))
                                    #file_path = r'D:\GITAM\Sem 4\CN\Protocol Project\characters\Jaiko.png'
                                    file_path = r'C:\Users\HP\Documents\Projects\DoraDora\character\Suneo.png'
                                    with open(file_path, 'rb') as file:
                                        send_receive(client, "102 Preparing to send image")

                                        image_data = file.read()
                                        file_size = len(image_data)
                                        client.send(str(file_size).encode("utf-8"))  # Send the file size first
                                        response = client.recv(1024).decode("utf-8")                               
                                        if 'ok' in response.lower():
                                            client.send(image_data)  # Send the image data
                                            response = client.recv(1024).decode("utf-8")
                                            break

                        elif "yes" in msg3.lower():
                            # Dekisugi
                            msg = send_receive(client, "QUES what colour does he wear")
                            if "blue" in msg.lower():
                                msg = send_receive(client, "GESS Is your character HIDETOSHI DEKISUGI?")
                                if "yes" in msg.lower():
                                    client.send("102 Yayy I guessed it right".encode("utf-8"))
                                    #file_path = r'D:\GITAM\Sem 4\CN\Protocol Project\characters\Jaiko.png'
                                    file_path = r'C:\Users\HP\Documents\Projects\DoraDora\character\Dekisugi.png'
                                    with open(file_path, 'rb') as file:
                                        send_receive(client, "102 Preparing to send image")

                                        image_data = file.read()
                                        file_size = len(image_data)
                                        client.send(str(file_size).encode("utf-8"))  # Send the file size first
                                        response = client.recv(1024).decode("utf-8")                               
                                        if 'ok' in response.lower():
                                            client.send(image_data)  # Send the image data
                                            response = client.recv(1024).decode("utf-8")
                                            break

                else:
                    # Doraemon
                    msg1 = send_receive(client, "QUES Is he a robot")
                    if "yes" in msg1.lower():
                        msg2 = send_receive(client, "QUES Is he strong")
                        if "no" in msg2.lower():
                            msg1 = send_receive(client, "QUES Does he have a bow")
                            msg2 = send_receive(client, "QUES Does he belong to the 22nd century")
                            if "no" in msg1.lower() and "yes" in msg2.lower():
                                msg = send_receive(client, "GESS Is your character DORAEMON?")
                                if "yes" in msg.lower():
                                    client.send("102 Yayy I guessed it right".encode("utf-8"))
                                    #file_path = r'D:\GITAM\Sem 4\CN\Protocol Project\characters\Jaiko.png'
                                    file_path = r'C:\Users\HP\Documents\Projects\DoraDora\character\Doraemon.png'
                                    with open(file_path, 'rb') as file:
                                        send_receive(client, "102 Preparing to send image")

                                        image_data = file.read()
                                        file_size = len(image_data)
                                        client.send(str(file_size).encode("utf-8"))  # Send the file size first
                                        response = client.recv(1024).decode("utf-8")                               
                                        if 'ok' in response.lower():
                                            client.send(image_data)  # Send the image data
                                            response = client.recv(1024).decode("utf-8")
                                            break

    # End of the game
    msg1=send_receive(client, "102 Image sent successfully, check the folder which has client programs")
    print("Image sent successfully")
    msg2= send_receive(client, "102 Thank you for playing")
    if 'quit' in msg2.lower():
        client.send(CLOSING_MESSAGE.encode("utf-8"))
        print(CLOSING_MESSAGE)

except Exception as e:
    print("An error occurred:", e)

finally:
    client.close()
    server.close()
