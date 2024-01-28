from pydub import AudioSegment

from os import listdir

old_folder=f"./tracks/гоч_old"
new_folder=f"./tracks/гоч"

files = listdir(old_folder)

for i in files:
    print(i[:-4])
    m4a_file=AudioSegment.from_file(old_folder+"/"+i, format="m4a")
    m4a_file.export(new_folder+"/"+i[:-4]+".mp3", format="mp3")


