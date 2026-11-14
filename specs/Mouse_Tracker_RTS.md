# Mouse_Tracker_RTS.blend

## scene "Scene"  camera=Camera
game: fps=60 physics=BULLET gravity=9.8

### Light  [LIGHT]  pos=(4.08, 1.01, 5.90) rot_deg=(37.26, 3.16, 106.94) size=(0.00, 0.00, 0.00)
physics: STATIC mass=1.0

### Camera  [CAMERA]  pos=(38.95, -37.60, 27.40) rot_deg=(63.56, 0.00, 46.69) size=(0.00, 0.00, 0.00)
camera: lens=90.0 type=PERSP ortho_scale=7.31
physics: STATIC mass=1.0

### Plane  [MESH]  pos=(0.00, 0.00, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(32.89, 32.89, 0.00)
mesh "Plane": 4 verts 1 faces colour=#CCCCCC
physics: STATIC mass=1.0

### Cube  [MESH]  pos=(0.00, 0.00, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(0.70, 0.70, 0.70) (hidden)
mesh "Cube.001": 8 verts 6 faces
physics: DYNAMIC mass=10.0

### GoRing  [MESH]  pos=(0.00, 1.21, 0.00) rot_deg=(0.00, -0.00, 0.00) size=(2.50, 2.50, 0.05)
mesh "Torus": 144 verts 96 faces colour=#CCCCCC
physics: STATIC mass=1.0
- prop Buffer (BOOL) = False

### BufferRing  [MESH]  pos=(-0.00, 2.22, 0.81) rot_deg=(0.00, -0.00, 0.00) size=(9.73, 9.73, 0.00) parent=GoRing
mesh "Torus.001": 48 verts 0 faces colour=#CCCCCC
physics: STATIC mass=1.0
- prop Buffer (BOOL) = False

### ScriptedTracker  [MESH]  pos=(-0.00, -0.00, 0.03) rot_deg=(0.00, 180.00, 0.00) size=(2.00, 2.00, 2.00)
mesh "Cone": 33 verts 33 faces colour=#CCCCCC
physics: NO_COLLISION mass=1.0
- prop Tracker (FLOAT) = 0.0
- prop SetLoc (FLOAT) = 0.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, tick_skip=10, controllers=(bpy.data.objects['ScriptedTracker']...PythonController,), mouse_event=MOUSEOVERANY, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- SENSOR MOUSE "mouse_leftclick" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['ScriptedTracker']...PythonController,), mouse_event=LEFTCLICK, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_RTS.main -> []

### RTSUnit  [MESH]  pos=(-14.10, -0.00, 1.00) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.001": 4 verts 1 faces colour=#CCCCCC
physics: STATIC mass=1.0
- prop GoTo (BOOL) = False
- SENSOR MOUSE "Click" -> [And]: controllers=(bpy.data.objects['RTSUnit']...AndController,), mouse_event=LEFTCLICK, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- SENSOR PROPERTY "GOTO_T" -> [And.001]: controllers=(bpy.data.objects['RTSUnit']...AndController,), evaluation_type=PROPEQUAL, property=GoTo, value=True, value_min=True
- SENSOR COLLISION "Near" -> [And.002]: controllers=(bpy.data.objects['RTSUnit']...AndController,), property=Buffer
- CONTROLLER LOGIC_AND "And" -> [GOTO_T]
- CONTROLLER LOGIC_AND "And.001" -> [Steering]
- CONTROLLER LOGIC_AND "And.002" -> [GOTO_F]
- ACTUATOR PROPERTY "GOTO_T": mode=ASSIGN, property=GoTo, value=True, object_property=True
- ACTUATOR STEERING "Steering": mode=SEEK, velocity=3.0, acceleration=3.0, turn_speed=141.4, distance=1.0, target=obj:GoRing, facing=True, facing_axis=X, lock_z_velocity=True
- ACTUATOR PROPERTY "GOTO_F": mode=ASSIGN, property=GoTo, value=False, object_property=False

### Tracker  [MESH]  pos=(-0.00, -6.84, 0.03) rot_deg=(0.00, 180.00, 0.00) size=(2.00, 2.00, 2.00) (hidden)
mesh "Cone.001": 33 verts 33 faces colour=#CCCCCC
physics: NO_COLLISION mass=1.0

## text blocks
### mouse_tracker_RTS.py  (30 lines)
```
import bpy
import bge

####
## MOUSE TRACKER
## FROM https://youtu.be/-IeNnw6zzvQ
## CLICK AND DRAG TO MOVE TRACKER
#m ouse is tracked by ScriptedTracker object during mouse move
# GoRing will be placed at the clicked location
# RTSUnit will travel to the GoRing

####

def main():

    scene = bge.logic.getCurrentScene()
    cont = bge.logic.getCurrentController()

    mouse_over = cont.sensors["mouse_over"]
    mouse_click = cont.sensors["mouse_leftclick"]

    if mouse_over.positive:
        tracker = scene.objects["ScriptedTracker"]
        tracker.worldPosition = mouse_over.hitPosition
        tracker.worldPosition.z += 1

    if mouse_over.positive and mouse_click.positive:
        target = scene.objects["GoRing"]
        target.worldPosition = mouse_over.hitPosition
        target.worldPosition.z = 0
```