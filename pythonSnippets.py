#Sample python code snippets
# Name: NameOfPythonFile.py
# Description: What it does
# Requirements: modules needed
# Author: 

# Import modules
import arcpy, os, math, string, distutils

# Import a particular function from a module (enhance performance)
from acrpy import env
from distutils.dir_util import mkpath

# ----------------------------------------# 
## SETTING DIRECTORIES & GETTING PATHS ##
os.getcwd()

#Change directory
workspace = r"C:\Users\tessam\Documents\Python\Python 101"
os.chdir(workspace)

#Create a new directory or folders
from distutils.dir_util import mkpath
os.m


# ----------------------------------------# 
## WORKING WITH LISTS ##
# Populate a vector with number sequence (incrementing by two here)
listCount = [n for n in range(0,10,2)]
print '\n'.join(map(str, listCount))

# Print without the brackets
print str(listCount).strip('[]')

# Print contents of a list
for x in var:
        print x

# Nested loops #
x=range(0,4)
y=range(0,4)
for var in x:
    for var2 in y:
        print "X = " + str(var) + " , " + "Y = " + str(var2)


# Get list of feature classes in a .gdb & keep a running count
# of which empty feature classes are remove
fcs = arcpy.ListFeatureClasses()
    for fc in fcList:
        count = arcpy.GetCount_management(fc)
        if count [0] == '0':
            arcpy.Delete_management(fc)
            deleteCount += 1
        elif count [0] > '0':
            keepCount += 1



# ----------------------------------------# 
## PRINTING EXAMPLES ##
# How to set printing format 
for fc in fcs:
	#describe the feature class
	desc = arcpy.Describe(fc)
	
	#define a new variable reflecting the spatial reference
	sp = desc.SpatialReference

	#Print the three variables as follows
	print('{0}:{1} ({2})'.format(fc, sp.Name, sp.factoryCode))

# How to print local variables
print "\n".join(locals())
# More sophisticated way
for x in dir():
        myval = eval(x)
        print x, "is", type(x), "and is equal to", myval
        
# Quickly make a list and print it
listPrint = [str(n) for n in dir(arcpy)]
print "\n"+1.join(listPrint)


# ----------------------------------------# 
## FOR USE IN PYTHON ARCGIS SCRIPT TOOLS ##
# How to overwrite existing data within a script
arcpy.env.overwriteOutput = True

# How to create an input requirement and then record it's path
dest = arcpy.GetParameterAsText(0)
destPath = os.path.dirname(dest)
destPathName = os.path.basename(dest)

# Set a parameter for use in ArcGIS toolkit
workpath = acrpy.GetParameterAsText(0)

# Print a message in the tool window
firstMessage = 'Remove empty feature classes from a Geodatabase'
arcpy.AddMessage(firstMessage)
arcpy.AddMessage("Feature classes removed: " + str(variable))
 
