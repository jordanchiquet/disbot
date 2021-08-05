import youtube_dl


print("Hello world")
yturl = input("vid url:")
print("input val: [" + yturl + "]")

with youtube_dl.YoutubeDL({'format':'22', 'quiet': False}) as ydl:
    ydl.download([yturl])