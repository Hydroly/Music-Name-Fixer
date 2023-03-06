import music_tag
import pathlib
import os

PATH = "../music2/"
for filename in os.listdir(PATH):
    extension = pathlib.Path(filename).suffix
    try:
        f = music_tag.load_file(PATH + filename)
        if (f["artist"]) != "":
            artist = (f["artist"])
            title = (f["title"])
            new_filename = str(artist.value) + " - " + str(title.value) + extension

            if new_filename != filename:
                # print ("+ renaming %s to %s" % (filename, new_filename))
                os.rename(PATH + filename, PATH + new_filename)
    except Exception as e:
        s = str(e).split("\n")
        for i in s:
            if i.startswith("[WinError 183]"):
                print("For file <" + filename + "> to <" + new_filename + "> already exists")
            else:
                # print(e)
                pass
            try:
                new_filename = new_filename.replace("/", "_")
                new_filename = new_filename.replace(":", " ")
                new_filename = new_filename.replace("?", "")
                os.rename(PATH + filename, PATH + new_filename)
            except:
                print("For file <" + filename + "> to <" + new_filename + "> new filename special characters")
