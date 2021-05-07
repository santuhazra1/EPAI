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

def resize_prcntg_prop(folder_path, percent_width):
    '''This function resizes all the images in a given folder with width percentage
    and proportionally its height changes'''
    def resize(filepath, percent_width):
        percent_width = int(percent_width) / 100
        img = Image.open(filepath)
        updated_height = int(img.height * percent_width)
        updated_width = int(img.width * percent_width)
        img = img.resize((updated_width, updated_height), Image.NEAREST)
        img.save(filepath)
    list(map(lambda path: resize(path, percent_width),get_path_list(folder_path)))

def resize_width_prop(folder_path, width):
    '''This function resizes all the images in a given folder with width pixcels
    and proportionally its height changes'''
    def resize(filepath, width):
        img = Image.open(filepath)
        updated_width = int(width)
        width_ratio =  updated_width / img.width
        updated_height = int(img.height * width_ratio)
        img = img.resize((updated_width, updated_height), Image.NEAREST)
        img.save(filepath)
    list(map(lambda path: resize(path, width),get_path_list(folder_path)))

def resize_height_prop(folder_path, height):
    '''This function resizes all the images in a given folder with height pixcels
    and proportionally its width changes'''
    def resize(filepath, height):
        img = Image.open(filepath)
        updated_height = int(height)
        height_ratio =  updated_height/ img.height
        updated_width = int(img.width * height_ratio)
        img = img.resize((updated_width, updated_height), Image.NEAREST)
        img.save(filepath)
    list(map(lambda path: resize(path, height),get_path_list(folder_path)))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-f', '--folderpath', 
                        type=str,
                        help='Folder path of the image directory.')
    parser.add_argument('-res_p', '--resize_prcntg', type=int, metavar='<resize_Percentage>',
                        help='Resize Percentage Value')
    parser.add_argument('-res_w', '--resize_width', type=int, metavar='<resize_Width>',
                        help='Resize Width Value')
    parser.add_argument('-res_h', '--resize_height', type=int, metavar='<resize_Height>',
                        help='Resize Height Value')
    args = parser.parse_args()
    if args.resize_prcntg is not None:
        resize_prcntg_prop(args.folderpath, args.resize_prcntg)
    elif args.resize_width is not None:
        resize_width_prop(args.folderpath, args.resize_width)
    elif args.resize_height is not None:
        resize_height_prop(args.folderpath, args.resize_height)