from pytube import YouTube

link = input("Enter Link>>  ")
yt = YouTube(link)

#print(yt.streams.filter(only_audio=True))
#print(yt.streams.filter(only_video=True))

ys = yt.streams.get_highest_resolution()
ys = yt.streams.get_by_itag('22')
ys.download('/storage/emulated/0/Download')