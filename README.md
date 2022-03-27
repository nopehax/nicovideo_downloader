# Nicovideo Downloader

Downloads the video in the quality that you're able to view at. *Does NOT allow you to download at a higher quality if you don't have premium*
Allows you to extract audio only

Made this cos the nicovideo downloaders online all seem very sus

# How to use
1) play the video you want to download
2) F12 and go to the network tab
3) there'll be a GET request of xhr type
4) copy the url and paste it into the URL variable
5) skip to the end of the video to find out how many pieces there are in total and put it in the PIECE variable
6) change the DIR variable to wherever you want the output files to be

_If you want the video, skip the `extractAudio()` step and use `combine(".ts")`_

# To do
make it so that you're able to download by just using the link to the video
