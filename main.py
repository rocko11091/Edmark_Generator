"""
Program Name: Edmark Generator

Developer: Rikhav Kothari

Description:

Algorithm:

Pt. 1
- Ask for user if user will enter lesson number or word
- If lesson #, search list for word
- If word, search list for word, identify location, return lesson #

Pt. 2
- follow PyScramble Algorithm
- ask for

Pt. 3



Resources:

how to call an image in a web browser
- With default - https://pythonconquerstheuniverse.wordpress.com/2010/10/16/how-to-open-a-web-browser-from-python/
- With non-default - https://stackoverflow.com/questions/3744573/python-code-to-open-image-in-browser

how to insert text/other image into an image
- https://stackoverflow.com/questions/3744573/python-code-to-open-image-in-browser
- https://stackoverflow.com/questions/8154825/how-can-i-write-text-over-an-image-and-overlay-another-image-on-it-in-python
"""
import PIL
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

import webbrowser
import os

cur_wd = os.getcwd()
print (cur_wd)

#Read, open image
im_file_name = "edmark_wkst_1_template.jpg"
im = Image.open(im_file_name)


#rotate image clockwise
#im = im.rotate(90)

#show image
im.show()



font_Comic = 


"""
Old Code
url = "edmark_wkst_1.jpg"
#Display image
webbrowser.open(url)
"""

