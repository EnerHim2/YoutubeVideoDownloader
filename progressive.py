import sys
from pytube import *

print(sys.argv[1])
yt = YouTube(sys.argv[1])   
yt.streams.filter(progressive=True)
try:
    yt.streams.get_by_itag(22).download()
except:
    print("ITAG 22 Failed. Trying 399")
    try:
        yt.streams.get_by_itag(18).download()
    except:
        print("ITAG 399 Failed. Trying First")
        yt.streams.first().download()

print('Download Complete')