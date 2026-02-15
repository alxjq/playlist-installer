import yt_dlp

print("=====================")
print("--==    Lister   ==--")
print("=====================")

def print_playlist_ids(playlist_url):
    ydl_opts = {
        'quiet': True,
        'extract_flat': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        playlist = ydl.extract_info(playlist_url, download=False)

        with open("downloaded.txt", "w", encoding="utf-8") as f:
            for video in playlist['entries']:
                if video and 'id' in video:
                    f.write(f"youtube {video['id']}\n")

    print("Video IDs have been saved to the 'downloaded.txt' file.")


# Usage
playlist_link = input("Enter the playlist URL: ")
print_playlist_ids(playlist_link)
