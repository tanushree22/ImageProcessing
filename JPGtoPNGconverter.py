# note-- make sure that this code and your image folder(you want to process) is in the same directory.
import sys
import os
from PIL import Image
if len(sys.argv)<3:
    print('give two arguments please!')
    exit
# grab first and second argument from command line
# orgfolder is the existing folder of images having images in jpg format
# newfolder is the folder which will be created after exec.of the code , having the images in .png format
orgfolder=sys.argv[1]
newfolder=sys.argv[2]
print(orgfolder,newfolder)
# check if second folder given in as argument exists , if not create the folder
path=os.path.join('./',newfolder)
if os.path.isdir(path)== False:
    os.mkdir(path)
# loop through the directory
for subdirs,dirs,files in os.walk(os.path.join('./',orgfolder)):
    for f in files:
        try:
            print(f)
            img=Image.open(os.path.join('./',orgfolder,f))
            print(img)
            filename,ext=f.split('.')
            # saving the new file in second directory
            img.save(os.path.join(path,filename+".png"),'png')
        except:
            continue  #if the file is not image then it will jut move on to next iteration6
        