# FatigueSurveyor-Windows

This branch is for windows use, without docker.



## Prerequisites

- python3 and know the install location (like 'C:\Python38-32')

- PATH variable includes python components:

  1. open 'Control Panel'

  2. search for 'Environment'

  3. click 'Edit the System Environment Variables' button

  4. click 'Environment Variables' button

  5. edit an existing PATH variable or create one

     - edit:values are presented on separate lines
       			C:\Python38-32
       			C:\Python38-32\Lib\site-packages\
       			C:\Python38-32\Scripts\

     - create PATH:
       			C:\Python38-32;C:\Python38-32\Lib\site-packages\;C:\Python38-32\Scripts\

       

  6. click 'OK' to close all the Control Panel dialogs








## Structure and usage

### install requirements



`cd $env:HOMEPATH`

`curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`

`python get-pip.py`

`pip3 install opencv-python`

`pip3 install imutils`

`pip3 install PyQt5`

`pip3 install google-api-python-client`

`pip3 install oauth2client`







**clone this branch in C:\  for path length reasons**

  

### Start Survey Application

open command prompt

`python [path to FatigueSurveyorApp\src\main.py] `
