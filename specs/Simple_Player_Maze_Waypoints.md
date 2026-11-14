# Simple_Player_Maze_Waypoints.blend

## scene "Scene"  camera=Camera
game: fps=60 physics=BULLET gravity=0.0

### Light  [LIGHT]  pos=(3.48, 1.01, 5.90) rot_deg=(37.26, 3.16, 106.94) size=(0.00, 0.00, 0.00)
physics: STATIC mass=1.0

### Camera  [CAMERA]  pos=(-0.20, 0.00, 16.08) rot_deg=(0.00, 0.00, 0.00) size=(0.00, 0.00, 0.00)
camera: lens=8.0 type=ORTHO ortho_scale=69.31
physics: STATIC mass=1.0

### Player  [MESH]  pos=(-0.97, -3.13, 0.05) rot_deg=(0.00, 0.00, 0.00) size=(1.23, 1.23, 1.23)
mesh "Cube.009": 8 verts 6 faces colour=#CCCCCC
physics: CHARACTER mass=1.0
- prop Direction (STRING) = 
- prop Hit (STRING) = 
- SENSOR KEYBOARD "W" -> [W]: controllers=(bpy.data.objects['Player']...AndController,), key=W, modifier_key_1=NONE, modifier_key_2=NONE
- SENSOR KEYBOARD "S" -> [S]: controllers=(bpy.data.objects['Player']...AndController,), key=S, modifier_key_1=NONE, modifier_key_2=NONE
- SENSOR KEYBOARD "A" -> [A]: controllers=(bpy.data.objects['Player']...AndController,), key=A, modifier_key_1=NONE, modifier_key_2=NONE
- SENSOR KEYBOARD "D" -> [D]: controllers=(bpy.data.objects['Player']...AndController,), key=D, modifier_key_1=NONE, modifier_key_2=NONE
- SENSOR COLLISION "Collision" -> [Python, And]: controllers=(bpy.data.objects['Player']...PythonController, bpy.data.objects['Player']...AndController), property=LeftWarp, material=LeftWarp
- SENSOR COLLISION "Collision.001" -> [Python.001, And.001]: controllers=(bpy.data.objects['Player']...PythonController, bpy.data.objects['Player']...AndController), property=RightWarp, material=RightWarp
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

### BottomWall  [MESH]  pos=(-0.19, -18.61, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(69.54, 17.65, 2.00) (hidden)
mesh "Cube.001": 36 verts 23 faces colour=#CCCCCC
physics: STATIC mass=1.0

### TopWall  [MESH]  pos=(-0.18, 18.50, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(69.56, 18.73, 2.00) (hidden)
mesh "Cube.002": 44 verts 26 faces colour=#CCCCCC
physics: STATIC mass=1.0

### TopLeftWall  [MESH]  pos=(-34.25, 9.29, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(1.04, 18.07, 2.00) (hidden)
mesh "Cube.003": 8 verts 6 faces colour=#CCCCCC
physics: STATIC mass=1.0

### BottomLeftWall  [MESH]  pos=(-34.33, -10.36, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(1.04, 16.18, 2.00) (hidden)
mesh "Cube.004": 8 verts 6 faces colour=#CCCCCC
physics: STATIC mass=1.0

### TopRightWall  [MESH]  pos=(34.25, 10.17, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(1.04, 17.44, 2.00) (hidden)
mesh "Cube.005": 8 verts 6 faces colour=#CCCCCC
physics: STATIC mass=1.0

### BottomRightWall  [MESH]  pos=(34.17, -10.16, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(1.04, 17.44, 2.00) (hidden)
mesh "Cube.006": 8 verts 6 faces colour=#CCCCCC
physics: STATIC mass=1.0

### Floor  [MESH]  pos=(0.00, 0.00, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(69.52, 37.28, 0.10) (hidden)
mesh "Cube.007": 8 verts 6 faces colour=#CCCCCC
physics: STATIC mass=1.0

### Cube  [MESH]  pos=(0.00, 0.00, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(66.00, 38.00, 6.05) (hidden)
mesh "Cube.035": 1392 verts 1408 faces
physics: STATIC mass=1.0

### Maze  [MESH]  pos=(0.00, 0.00, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(70.13, 38.07, 3.28)
mesh "Plane": 1458 verts 1424 faces colour=#CCCCCC
physics: STATIC mass=1.0
- prop maze (FLOAT) = 0.0

### Floor.001  [MESH]  pos=(0.00, 0.00, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(70.11, 37.28, 0.10) (hidden)
mesh "Cube.008": 8 verts 4 faces colour=#CCCCCC
physics: STATIC mass=1.0

### MazeTops  [MESH]  pos=(0.00, 0.00, 0.10) rot_deg=(0.00, 0.00, 0.00) size=(69.63, 38.07, 1.23)
mesh "Plane.003": 516 verts 365 faces colour=#CCCCCC
physics: STATIC mass=1.0

### NavMeshBASE  [MESH]  pos=(0.00, 0.00, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(70.13, 38.07, 0.10) (hidden)
mesh "Plane.004": 806 verts 50 faces colour=#CCCCCC
physics: STATIC mass=1.0
- prop maze (FLOAT) = 0.0

### Navmesh  [MESH]  pos=(0.00, 0.00, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(68.70, 36.90, 0.00)
mesh "Navmesh.001": 520 verts 616 faces
physics: NAVMESH mass=1.0

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

### TheRabbit  [MESH]  pos=(-36.60, -20.90, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 2.00)
mesh "Cube.010": 8 verts 6 faces
physics: STATIC mass=1.0
- prop x (INT) = 1
- prop y (INT) = 0
- prop direction (STRING) = 
- SENSOR DELAY "Start" -> [And]: use_tap=True, controllers=(bpy.data.objects['TheRabbit']...AndController,)
- SENSOR PROPERTY "Property" -> [And.001]: use_pulse_true_level=True, controllers=(bpy.data.objects['TheRabbit']...AndController,), evaluation_type=PROPEQUAL, property=direction, value=RIGHT, value_min=RIGHT
- SENSOR PROPERTY "X>70" -> [And.002]: controllers=(bpy.data.objects['TheRabbit']...AndController,), evaluation_type=PROPGREATERTHAN, property=x, value=80, value_min=80
- SENSOR PROPERTY "UP" -> [And.003]: use_pulse_true_level=True, controllers=(bpy.data.objects['TheRabbit']...AndController,), evaluation_type=PROPEQUAL, property=direction, value=UP, value_min=UP
- SENSOR PROPERTY "Y>40" -> [And.004]: controllers=(bpy.data.objects['TheRabbit']...AndController,), evaluation_type=PROPGREATERTHAN, property=y, value=42, value_min=42
- SENSOR PROPERTY "LEFT" -> [And.005]: use_pulse_true_level=True, controllers=(bpy.data.objects['TheRabbit']...AndController,), evaluation_type=PROPEQUAL, property=direction, value=LEFT, value_min=LEFT
- SENSOR PROPERTY "X<0" -> [And.006]: controllers=(bpy.data.objects['TheRabbit']...AndController,), evaluation_type=PROPLESSTHAN, property=x, value=0, value_min=0
- SENSOR PROPERTY "DOWN" -> [And.007]: use_pulse_true_level=True, controllers=(bpy.data.objects['TheRabbit']...AndController,), evaluation_type=PROPEQUAL, property=direction, value=DOWN, value_min=DOWN
- SENSOR PROPERTY "Y<0" -> [And.008]: controllers=(bpy.data.objects['TheRabbit']...AndController,), evaluation_type=PROPLESSTHAN, property=y, value=0, value_min=0
- CONTROLLER LOGIC_AND "And" -> [RIGHT_Start]
- CONTROLLER LOGIC_AND "And.001" -> [x+1, addx1]
- CONTROLLER LOGIC_AND "And.002" -> [UP]
- CONTROLLER LOGIC_AND "And.003" -> [addy1, y+1]
- CONTROLLER LOGIC_AND "And.004" -> [LEFT]
- CONTROLLER LOGIC_AND "And.005" -> [subX1, LEFT.001]
- CONTROLLER LOGIC_AND "And.006" -> [DOWN]
- CONTROLLER LOGIC_AND "And.007" -> [suby1, DOWN.001]
- CONTROLLER LOGIC_AND "And.008" -> [Property.001]
- ACTUATOR PROPERTY "RIGHT_Start": mode=ASSIGN, property=direction, value="RIGHT", object_property="RIGHT"
- ACTUATOR MOTION "x+1": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_x=1.0, offset_location=(1.0, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR PROPERTY "addx1": mode=ADD, property=x, value=1, object_property=1
- ACTUATOR PROPERTY "UP": mode=ASSIGN, property=direction, value="UP", object_property="UP"
- ACTUATOR PROPERTY "addy1": mode=ADD, property=y, value=1, object_property=1
- ACTUATOR MOTION "y+1": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_y=1.0, offset_location=(0.0, 1.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR PROPERTY "LEFT": mode=ASSIGN, property=direction, value="LEFT", object_property="LEFT"
- ACTUATOR PROPERTY "subX1": mode=ADD, property=x, value=-1, object_property=-1
- ACTUATOR MOTION "LEFT.001": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_x=-1.0, offset_location=(-1.0, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR PROPERTY "DOWN": mode=ASSIGN, property=direction, value="DOWN", object_property="DOWN"
- ACTUATOR PROPERTY "suby1": mode=ADD, property=y, value=-1, object_property=-1
- ACTUATOR MOTION "DOWN.001": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_y=-1.0, offset_location=(0.0, -1.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR PROPERTY "Property.001": mode=ASSIGN, property=direction, value="RIGHT", object_property="RIGHT"

### 1  [MESH]  pos=(25.96, -3.13, 0.81) rot_deg=(0.00, 0.00, 0.00) size=(0.37, 0.37, 0.37)
mesh "Cube.011": 8 verts 6 faces colour=#CCCCCC
physics: STATIC mass=1.0
- prop Waypoint (INT) = 0
- prop 1 (INT) = 0

### 2  [MESH]  pos=(25.52, 3.69, 0.63) rot_deg=(0.00, 0.00, 0.00) size=(0.37, 0.37, 0.37)
mesh "Cube.026": 8 verts 6 faces colour=#CCCCCC
physics: STATIC mass=1.0
- prop Waypoint (INT) = 0
- prop 2 (INT) = 0

### 3  [MESH]  pos=(21.24, 3.58, 0.63) rot_deg=(0.00, 0.00, 0.00) size=(0.37, 0.37, 0.37)
mesh "Cube.027": 8 verts 6 faces colour=#CCCCCC
physics: STATIC mass=1.0
- prop Waypoint (INT) = 0
- prop 2 (INT) = 0

### 4  [MESH]  pos=(21.24, 10.02, 0.63) rot_deg=(0.00, 0.00, 0.00) size=(0.37, 0.37, 0.37)
mesh "Cube.028": 8 verts 6 faces colour=#CCCCCC
physics: STATIC mass=1.0
- prop Waypoint (INT) = 0
- prop 2 (INT) = 0

### 5  [MESH]  pos=(16.80, 10.19, 0.63) rot_deg=(0.00, 0.00, 0.00) size=(0.37, 0.37, 0.37)
mesh "Cube.029": 8 verts 6 faces colour=#CCCCCC
physics: STATIC mass=1.0
- prop Waypoint (INT) = 0
- prop 2 (INT) = 0

### 6  [MESH]  pos=(15.43, 14.96, 0.63) rot_deg=(0.00, 0.00, 0.00) size=(0.37, 0.37, 0.37)
mesh "Cube.030": 8 verts 6 faces colour=#CCCCCC
physics: STATIC mass=1.0
- prop Waypoint (INT) = 0
- prop 2 (INT) = 0

### 7  [MESH]  pos=(12.08, 10.24, 0.63) rot_deg=(0.00, 0.00, 0.00) size=(0.37, 0.37, 0.37)
mesh "Cube.032": 8 verts 6 faces colour=#CCCCCC
physics: STATIC mass=1.0
- prop Waypoint (INT) = 0
- prop 2 (INT) = 0

### 8  [MESH]  pos=(8.09, 10.47, 0.63) rot_deg=(0.00, 0.00, 0.00) size=(0.37, 0.37, 0.37)
mesh "Cube.033": 8 verts 6 faces colour=#CCCCCC
physics: STATIC mass=1.0
- prop Waypoint (INT) = 0
- prop 2 (INT) = 0

### 9  [MESH]  pos=(7.53, 7.97, 0.63) rot_deg=(0.00, 0.00, 0.00) size=(0.37, 0.37, 0.37)
mesh "Cube.034": 8 verts 6 faces colour=#CCCCCC
physics: STATIC mass=1.0
- prop Waypoint (INT) = 0
- prop 2 (INT) = 0

### 10  [MESH]  pos=(5.59, 7.97, 0.63) rot_deg=(0.00, 0.00, 0.00) size=(0.37, 0.37, 0.37)
mesh "Cube.036": 8 verts 6 faces colour=#CCCCCC
physics: STATIC mass=1.0
- prop Waypoint (INT) = 0
- prop 2 (INT) = 0

### 11  [MESH]  pos=(5.64, 3.30, 0.63) rot_deg=(0.00, 0.00, 0.00) size=(0.37, 0.37, 0.37)
mesh "Cube.039": 8 verts 6 faces colour=#CCCCCC
physics: STATIC mass=1.0
- prop Waypoint (INT) = 0
- prop 2 (INT) = 0

### 12  [MESH]  pos=(3.31, 3.19, 0.63) rot_deg=(0.00, 0.00, 0.00) size=(0.37, 0.37, 0.37)
mesh "Cube.040": 8 verts 6 faces colour=#CCCCCC
physics: STATIC mass=1.0
- prop Waypoint (INT) = 0
- prop 2 (INT) = 0

### 13  [MESH]  pos=(3.03, -3.19, 0.63) rot_deg=(0.00, 0.00, 0.00) size=(0.37, 0.37, 0.37)
mesh "Cube.041": 8 verts 6 faces colour=#CCCCCC
physics: STATIC mass=1.0
- prop Waypoint (INT) = 0
- prop 2 (INT) = 0

### 14  [MESH]  pos=(-3.79, -3.14, 0.63) rot_deg=(0.00, 0.00, 0.00) size=(0.37, 0.37, 0.37)
mesh "Cube.042": 8 verts 6 faces colour=#CCCCCC
physics: STATIC mass=1.0
- prop Waypoint (INT) = 0
- prop 2 (INT) = 0

### 15  [MESH]  pos=(-3.68, 2.97, 0.63) rot_deg=(0.00, 0.00, 0.00) size=(0.37, 0.37, 0.37)
mesh "Cube.043": 8 verts 6 faces colour=#CCCCCC
physics: STATIC mass=1.0
- prop Waypoint (INT) = 0
- prop 2 (INT) = 0

### 16  [MESH]  pos=(-6.13, 3.19, 0.63) rot_deg=(0.00, 0.00, 0.00) size=(0.37, 0.37, 0.37)
mesh "Cube.044": 8 verts 6 faces colour=#CCCCCC
physics: STATIC mass=1.0
- prop Waypoint (INT) = 0
- prop 2 (INT) = 0

### 17  [MESH]  pos=(-6.02, 7.91, 0.63) rot_deg=(0.00, 0.00, 0.00) size=(0.37, 0.37, 0.37)
mesh "Cube.045": 8 verts 6 faces colour=#CCCCCC
physics: STATIC mass=1.0
- prop Waypoint (INT) = 0
- prop 2 (INT) = 0

### 18  [MESH]  pos=(-8.40, 8.08, 0.63) rot_deg=(0.00, 0.00, 0.00) size=(0.37, 0.37, 0.37)
mesh "Cube.046": 8 verts 6 faces colour=#CCCCCC
physics: STATIC mass=1.0
- prop Waypoint (INT) = 0
- prop 2 (INT) = 0

### 19  [MESH]  pos=(-8.51, 10.41, 0.63) rot_deg=(0.00, 0.00, 0.00) size=(0.37, 0.37, 0.37)
mesh "Cube.047": 8 verts 6 faces colour=#CCCCCC
physics: STATIC mass=1.0
- prop Waypoint (INT) = 0
- prop 2 (INT) = 0

### 20  [MESH]  pos=(-12.46, 10.13, 0.63) rot_deg=(0.00, 0.00, 0.00) size=(0.37, 0.37, 0.37)
mesh "Cube.048": 8 verts 6 faces colour=#CCCCCC
physics: STATIC mass=1.0
- prop Waypoint (INT) = 0
- prop 2 (INT) = 0

### 21  [MESH]  pos=(-12.84, 7.86, 0.63) rot_deg=(0.00, 0.00, 0.00) size=(0.37, 0.37, 0.37)
mesh "Cube.049": 8 verts 6 faces colour=#CCCCCC
physics: STATIC mass=1.0
- prop Waypoint (INT) = 0
- prop 2 (INT) = 0

### 22  [MESH]  pos=(-15.06, 7.41, 0.63) rot_deg=(0.00, 0.00, 0.00) size=(0.37, 0.37, 0.37)
mesh "Cube.050": 8 verts 6 faces colour=#CCCCCC
physics: STATIC mass=1.0
- prop Waypoint (INT) = 0
- prop 2 (INT) = 0

### 23  [MESH]  pos=(-14.90, -0.69, 0.63) rot_deg=(0.00, 0.00, 0.00) size=(0.37, 0.37, 0.37)
mesh "Cube.051": 8 verts 6 faces colour=#CCCCCC
physics: STATIC mass=1.0
- prop Waypoint (INT) = 0
- prop 2 (INT) = 0

### 24  [MESH]  pos=(-12.62, -1.08, 0.63) rot_deg=(0.00, 0.00, 0.00) size=(0.37, 0.37, 0.37)
mesh "Cube.052": 8 verts 6 faces colour=#CCCCCC
physics: STATIC mass=1.0
- prop Waypoint (INT) = 0
- prop 2 (INT) = 0

### 25  [MESH]  pos=(-12.57, -7.24, 0.63) rot_deg=(0.00, 0.00, 0.00) size=(0.37, 0.37, 0.37)
mesh "Cube.053": 8 verts 6 faces colour=#CCCCCC
physics: STATIC mass=1.0
- prop Waypoint (INT) = 0
- prop 2 (INT) = 0

### 26  [MESH]  pos=(-10.57, -7.69, 0.63) rot_deg=(0.00, 0.00, 0.00) size=(0.37, 0.37, 0.37)
mesh "Cube.054": 8 verts 6 faces colour=#CCCCCC
physics: STATIC mass=1.0
- prop Waypoint (INT) = 0
- prop 2 (INT) = 0

### 27  [MESH]  pos=(-10.12, -17.02, 0.63) rot_deg=(0.00, 0.00, 0.00) size=(0.37, 0.37, 0.37)
mesh "Cube.055": 8 verts 6 faces colour=#CCCCCC
physics: STATIC mass=1.0
- prop Waypoint (INT) = 0
- prop 2 (INT) = 0

### 28  [MESH]  pos=(21.08, -16.96, 0.63) rot_deg=(0.00, 0.00, 0.00) size=(0.37, 0.37, 0.37)
mesh "Cube.056": 8 verts 6 faces colour=#CCCCCC
physics: STATIC mass=1.0
- prop Waypoint (INT) = 0
- prop 2 (INT) = 0

### 29  [MESH]  pos=(21.52, -14.30, 0.63) rot_deg=(0.00, 0.00, 0.00) size=(0.37, 0.37, 0.37)
mesh "Cube.057": 8 verts 6 faces colour=#CCCCCC
physics: STATIC mass=1.0
- prop Waypoint (INT) = 0
- prop 2 (INT) = 0

### 30  [MESH]  pos=(25.24, -14.35, 0.63) rot_deg=(0.00, 0.00, 0.00) size=(0.37, 0.37, 0.37)
mesh "Cube.058": 8 verts 6 faces colour=#CCCCCC
physics: STATIC mass=1.0
- prop Waypoint (INT) = 0
- prop 2 (INT) = 0

### 31  [MESH]  pos=(26.02, -17.13, 0.63) rot_deg=(0.00, 0.00, 0.00) size=(0.37, 0.37, 0.37)
mesh "Cube.059": 8 verts 6 faces colour=#CCCCCC
physics: STATIC mass=1.0
- prop Waypoint (INT) = 0
- prop 2 (INT) = 0

### 32  [MESH]  pos=(32.62, -17.13, 0.63) rot_deg=(0.00, 0.00, 0.00) size=(0.37, 0.37, 0.37)
mesh "Cube.060": 8 verts 6 faces colour=#CCCCCC
physics: STATIC mass=1.0
- prop Waypoint (INT) = 0
- prop 2 (INT) = 0

### 33  [MESH]  pos=(32.46, -8.02, 0.63) rot_deg=(0.00, 0.00, 0.00) size=(0.37, 0.37, 0.37)
mesh "Cube.061": 8 verts 6 faces colour=#CCCCCC
physics: STATIC mass=1.0
- prop Waypoint (INT) = 0
- prop 2 (INT) = 0

### 34  [MESH]  pos=(32.96, -4.91, 0.63) rot_deg=(0.00, 0.00, 0.00) size=(0.37, 0.37, 0.37)
mesh "Cube.062": 8 verts 6 faces colour=#CCCCCC
physics: STATIC mass=1.0
- prop Waypoint (INT) = 0
- prop 2 (INT) = 0

### Enemy  [MESH]  pos=(32.39, -3.06, 0.81) rot_deg=(0.00, 0.00, 0.00) size=(1.55, 1.55, 1.55)
mesh "Cube": 8 verts 6 faces colour=#CCCCCC
physics: DYNAMIC mass=1.0
- prop Enemy (BOOL) = False
- prop Waypoint (INT) = 1
- SENSOR ALWAYS "1" -> [1]: use_pulse_true_level=True, controllers=(bpy.data.objects['Enemy']...AndController,)
- SENSOR COLLISION "Waypoint" -> [Python]: controllers=(bpy.data.objects['Enemy']...PythonController,), property=Waypoint
- SENSOR PROPERTY "0" -> [Python]: controllers=(bpy.data.objects['Enemy']...PythonController,), evaluation_type=PROPGREATERTHAN, property=Waypoint, value=0, value_min=0
- CONTROLLER LOGIC_AND "1" -> [TargetWaypoint]
- CONTROLLER PYTHON "Python" script=waypoints.py -> []
- ACTUATOR STEERING "TargetWaypoint": mode=SEEK, velocity=10.0, acceleration=3.0, turn_speed=720.0, distance=1.0, navmesh=obj:Navmesh, facing=True, facing_axis=X, lock_z_velocity=True

### Enemy.001  [MESH]  pos=(-8.22, 17.20, 0.81) rot_deg=(0.00, 0.00, 0.00) size=(1.55, 1.55, 1.55)
mesh "Cube.063": 8 verts 6 faces colour=#CCCCCC
physics: DYNAMIC mass=1.0
- prop Enemy (BOOL) = False
- prop Waypoint (INT) = 19
- SENSOR ALWAYS "1" -> [1]: use_pulse_true_level=True, controllers=(bpy.data.objects['Enemy.001']...AndController,)
- SENSOR COLLISION "Waypoint" -> [Python]: controllers=(bpy.data.objects['Enemy.001']...PythonController,), property=Waypoint
- SENSOR PROPERTY "0" -> [Python]: controllers=(bpy.data.objects['Enemy.001']...PythonController,), evaluation_type=PROPGREATERTHAN, property=Waypoint, value=0, value_min=0
- CONTROLLER LOGIC_AND "1" -> [TargetWaypoint]
- CONTROLLER PYTHON "Python" script=waypoints.py -> []
- ACTUATOR STEERING "TargetWaypoint": mode=SEEK, velocity=10.0, acceleration=3.0, turn_speed=720.0, distance=1.0, navmesh=obj:Navmesh, facing=True, facing_axis=X, lock_z_velocity=True

### Enemy.002  [MESH]  pos=(-28.71, -1.00, 0.81) rot_deg=(0.00, 0.00, 0.00) size=(1.55, 1.55, 1.55)
mesh "Cube.064": 8 verts 6 faces colour=#CCCCCC
physics: DYNAMIC mass=1.0
- prop Enemy (BOOL) = False
- prop Waypoint (INT) = 23
- SENSOR ALWAYS "1" -> [1]: use_pulse_true_level=True, controllers=(bpy.data.objects['Enemy.002']...AndController,)
- SENSOR COLLISION "Waypoint" -> [Python]: controllers=(bpy.data.objects['Enemy.002']...PythonController,), property=Waypoint
- SENSOR PROPERTY "0" -> [Python]: controllers=(bpy.data.objects['Enemy.002']...PythonController,), evaluation_type=PROPGREATERTHAN, property=Waypoint, value=0, value_min=0
- CONTROLLER LOGIC_AND "1" -> [TargetWaypoint]
- CONTROLLER PYTHON "Python" script=waypoints.py -> []
- ACTUATOR STEERING "TargetWaypoint": mode=SEEK, velocity=10.0, acceleration=3.0, turn_speed=720.0, distance=1.0, navmesh=obj:Navmesh, facing=True, facing_axis=X, lock_z_velocity=True

## text blocks
### Text  (8 lines)
```
W A S D keys to move player
Enemies travel around the map using (green) waypoints
They dont sense or bother the player 

Keeping things simple here

See scripts waypoint.py and Warp_L_R.py 
for fancy functionality
```
### Warp_L_R.py  (24 lines)
```
import bge

## Warp the player from one side of map to next at exits

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
### waypoints.py  (29 lines)
```
import bge

scene = bge.logic.getCurrentScene()
cont = bge.logic.getCurrentController()
own  = cont.owner


curWaypoint = own['Waypoint']
seek = own.actuators['TargetWaypoint'] 

## detect collision with waypoint set next waypoint
hitObj = own.sensors['Waypoint'].hitObject

if hitObj is not None:
   ## convert number name to integer
    hitNum = int(hitObj.name) 
    hitNum += 1
    own['Waypoint'] = hitNum
    #convert integer back to string
    targetName = str(hitNum)

if own['Waypoint'] > 34:
    own['Waypoint'] = 1
  
## set controller owner seek actuator target to waypoint    
targetName =  str(own['Waypoint'])
varTarget =  scene.objects[targetName]
seek.target = str(varTarget)

```