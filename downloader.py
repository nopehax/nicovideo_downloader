import requests, os
DIR = "D:\Music\Music\Mafumafu\lost"
PIECE = 36
URL = "https://vodedge008.dmc.nico/hlsvod/ht2_nicovideo/nicovideo-sm20359879_46bb460da5e857e2756d9975f81a0eacbcc26bb18bcec2b2d9bf1d2860753a75/1/ts/{}.ts?ht2_nicovideo=6-3Mf1WgerMR_1648369159258.gcov34sdfd_r9e9s9_blhbrkznqkhw"

def download():
    for i in range(1, PIECE+1):
        file = requests.get(URL.format(i), allow_redirects=True) 
        with open("{}\{}.ts".format(DIR, i), 'wb') as f:
            f.write(file.content)
        f.close

def extractAudio():
    command = 'ffmpeg -i "%s\{0}.ts" -vn -acodec copy "%s\{0}.aac"' % (DIR, DIR)
    os.system("cd 'Downloads'")
    for i in range(1, PIECE+1):
        os.system(command.format(i))

def combine(ext):
    names = list()
    with open(DIR + "\list.txt", 'w') as f:
        for file in os.listdir(DIR):
            if file.endswith(ext):
                names.append(file)
        names.sort(key=lambda x: int(x.split('.')[0]))
        for i in names:
            f.writelines("file '%s\%s'\n" % (DIR, i))
        f.close()

    os.system('ffmpeg -f concat -safe 0 -i "%s" -c copy "%s\output%s"' % (DIR + "\list.txt", DIR, ext))
    #os.system('ffmpeg -i "%s\output.aac" "%s\output.mp3"' % (DIR, DIR))

combine(".aac")
