import sys
import os
from pytube import YouTube

if not (os.path.exists("links.txt")):
    print("You need a links.txt file in the same folder as this script!")
    exit(0)

if os.path.exists('./music'):
    pass
else:
    sys.stdout.write('[+] Creating ./music directory.')
    os.mkdir('./music')

with open('links.txt','r') as f:

    data=f.readlines()
    lines=[line.rstrip() for line in data]

    for link in lines:
        if ("##GENRE" in link):
            link=link.replace(" ","")
            link=link.split(":")
            genre=link[1]
            sys.stdout.write(f"[*] Adding to genre: {genre}\n")
            if (os.path.exists(f"./music/{genre}")):
                pass
            else:
                sys.stdout.write(f"[+] Adding folder for the {genre} genre.\n")
                os.mkdir(f"./music/{genre}")

        if ("##ARTIST" in link):
            link=link.replace(" ","")
            link=link.split(":")
            artist=link[1]
            sys.stdout.write(f"[*] Adding to artist: {artist}\n")
            if (os.path.exists(f"./music/{genre}/{artist}")):
                pass
            else:
                sys.stdout.write(f"[+] Adding folder for {artist} in the {genre} genre.\n")
                os.mkdir(f"./music/{genre}/{artist}")


        if ("youtube.com" in link):
            sys.stdout.write(f'[*] Handling: {link}\n')
            video=YouTube(link)
            badFilenameSymbols=["!","@","#","$","%","&","*","=","|","{","}",":","'",'"',"\\","/","?","<",">"]
            for symbol in badFilenameSymbols:
                video.title=video.title.replace(symbol,"")
            video.title=video.title.replace(" ","+")
            if (genre):
                path=f'./music/{genre}/unknown/'
                if (artist):
                    path=f'./music/{genre}/{artist}/'
            if (artist):
                path=f'./music/unknown/{artist}/'
                if genre:
                    path=f'./music/{genre}/{artist}/'
            else:
                path=f'./music/unkown/unkown/'
            audio=video.streams.filter(only_audio=True).all()
            audio[0].download(path)
    sys.stdout.write("[*] All done!\n")
    
