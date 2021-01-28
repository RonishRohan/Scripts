import youtube_dl
import re
import urllib
from pydub import AudioSegment

ydl_opts = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': 'mp3',
        'outtmpl': '%(title)s.%(ext)s',
        'restrictfilenames': True,
        'noplaylist': True,
        'nocheckcertificate': True,
        'ignoreerrors': False,
        'logtostderr': False,
        'quiet': True,
        'no_warnings': True,
        'default_search': 'auto',
        'source_address': '0.0.0.0',
    }
search = []

def DownloadVideo(URL):
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		ydl.download([URL])
		pass
	pass

def GetYoutubeVideo(query):
	query = query.strip().replace(' ', '+')
	html = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={query}")
	urls = re.findall(r"watch\?v=(\S{11})", html.read().decode())
	result = urls[0]
	return result

