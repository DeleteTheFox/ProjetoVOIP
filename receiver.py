import socket
import pyaudio
import numpy as np


#Teste commit pelo linux
# Setup for receiving audio
CHUNK_SIZE = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
HOST = '192.168.12.196'
PORT = 3306

# Initialize pyaudio
p = pyaudio.PyAudio()

# Open stream for playback
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                output=True,
                frames_per_buffer=CHUNK_SIZE)

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

print(f"Server started at {HOST}:{PORT}, waiting for audio data...")

while True:
    # Receive audio data from the client
    data, addr = server_socket.recvfrom(CHUNK_SIZE * 2)  # Adjust based on chunk size
    if data:
        audio_data = np.frombuffer(data, dtype=np.int16)
        stream.write(audio_data.tobytes())  # Play the received audio
