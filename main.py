from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory
from moviepy import VideoFileClip
import os

Tk().withdraw()
# Selecionar o video
mp4_arquivo = askopenfilename(filetypes=[("Vídeos MP4", "*.mp4")], title="Selecione o arquivo MP4")
if mp4_arquivo:
    print(f"Arquivo selecionado: {mp4_arquivo}")
    # selecionar pasta para salvar o arquivo
    saida_dir = askdirectory(title="Selecione a pasta para salvar o GIF")
    if saida_dir:
        # Cria o caminho do arquivo
        gif_arquivo = os.path.join(saida_dir, "sem_nome.gif") 
        clip = VideoFileClip(mp4_arquivo)
        # Converte de MP4 para GIF
        clip_resized = clip.resized(height=420) 
        clip_trimmed = clip_resized.subclipped(0, 2) 
        clip_trimmed.write_gif(gif_arquivo, fps=30)
        #clip.write_gif(gif_arquivo, fps=60) 
        print(f"GIF salvo como: {gif_arquivo}")
    else:
        print("Nenhuma pasta foi selecionada.")
else:
    print("Nenhum arquivo foi selecionado.")
