from pytube import YouTube
import cv2
import matplotlib.pyplot as plt

# URL do vídeo do YouTube
video_url = 'https://www.youtube.com/watch?v=em1lhLC06M0'

# Baixe o vídeo
yt = YouTube(video_url)
stream = yt.streams.get_highest_resolution()
stream.download()

# Abra o vídeo baixado
video_capture = cv2.VideoCapture(yt.title + ".mp4")

# Verifique se o vídeo foi aberto corretamente
if not video_capture.isOpened():
    print("Erro ao abrir o vídeo.")
    exit()

frame_count = 0

while True:
    # Leia um quadro do vídeo
    ret, frame = video_capture.read()

    # Verifique se a leitura do quadro foi bem-sucedida
    if not ret:
        break

    # Exibir o quadro usando Matplotlib
    plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    plt.show(block=False)
    plt.pause(0.1)
    plt.clf()

    # Faça algo com o quadro, como análise

    # Incrementa o contador de quadros
    frame_count += 1

# Libere o objeto de captura e feche a janela Matplotlib
video_capture.release()
plt.close()
