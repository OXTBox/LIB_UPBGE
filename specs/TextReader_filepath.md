# TextReader_filepath.blend

## scene "Scene"  camera=Camera
game: fps=60 physics=BULLET gravity=9.8

### Light  [LIGHT]  pos=(4.08, 1.01, 5.90) rot_deg=(37.26, 3.16, 106.94) size=(0.00, 0.00, 0.00)
physics: STATIC mass=1.0

### Camera  [CAMERA]  pos=(0.00, 0.00, 4.96) rot_deg=(0.00, 0.00, 0.00) size=(0.00, 0.00, 0.00)
camera: lens=12.0 type=PERSP ortho_scale=7.31
physics: STATIC mass=1.0

### Title  [FONT]  pos=(0.00, 2.48, -0.29) rot_deg=(0.00, 0.00, 0.00) size=(7.86, 1.06, 0.00)
text: "READ TEXT FROM  FILE 'test.txt'
IN SAME directory AS BLEND FILE"
physics: NO_COLLISION mass=1.0

### TextObject  [FONT]  pos=(0.00, 0.12, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(7.33, 0.71, 0.02)
text: "PRESS P TO TEST"
physics: NO_COLLISION mass=1.0
- prop Text (STRING) = 
- prop line (INT) = 0
- prop end (BOOL) = False
- prop length (INT) = 0
- prop init (BOOL) = False
- SENSOR PROPERTY "InitFalse" -> [Init]: controllers=(bpy.data.objects['TextObject']...PythonController,), evaluation_type=PROPEQUAL, property=init, value=False, value_min=False
- SENSOR DELAY "InitDelay0" -> [Init]: controllers=(bpy.data.objects['TextObject']...PythonController,)
- SENSOR DELAY "readDelay" -> [Python.001]: controllers=(bpy.data.objects['TextObject']...PythonController,), delay=30, use_repeat=True
- SENSOR PROPERTY "Length>0" -> [Python.001]: controllers=(bpy.data.objects['TextObject']...PythonController,), evaluation_type=PROPGREATERTHAN, property=length, value=0, value_min=0
- SENSOR PROPERTY "Property" -> [Python.001]: controllers=(bpy.data.objects['TextObject']...PythonController,), evaluation_type=PROPEQUAL, property=end, value=False, value_min=False
- CONTROLLER PYTHON "Init" script=textRead_localPath.py -> []
- CONTROLLER PYTHON "Python.001" script=textRead_localPath.displayLines -> []

## text blocks
### About  (4 lines)
```
Reads from file 'test.txt' in same folder as blend file
Displays each line of the file


```
### test.txt  (11 lines)
```
Text Reader Test.txt
Line 1
Line 2
Line 3
Line 4
Line 5
Line 6
Line 7
Line 8
Line 9
Line 10
```
### textRead_localPath.py  (47 lines)
```
import bpy
import bge
import os

# get current directory
blendFilePath = bpy.data.filepath
directory = os.path.dirname(blendFilePath)

global count
lines = []
    
filePath = directory +'\\test.txt'
print(filePath)
with open(filePath) as f:
    lines = f.readlines()  


## define this scripted text object
scene = bge.logic.getCurrentScene()
cont = bge.logic.getCurrentController()
TextObject = cont.owner
TextObject['length'] = len(lines)
TextObject['init'] = True

def displayLines():
    count = TextObject['line']
    count += 1
    print(count)
    
    if count > len(lines):
        TextObject['end'] = True
        return

    TextObject['Text'] = lines[count]
    TextObject['line'] = count
    
    ## RENDER TO PNGS IF YOU WANT TO
    #number = str('%04d' % TextObject['line'])
    #bge.render.makeScreenshot('//frame' + number + '.png')
    
    



     
    
    
```