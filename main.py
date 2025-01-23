import yt_dlp
import json
import sys

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # VIDEO DOWLOAD
    # sss="https://www.youtube.com/playlist?list=PL6Nx1KDcurkBdxssD1k56SDnwuTuX2bBr"
    # ydl_opts={
    #     'format': 'mkv/bestvideo/best',
    #     'paths': {"temp": "1c lessons/buff/", 'home': "1c lessons/buff/"},
    #     'ignoreerrors': True
    # }
    #
    # with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    #     ydl.download(sss)
    #
    # sys.exit()

    #AUDIO DOWLOAD
    video_url = "https://youtu.be/3vOu4OgRT1w?si=IYqScKTNOoT-IDSl"
    ydl_opts = {
        'format': 'm4a/bestaudio/best',
        'ffmpeg_location': 'C:\\ffmpeg\\bin',
        'paths': {"temp": "tracks/buff/", 'home': "tracks/buff/"},
        'postprocessors': [{  # Extract audio using ffmpeg
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }],
        'ignoreerrors': True
    }



    with yt_dlp.YoutubeDL(ydl_opts) as ydl:

        err_code = ydl.download(video_url)


