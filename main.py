import yt_dlp
import json

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    #гоч
    video_url = "https://www.youtube.com/watch?v=_LDA3OX3Ww4&list=PLfQAxVHE2OPKHbleRw1iKWisdzgmST9_w&index=1"
    #ваг
    #video_url = "https://www.youtube.com/playlist?list=PLfQAxVHE2OPI0_bAPpwnUO3LlSUhOc64r"

    #video_url = "https://www.youtube.com/watch?v=mtbGja6z-Y4&list=WL&index=1"

    ydl_opts = {
        'format': 'm4a/bestaudio/best',
        'ffmpeg_location': 'C:\\ffmpeg\\bin',
        #'outtmpl': 'tracks/гоч',
        'paths': {"temp": "tracks/гоч", 'home': "tracks/гоч"},
        # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
        'postprocessors': [{  # Extract audio using ffmpeg
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }],
        'ignoreerrors': False
    }

    ydl_opts = {
        'format': 'm4a/bestaudio/best',
        'ffmpeg_location': 'C:\\ffmpeg\\bin',
        'postprocessors': [{  # Extract audio using ffmpeg
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }],
        'ignoreerrors': True
    }

    # with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    #     info = ydl.extract_info(video_url, download=False)
    #     print(json.dumps(ydl.sanitize_info(info)))

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:

        err_code =  ydl.download(video_url)


