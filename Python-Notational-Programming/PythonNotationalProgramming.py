import os, sys, io, time
import shutil, logging
import subprocess

def read_text():
    txt = []
    captions = os.listdir('Text')
    for caption in captions:
        if caption.startswith('.'):
            continue;
        caption_file = caption
        with io.open("Text/"+caption_file) as cf:
            for i, line in enumerate(cf):
                txt.append(line.strip())
        return txt
        break;

def write_python_file(dir, text):
    os.chdir(cwd+"/"+dir)
    f = open("Output.py","w+")
    f.write("if __name__ == '__main__':")
    f.write('\n'+'\t')
    for t in text:
        f.write(t)
        f.write('\n'+'\t')
    f.close()

if __name__ == '__main__':
    # Get Current Working Directory
    cwd = os.getcwd()
    
    # Read Text File
    text = read_text()

    # Come Back To Original Directory
    os.chdir(cwd)

    # Create Text File and Paste Copied Input
    write_python_file('Output',text)

    # While In The Output Directory, Run The File Just Created
    subprocess.call(" python Output.py 1", shell = True)

    # Come back To Original Directory
    os.chdir(cwd)