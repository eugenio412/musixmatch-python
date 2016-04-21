import urllib.request, urllib.error, urllib.parse
import json
import socket
import random
apikey_musixmatch = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
apiurl_musixmatch = 'http://api.musixmatch.com/ws/1.1/'

def find_id(search_term):
        while True:
            querystring = apiurl_musixmatch + "track.search?q=" + urllib.parse.quote(search_term) + "&apikey=" + apikey_musixmatch + "&format=plain"
            request = urllib.request.Request(querystring)
            #request.add_header("Authorization", "Bearer " + client_access_token)
            request.add_header("User-Agent", "curl/7.9.8 (i686-pc-linux-gnu) libcurl 7.9.8 (OpenSSL 0.9.6b) (ipv6 enabled)") #Must include user agent of some sort, otherwise 403 returned
            while True:
                try:
                    response = urllib.request.urlopen(request, timeout=4) #timeout set to 4 seconds; automatically retries if times out
                    raw = response.read()
                except socket.timeout:
                    print("Timeout raised and caught")
                    continue
                break
            json_obj = json.loads(raw.decode('utf-8'))
            body = json_obj["message"]["body"]["track_list"]
            num_hits = len(body)
            if num_hits==0:
                return(("No results for: " + search_term))
            for result in body:
                if result["track"]["has_lyrics"] == 1:
                    return result["track"]["track_id"]


def song_lyric(track_id):
        while True:
            querystring = apiurl_musixmatch + "track.lyrics.get?track_id=" + str(track_id) + "&apikey=" + apikey_musixmatch + "&format=plain&f_has_lyrics=1"
            request = urllib.request.Request(querystring)
            #request.add_header("Authorization", "Bearer " + client_access_token)
            request.add_header("User-Agent", "curl/7.9.8 (i686-pc-linux-gnu) libcurl 7.9.8 (OpenSSL 0.9.6b) (ipv6 enabled)") #Must include user agent of some sort, otherwise 403 returned
            while True:
                try:
                    response = urllib.request.urlopen(request, timeout=4) #timeout set to 4 seconds; automatically retries if times out
                    raw = response.read()
                except socket.timeout:
                    print("Timeout raised and caught")
                    continue
                break
            json_obj = json.loads(raw.decode('utf-8'))
            body = json_obj["message"]["body"]["lyrics"]["lyrics_body"]
            return body

def main():
    q = "negramaro estate"
    track_id = (find_id(q))
    print (track_id)
    print (song_lyric(track_id))

if __name__ == '__main__':
    main()
