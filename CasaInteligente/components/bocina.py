import pygame
from threading import Thread
from youtube_dl import YoutubeDL
from youtubesearchpython import VideosSearch
import sys
import os
import time


def play_sound():
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue

"""
Esta clase es para utilizar el jack 3.5 mm para reproducir sonido
"""
class Bocina(object):
    def __init__(self, path, name):
        """
        Constructor del objeto

        Args:
            path (str): Path donde se encuentra el archivo de sonido que se va a reproducir en la alarma
            name (str): Nombre del dispositivo
        """        
        self.name = name
        self.path = path
        pygame.mixer.init()
        pygame.mixer.music.load(path)

    def on(self):
        """
        Crea un Thread para reproducir el archivo
        """        
        Thread(target=play_sound).start()

    def off(self):
        """
        Detiene la reproducción
        """        
        pygame.mixer.music.stop()

    def search(self, query):
        query = "tusa"
        videosSearch = VideosSearch(query, limit=1)
        result = videosSearch.result()
        url = result["result"][0]["link"]
        name = result["result"][0]["title"]
        return url, name 

    def download_video(self, url):
        audio_downloder = YoutubeDL({'format':'bestaudio'})
        audio_downloder.download([url])
        path = "KAROL G, Nicki Minaj - Tusa (Official Video)-tbneQDc2H3I.webm"
        return

    def video_to_mp3(self, file_name):
        """ Transforms video file into a MP3 file """
        try:
            file, extension = os.path.splitext(file_name)
            # Convert video into .wav file
            os.system('ffmpeg -i {file}{ext} {file}.wav'.format(file=file, ext=extension))
            # Convert .wav into final .mp3 file
            os.system('lame {file}.wav {file}.mp3'.format(file=file))
            os.remove('{}.wav'.format(file))  # Deletes the .wav file
            print('"{}" successfully converted into MP3!'.format(file_name))
        except OSError as err:
            print(err.reason)
            return


    def play(self,query):
        url,name = self.search(query)
        self.download_video(url)
        self.video_to_mp3(name + ".webm")
        pygame.mixer.init()
        pygame.mixer.music.load(name+".mp3")
        self.on()
        return