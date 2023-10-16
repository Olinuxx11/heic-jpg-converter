import os, subprocess

directory = 'examples/'

for filename in os.listdir(directory):
  if filename.lower().endswith((".heic", ".HEIC")):
    print(f"Converting {os.path.join(directory, filename)} ...")
    subprocess.run(["ImageMagick-7.1.1-20-portable/magick.exe", directory+filename, f"{directory + filename[0:-5]}.jpg"])
    print("Done!")