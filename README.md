# Youtube Video Downloader
### You can use these python scripts to download YouTube videos
## How to use
### Make sure you have python installed

### --Download/Clone these scripts
### --Run the command in the directory: 'pip install -r req.txt'

There are 2 scripts in the folder. 'adaptive.py' and 'prgressive.py'
You can use any of these two scripts but there will be differences.
'progressive.py' uses progressive download which will be faster but will be limited to a max quality of 720p
'adaptive.py' uses adaptive streaming download which will be slower but is not limited by quality.

### Usage Example for Progressive Download: 
python progressive.py https://youtu.be/v0SWwJ-zVb8
### Usage Example for Adaptive Streaming Download: 
python adaptive.py https://youtu.be/v0SWwJ-zVb8
