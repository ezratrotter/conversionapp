# conversionapp
Python application that converts and replaces coordinate columns in a Microsoft Access Database

App.py contains a PtQt5 Graphic user interface

converter.py contains a python script using PyProj that will read in the columns from the database, convert them, then rewrite them into the database again

updater.py contains a python script that looks up EPSG codes and finds the corresponding name. This is implemented in App.py to show the name of the Coordinate system that the user has chosen to enhance the user experience
