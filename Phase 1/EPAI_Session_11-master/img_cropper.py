from PIL import Image
import glob
import argparse

def get_path_list(folder_path):
    '''Given a folder path this function returns a list of all jpg, jpeg and png image names
    in that folder'''
    types = ('*.jpg', '*.jpeg', '*.png')
    flatten = lambda l: [item for sublist in l for item in sublist]
    files_grabbed = flatten([glob.glob(folder_path + file) for file in types])
    return files_grabbed


def crop_px(folder_path, new_height, new_width):
    '''This function crops all the images in a given folder with height and width pixcels
    and list out rest all files where cropping was not possible due to size mismatch'''
    def crop(filepath, new_height, new_width):
        img = Image.open(filepath)
        width, height = img.size   # Get dimensions
        new_height, new_width = int(new_height), int(new_width)
        if new_height <= height and new_width <= width:
            left = (width - new_width)/2
            top = (height - new_height)/2
            right = (width + new_width)/2
            bottom = (height + new_height)/2

            # Crop the center of the image
            img = img.crop((left, top, right, bottom))
            img.save(filepath)
        else:
            filename = filepath.replace(folder_path,"")
            print(f"Not cropped: {filename}")
    list(map(lambda path: crop(path, new_height, new_width),get_path_list(folder_path)))

def crop_prcntg(folder_path, new_height_prcntg, new_width_prcntg):
    '''This function crops all the images in a given folder with height and width percentages
    and list out rest all files where cropping was not possible due to size mismatch'''
    def crop(filepath, new_height_prcntg, new_width_prcntg):
        img = Image.open(filepath)
        width, height = img.size   # Get dimensions
        new_height, new_width = int(height * (int(new_height_prcntg)/100)), int(width * (int(new_width_prcntg)/100))
        if new_height <= height and new_width <= width:
            left = (width - new_width)/2
            top = (height - new_height)/2
            right = (width + new_width)/2
            bottom = (height + new_height)/2

            # Crop the center of the image
            img = img.crop((left, top, right, bottom))
            img.save(filepath)
        else:
            filename = filepath.replace(folder_path,"")
            print(f"Not cropped: {filename}")
    list(map(lambda path: crop(path, new_height_prcntg, new_width_prcntg),get_path_list(folder_path)))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-f', '--folderpath', 
                        type=str,
                        help='Folder path of the image directory.')
    parser.add_argument('-crp_px', '--crop_pixel', nargs=2, type=int, metavar='<cropping_pixcel>',
                        help='Crop Pixcel Value')
    parser.add_argument('-crp_p', '--crop_prcntg', nargs=2, type=int, metavar='<cropping_prcntg>',
                        help='Crop Percentage Value')
    args = parser.parse_args()
    if args.crop_pixel is not None:
        height, width = args.crop_pixel
        crop_px(args.folderpath, height, width)
    elif args.crop_prcntg is not None:
        height, width = args.crop_prcntg
        crop_prcntg(args.folderpath, height, width)
