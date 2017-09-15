import script as sc
import dbus_interface as di

title, artist = di.get_music_info_from_dbus(0)
track_id = (sc.find_id(title + " " + artist)) 
print(track_id)
print(sc.song_lyric(title, artist))
 
