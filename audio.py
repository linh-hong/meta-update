#import pprint
import mutagen
from mutagen.flac import FLAC
from mutagen.mp3 import MP3
from mutagen.id3 import ID3
from mutagen.easyid3 import EasyID3
import glob

def sync_name_on_folder(folderpath):
    subitems = glob.glob(folderpath + "/*")
    for item in subitems:
        sync_name_title(item)

def sync_name_title(file):
    fileinfo = get_file_split(file)
    metadata = None
    if (fileinfo[1] == "flac"):
        metadata = FLAC(file)
    elif (fileinfo[1] == "mp3"):
        metadata = EasyID3(file)
    if (metadata != None and fileinfo[0] != metadata["title"][0]):
        print(f"Handling ... {file}")
        print(f'   \"{metadata["title"][0]}\" --> \"{fileinfo[0]}\"')
        metadata["title"] = [fileinfo[0]]
        metadata.save()

def print_meta_data(file):
    fileinfo = get_file_split(file)
    metadata = None
    if (fileinfo[1] == "flac"):
        metadata = FLAC(file)
    elif (fileinfo[1] == "mp3"):
        metadata = EasyID3(file)
    if (metadata != None):
        print(metadata)

def get_file_split(filepath):
    name_and_ext = filepath[str.rfind(filepath,"/")+1:]
    period_index = str.find(name_and_ext,".")
    file_split = [name_and_ext[0:period_index], name_and_ext[period_index+1:]]
    return file_split

#filepath = "/Users/honggialinh/Music/en/Best Of Olivia/You Are The Reason - Calum Scott, Leona Lewis.flac"
filepath = "/Users/honggialinh/Music/en/Best Of Olivia/01 Sweet Memories.mp3"
folderpath = "/Users/honggialinh/Music/en/Best Of Olivia"

#sync_name_title(filepath)

#print(get_file_split(filepath))
#print_meta_data_mp3(filepath)
sync_name_on_folder(folderpath)
#sync_name_title(filepath)
#print_meta_data_flac(filepath)

#f = EasyID3(filepath)
#mutagen.File(filepath)
#print(f.info)
#print(f)
#pp = pprint.PrettyPrinter(depth=4, indent=3)
#pp.pprint(f)
#