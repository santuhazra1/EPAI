from PIL import Image
import os
import glob
import argparse

def get_path_list(folder_path):
    '''Given a folder path this function returns a list of all jpg and jpeg image names
    in that folder'''
    types = ('*.jpg', '*.jpeg')
    flatten = lambda l: [item for sublist in l for item in sublist]
    files_grabbed = flatten([glob.glob(folder_path + file) for file in types])
    return files_grabbed

def convert_jpg_to_png(filepath):
    '''This function converts a jpg or jpeg file to png file and removes the old file from directory'''
    if filepath[-4:] == ".jpg":
        file_name = filepath[:-4]
    else:
        file_name = filepath[:-5]
    img = Image.open(filepath)
    img.save(file_name + ".png")
    os.remove(filepath)

def convert(folderpath):
    '''This function converts all files in the folderpath from jpg or jpeg to png format'''
    list(map(lambda path: convert_jpg_to_png(path),get_path_list(folderpath)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-f', '--folderpath', 
                        type=str,
                        help='Folder path of the image directory.')
    args = parser.parse_args()
    convert(args.folderpath)