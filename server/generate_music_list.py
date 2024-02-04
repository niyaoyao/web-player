
# -*- coding:utf-8 -*-
        
import json
import os
import re
import sys
import argparse


        
import logging
logging.basicConfig(level = logging.INFO)
LOG = logging.getLogger("generate_music_list")

        
        
def read_args():
    parse = argparse.ArgumentParser()
    parse.add_argument('-d', '--directory', help='The dir of Python Script.', type=str, required=False)
    args = parse.parse_args()
    return args
        
        
class GenerateMusicList(object):
    def __init__(self, directory=None):
        self.directory = directory
    def log_properties(self):
        LOG.info(self.__dict__)
        
    def run(self):
        self.log_properties()
        dirs = os.listdir(self.directory)
        filepath_list = []
        for filepath in dirs:
            filename, file_extension = os.path.splitext(filepath)
            if file_extension == '.mp4' or file_extension == '.mp3'  :
                filepath_list.append(filepath)
        json_path = os.path.join(self.directory, 'musics.json')
        json_string = json.dumps(filepath_list)
        LOG.info(json_string)
        with open(json_path, 'w') as json_file:
            json_file.write(json_string)
            
        
if __name__ == '__main__':
    args = read_args()
        

    instance = GenerateMusicList(directory= args.directory)
    instance.run()
    
        