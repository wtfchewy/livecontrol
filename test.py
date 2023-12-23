import live
import random

set = live.Set()
set.scan(scan_clip_names=True)

for track in set.tracks:
    print(f"Name: {track.name}")
    print(f"Volume: {track.volume}")
    print(f"Armed: {track.arm}")
    print(f"Muted: {track.mute}")
    track.solo = True
    print(f"Solo: {track.solo}")
    print("-----")
    
#set.start_playing()
