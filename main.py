from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from moviepy import VideoFileClip

Tk().withdraw()
mp4_arquivo = askopenfilename(filetypes=[("mp4", "*.mp4")], title="Selecione o arquivo MP4")
if mp4_arquivo:
    print(f"Arquivo selecionado: {mp4_arquivo}")
    gif_arquivo = asksaveasfilename(
        defaultextension=".gif",
        filetypes=[("gif", "*.gif")],
        title="Escolha o local e o nome do gif"
    )
    if gif_arquivo:
        clip = VideoFileClip(mp4_arquivo)
        clip_resized = clip.resized(height=280) 
        clip_trimmed = clip_resized.subclipped(0, 5) 
        clip_trimmed.write_gif(gif_arquivo, fps=15)
        print(f"GIF salvo como: {gif_arquivo}")
    else:
        print("Nenhuma pasta foi selecionada.")
else:
    print("Nenhum arquivo foi selecionado.")
