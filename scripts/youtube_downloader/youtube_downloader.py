# Script para descargar el video que quiera de youtube introduciendo el link web.
from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("Ha habido un error en la descarga de tu video")
    print("La descarga ha sido completada!")


link = input("Introduce tu link de youtube aqui!! URL: ")   
Download(link)