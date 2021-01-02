import sys, os
from pytube import *

failed_AV = False

print(sys.argv[1])
try:
    yt = YouTube(sys.argv[1])   
except:
    print('No YouTube link has been provided.')
    exit()

print('\nVideo ITAGS')
print(yt.streams.filter(progressive=False))
print('\nAudio ITAGS')
print(yt.streams.filter(progressive=False, only_audio=True))
print('\nAttempting Video Download')
# ITAG 137 : 1080p
# ITAG 22 : 720p    
# ITAG 299 : 1080p60fps    
try:
    yt.streams.get_by_itag(137).download()
    os.rename(yt.streams.first().default_filename, "vid.mp4")
    print('Found Video, Downloading..')
except:
    print('ITAG 137 Failed (1080p). Trying 299 (1080p60)')
    try:
        yt.streams.get_by_itag(299).download()
        os.rename(yt.streams.first().default_filename, "vid.mp4")
        print('Found Video, Downloading..')
    except:
        print('ITAG 299 (1080p60) Failed. Trying 22 (720p)')
        try:
            yt.streams.get_by_itag(22).download()
            os.rename(yt.streams.first().default_filename, "vid.mp4")
            print('Found Video, Downloading..')
        except:
            print("\nFAILED VIDEO DOWNLOAD. NO VALID ITAG")
            failed_AV = True

print('\nAttempting AUDIO Download')

try:
    yt.streams.get_by_itag(140).download()
    os.rename(yt.streams.first().default_filename, "audio.mp4")
    print('Found Audio, Downloading..')
except:
    print("\nFAILED AUDIO DOWNLOAD. NO VALID ITAG")
    failed_AV = True

if failed_AV == False:
    os.system('ffmpeg -i vid.mp4 -i audio.mp4 -c:v copy -c:a copy output.mp4')
    print('\n Downloaded video. Merging AU')
    os.remove('vid.mp4')
    os.remove('audio.mp4')
    print('\nRemoved Temperary Files')
    os.rename('output.mp4', yt.streams.first().default_filename)
else:
    try:
        os.rename('vid.mp4', yt.streams.first().default_filename)
    except:
        os.rename('audio.mp4', yt.streams.first().default_filename)
