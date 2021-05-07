from PIL import Image
import os
import glob
import argparse
import warnings
warnings.filterwarnings("ignore")

def get_path_list(folder_path):
    '''Given a folder path this function returns a list of all png image names
    in that folder'''
    files_grabbed = glob.glob(folder_path + '*.png')
    return files_grabbed

def convert_jpg_to_png(filepath):
    '''This function converts a png file to jpg file and removes the old file from directory'''
    if filepath[-4:] == ".png":
        file_name = filepath[:-4]
    img = Image.open(filepath)
    img = img.convert('RGB')
    img.save(file_name + ".jpg")
    os.remove(filepath)

def convert(folderpath):
    '''This function converts all files in the folderpath from png to jpg format'''
    list(map(lambda path: convert_jpg_to_png(path),get_path_list(folderpath)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-f', '--folderpath', 
                        type=str,
                        help='Folder path of the image directory.')
    args = parser.parse_args()
    convert(args.folderpath)