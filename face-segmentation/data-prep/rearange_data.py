from xml.dom import minidom
from shutil import copyfile
import os
import sys

root_path = '/home/ivanna/data/headsegmentation/'
path_to_xml='/home/ivanna/data/headsegmentation/training.xml'
path_to_training_files = '/home/ivanna/data/headsegmentation/training_arranged/'
xml_doc = minidom.parse(path_to_xml)
imgs= xml_doc.getElementsByTagName('srcimg') 
labels= xml_doc.getElementsByTagName('labelimg') 

for i in range(len(imgs)):
    img = imgs[i].attributes['name'].value
    lbl = labels[i].attributes['name'].value
    src_img = root_path + img.replace('\\', '/')
    src_lbl = root_path + img.replace('\\', '/')
    dest_img = path_to_training_files + str(i) + '.' + img.split('.')[-1]
    dest_lbl = path_to_training_files + str(i) + '_gt.' + lbl.split('.')[-1]
    #print(dest_img)
    #print(dest_lbl)
    copyfile(src_img, dest_img)
    copyfile(src_lbl, dest_lbl)
