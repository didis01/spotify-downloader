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
    
        youtube_video = YouTube(url)
        youtube_video_streams = youtube_video.streams.filter(only_audio=True, file_extension='mp4')

        correctIndex = 0

        selected_bitrate_normalised = 160000 / 1000

        for i,vid in enumerate(youtube_video_streams):
            currKbps = int(re.sub("[^0-9]", "", vid.abr))
            if currKbps < selected_bitrate_normalised:
                correctIndex = i

        video_stream = youtube_video_streams[correctIndex]

        video_stream.download(output_path="./music/", filename=search_query+".mp4")


    except:
        print("Error")



print("Enter your .csv file name")
name = input("->")
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
    print("Downloading " + a + " from " + artist[x])
    download(search_string)
    x=x+1