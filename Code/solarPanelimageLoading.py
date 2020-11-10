#!/usr/bin/env python
# coding: utf-8

# In[10]:


#!/usr/bin/env python
# coding: utf-8

# In[22]:

import random
from sklearn.preprocessing import LabelBinarizer
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np
import glob
import cv2
import os
import shutil

y = "/Users/aarav/Downloads/soilingDatasetSolarPanel/PanelImages/"
x = "/Users/aarav/Documents/testmultiplycsv.csv"

def load_solar_images(inputPath):
    
    val_list = [] #This list is used to transfer the validation data
    train_list = [] #This list is used to transfer the training data
    
    column = ["0.291411765","solar_Fri_Jun_16_10__0__11_2017_L_0.906153208302_I_0.321592156863.jpg"]
    dataframe = pd.read_csv(inputPath, usecols=column)
    
    for c in range(0,8646) : 
        val_list.append(c)
        
    train_list = random.sample(range(0,8646),6916) #taking random 80% sample of data for training
    
    for a in range(0,8646): 
        if a in lst: 
            val_list.remove(a) #removes training data from validation list
            
    for a in train_list : 
        imagePath = dataframe.loc[a,"solar_Fri_Jun_16_10__0__11_2017_L_0.906153208302_I_0.321592156863.jpg"]
        directory = y+imagePath
        shutil.move(directory,"/Users/aarav/Documents/final_model/train/high") #moves to training directory
    
    for x in val_list: 
        imagePath = dataframe.loc[x,"solar_Fri_Jun_16_10__0__11_2017_L_0.906153208302_I_0.321592156863.jpg"]
        direct = y+imagePath
        shutil.move(direct,"/Users/aarav/Documents/final_model/validation/high") #moves to validation directory 
        
load_solar_images(x)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




