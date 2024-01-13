import csv
from pytube import YouTube
from youtube_search import YoutubeSearch
import json
import re


def download(search_query):
    try:
        youtube_results = YoutubeSearch(search_query, max_results=1).to_json()
        youtube_first_video = json.loads(youtube_results)['videos'][0]
        url = "https://www.youtube.com" + youtube_first_video['url_suffix']
        name = youtube_first_video['title']
        youtube_video = YouTube(url)
        youtube_video_streams = youtube_video.streams.filter(only_audio=True, file_extension='mp4')
        print("Downloading " + name)
        correctIndex = 0

        selected_bitrate_normalised = 160000 / 1000

        for i,vid in enumerate(youtube_video_streams):
            currKbps = int(re.sub("[^0-9]", "", vid.abr))
            if currKbps < selected_bitrate_normalised:
                correctIndex = i

        video_stream = youtube_video_streams[correctIndex]

        video_stream.download(output_path="./music/", filename=name+".mp4")


    except:
        print("Error")

while True:


    print("Select operation: \n 1. Download from spotify playlist. \n 2. Search by name.")
    mode = int(input("-> "))

    if mode == 1:
        print("Enter your .csv file name")
        name = input("-> ")
        songs=[]
        artist=[]
        x=0

        with open(name, 'r', encoding='utf-8') as rf:
            reader = csv.reader(rf, delimiter=',')
            for row in reader:
                artist.append(row[3])
            del artist[0]
            rf.close()

        with open(name, 'r', encoding='utf-8') as rf1:
            reader = csv.reader(rf1, delimiter=',')
            for row in reader:
                songs.append(row[1])
            del songs[0]
            rf1.close()

        print(len(songs))

        for a in songs:
            search_string=a + " from " + artist[x]
            download(search_string)
            x=x+1
    elif mode == 2:
        print("Enter the name")
        download(input("-> "))
        print("Finished\n\n")

    else:
        print("Select something pls\n")
