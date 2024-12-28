from cx_Freeze import setup, Executable
import os


include_files = [("ffmpeg.exe", "ffmpeg.exe")]

# Dependencies are automatically detected, but they might need fine-tuning.
build_exe_options = {
    "packages": ["tkinter", "moviepy", "tkinter.filedialog"],
    
}
setup(
    name="MP4 to GIF",
    version="1.0",
    description="Converter Videos MP4 para GIF",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base="Win32GUI")],
)