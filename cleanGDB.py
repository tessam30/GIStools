# Name: CleanGDB.py
# Description: Clean-up geodatabase using loops to eliminate empty feature classes
# Requirements: sys, string and arcpy toolboxes, no extensions needed
# Author: Tim Essam, GeoCenter

#Import the modules needed to run the script
import sys, string, arcpy

#Use the from statement to load submodule env; don't need to type arcpy all the time
from arcpy import env
from string import *

workpath = arcpy.GetParameterAsText(0)

#Set up workspace
env.workspace = workpath

firstMessage = '\nRemove Empty Feature Classes from a geodatabase - developed by USAID GeoCenter. \n'
print firstMessage
arcpy.AddMessage(firstMessage)

#List feature classes in current geodatabase to variable fcList
fcList = arcpy.ListFeatureClasses()

#How many feature classes in gdb?
beg = len(fcList)

#Instead list how many files are in the variable
arcpy.AddMessage("Feature classes to be reviewed: " + str(beg))

#keep a count of how many files were deleted/kept
deleteCount = 0
keepCount = 0

#Loop through gdb and remove empty features classes, return a count.
try:
    for fc in fcList:
        count = arcpy.GetCount_management(fc)
        if count [0] == '0':
            arcpy.Delete_management(fc)
            deleteCount += 1
        elif count [0] > '0':
            keepCount += 1
            
except:
    print arcpy.GetMessages()

#print how many feature classes remain in gdb
arcpy.AddMessage("Feature classes removed: " + str(deleteCount))
arcpy.AddMessage("Feature classes preserved: " + str(keepCount))
arcpy.AddMessage('\nContact tessam[at]usaid.gov with any comments or information related to this tool.\n')
