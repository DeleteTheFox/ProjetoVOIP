import socket
import pyaudio

# Configurações
CHUNK_SIZE = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
SERVER_IP = '192.168.15.205'
SERVER_PORT = 3306

# Inicializa o socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Inicializa PyAudio
p = pyaudio.PyAudio()

# Callback para processar áudio
def callback(in_data, frame_count, time_info, status):
    client_socket.sendto(in_data, (SERVER_IP, SERVER_PORT))
    return (None, pyaudio.paContinue)

# Abre o stream com callback
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK_SIZE,
                stream_callback=callback)

print(f"Client started, sending audio to {SERVER_IP}:{SERVER_PORT}")

# Mantém o programa rodando
stream.start_stream()
try:
    while stream.is_active():
        pass
except KeyboardInterrupt:
    print("\nStopping...")

# Encerra os recursos
stream.stop_stream()
stream.close()
p.terminate()
client_socket.close()
