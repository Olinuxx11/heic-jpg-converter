import customtkinter as ctk
from tkinter.filedialog import askdirectory
import subprocess
import os

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title("HEIC to JPG Converter | Version 1.0")
root.geometry("480x480")
root.resizable(False, False)

sourceFolder = ""
destinationFolder = ""

def chooseSourceFolder():
  global sourceFolder
  sourceFolder = askdirectory()
  if sourceFolder != "" and destinationFolder != "":
    buttonConvert.configure(state="normal")

def chooseDestinationFolder():
  global destinationFolder
  destinationFolder = askdirectory()
  if sourceFolder != "" and destinationFolder != "":
    buttonConvert.configure(state="normal")

def convert():
  global sourceFolder
  global destinationFolder
  print("Conversion started...")
  for filename in os.listdir(sourceFolder):
    if filename.lower().endswith(".heic"):
      labelFileName = ctk.CTkLabel(master=frameSide, text=f"Converting {filename.lower()}", font=("Microsoft YaHei", 12))
      labelFileName.pack(pady=0, padx=0)
      print(f"Converting {sourceFolder+'/'+filename.lower()} ...")
      print(f"{destinationFolder+'/'+filename[0:-5]}.jpg")
      subprocess.run(["ImageMagick/magick.exe", sourceFolder+'/'+filename, f"{destinationFolder+'/'+filename[0:-5]}.jpg"])
  print("Conversion done!")

# ------------------------------------------------------------------

# Dark Frame in the middle of a window
frame = ctk.CTkFrame(master=root)
frame.pack(pady=25, padx=25, fill="both", expand=True)

# Top Label
label = ctk.CTkLabel(master=frame, text="HEIC to JPG Converter", font=("Microsoft YaHei", 20))
label.pack(pady=12, padx=10)

# Buttons
buttonSourceFolder = ctk.CTkButton(master=frame, text="Choose Source Folder", command=chooseSourceFolder, width=250, font=("Microsoft YaHei", 14, "bold"))
buttonSourceFolder.pack(pady=10, padx=0)

buttonDestFolder = ctk.CTkButton(master=frame, text="Choose Destination Folder", command=chooseDestinationFolder, width=250, font=("Microsoft YaHei", 14, "bold"))
buttonDestFolder.pack(pady=10, padx=0)

buttonConvert = ctk.CTkButton(master=frame, text="CONVERT", command=convert, font=("Microsoft YaHei", 16, "bold"), state="disabled")
buttonConvert.pack(pady=30, padx=0)

# Status Label
labelStatus = ctk.CTkLabel(master=frame, text="", font=("Microsoft YaHei", 14))
labelStatus.pack(pady=20, padx=10)


# Side Frame Panel
frameSide = ctk.CTkScrollableFrame(master=frame, width=300, height=300, fg_color="#333333")
frameSide.pack(pady=10, padx=10, fill="both", expand=True)

# ------------------------------------------------------------------

if __name__ == "__main__":
  root.mainloop()