import csv
from pytubefix import YouTube
from youtube_search import YoutubeSearch
import json



def downloadsong(search_query, path):
    try: 
        youtube_results = YoutubeSearch(search_query, max_results=1).to_json()
        youtube_first_video = json.loads(youtube_results)['videos'][0]
        url = "https://www.youtube.com" + youtube_first_video['url_suffix']
        name = youtube_first_video['title']

    
        # object creation using YouTube 
        yt = YouTube(url) 
        d_video=yt.streams.get_audio_only()
    except: 
        #to handle exception 
        print("Connection Error") 



    try: 
        # downloading the video 
        d_video.download(output_path="./music/"+path+"/", filename=name+".mp4")
        print(search_query)
    except: 
        print("Some Error in " + search_query)
            
        



while True:


    print("Select option: \n 1. Download from spotify playlist. \n 2. Search by name.")
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
            try: 
                search_string=a + " - " + artist[x]
                downloadsong(search_string, "artists/"+artist[x])
                x=x+1
            except:
                print("We are cooked!!!!")
    elif mode == 2:
        print("Enter the name")
        downloadsong(input("-> "),"downloads")
        print("Finished\n\n")

    else:
        print("Select something pls\n")
