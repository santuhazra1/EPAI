
from jpg_to_png import convert as j2p_convert
from png_to_jpg import convert as p2j_convert
from img_resizer import resize_prcntg_prop, resize_width_prop, resize_height_prop
from img_cropper import crop_px, crop_prcntg
# path = "D:\\Virtual Box\\shared\\Data Science\\Tutorial\\1. TSAI\\3. EPAI\\Session 11\\Assignment\\EPAI_Session_11\\images\\"

def main(args=None):
    '''This is the main function through which we can control command and pass arguments.'''
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-j2p', '--jpg_png_path', metavar='<folderpath>',
                        help='Folder path of the image directory.')
    parser.add_argument('-p2j', '--png_jpg_path', metavar='<folderpath>',
                        help='Folder path of the image directory.')
    parser.add_argument('-res_p', '--resize_prcntg', nargs=2, metavar='<folderpath>, <resize_Percentage>',
                        help='Folder Path and Resize Percentage Value')
    parser.add_argument('-res_w', '--resize_width', nargs=2, metavar='<folderpath>, <resize_Width>',
                        help='Folder Path and Resize Width Value')
    parser.add_argument('-res_h', '--resize_height', nargs=2, metavar='<folderpath>, <resize_Height>',
                        help='Folder Path and Resize Height Value')
    parser.add_argument('-crp_px', '--crop_pixel', nargs=3, metavar='<folderpath>, <cropping_height>, <cropping_width>',
                        help='Folder Path and Crop Pixcel Value')
    parser.add_argument('-crp_p', '--crop_prcntg', nargs=3, metavar='<folderpath>, <cropping_height_p>, <cropping_width_p>',
                        help='Folder Path and Crop Percentage Value')                      
    args = parser.parse_args()

    if args.jpg_png_path is not None:
        j2p_convert(args.jpg_png_path)
    elif args.png_jpg_path is not None:
        p2j_convert(args.png_jpg_path)
    elif args.resize_prcntg is not None:
        path, prcntg = args.resize_prcntg
        resize_prcntg_prop(path, prcntg)
    elif args.resize_width is not None:
        path, width = args.resize_width
        resize_width_prop(path, width)
    elif args.resize_height is not None:
        path, height = args.resize_height
        resize_height_prop(path, height)
    elif args.crop_pixel is not None:
        path, height, width = args.crop_pixel
        crop_px(path, height, width)
    elif args.crop_prcntg is not None:
        path, height, width = args.crop_prcntg
        crop_prcntg(path, height, width)

if __name__ == "__main__":
    main()

