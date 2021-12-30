import socket
from gtts import gTTS
import time
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Socket
port = 2500
BUFSIZE = 1024

addr = ("localhost", port)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(addr)
print('Waiting.....')

while True:
    data, addr = sock.recvfrom(BUFSIZE)
    print('받은 메시지:' , data.decode())
    if data.decode() == 'hello':
        print('음성 파일 전송중')
        tts = gTTS(
            text = 'Hi',
            lang ='en', slow = False
        )
        print('전송 완료')
    elif data.decode() == 'I\'m so sad':
        print('음성 파일 전송중')
        tts = gTTS(
            text = 'im sorry to hear that. i wanna cheer you up. Listen to music and relax',
            lang ='en', slow = False
        )
        print('전송 완료')
    elif data.decode() == 'I was so surprised':
        print('음성 파일 전송중')
        tts = gTTS(
            text = 'what happened? Calm down and take a deep breath.',
            lang ='en', slow = False
        )
        print('전송 완료')
    
    tts.save('message.mp3')
    
    file_name = 'message.mp3'

    f = open(file_name, "rb")
    data = f.read(BUFSIZE)
    while(data):
        if(sock.sendto(data, addr)):
            data = f.read(BUFSIZE)
            time.sleep(0.02) # Give receiver a bit time to save


    f.close()