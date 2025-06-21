# DoraDora - Socket-based Doraemon Character Guessing Game

**DoraDora** is a client-server game developed on a network using Python's socket programming. The user responds to a set of Yes/No questions regarding a mystery Doraemon character, and the server attempts to guess the character from the answers. After being guessed correctly, the server will send an image of the character to the client.


## Features

- **Interactive Character Guessing**
    - User plays by responding to server-created questions.
    - Server filters down the character smartly.

- **File Transfer**
    - When correctly guessed, the server transfers a character picture (`char.png`) to the client.

- **Predefined Character Set**
    - Has characters such as Doraemon, Nobita, Shizuka, Gian, Suneo, Jaiko, Dekisugi, and Doraemi.

- **Structured Protocol**
    - Utilizes message codes such as `QUES`, `GESS`, and `102` to ensure simplicity while communicating.


## Tech Stack

- **Language**: Python 3
- **Modules**: `socket`, `os` (optional), `shutil` (for older versions)
- **Platform**: Console-based client-server architecture


## Getting Started

```bash
# 1. Clone the repository
git clone https://github.com/your-username/DoraDora.git
cd DoraDora

# 2. Ensure Python 3 is installed
python --version

# 3. (Optional but recommended) Create a virtual environment
python -m venv venv
venv\Scripts\activate  # For Windows
source venv/bin/activate  # For Mac/Linux

# 4. Run the server
python serverProto.py

# 5. In another terminal, run the client
python clientProto.py
```


## How It Works

1. **Server** waits for a client connection.
2. **Client** sends a greeting message.
3. **Server** initiates a series of yes/no questions to guess the character.
4. Once guessed:
   - Server sends an image of the guessed character.
   - Client receives and stores it as `char.png`.
5. Both sides close the connection gracefully.


## Project Structure

```bash
DoraDora/
│
├── clientProto.py            # Handles communication and image reception
├── serverProto.py            # Manages logic, questions, and image sending
├── character/
│   ├── Doraemon.png
│   ├── Nobita.png
│   ├── Shizuka.png
│   ├── Gian.png
│   ├── Suneo.png
│   ├── Jaiko.png
│   ├── Doremi.png
│   └── Dekisugi.png
├── README.md
```

## Screenshots

1. **Connection** – Shows how the terminal looks when the client successfully connects to the server.  
   ![Server Connected](screenshots/ServerConnected.png)
   ![Client Connected](screenshots/ClientConnected.png)

2. **Question Exchange** – Server sends a question, and then the client responds with Yes/No.
   ![Question Exchange](screenshots/question_exchange.png)

3. **Server Guessing** – Server makes a guess with "GESS Is your character ABC?" and then it awaits confirmation.
   ![Server Guessing](screenshots/server_guessing.png)

4. **Correct Guess & Confirmation** – Server receives a "yes" response from the user and sends a celebration message.  
   ![Correct Guess](screenshots/correct_guess.png)


## Future Improvements

- GUI using `tkinter` or `PyQt`
- Adding more characters from the show
- Support multiplayer (two clients competing to help server guess faster)
- Add difficulty levels


## Developed by Team DoraDora

- Abhishek Karthik
- Deevi Veena Sree
- Mahi Shukla  
- Prasuk Jain
- R Sri Sai Lahari 


Enjoy the nostalgia through the Doraemon's world!
