from watchdog.observer import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time

"""
potentially rename the files by date
create subfolders corresponding to year and month
"""

class MyHandler(FileSystemEventHandler):
    i = 1
    def on_modified(self, event):
        new_name = 'new_file_' + str(self.i) + '.txt'

        for filename in os.listdir(folder_to_track):

            file_exists = os.path.isfile(f'{folder_destination}/{new_name}')
            while file_exists:
                self.i += 1
                new_name = 'new_file_' + str(self.i) + '.txt'
                file_exists = os.path.isfile(f'{folder_destination}/{new_name}')

            src = f'{folder_to_track}/{filename}'
            new_destination = f'{folder_destination}/{new_name}'
            os.rename(src, new_destination)

folder_to_track = 'C:/Users/Joshua/Desktop/MyFolder'
folder_destination = 'C:/Users/Joshua/Desktop/NewFolder'

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()