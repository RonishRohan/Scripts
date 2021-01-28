import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from youtube_scripts import GetYoutubeVideo, DownloadVideo

cid = "46a1a9c9997543f1824fcfbcb34e25fd"
secret = "d6baef160ed04896b19bc9772750aa1c"
client_credentials_manager=SpotifyClientCredentials(client_id=cid, client_secret=secret)
def GetPlaylistContents(userid ,playlist):
	sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
	playlists = sp.user_playlists(userid)
	for pl in playlists['items']:
		
		if pl['name']==playlist:
			results = sp.playlist(pl['id'], fields="tracks,next")
			tracks = results['tracks']
			return tracks
		pass
	pass
def ShowTracks(tracks):
	#for i, item in enumerate(tracks['items']):
    #    track = item['track']
    #    print("   %d %32.32s %s" % (i, track['artists'][0]['name'],
    #        track['name']))
    for i, item in enumerate(tracks['items']):
    	track = item['track']
    	print(track['name'])

    	pass

print("Enter the playlist you want to download")
name = input()
print("Enter user id")
id = input()
tracks = GetPlaylistContents(id, name)
print(f"Downloading your playlist({name})")
for item in tracks['items']:
	track = item['track']
	query = track['name']
	url = GetYoutubeVideo(query)
	print(f"Now downloading {query}")
	DownloadVideo(url)
	print(f"{query} is download!")
	pass
