from pytube import YouTube


def Download(link):
    youtubeObject = YouTube(link)
    # to get the highest resolution, you can use get_highest_resolution
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except: 
        print("There has been an error in downloading the video from the Youtube video")
    print("Congrants! Your video is succefully downloaded!")
    
link = input("Paste your Youtube video Link!! URL: ")
Download(link)