from os import scandir, rename
from os.path import splitext, exists, join
from shutil import move
from time import sleep

import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

sourceDir = "C:/Users/Dhruva Kathale/Downloads"
imgDir = "C:/Users/Dhruva Kathale/Desktop/Download Directory/Images"
vidDir = "C:/Users/Dhruva Kathale/Desktop/Download Directory/Vidoes"
audDir = "C:/Users/Dhruva Kathale/Desktop/Download Directory/Music"
docDir = "C:/Users/Dhruva Kathale/Desktop/Download Directory/Documents"


imgExt = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",".avif",
          ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]

vidExt = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg", ".mp4", ".mp4v", 
          ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]

audExt = [".m4a", ".flac", "mp3", ".wav", ".wma", ".aac"]

docExt = [".doc", ".docx", ".odt", ".csv", ".ppt",
          ".pdf", ".xls", ".xlsx", ".pptx"]

def changeName(loc,name):
    filename, extension = splitext(name)
    counter=1
    while exists(f"{loc}/{name}"):
        name=f"{filename}({str(counter)}){extension}"
        counter += 1
    return name

def moveFile(loc,entry,name):
    if exists(f"{loc}/{name}"):
        uniqueName = changeName(loc, name)
        oldName = join(loc, name)
        newName = join(loc, uniqueName)
        rename(oldName, newName)
    move(entry,loc)

class fileHandler(FileSystemEventHandler):

    def on_modified(self,event):
        with scandir(sourceDir) as entries:
            for instance in entries:
                name=instance.name
                self.isImage(instance,name)
                self.isVideo(instance,name)
                self.isAudio(instance,name)
                self.isDocument(instance,name)
                
    def isImage(self, instance, name):
        for Iext in imgExt:
            if name.endswith(Iext) or name.endswith(Iext.upper()):
                moveFile(imgDir,instance,name)
                logging.info(f"Moved image file: {name}")

    def isVideo(self, instance, name):
        for Vext in vidExt:
            if name.endswith(Vext) or name.endswith(Vext.upper()):
                moveFile(vidDir,instance,name)
                logging.info(f"Moved video file: {name}")

    def isAudio(self, instance, name):
        for Aext in audExt:
            if name.endswith(Aext) or name.endswith(Aext.upper()):
                moveFile(audDir,instance,name)
                logging.info(f"Moved audio file: {name}")

    def isDocument(self, instance, name):
        for Dext in docExt:
            if name.endswith(Dext) or name.endswith(Dext.upper()):
                moveFile(docDir,instance,name)
                logging.info(f"Moved document: {name}")

if __name__=="__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sourceDir
    event_handler = fileHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()