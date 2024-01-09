
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
    parse.add_argument('-p', '--placeholder', help='The Placeholder of Python Script.', type=str, required=False)
    parse.add_argument('-d', '--directory', help='The dir of Python Script.', type=str, required=False)
    args = parse.parse_args()
    return args
        
        
class GenerateMusicList(object):
    def __init__(self, placeholder, directory=None):
        self.placeholder = placeholder
        self.directory = directory
    def log_properties(self):
        LOG.info(self.__dict__)
        
    def run(self):
        self.log_properties()
        dirs = os.listdir(self.directory)
        filepath_list = []
        for filepath in dirs:
            filename, file_extension = os.path.splitext(filepath)
            if filename != '.DS_Store':
                filepath_list.append(filename)
        json_path = os.path.join(self.directory, 'musics.json')
        json_string = json.dumps(filepath_list)
        with open(json_path, 'w') as json_file:
            json_file.write(json_string)
            
        
if __name__ == '__main__':
    args = read_args()
        

    instance = GenerateMusicList(placeholder=args.placeholder, directory= args.directory)
    instance.run()
    
        