import os
from pickletools import optimize
from PIL import Image
import pandas as pd
import numpy as np
import time
import re

directory = '.\\simulated'
row_list = []
column_titles = ['ID', 
                 'Path', 
                 'Initial Energy', 
                 'Number of Spores', 
                 'Absorbtion Value', 
                 'Branch Rate', 
                 'At Border Conditions', 
                 'Viewing Angle', 
                 'Vision Distance', 
                 'Wiggle Angle', 
                 'Energy Per Step', 
                 'Energy Per Split', 
                 'Radius Petri', 
                 'Radius Length',
                 'Probability Random Walk',
                 'Water Agar Energy',
                 'Percentage food patch',
                 'Water Agar',
                 'Distribute',
                 'Food input'
                 ]

ID = 0

for filename in os.listdir(directory):
    if filename.endswith(".png"):
        file_name = filename.split('_')
        PRW, img_type = file_name[len(file_name)-1].split('.')
        if "false" in PRW: 
                PRW = False
        else:
                PRW = True
        print(file_name)
        dict = {
                'ID' : ID, 
                'Path' : filename, 
                'Initial Energy' : float(file_name[1]),
                'Number of Spores' : float(file_name[3]), 
                'Absorbtion Value' : float(file_name[5]),
                'Branch Rate' : float(file_name[7]),
                'At Border Conditions' : str(file_name[9]),
                'Viewing Angle' : float(file_name[11]),
                'Vision Distance' : float(file_name[13]),
                'Wiggle Angle' : float(file_name[15]),
                'Energy Per Step' : float(file_name[17]),
                'Energy Per Split' : float(file_name[19]),
                'Radius Petri' : float(file_name[21]),
                'Radius Length' : float(file_name[23]),
                'Probability Random Walk' : float(file_name[25]),
                'Water Agar Energy': float(file_name[27]),
                'Percentage food patch': float(file_name[29]),
                'Water Agar': str(file_name[31]),
                'Distribute': str(file_name[33]),
                'Food input': PRW
                }
        row_list.append(dict)
        img = Image.open(r'.\\simulated\\'+filename)
        # changed_img = rgb_im = img.convert('RGB') #if you want to convert image to jpg
        changed_path = str(ID)+'.png'
        img.save(r'.\\converted\\'+changed_path)
        ID += 1

df = pd.DataFrame(row_list, columns=column_titles)
df.to_csv('.\\converted\\map.csv')