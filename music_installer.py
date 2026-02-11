import yt_dlp

print("==========================")
print("+=    MUSIC INSTALLER    =+")
print("==========================")

def progress_hook(d):
    if d['status'] == 'downloading':
        percent = d.get('_percent_str', '0%')
        speed = d.get('_speed_str', 'Unknown')
        print(f"Downloading: {percent} | Speed: {speed}", end='\r')

    elif d['status'] == 'finished':
        print("\nSong downloaded. Converting to MP3...")

playlist_url = input("Enter playlist URL: ")

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'songs/%(title)s.%(ext)s',
    'progress_hooks': [progress_hook],
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])

print("\nAll songs downloaded.")
