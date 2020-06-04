# -*- coding: utf-8 -*-
""" convert fast huge number of depth .plk to .png files using multiprocessing """

""" issues """
# https://rebeccabilbro.github.io/convert-py2-pickles-to-py3/
# works only with Python2.7 @ depth_image = pickle.load(f)
# works only with Python3.6 @ depth_image = pickle.load(f, encoding='bytes')

import os
import cv2
import time
import pickle
import numpy as np
import concurrent.futures


# clear terminal ctrl+L
osName = os.name
if osName == 'posix':
    os.system('clear')
else:
    os.system('cls')




def pkl2png(folderName, subfolderCount):
    
    for i in range(subfolderCount):

        print('opening folder', folderName, 'opening subfolder', i)

        pklfilepath = path + folderName + '/'  + str(i) + '/' +  'depth.pkl'
        depfilepath = path + folderName + '/'  + str(i) + '/' +  'depth2.png'

        # print('converting this .pkl file', pklfilepath)
        # print('into this .png file', depfilepath)

        with open(pklfilepath, mode='rb') as f:
            # depth_image = pickle.load(f)  # Python2.7
            depth_image = pickle.load(f, encoding='bytes')  # Python3.6
            # depth_image = np.uint8(depth_image)

        cv2.imwrite(depfilepath, depth_image)




if __name__ == '__main__':

    path = os.path.dirname(__file__) + '/your/folder/path'
    print(path)

    startTime  = time.time()
    
    # folderName = ['a', 'b', 'c', 'd', 'e']
    # subfolderCount = [53, 50, 50, 59, 56]
    
    folderName = ['a', 'b', 'c', 'd']
    subfolderCount = [5, 5, 5, 5]
    
    arg = (folderName, subfolderCount)
    
    """ multi processing """
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(pkl2png, *arg)
        
    finishedTime = time.time()
    print('finished in', round(finishedTime-startTime, 2), 'second(s)')







    """ slow method """
    # #def pkl2png(path, name, subfoldercount):
    # for i in range(5):
        # pkl2png(folderName[i], subfolderCount[i])
    
    



    

    """ basic one by one """
    # i = 0
    # filepath        = path + folderName[0] + '/'  + str(i) + '/' +  'depth.pkl'
    # depthfilepath   = path + folderName[0] + '/'  + str(i) + '/' +  'depth.png'
    # print(filepath)

    # with open(filepath, mode='rb') as f:
    #     d_img = pickle.load(f)
    #     # d_img = np.uint8(d_img)
    # cv2.imwrite(depthfilepath, d_img) 
    
    