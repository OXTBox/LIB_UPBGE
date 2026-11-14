# Simple_Player_Maze.blend

## scene "Scene"  camera=Camera
game: fps=60 physics=BULLET gravity=0.0

### Player  [MESH]  pos=(-0.34, -3.16, 0.76) rot_deg=(0.00, 0.00, 0.00) size=(1.23, 1.23, 1.23)
mesh "Cube": 8 verts 6 faces colour=#CCCCCC
physics: CHARACTER mass=1.0
- prop Direction (STRING) = 
- prop Hit (STRING) = 
- SENSOR KEYBOARD "W" -> [W]: controllers=(bpy.data.objects['Player']...AndController,), key=W, modifier_key_1=NONE, modifier_key_2=NONE
- SENSOR KEYBOARD "S" -> [S]: controllers=(bpy.data.objects['Player']...AndController,), key=S, modifier_key_1=NONE, modifier_key_2=NONE
- SENSOR KEYBOARD "A" -> [A]: controllers=(bpy.data.objects['Player']...AndController,), key=A, modifier_key_1=NONE, modifier_key_2=NONE
- SENSOR KEYBOARD "D" -> [D]: controllers=(bpy.data.objects['Player']...AndController,), key=D, modifier_key_1=NONE, modifier_key_2=NONE
- SENSOR COLLISION "L_WARP" -> [Python, And]: controllers=(bpy.data.objects['Player']...PythonController, bpy.data.objects['Player']...AndController), property=LeftWarp, material=LeftWarp
- SENSOR COLLISION "R_WARP" -> [Python.001, And.001]: controllers=(bpy.data.objects['Player']...PythonController, bpy.data.objects['Player']...AndController), property=RightWarp, material=RightWarp
- CONTROLLER LOGIC_AND "W" -> [Y+]
- CONTROLLER LOGIC_AND "S" -> [Y-]
- CONTROLLER LOGIC_AND "A" -> [X-]
- CONTROLLER LOGIC_AND "D" -> [X+]
- CONTROLLER PYTHON "Python" script=Warp_L_R.warpRight -> []
- CONTROLLER LOGIC_AND "And" -> [Property]
- CONTROLLER PYTHON "Python.001" script=Warp_L_R.warpLeft -> []
- CONTROLLER LOGIC_AND "And.001" -> [Property.001]
- ACTUATOR MOTION "Y+": mode=OBJECT_CHARACTER, servo_mode=SERVO_LINEAR, force_max_y=0.33, offset_location=(0.0, 0.33, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "Y-": mode=OBJECT_CHARACTER, servo_mode=SERVO_LINEAR, force_max_y=-0.33, offset_location=(0.0, -0.33, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "X-": mode=OBJECT_CHARACTER, servo_mode=SERVO_LINEAR, force_max_x=-0.33, offset_location=(-0.33, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_add_character_location=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "X+": mode=OBJECT_CHARACTER, servo_mode=SERVO_LINEAR, force_max_x=0.33, offset_location=(0.33, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR PROPERTY "Property": mode=ASSIGN, property=Hit, value="LeftWarp", object_property="LeftWarp"
- ACTUATOR PROPERTY "Property.001": mode=ASSIGN, property=Hit, value="RightWarp", object_property="RightWarp"

### Light  [LIGHT]  pos=(3.48, 1.01, 5.90) rot_deg=(37.26, 3.16, 106.94) size=(0.00, 0.00, 0.00)
physics: STATIC mass=1.0

### Camera  [CAMERA]  pos=(-0.20, 0.00, 16.08) rot_deg=(0.00, 0.00, 0.00) size=(0.00, 0.00, 0.00)
camera: lens=8.0 type=ORTHO ortho_scale=69.31
physics: STATIC mass=1.0

### BottomWall  [MESH]  pos=(-0.60, -18.61, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(68.56, 0.96, 2.00)
mesh "Cube.001": 8 verts 6 faces colour=#CCCCCC
physics: STATIC mass=1.0

### TopWall  [MESH]  pos=(-0.60, 18.50, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(68.56, 0.96, 2.00)
mesh "Cube.002": 8 verts 6 faces colour=#CCCCCC
physics: STATIC mass=1.0

### TopLeftWall  [MESH]  pos=(-34.25, 9.89, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(1.04, 19.04, 2.00)
mesh "Cube.003": 8 verts 6 faces colour=#CCCCCC
physics: STATIC mass=1.0

### BottomLeftWall  [MESH]  pos=(-34.33, -10.36, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(1.04, 16.18, 2.00)
mesh "Cube.004": 8 verts 6 faces colour=#CCCCCC
physics: STATIC mass=1.0

### TopRightWall  [MESH]  pos=(34.25, 10.17, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(1.04, 17.44, 2.00)
mesh "Cube.005": 8 verts 6 faces colour=#CCCCCC
physics: STATIC mass=1.0

### BottomRightWall  [MESH]  pos=(34.17, -10.16, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(1.04, 17.44, 2.00)
mesh "Cube.006": 8 verts 6 faces colour=#CCCCCC
physics: STATIC mass=1.0

### Floor  [MESH]  pos=(-0.60, 0.00, -1.00) rot_deg=(0.00, 0.00, 0.00) size=(73.15, 37.28, 0.10)
mesh "Cube.007": 8 verts 6 faces colour=#CCCCCC
physics: STATIC mass=1.0

### Cube  [MESH]  pos=(0.00, 0.00, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(66.00, 38.00, 6.05) (hidden)
mesh "Cube.035": 1392 verts 1408 faces
physics: STATIC mass=1.0

### Maze  [MESH]  pos=(-32.93, -16.77, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(65.60, 36.20, 3.00)
mesh "Plane": 1416 verts 1239 faces
physics: STATIC mass=1.0

### LeftWarp  [MESH]  pos=(-35.15, -0.93, 0.35) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 2.00)
mesh "Cube.037": 8 verts 6 faces colour=#CCCCCC
physics: STATIC mass=1.0
- prop LeftWarp (BOOL) = False

### LeftWarpIn  [MESH]  pos=(-32.75, -0.99, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.002": 4 verts 1 faces colour=#CCCCCC
physics: NO_COLLISION mass=1.0

### RightWarp  [MESH]  pos=(36.08, 0.06, 0.36) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 2.00)
mesh "Cube.038": 8 verts 6 faces colour=#CCCCCC
physics: DYNAMIC mass=1.0
- prop RightWarp (STRING) = 

### RightWarpIn  [MESH]  pos=(32.90, 0.00, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.001": 4 verts 1 faces colour=#CCCCCC
physics: NO_COLLISION mass=1.0

## text blocks
### Text  (3 lines)
```
WASD to move
see Warp_L_R.py
for how the left and right warps work
```
### Warp_L_R.py  (22 lines)
```
import bge

scene = bge.logic.getCurrentScene()
cont = bge.logic.getCurrentController()

leftWarp = scene.objects["LeftWarpIn"]
leftLoc = leftWarp.worldPosition

rightWarp = scene.objects["RightWarpIn"]
rightLoc = rightWarp.worldPosition

player = scene.objects["Player"]


def warpLeft():
    # set the position of the player
    player.worldPosition = leftLoc

def warpRight():
    # set the position of the player
    player.worldPosition = rightLoc

```