# Mouse_Tracker_01.blend

## scene "Scene"  camera=Camera
game: fps=60 physics=BULLET gravity=9.8

### Light  [LIGHT]  pos=(4.08, 1.01, 5.90) rot_deg=(37.26, 3.16, 106.94) size=(0.00, 0.00, 0.00)
physics: STATIC mass=1.0

### Camera  [CAMERA]  pos=(7.36, -6.93, 4.96) rot_deg=(63.56, 0.00, 46.69) size=(0.00, 0.00, 0.00)
camera: lens=50.0 type=PERSP ortho_scale=7.31
physics: STATIC mass=1.0

### Tracker  [MESH]  pos=(0.00, 0.00, 0.78) rot_deg=(0.00, 180.00, 0.00) size=(2.00, 2.00, 2.00)
mesh "Cone": 33 verts 33 faces colour=#CCCCCC
physics: NO_COLLISION mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['Tracker']...PythonController,), mouse_event=MOUSEOVERANY, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- SENSOR MOUSE "mouse_leftclick" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['Tracker']...PythonController,), mouse_event=LEFTCLICK, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker.main -> []

### Plane  [MESH]  pos=(0.00, 0.00, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(32.89, 32.89, 0.00)
mesh "Plane": 4 verts 1 faces colour=#CCCCCC
physics: STATIC mass=1.0

## text blocks
### mouse_tracker.py  (27 lines)
```

import bge

####
## MOUSE TRACKER
## FROM https://youtu.be/-IeNnw6zzvQ
## CLICK AND DRAG TO MOVE TRACKER
####

def main():
    loc = [0,0,0]
    scene = bge.logic.getCurrentScene()
    cont = bge.logic.getCurrentController()

    mouse_over = cont.sensors["mouse_over"]
    mouse_click = cont.sensors["mouse_leftclick"]

    if mouse_over.positive and mouse_click.positive:
        tracker = scene.objects["Tracker"]
        xyz = mouse_over.hitPosition
        tracker.worldPosition = xyz 
        
        



        
```