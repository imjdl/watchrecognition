#!/use/bin env python3
# coding = utf-8

import os
import sys
path = os.path.dirname(os.path.abspath(__file__))
img_list = []
for _,_,files in os.walk(path):
    img_list = files

img_list.remove(__file__)
args =  sys.argv
try:
    newname = args[1]
except IndexError:
    newname = 'n_'
filenumber = 0
for i in img_list:
    os.rename(i, newname+"-"+str(filenumber)+".jpg")
    filenumber+=1



