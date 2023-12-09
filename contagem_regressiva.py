import os
current_directory = os.getcwd()
print("Diretório Atual:", current_directory)
import tkinter as tk
import time

def countdown():
    seconds = int(entry.get())
    while seconds > 0:
        time_label.config(text=f"Tempo restante: {seconds} segundos")
        seconds -= 1
        root.update()
        time.sleep(1)
    time_label.config(text="Contagem regressiva encerrada!")

root = tk.Tk()
root.title("Contagem Regressiva")

entry = tk.Entry(root, width=5)
entry.pack()

start_button = tk.Button(root, text="Iniciar Contagem", command=countdown)
start_button.pack()

time_label = tk.Label(root, text="")
time_label.pack()

root.mainloop()