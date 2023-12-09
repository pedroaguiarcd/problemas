# import pygame
# import tkinter as tk
# from tkinter import filedialog

# pygame.init()

# def escolher_musica():
    # file_path = filedialog.askopenfilename(filetypes=[("messi", "*.mp3")])
    # if file_path:
        # pygame.mixer.music.load(messi.mp3)
        # pygame.mixer.music.play(-1)

# root = tk.Tk()
# root.withdraw() 
# escolher_musica()
# while pygame.mixer.music.get_busy():
    # pass
# pygame.mixer.music.stop()
# pygame.quit()

import pygame
pygame.init()
pygame.mixer.music.load('021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()

