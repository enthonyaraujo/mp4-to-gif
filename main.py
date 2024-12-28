import tkinter as tk
import os
from tkinter.filedialog import askopenfilename, asksaveasfilename
from moviepy import VideoFileClip

ffmpeg_path = os.path.join(os.path.dirname(__file__), "ffmpeg.exe")
os.environ["FFMPEG_BINARY"] = ffmpeg_path


def converter(*args):
    mp4_arquivo = askopenfilename(filetypes=[("mp4", "*.mp4")], title="Selecione o arquivo MP4")
    if mp4_arquivo:
        print(f"Arquivo selecionado: {mp4_arquivo}")
        gif_arquivo = asksaveasfilename(
            defaultextension=".gif",
            filetypes=[("gif", "*.gif")],
            title="Escolha o local e o nome do gif"
        )
        if gif_arquivo:
            try: 
                clip = VideoFileClip(mp4_arquivo)
                clip_resized = clip.resized(height=280) 
                clip_trimmed = clip_resized.subclipped(0, 5) 
                clip_trimmed.write_gif(gif_arquivo, fps=15)
                label.config(text=f"GIF salvo em:\n{gif_arquivo}", fg="green")
                
            except Exception as e:
                label.config(text="Erro ao salvar o GIF.", fg="red")
            
                
        else:
            label.config(text=f"Nehuma pasta foi selecionada")
            
    else:
        label.config(text=f"Nenhum arquivo foi selecionado")
        

window = tk.Tk() #criação da janela principal 
window.title("Converter MP4 para GIF") #titulo
window.geometry("400x150")  # largura x altura

button = tk.Button(window, text="Selecione o Arquivo MP4", command=converter)
button.pack()

label = tk.Label(window, text="") #adicionando mensangem de salvemento do arquivo
label.pack()

window.mainloop()
