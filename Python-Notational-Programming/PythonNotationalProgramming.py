import os, sys, io, time
import shutil, logging

def read_text():
    captions = os.listdir('Text')
    for caption in captions:
        if caption.startswith('.'):
            continue;
        caption_file = caption
        with io.open("Text/"+caption_file) as cf:
            txt = cf.read()
            #print(txt)
        return str(txt)
        break;

if __name__ == '__main__':
    # Get Current Working Directory
    cwd = os.getcwd()
    
    # Read Text File
    text = read_text()

    # Come Back To Original Directory
    os.chdir(cwd)

    # Print Text File
    print(text)
