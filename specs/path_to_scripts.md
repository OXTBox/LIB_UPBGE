# path_to_scripts.blend

## scene "Scene"  camera=Camera
game: fps=60 physics=BULLET gravity=9.8

### Cube  [MESH]  pos=(0.00, 0.00, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 2.00)
mesh "Cube": 8 verts 6 faces colour=#CCCCCC
physics: STATIC mass=1.0
- SENSOR DELAY "Actuator" -> [Python]: controllers=(bpy.data.objects['Cube']...PythonController,)
- CONTROLLER PYTHON "Python" script=path_to_scripts.py -> []

### Light  [LIGHT]  pos=(4.08, 1.01, 5.90) rot_deg=(37.26, 3.16, 106.94) size=(0.00, 0.00, 0.00)
physics: STATIC mass=1.0

### Camera  [CAMERA]  pos=(7.36, -6.93, 4.96) rot_deg=(63.56, 0.00, 46.69) size=(0.00, 0.00, 0.00)
camera: lens=50.0 type=PERSP ortho_scale=7.31
physics: STATIC mass=1.0

## text blocks
### path_to_scripts.py  (14 lines)
```
import sys
import bge

''' get the path to the scripts folder
    based on the current blend file
    this should run first in the event
    that scripts moved to that folder
    can't be found by the blend file '''
    
scriptFolder = bge.logic.expandPath('//Scripts')
if not scriptFolder in sys.path:
    sys.path.append(bge.logic.expandPath('//Scripts'))
    
print(scriptFolder)
```