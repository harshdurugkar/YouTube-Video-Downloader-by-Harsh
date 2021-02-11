from django.shortcuts import render
from pytube import YouTube
import os

url = ''


def ytd_home(request):
    return render(request, 'index.html')


def yt_download(request):
    global url
    url = request.GET.get('url')
    try:
        obj = YouTube(url)
        resolutions = []
        strm_all = obj.streams.filter(progressive=True, file_extension='mp4').all()
        for i in strm_all:
            resolutions.append(i.resolution)
        resolutions = list(dict.fromkeys(resolutions))
        embed_link = url.replace("watch?v=", "embed/")
        return render(request, 'yt_download.html', {'rsl': resolutions, 'embd': embed_link})
    except:
        return render(request, 'sorry.html')


def download_complete(request, resolutions):
    global url
    try:
        homedir = os.path.expanduser("~")
        dirs = homedir + '/Downloads'
        print(f'DIRECT :', f'{dirs}/Downloads')
        if request.method == "POST":
            YouTube(url).streams.get_by_resolution(resolutions).download(homedir + '/Downloads')
            return render(request, 'download_complete.html')
        else:
            return render(request, 'sorry.html')
    except:
        return render(request, 'sorry.html')

