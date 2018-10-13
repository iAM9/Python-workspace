#!/usr/bin/env python

#################################
import sys
import os
import shutil
import subprocess

import time

import random

import Tkinter
import tkMessageBox
from tkMessageBox import *
from tkFileDialog import *

import ffmpy
import ffprobe


#################################

def compile(absPath):
    listOfFullFilePaths = []
    listOfFileNames = []
    totalSize = 0
    videoSeconds = []

    for path, subdirs, files in os.walk(absPath):
        for name in files:
            if name.endswith(".mp4") or name.endswith(".mov"):
                filePath = os.path.join(path, name)
                listOfFileNames.append(name)
                listOfFullFilePaths.append(filePath)

    print ("\n".join(listOfFullFilePaths))
    print "\n"
    print ("\n".join(listOfFileNames))
    print "\n==============================================="
    print "\n\nSource folder selected: " + str(absPath)
    print "\n==============================================="
    print "\n==============================================="

    for i in xrange(0, len(listOfFileNames)):
        videoName = listOfFileNames[i]
        videoFile = listOfFullFilePaths[i]
        currentDir = os.getcwd()
        videoSec2 = subprocess.check_output(
            ['\"'+os.getcwd() + '\\ffmpegwin64\\ffmpegwin64\\bin\\ffprobe.exe\"', '-i', videoFile, '-show_entries',
             'format=duration', '-v', 'quiet', '-of', 'csv=%s' % ("p=0")])

     #   hms = subprocess.check_output([os.getcwd() + '\\ffmpegwin64\\ffmpegwin64\\bin\\ffprobe.exe', '-i', videoFile, '-show_entries','format=duration', '-v', 'quiet', '-of', 'csv=%s' % ("p=0"), '-sexagesimal'])

      #  print(hms)
        videoSec = float(videoSec2)
        tm = time.gmtime(videoSec)
        # videoData = ffprobe.FFProbe(videoFile)
        # print str(videoData)
        # for stream in videoData.streams:
        # if stream.isVideo():
        # videoSec = stream.durationSeconds()

        # D:/newfolder/temp/ruin.mp4

        outputNameTempList = []
        temp1 = listOfFullFilePaths[i]
        while temp1 != absPath:
            base = os.path.basename(temp1)
            temp1 = os.path.dirname(temp1)
            base = base + '_'

            outputNameTempList.insert(0, base)

        print outputNameTempList
        outputName = ''.join(outputNameTempList)

        outputName = outputName.replace(".mov_", "")
        outputName = outputName.replace(".mp4_", "")

        exeDir = '\"' + currentDir + '\\ffmpegwin64\\ffmpegwin64\\bin\\ffmpeg.exe\" -i \"'



        drawtextSettings1 = '-vf [in]\"drawtext=fontfile=\'/Windows/Fonts/arial.ttf\':fontsize=20:box=1:text=\''


        # for beginning of video
        frameSettings = '\" -ss 1 -r 1 -vframes 1 -q:v 2 '
        outputName1 = outputName + "_01_begin.jpeg"
        finalName = os.path.dirname(videoFile) + "\\" + outputName1
        drawtextSettings2 = '\', drawtext=fontfile=\'/Windows/Fonts/arial.ttf\':fontsize=20:box=1:x=main_w-text_w:text=\'0\:0\:1\'\"'
        print outputName1
        drawtextSettings_begin = drawtextSettings1 + outputName1 + drawtextSettings2
        settings = frameSettings + drawtextSettings_begin
        outputStr = exeDir + videoFile + settings + ' \"' + finalName + '\"'
        subprocess.call(outputStr, shell=True)

        # for middle of video
        frameSettings = '\" -ss '+str(videoSec/2)+' -r 1 -vframes 1 -q:v 2 '
        outputName2 = outputName + "_02_mid.jpeg"
        finalName = os.path.dirname(videoFile) + "\\" + outputName2
        print outputName2
        drawtextSettings2 = '\', drawtext=fontfile=\'/Windows/Fonts/arial.ttf\':fontsize=20:box=1:x=main_w-text_w:text=\''+str(time.gmtime(videoSec/2)[3])+'\:'+str(time.gmtime(videoSec/2)[4])+'\:'+str(time.gmtime(videoSec/2)[5])+'\'\"'
        drawtextSettings_begin = drawtextSettings1 + outputName2 + drawtextSettings2
        settings = frameSettings + drawtextSettings_begin
        outputStr = exeDir + videoFile + settings + ' \"' + finalName + '\"'
        subprocess.call(outputStr, shell=True)

        # for end of video
        frameSettings = '\" -ss ' + str(videoSec-1) + ' -r 1 -vframes 1 -q:v 2 '
        outputName2 = outputName + "_03_mid.jpeg"
        finalName = os.path.dirname(videoFile) + "\\" + outputName2
        print outputName2
        drawtextSettings2 = '\', drawtext=fontfile=\'/Windows/Fonts/arial.ttf\':fontsize=20:box=1:x=main_w-text_w:text=\'' + str(
            time.gmtime(videoSec-1)[3]) + '\:' + str(time.gmtime(videoSec-1)[4]) + '\:' + str(
            time.gmtime(videoSec-1)[5]) + '\'\"'
        drawtextSettings_begin = drawtextSettings1 + outputName2 + drawtextSettings2
        settings = frameSettings + drawtextSettings_begin
        outputStr = exeDir + videoFile + settings + ' \"' + finalName + '\"'
        subprocess.call(outputStr, shell=True)


        # # for end of video
        # outputName2 = outputName + "_03_end.jpeg"
        # #outputName.replace("01_begin.jpeg","03_end.jpeg")
        # finalName = os.path.dirname(videoFile) + "\\" + outputName2
        # print outputName2
        # outputStr = currentDir + '/ffmpeg-20160718-450cf40-win64-static/ffmpeg-20160718-450cf40-win64-static/bin/ffmpeg.exe -i \"' + videoFile + '\" -ss '+str(videoSec-5)+' -r 1 -qscale 0 -vframes 1 -vf \"drawtext=fontfile=/Windows/Fonts/arial.ttf:fontsize=20:box=1:text=\'' + outputName2 + '\'\" \"' + finalName + '\"'
        # subprocess.call(outputStr, shell=True)

        # # for mid of video
        # outputName3 = outputName + "_02_mid.jpeg"
        # finalName = os.path.dirname(videoFile) + "\\" + outputName3
        # print outputName3
        # outputStr = currentDir + '/ffmpeg-20160718-450cf40-win64-static/ffmpeg-20160718-450cf40-win64-static/bin/ffmpeg.exe  -i \"' + videoFile + '\" -ss ' + str((videoSec/2)-0.1) + ' -r 1 -qscale 0 -vframes 1 -vf \"drawtext=fontfile=/Windows/Fonts/arial.ttf:fontsize=20:box=1:text=\'' + outputName3 + '\'\" \"' + finalName + '\"'
        # subprocess.call(outputStr, shell=True)
    print "Screen-grabs collected succesfully!"


##############################################




##############################################
def cmd_about():
    showinfo("About", "")


##############################################



##############################################
def cmd_selectFolder():
    absPath = askdirectory()
    if absPath == '':
        print "Nothing selected"
    else:
        # print absPath
        compile(absPath)


##############################################



##############################################
if __name__ == '__main__':
    top = Tkinter.Tk()
    top.title("")
    Tkinter.Label(top, text="----======----======----======----").pack()
    Tkinter.Button(top, text='Select Folder', command=cmd_selectFolder).pack()
    Tkinter.Button(top, text='About', command=cmd_about).pack()

    top.mainloop()


##############################################


#################### ROUGH WORK ################

# ffmpeg -ss 230 -i videoName -r 1 -vframes 1 -drawtext="fontsize=20: box=1: text="



#     for videoFile in listOfFullFilePaths:
#         videoData = ffprobe.FFProbe(videoFile)
#         print str(videoData)
#         for stream in videoData.streams:
# 			if stream.isVideo():
# 				videoSec = stream.durationSeconds()
# 				#videoSeconds.append(videoSec)

# 	temp = videoFile+".jpeg"
# 	print temp

# #ffmpeg -ss 230 -i RUIN.mp4 -r 1

# 	subprocess.call(['ffmpeg',  '-ss', ' '+str(videoSec), '-i', ' '+videoFile, '-r', '1', '-vframes', '1', 'output123.jpeg'], shell=True)

