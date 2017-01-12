"""
Get numbers from pictures.   Author:ZCB
Lib: PIL,pyocr
Ref:https://github.com/jflesch/pyocr
"""


import os
from PIL import Image
import pyocr
import pyocr.builders

def trimPics(imagePath,outPath,box): 
    """
        type: imagePath(str) , box: turple(4)(LeftTopx,LeftTopy,RightDownx,RightDowny)
    """
    im = Image.open(imagePath)
    region = im.crop(box)  

    # split the pic based on color
    r,g,b = region.split()
    
    r.save(outPath) 
    return 1



def im2str(imagePath):
    """
        type: imagePath(str) 
        rtype: str
    """
    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        print("No OCR tool found")
        sys.exit(1)
    # The tools are returned in the recommended order of usage
    tool = tools[0]

    txt = tool.image_to_string(
    Image.open(imagePath),
    lang='eng',
    builder=pyocr.builders.TextBuilder()
    )
    
    return txt

def ocrBike(imagePath):
    """
        type: imagePath(str) 
        rtype: str,str
    """
    #box for bikeNo
    box=(460,0,570,40)
    trimPics(imagePath,'bikeNo.jpeg',box)
    txt=im2str('bikeNo.jpeg')
    #save digits
    bikeNo = ''.join([s for s in txt if s.isdigit()])

    #box for bikecode
    box=(130,100,570,230)
    trimPics(imagePath,'bikeCode.jpeg',box)
    txt=im2str('bikeCode.jpeg')
    #print(bikeCode) 
    #save digits
    bikeCode = ''.join([s for s in txt if s.isdigit()])
    return imagePath,bikeNo,bikeCode



if __name__ == '__main__':
    
    
    #trimPics('test.jpeg','bikeNo.jpeg',(460,510,570,545))
    #bikeNo=im2str('bikeNo.jpeg')
    picDir='pics'

    for i in os.listdir(picDir):
        if 'jpeg' in i or 'png' in i or 'jpg' in i:
            print(ocrBike(picDir+'/'+i))




    

