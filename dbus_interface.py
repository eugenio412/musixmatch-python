## Modified from these answers:
##   "Get spotify currently playing track" by jooon
##   https://stackoverflow.com/questions/33883360/get-spotify-currently-playing-track

##   "Splitting a string with brackets using regular expression in python"
##   https://stackoverflow.com/questions/21662474/splitting-a-string-with-brackets-using-regular-expression-in-python

import dbus
import re

def get_music_info_from_dbus(idebug):
  session_bus = dbus.SessionBus()
  spotify_bus = session_bus.get_object("org.mpris.MediaPlayer2.spotify", "/org/mpris/MediaPlayer2")
  spotify_properties = dbus.Interface(spotify_bus, "org.freedesktop.DBus.Properties")
  metadata = spotify_properties.Get("org.mpris.MediaPlayer2.Player", "Metadata")

  # The property Metadata behaves like a python dict
  if idebug > 1:
    for key, value in metadata.items():
      print(str(key)+str(value))

  # To print the title
  title = str(metadata['xesam:title'])

  # To split artist string
  temp = str(metadata['xesam:artist'])
  temp = re.findall("\'.*?\'", temp)
  temp = temp[0]
  temp = temp.strip("'")
  artist = temp

  if idebug > 0:
    print("Title:  "+title)
    print("Artist: "+artist)

  return title, artist

def main():
  get_music_info_from_dbus(1)

if __name__ == '__main__':
  main()
