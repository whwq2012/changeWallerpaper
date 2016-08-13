# -*-coding:utf-8-*-
# Created by whwq2012 on 2016/8/13.
import win32api
import win32con
import win32gui
import os
import pickle
import random
AllphotoFolder = 'G:\\anima_photo\\'
cachePhotoList = AllphotoFolder+'cacheList'
photoList = dict()
if os.path.exists(cachePhotoList):
    f = open(cachePhotoList, 'rb')
    photoList = pickle.load(f)
    f.close()
else:
    allPath = os.listdir(AllphotoFolder)
    for folderPath in allPath:
        singlePhotoList = os.listdir(AllphotoFolder + folderPath)
        photoList[folderPath] = singlePhotoList
    f = open(cachePhotoList, 'wb')
    pickle.dump(photoList, f)
    f.close()
folder = random.choice(photoList.keys())
photo_path = AllphotoFolder + folder + '\\' + random.choice(photoList[folder])
print photo_path
k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, 'Control Panel\\Desktop', 0, win32con.KEY_SET_VALUE)
win32api.RegSetValueEx(k, 'TileWallpaper', 0, win32con.REG_SZ, '0')
win32api.RegSetValueEx(k, 'WallpaperStyle', 0, win32con.REG_SZ, '1')
'''
居中  TileWallpaper=0, WallpaperStyle=1
平铺  TileWallpaper=1, WallpaperStyle=0
拉伸  TileWallpaper=0, WallpaperStyle=2
'''
win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, photo_path) # win32con.SPI_SETDESKWALLPAPER 的意思是换壁纸模式
