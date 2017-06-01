import sys
import requests
import os
import codecs

youtube_ids = open("ids.txt", "r")
lyrics_dir_path = "data/lyrics/"
sounds_dir_path = "data/sound/"
counter = 0

is_downloaded = True
for line in youtube_ids.readlines():
    yt_id = line.rstrip("\n")

    sound_path = sounds_dir_path + str(counter).zfill(4)
    lyrics_path = lyrics_dir_path + str(counter).zfill(4) + ".txt"
    counter += 1
    if yt_id == "DONE":
        is_downloaded = False
        continue
    if is_downloaded:
        continue
    video_url = "https://www.youtube.com/watch?v=" + yt_id
    os.system('youtube-dl --extract-audio --audio-format mp3 --prefer-ffmpeg -o /Users/diveeshs/ds.data/Stanford/Senior/Spring/CS224S/CS224S/' + sound_path + ".m4a " + video_url)
    lyrics_url = "http://video.google.com/timedtext?lang=en&v=" + yt_id
    lyrics = requests.get(lyrics_url)
    lyrics_file = codecs.open(lyrics_path, mode='w+', encoding='utf-8')
    lyrics_file.write(lyrics.text)
    
