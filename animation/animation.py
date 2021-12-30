# Description: This is a virtual assistant program that gets the date, current time, responds back with a
#              random greeting, and returns inforamtion on a person

# pip install pyaudio
# pip install SpeechRecognition
# pip isntall gTTS - google Text To Speech
# pip install wikipedia
# pip install playsound

# SAY 'okay computer hi' then redbuddy smiles to you!
# Example: SAY "Okay computer what's today's date and what time is it and who is Neil Armstrong"

# Import the libraries
import sys,os

# FOR ANIMATION
import pygame
import threading
import sys
print(sys.path)

import face as fm


############## Creating sprites and groups ##############
# bagic

# eyelid
bagic_eyelid_sprites = pygame.sprite.Group()
bagic_eyelid = fm.Eyelid('./animation/default-face-image/eyelid/*.png')
bagic_eyelid_sprites.add(bagic_eyelid)

# eyeball
bagic_eyeball_sprites = pygame.sprite.Group()
bagic_eyeball = fm.Eyeball('./animation/default-face-image/eyeball/*.png')
bagic_eyeball_sprites.add(bagic_eyeball)

# pupil
bagic_pupil_sprites = pygame.sprite.Group()
bagic_pupil = fm.Pupil("./animation/default-face-image/pupil/*.png")
bagic_pupil_sprites.add(bagic_pupil)

# nostril
bagic_nostril_sprites = pygame.sprite.Group()
bagic_nostril = fm.Nostril("./animation/default-face-image/nostril/*.png")
bagic_nostril_sprites.add(bagic_nostril)

# mouth
bagic_mouth_sprites = pygame.sprite.Group()
bagic_mouth = fm.Mouth("./animation/default-face-image/mouth/*.png")
bagic_mouth_sprites.add(bagic_mouth)


class Job(threading.Thread):

    def __init__(self, *args, **kwargs):
        super(Job, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()  # The flag used to pause the thread
        self.__flag.set()  # Set to True
        self.__running = threading.Event()  # Used to stop the thread identification
        self.__running.set()  # Set running to True

    def run(self):
        pygame.init()
        clock = pygame.time.Clock()
        # Game Screen
        screen_width = 650
        screen_height = 1150
        screen = pygame.display.set_mode((screen_width, screen_height))
        background = pygame.image.load("./animation/background.png")
        pygame.display.set_caption("diggy animation")
        pygame.mouse.set_visible(False)
        while self.__running.isSet():
            # return immediately when it is True, block until the internal flag is True when it is False
            self.__flag.wait()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()
            screen.blit(background, (0, 0))

            bagic_eyeball_sprites.draw(screen)
            bagic_eyeball_sprites.update()

            bagic_pupil_sprites.draw(screen)
            bagic_pupil_sprites.update()

            bagic_eyelid_sprites.draw(screen)
            bagic_eyelid_sprites.update()

            bagic_nostril_sprites.draw(screen)
            bagic_nostril_sprites.update()

            bagic_mouth_sprites.draw(screen)
            bagic_mouth_sprites.update()

            clock.tick(10)

    def pause(self):
        self.__flag.clear()  # Set to False to block the thread

    def resume(self):
        self.__flag.set()  # Set to True, let the thread stop blocking

    def stop(self):
        self.__flag.set()  # Resume the thread from the suspended state, if it is already suspended
        self.__running.clear()  # Set to False












