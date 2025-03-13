import socket
import pyaudio
import numpy as np

# Setup for sending audio
CHUNK_SIZE = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
# SERVER_IP = 'localhost'
SERVER_IP = '192.168.15.205'
SERVER_PORT = 3306

# Initialize pyaudio
p = pyaudio.PyAudio()

# Open stream for microphone input
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK_SIZE)

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(f"Client started, sending audio to {SERVER_IP}:{SERVER_PORT}")

while True:
    # Capture audio from the microphone
    audio_data = stream.read(CHUNK_SIZE)

    # Send audio data to the server
    client_socket.sendto(audio_data, (SERVER_IP, SERVER_PORT))