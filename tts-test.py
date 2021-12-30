from gtts import gTTS

tts = gTTS(
    text = '하이루',
    lang ='ko', slow = False
)

tts.save('하이루.mp3')