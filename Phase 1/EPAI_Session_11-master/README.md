## Image Handler Module

#### In this app we have created mainly 4 image modules with functionalities as  jpg to png conversion, png to jpg conversion, image resizing and image cropping. now let's discuss all these in details:

#### jpg and jpeg to png format conversion:

###### To convert jpg images to png we have used PIL library. Given a folder name this function will directly convert all jpg and jpeg files to png file format. We can pass folder path with -j2p argument from command prompt.

#### png to jpg format conversion:

###### To convert png images to jpg we have used PIL library. Given a folder name this function will directly convert all png files to jpg file format. We can pass folder path with -p2j argument from command prompt.

#### Image Resizing:

###### Here we have implemented 3 different functionalities as resize with percentage value, resize with width pixel value and resize with height pixel value. We can pass folder path and percentage , width and height pixels values with res_p, res_w and res_h correspondingly.

#### Image Cropping:

###### Here we have implemented 2 different functionalities as crop with percentage value and crop with height and width pixel values. We can pass folder path and height width percentage or height width pixels values with crp_px and crp_p correspondingly.