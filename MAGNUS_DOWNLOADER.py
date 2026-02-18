import os
import subprocess
import zipfile
import urllib.request
from yt_dlp import YoutubeDL

# ===== logo =====
def logo():
    print(r"""
 ___  ___  ___  _____  _   _ _   _ _____ 
|  \/  | / _ \|  __ \| \ | | | | /  ___|
| .  . |/ /_\ \ |  \/|  \| | | | \ `--. 
| |\/| ||  _  | | __ | . ` | | | |`--. \
| |  | || | | | |_\ \| |\  | |_| /\__/ /
\_|  |_/\_| |_/\____/\_| \_/\___/\____/ 
    """)

logo()

# ===== kontrola ffmpeg =====
def is_ffmpeg_installed():
    try:
        subprocess.run(["ffmpeg", "-version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("[CHECK] ffmpeg je nainstalovaný ✅")
        return True
    except FileNotFoundError:
        print("[CHECK] ffmpeg nebyl nalezen ❌")
        return False

def download_ffmpeg():
    print("[INFO] Stahuji ffmpeg...")
    ffmpeg_dir = os.path.join(os.getcwd(), "ffmpeg")
    os.makedirs(ffmpeg_dir, exist_ok=True)
    zip_path = os.path.join(ffmpeg_dir, "ffmpeg.zip")
    
    url = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
    print("[INFO] URL:", url)
    urllib.request.urlretrieve(url, zip_path)
    
    print("[INFO] Rozbaluji ffmpeg...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(ffmpeg_dir)
    
    # Přesuneme binární soubory do ffmpeg/bin
    extracted_dir = [d for d in os.listdir(ffmpeg_dir) if os.path.isdir(os.path.join(ffmpeg_dir, d))][0]
    bin_dir = os.path.join(ffmpeg_dir, "bin")
    os.makedirs(bin_dir, exist_ok=True)
    ffmpeg_exe = os.path.join(bin_dir, "ffmpeg.exe")
    os.rename(os.path.join(ffmpeg_dir, extracted_dir, "bin", "ffmpeg.exe"),
              ffmpeg_exe)
    
    print("[INFO] ffmpeg je připraven ✅")
    return os.path.abspath(ffmpeg_exe)

def add_ffmpeg_to_system_path(ffmpeg_path):
    ffmpeg_dir = os.path.dirname(ffmpeg_path)
    try:
        # setx trvale přidá cestu do PATH (Windows)
        subprocess.run(f'setx PATH "%PATH%;{ffmpeg_dir}"', shell=True, check=True)
        print(f"[INFO] ffmpeg byl přidán do systémového PATH ✅")
        print("[INFO] Restartuj terminál nebo počítač, aby se změna projevila")
    except subprocess.CalledProcessError:
        print("[ERROR] Nepodařilo se přidat ffmpeg do PATH. Zkontroluj práva administrátora.")

# ===== main =====
if not is_ffmpeg_installed():
    ffmpeg_path = download_ffmpeg()
    add_ffmpeg_to_system_path(ffmpeg_path)
else:
    ffmpeg_path = "ffmpeg"  # pokud je už v PATH

# ===== výběr režimu =====
print("\nVyber režim:")
print("1 - Jedno video")
print("2 - Více videí")
print("3 - Jen audio")
vyber = input("Zadej číslo: ").strip()

# ===== vstup od uživatele =====
if vyber == "2":
    odkazy = input("Zadej odkazy na videa (oddělené čárkou): ").split(",")
    odkazy = [odk.strip() for odk in odkazy]
else:
    odkaz = input("Zadej odkaz na YouTube video: ").strip()
    odkazy = [odkaz]


command = {
    "format": "bv*[vcodec^=avc][height<=720]+ba[acodec^=mp4a]/best[ext=mp4]",
    "outtmpl": "%(title)s [%(id)s].%(ext)s",
    "merge_output_format": "mp4",
}


# ===== audio režim =====
if vyber == "3":
    command["format"] = "bestaudio/best"
    command["postprocessors"] = [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]

# ===== stahování =====
print("\n[INFO] Spouštím stahování...")
with YoutubeDL(command) as ydl:
    ydl.download(odkazy)

print("\n[INFO] Stahování dokončeno ✅")
