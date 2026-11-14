# Dodge_Tunnel.blend

## scene "Scene"  camera=Camera
game: fps=60 physics=BULLET gravity=0.0

### Player  [MESH]  pos=(0.00, 0.00, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 2.00)
mesh "Cube": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=2.0
- SENSOR KEYBOARD "UP" -> [And]: controllers=(bpy.data.objects['Player']...AndController,), key=W, modifier_key_1=NONE, modifier_key_2=NONE
- SENSOR KEYBOARD "DOWN" -> [And.001]: controllers=(bpy.data.objects['Player']...AndController,), key=S, modifier_key_1=NONE, modifier_key_2=NONE
- SENSOR KEYBOARD "LEFT" -> [And.002]: controllers=(bpy.data.objects['Player']...AndController,), key=A, modifier_key_1=NONE, modifier_key_2=NONE
- SENSOR KEYBOARD "RIGHT" -> [And.003]: controllers=(bpy.data.objects['Player']...AndController,), key=D, modifier_key_1=NONE, modifier_key_2=NONE
- CONTROLLER LOGIC_AND "And" -> [UP]
- CONTROLLER LOGIC_AND "And.001" -> [DOWn]
- CONTROLLER LOGIC_AND "And.002" -> [LEFT]
- CONTROLLER LOGIC_AND "And.003" -> [RIGHT]
- ACTUATOR MOTION "UP": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, offset_location=(0.0, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.3, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_local_linear_velocity=True, use_add_linear_velocity=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "DOWn": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, offset_location=(0.0, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, -0.3, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_local_linear_velocity=True, use_add_linear_velocity=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "LEFT": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, offset_location=(0.0, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(-0.3, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_local_linear_velocity=True, use_add_linear_velocity=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "RIGHT": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, offset_location=(0.0, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.3, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_local_linear_velocity=True, use_add_linear_velocity=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True

### Light  [LIGHT]  pos=(4.08, 1.01, 5.90) rot_deg=(37.26, 3.16, 106.94) size=(0.00, 0.00, 0.00)
physics: STATIC mass=1.0

### Camera  [CAMERA]  pos=(0.00, 0.00, 5.41) rot_deg=(0.00, 0.00, 0.00) size=(0.00, 0.00, 0.00)
camera: lens=7.0 type=PERSP ortho_scale=34.01
physics: STATIC mass=1.0

### CLIP  [MESH]  pos=(0.00, 0.00, 2.09) rot_deg=(0.00, 0.00, 0.00) size=(20.47, 14.70, 0.00)
mesh "Plane.004": 4 verts 1 faces colour=#CCCCCC
physics: STATIC mass=1.0
- prop CLIP (STRING) = CLIP

### BottomWall  [MESH]  pos=(0.00, -6.90, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(20.50, 0.30, 2.00)
mesh "Cube.005": 8 verts 6 faces
physics: STATIC mass=1.0
- prop wall (BOOL) = False

### LeftWall  [MESH]  pos=(-10.16, 0.00, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(0.29, 13.02, 2.00)
mesh "Cube.002": 8 verts 6 faces
physics: STATIC mass=1.0
- prop wall (BOOL) = False

### RightWall  [MESH]  pos=(10.09, 0.00, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(0.29, 13.02, 2.00)
mesh "Cube.003": 8 verts 6 faces
physics: STATIC mass=1.0
- prop wall (FLOAT) = 0.0

### TopWall  [MESH]  pos=(0.00, 6.78, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(20.50, 0.30, 2.00)
mesh "Cube.004": 8 verts 6 faces
physics: STATIC mass=1.0
- prop wall (BOOL) = False

### CubeObstacle  [MESH]  pos=(0.00, 0.00, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 2.00) (hidden)
mesh "Cube.001": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- SENSOR DELAY "END" -> [END]: controllers=(bpy.data.objects['CubeObstacle']...OrController,), delay=300
- SENSOR COLLISION "CLIP" -> [END]: controllers=(bpy.data.objects['CubeObstacle']...OrController,), property=CLIP
- SENSOR COLLISION "Collision" -> [END]: controllers=(bpy.data.objects['CubeObstacle']...OrController,), property=wall
- SENSOR ALWAYS "MOVE" -> [MOVE]: controllers=(bpy.data.objects['CubeObstacle']...AndController,)
- CONTROLLER LOGIC_OR "END" -> [END]
- CONTROLLER LOGIC_AND "MOVE" -> [MOVE]
- ACTUATOR EDIT_OBJECT "END": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True
- ACTUATOR MOTION "MOVE": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_z=0.1, offset_location=(0.0, 0.0, 0.1), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True

### Spawner1  [MESH]  pos=(-11.26, 8.85, -20.00) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane": 4 verts 1 faces
physics: STATIC mass=1.0
- prop DirX (INT) = 1
- prop DirY (INT) = 0
- prop Reverse (BOOL) = False
- prop Y (INT) = 1
- prop Spawn (BOOL) = False
- SENSOR PROPERTY "Right" -> [Right, Xminus]: controllers=(bpy.data.objects['Spawner1']...AndController, bpy.data.objects['Spawner1']...AndController), evaluation_type=PROPEQUAL, property=DirX, value=1, value_min=1
- SENSOR PROPERTY "Left" -> [Left, xPlus]: controllers=(bpy.data.objects['Spawner1']...AndController, bpy.data.objects['Spawner1']...AndController), evaluation_type=PROPEQUAL, property=DirX, value=-1, value_min=-1
- SENSOR PROPERTY "Up" -> [Up, LifftStop]: controllers=(bpy.data.objects['Spawner1']...AndController, bpy.data.objects['Spawner1']...AndController), evaluation_type=PROPEQUAL, property=DirY, value=1, value_min=1
- SENSOR PROPERTY "Down" -> [Down, DropStop]: controllers=(bpy.data.objects['Spawner1']...AndController, bpy.data.objects['Spawner1']...AndController), evaluation_type=PROPEQUAL, property=DirY, value=-1, value_min=-1
- SENSOR DELAY "HDELAY" -> [Drop, Xminus, xPlus, Lift]: controllers=(bpy.data.objects['Spawner1']...AndController, bpy.data.objects['Spawner1']...AndController, bpy.data.objects['Spawner1']...AndController, bpy.data.objects['Spawner1']...AndController), delay=60, duration=1, use_repeat=True
- SENSOR DELAY "VDELAY" -> [DropStop, LifftStop]: controllers=(bpy.data.objects['Spawner1']...AndController, bpy.data.objects['Spawner1']...AndController), delay=1, use_repeat=True
- SENSOR PROPERTY "DirY0" -> [Drop, Lift]: controllers=(bpy.data.objects['Spawner1']...AndController, bpy.data.objects['Spawner1']...AndController), evaluation_type=PROPEQUAL, property=DirY, value=0, value_min=0
- SENSOR PROPERTY "ReverseF" -> [Drop]: controllers=(bpy.data.objects['Spawner1']...AndController,), evaluation_type=PROPEQUAL, property=Reverse, value=FALSE, value_min=FALSE
- SENSOR PROPERTY "ReverseT" -> [Lift, LifftStop]: controllers=(bpy.data.objects['Spawner1']...AndController, bpy.data.objects['Spawner1']...AndController), evaluation_type=PROPEQUAL, property=Reverse, value=TRUE, value_min=TRUE
- SENSOR PROPERTY "Y1" -> [And]: controllers=(bpy.data.objects['Spawner1']...OrController,), evaluation_type=PROPLESSTHAN, property=Y, value=1, value_min=1
- SENSOR PROPERTY "Y22" -> [And]: controllers=(bpy.data.objects['Spawner1']...OrController,), evaluation_type=PROPGREATERTHAN, property=Y, value=30, value_min=30
- SENSOR DELAY "SpawnDelay" -> [RND]: controllers=(bpy.data.objects['Spawner1']...AndController,), delay=5, use_repeat=True
- SENSOR PROPERTY "SPAWNT" -> [SPAWN]: controllers=(bpy.data.objects['Spawner1']...AndController,), evaluation_type=PROPEQUAL, property=Spawn, value=TRUE, value_min=TRUE
- CONTROLLER LOGIC_AND "Right" -> [Right]
- CONTROLLER LOGIC_AND "Left" -> [Left]
- CONTROLLER LOGIC_AND "Up" -> [Up]
- CONTROLLER LOGIC_AND "Down" -> [Down]
- CONTROLLER LOGIC_AND "Xminus" -> [xMinus]
- CONTROLLER LOGIC_AND "xPlus" -> [xPlus]
- CONTROLLER LOGIC_AND "Drop" -> [DROP, YPlus]
- CONTROLLER LOGIC_AND "DropStop" -> [DropStop]
- CONTROLLER LOGIC_AND "Lift" -> [LIFT, YMinus]
- CONTROLLER LOGIC_AND "LifftStop" -> [DropStop]
- CONTROLLER LOGIC_OR "And" -> [REVERSE]
- CONTROLLER LOGIC_AND "RND" -> [SpawnRND]
- CONTROLLER LOGIC_AND "SPAWN" -> [SPAWN]
- ACTUATOR MOTION "Right": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_x=0.5, offset_location=(0.5, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "Left": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_x=-0.5, offset_location=(-0.5, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "Up": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_y=0.5, offset_location=(0.0, 0.5, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "Down": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_y=-0.5, offset_location=(0.0, -0.5, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR PROPERTY "xMinus": mode=ASSIGN, property=DirX, value=-1, object_property=-1
- ACTUATOR PROPERTY "xPlus": mode=ASSIGN, property=DirX, value=1, object_property=1
- ACTUATOR PROPERTY "DROP": mode=ASSIGN, property=DirY, value=-1, object_property=-1
- ACTUATOR PROPERTY "YPlus": mode=ADD, property=Y, value=1, object_property=1
- ACTUATOR PROPERTY "LIFT": mode=ASSIGN, property=DirY, value=1, object_property=1
- ACTUATOR PROPERTY "YMinus": mode=ADD, property=Y, value=-1, object_property=-1
- ACTUATOR PROPERTY "DropStop": mode=ASSIGN, property=DirY, value=0, object_property=0
- ACTUATOR PROPERTY "REVERSE": mode=TOGGLE, property=Reverse
- ACTUATOR RANDOM "SpawnRND": seed=6347, property=Spawn, distribution=BOOL_UNIFORM, chance=0.1, int_mean=0.1, float_value=0.1, float_min=0.1, float_mean=0.1, half_life_time=0.1
- ACTUATOR EDIT_OBJECT "SPAWN": mode=ADDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, object=obj:CubeObstacle, track_object=obj:CubeObstacle, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### Spawner1b  [MESH]  pos=(-11.28, -2.02, -20.00) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.002": 4 verts 1 faces
physics: STATIC mass=1.0
- prop DirX (INT) = 1
- prop DirY (INT) = 0
- prop Reverse (BOOL) = False
- prop Y (INT) = 16
- prop Spawn (BOOL) = False
- SENSOR PROPERTY "Right" -> [Right, Xminus]: controllers=(bpy.data.objects['Spawner1b']...AndController, bpy.data.objects['Spawner1b']...AndController), evaluation_type=PROPEQUAL, property=DirX, value=1, value_min=1
- SENSOR PROPERTY "Left" -> [Left, xPlus]: controllers=(bpy.data.objects['Spawner1b']...AndController, bpy.data.objects['Spawner1b']...AndController), evaluation_type=PROPEQUAL, property=DirX, value=-1, value_min=-1
- SENSOR PROPERTY "Up" -> [Up, LifftStop]: controllers=(bpy.data.objects['Spawner1b']...AndController, bpy.data.objects['Spawner1b']...AndController), evaluation_type=PROPEQUAL, property=DirY, value=1, value_min=1
- SENSOR PROPERTY "Down" -> [Down, DropStop]: controllers=(bpy.data.objects['Spawner1b']...AndController, bpy.data.objects['Spawner1b']...AndController), evaluation_type=PROPEQUAL, property=DirY, value=-1, value_min=-1
- SENSOR DELAY "HDELAY" -> [Drop, Xminus, xPlus, Lift]: controllers=(bpy.data.objects['Spawner1b']...AndController, bpy.data.objects['Spawner1b']...AndController, bpy.data.objects['Spawner1b']...AndController, bpy.data.objects['Spawner1b']...AndController), delay=60, duration=1, use_repeat=True
- SENSOR DELAY "VDELAY" -> [DropStop, LifftStop]: controllers=(bpy.data.objects['Spawner1b']...AndController, bpy.data.objects['Spawner1b']...AndController), delay=1, use_repeat=True
- SENSOR PROPERTY "DirY0" -> [Drop, Lift]: controllers=(bpy.data.objects['Spawner1b']...AndController, bpy.data.objects['Spawner1b']...AndController), evaluation_type=PROPEQUAL, property=DirY, value=0, value_min=0
- SENSOR PROPERTY "ReverseF" -> [Drop]: controllers=(bpy.data.objects['Spawner1b']...AndController,), evaluation_type=PROPEQUAL, property=Reverse, value=FALSE, value_min=FALSE
- SENSOR PROPERTY "ReverseT" -> [Lift, LifftStop]: controllers=(bpy.data.objects['Spawner1b']...AndController, bpy.data.objects['Spawner1b']...AndController), evaluation_type=PROPEQUAL, property=Reverse, value=TRUE, value_min=TRUE
- SENSOR PROPERTY "Y1" -> [And]: controllers=(bpy.data.objects['Spawner1b']...OrController,), evaluation_type=PROPLESSTHAN, property=Y, value=1, value_min=1
- SENSOR PROPERTY "Y22" -> [And]: controllers=(bpy.data.objects['Spawner1b']...OrController,), evaluation_type=PROPGREATERTHAN, property=Y, value=30, value_min=30
- SENSOR DELAY "SpawnDelay" -> [RND]: controllers=(bpy.data.objects['Spawner1b']...AndController,), delay=5, use_repeat=True
- SENSOR PROPERTY "SPAWNT" -> [SPAWN]: controllers=(bpy.data.objects['Spawner1b']...AndController,), evaluation_type=PROPEQUAL, property=Spawn, value=TRUE, value_min=TRUE
- CONTROLLER LOGIC_AND "Right" -> [Right]
- CONTROLLER LOGIC_AND "Left" -> [Left]
- CONTROLLER LOGIC_AND "Up" -> [Up]
- CONTROLLER LOGIC_AND "Down" -> [Down]
- CONTROLLER LOGIC_AND "Xminus" -> [xMinus]
- CONTROLLER LOGIC_AND "xPlus" -> [xPlus]
- CONTROLLER LOGIC_AND "Drop" -> [DROP, YPlus]
- CONTROLLER LOGIC_AND "DropStop" -> [DropStop]
- CONTROLLER LOGIC_AND "Lift" -> [LIFT, YMinus]
- CONTROLLER LOGIC_AND "LifftStop" -> [DropStop]
- CONTROLLER LOGIC_OR "And" -> [REVERSE]
- CONTROLLER LOGIC_AND "RND" -> [SpawnRND]
- CONTROLLER LOGIC_AND "SPAWN" -> [SPAWN]
- ACTUATOR MOTION "Right": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_x=0.5, offset_location=(0.5, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "Left": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_x=-0.5, offset_location=(-0.5, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "Up": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_y=0.5, offset_location=(0.0, 0.5, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "Down": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_y=-0.5, offset_location=(0.0, -0.5, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR PROPERTY "xMinus": mode=ASSIGN, property=DirX, value=-1, object_property=-1
- ACTUATOR PROPERTY "xPlus": mode=ASSIGN, property=DirX, value=1, object_property=1
- ACTUATOR PROPERTY "DROP": mode=ASSIGN, property=DirY, value=-1, object_property=-1
- ACTUATOR PROPERTY "YPlus": mode=ADD, property=Y, value=1, object_property=1
- ACTUATOR PROPERTY "LIFT": mode=ASSIGN, property=DirY, value=1, object_property=1
- ACTUATOR PROPERTY "YMinus": mode=ADD, property=Y, value=-1, object_property=-1
- ACTUATOR PROPERTY "DropStop": mode=ASSIGN, property=DirY, value=0, object_property=0
- ACTUATOR PROPERTY "REVERSE": mode=TOGGLE, property=Reverse
- ACTUATOR RANDOM "SpawnRND": seed=7022, property=Spawn, distribution=BOOL_UNIFORM, chance=0.1, int_mean=0.1, float_value=0.1, float_min=0.1, float_mean=0.1, half_life_time=0.1
- ACTUATOR EDIT_OBJECT "SPAWN": mode=ADDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, object=obj:CubeObstacle, track_object=obj:CubeObstacle, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### Spawner2  [MESH]  pos=(11.16, -8.95, -20.00) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.001": 4 verts 1 faces
physics: STATIC mass=1.0
- prop DirX (INT) = -1
- prop DirY (INT) = 0
- prop Reverse (BOOL) = False
- prop Y (INT) = 30
- prop Spawn (BOOL) = False
- SENSOR PROPERTY "Right" -> [Right, Xminus]: controllers=(bpy.data.objects['Spawner2']...AndController, bpy.data.objects['Spawner2']...AndController), evaluation_type=PROPEQUAL, property=DirX, value=1, value_min=1
- SENSOR PROPERTY "Left" -> [Left, xPlus]: controllers=(bpy.data.objects['Spawner2']...AndController, bpy.data.objects['Spawner2']...AndController), evaluation_type=PROPEQUAL, property=DirX, value=-1, value_min=-1
- SENSOR PROPERTY "Up" -> [Up, LifftStop]: controllers=(bpy.data.objects['Spawner2']...AndController, bpy.data.objects['Spawner2']...AndController), evaluation_type=PROPEQUAL, property=DirY, value=1, value_min=1
- SENSOR PROPERTY "Down" -> [Down, DropStop]: controllers=(bpy.data.objects['Spawner2']...AndController, bpy.data.objects['Spawner2']...AndController), evaluation_type=PROPEQUAL, property=DirY, value=-1, value_min=-1
- SENSOR DELAY "HDELAY" -> [Drop, Xminus, xPlus, Lift]: controllers=(bpy.data.objects['Spawner2']...AndController, bpy.data.objects['Spawner2']...AndController, bpy.data.objects['Spawner2']...AndController, bpy.data.objects['Spawner2']...AndController), delay=60, duration=1, use_repeat=True
- SENSOR DELAY "VDELAY" -> [DropStop, LifftStop]: controllers=(bpy.data.objects['Spawner2']...AndController, bpy.data.objects['Spawner2']...AndController), delay=1, use_repeat=True
- SENSOR PROPERTY "DirY0" -> [Drop, Lift]: controllers=(bpy.data.objects['Spawner2']...AndController, bpy.data.objects['Spawner2']...AndController), evaluation_type=PROPEQUAL, property=DirY, value=0, value_min=0
- SENSOR PROPERTY "ReverseF" -> [Drop]: controllers=(bpy.data.objects['Spawner2']...AndController,), evaluation_type=PROPEQUAL, property=Reverse, value=FALSE, value_min=FALSE
- SENSOR PROPERTY "ReverseT" -> [Lift, LifftStop]: controllers=(bpy.data.objects['Spawner2']...AndController, bpy.data.objects['Spawner2']...AndController), evaluation_type=PROPEQUAL, property=Reverse, value=TRUE, value_min=TRUE
- SENSOR PROPERTY "Y1" -> [And]: controllers=(bpy.data.objects['Spawner2']...OrController,), evaluation_type=PROPLESSTHAN, property=Y, value=1, value_min=1
- SENSOR PROPERTY "Y22" -> [And]: controllers=(bpy.data.objects['Spawner2']...OrController,), evaluation_type=PROPGREATERTHAN, property=Y, value=30, value_min=30
- SENSOR DELAY "SpawnDelay" -> [RND]: controllers=(bpy.data.objects['Spawner2']...AndController,), delay=5, use_repeat=True
- SENSOR PROPERTY "SPAWNT" -> [SPAWN]: controllers=(bpy.data.objects['Spawner2']...AndController,), evaluation_type=PROPEQUAL, property=Spawn, value=TRUE, value_min=TRUE
- CONTROLLER LOGIC_AND "Right" -> [Right]
- CONTROLLER LOGIC_AND "Left" -> [Left]
- CONTROLLER LOGIC_AND "Up" -> [Up]
- CONTROLLER LOGIC_AND "Down" -> [Down]
- CONTROLLER LOGIC_AND "Xminus" -> [xMinus]
- CONTROLLER LOGIC_AND "xPlus" -> [xPlus]
- CONTROLLER LOGIC_AND "Drop" -> [DROP, YPlus]
- CONTROLLER LOGIC_AND "DropStop" -> [DropStop]
- CONTROLLER LOGIC_AND "Lift" -> [LIFT, YMinus]
- CONTROLLER LOGIC_AND "LifftStop" -> [DropStop]
- CONTROLLER LOGIC_OR "And" -> [REVERSE]
- CONTROLLER LOGIC_AND "RND" -> [SpawnRND]
- CONTROLLER LOGIC_AND "SPAWN" -> [SPAWN]
- ACTUATOR MOTION "Right": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_x=0.5, offset_location=(0.5, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "Left": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_x=-0.5, offset_location=(-0.5, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "Up": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_y=0.5, offset_location=(0.0, 0.5, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "Down": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_y=-0.5, offset_location=(0.0, -0.5, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR PROPERTY "xMinus": mode=ASSIGN, property=DirX, value=-1, object_property=-1
- ACTUATOR PROPERTY "xPlus": mode=ASSIGN, property=DirX, value=1, object_property=1
- ACTUATOR PROPERTY "DROP": mode=ASSIGN, property=DirY, value=-1, object_property=-1
- ACTUATOR PROPERTY "YPlus": mode=ADD, property=Y, value=1, object_property=1
- ACTUATOR PROPERTY "LIFT": mode=ASSIGN, property=DirY, value=1, object_property=1
- ACTUATOR PROPERTY "YMinus": mode=ADD, property=Y, value=-1, object_property=-1
- ACTUATOR PROPERTY "DropStop": mode=ASSIGN, property=DirY, value=0, object_property=0
- ACTUATOR PROPERTY "REVERSE": mode=TOGGLE, property=Reverse
- ACTUATOR RANDOM "SpawnRND": seed=9757, property=Spawn, distribution=BOOL_UNIFORM, chance=0.1, int_mean=0.1, float_value=0.1, float_min=0.1, float_mean=0.1, half_life_time=0.1
- ACTUATOR EDIT_OBJECT "SPAWN": mode=ADDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, object=obj:CubeObstacle, track_object=obj:CubeObstacle, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### Spawner2b  [MESH]  pos=(11.18, 1.99, -20.00) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.003": 4 verts 1 faces
physics: STATIC mass=1.0
- prop DirX (INT) = -1
- prop DirY (INT) = 0
- prop Reverse (BOOL) = False
- prop Y (INT) = 14
- prop Spawn (BOOL) = False
- SENSOR PROPERTY "Right" -> [Right, Xminus]: controllers=(bpy.data.objects['Spawner2b']...AndController, bpy.data.objects['Spawner2b']...AndController), evaluation_type=PROPEQUAL, property=DirX, value=1, value_min=1
- SENSOR PROPERTY "Left" -> [Left, xPlus]: controllers=(bpy.data.objects['Spawner2b']...AndController, bpy.data.objects['Spawner2b']...AndController), evaluation_type=PROPEQUAL, property=DirX, value=-1, value_min=-1
- SENSOR PROPERTY "Up" -> [Up, LifftStop]: controllers=(bpy.data.objects['Spawner2b']...AndController, bpy.data.objects['Spawner2b']...AndController), evaluation_type=PROPEQUAL, property=DirY, value=1, value_min=1
- SENSOR PROPERTY "Down" -> [Down, DropStop]: controllers=(bpy.data.objects['Spawner2b']...AndController, bpy.data.objects['Spawner2b']...AndController), evaluation_type=PROPEQUAL, property=DirY, value=-1, value_min=-1
- SENSOR DELAY "HDELAY" -> [Drop, Xminus, xPlus, Lift]: controllers=(bpy.data.objects['Spawner2b']...AndController, bpy.data.objects['Spawner2b']...AndController, bpy.data.objects['Spawner2b']...AndController, bpy.data.objects['Spawner2b']...AndController), delay=60, duration=1, use_repeat=True
- SENSOR DELAY "VDELAY" -> [DropStop, LifftStop]: controllers=(bpy.data.objects['Spawner2b']...AndController, bpy.data.objects['Spawner2b']...AndController), delay=1, use_repeat=True
- SENSOR PROPERTY "DirY0" -> [Drop, Lift]: controllers=(bpy.data.objects['Spawner2b']...AndController, bpy.data.objects['Spawner2b']...AndController), evaluation_type=PROPEQUAL, property=DirY, value=0, value_min=0
- SENSOR PROPERTY "ReverseF" -> [Drop]: controllers=(bpy.data.objects['Spawner2b']...AndController,), evaluation_type=PROPEQUAL, property=Reverse, value=FALSE, value_min=FALSE
- SENSOR PROPERTY "ReverseT" -> [Lift, LifftStop]: controllers=(bpy.data.objects['Spawner2b']...AndController, bpy.data.objects['Spawner2b']...AndController), evaluation_type=PROPEQUAL, property=Reverse, value=TRUE, value_min=TRUE
- SENSOR PROPERTY "Y1" -> [And]: controllers=(bpy.data.objects['Spawner2b']...OrController,), evaluation_type=PROPLESSTHAN, property=Y, value=1, value_min=1
- SENSOR PROPERTY "Y22" -> [And]: controllers=(bpy.data.objects['Spawner2b']...OrController,), evaluation_type=PROPGREATERTHAN, property=Y, value=30, value_min=30
- SENSOR DELAY "SpawnDelay" -> [RND]: controllers=(bpy.data.objects['Spawner2b']...AndController,), delay=5, use_repeat=True
- SENSOR PROPERTY "SPAWNT" -> [SPAWN]: controllers=(bpy.data.objects['Spawner2b']...AndController,), evaluation_type=PROPEQUAL, property=Spawn, value=TRUE, value_min=TRUE
- CONTROLLER LOGIC_AND "Right" -> [Right]
- CONTROLLER LOGIC_AND "Left" -> [Left]
- CONTROLLER LOGIC_AND "Up" -> [Up]
- CONTROLLER LOGIC_AND "Down" -> [Down]
- CONTROLLER LOGIC_AND "Xminus" -> [xMinus]
- CONTROLLER LOGIC_AND "xPlus" -> [xPlus]
- CONTROLLER LOGIC_AND "Drop" -> [DROP, YPlus]
- CONTROLLER LOGIC_AND "DropStop" -> [DropStop]
- CONTROLLER LOGIC_AND "Lift" -> [LIFT, YMinus]
- CONTROLLER LOGIC_AND "LifftStop" -> [DropStop]
- CONTROLLER LOGIC_OR "And" -> [REVERSE]
- CONTROLLER LOGIC_AND "RND" -> [SpawnRND]
- CONTROLLER LOGIC_AND "SPAWN" -> [SPAWN]
- ACTUATOR MOTION "Right": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_x=0.5, offset_location=(0.5, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "Left": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_x=-0.5, offset_location=(-0.5, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "Up": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_y=0.5, offset_location=(0.0, 0.5, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "Down": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_y=-0.5, offset_location=(0.0, -0.5, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR PROPERTY "xMinus": mode=ASSIGN, property=DirX, value=-1, object_property=-1
- ACTUATOR PROPERTY "xPlus": mode=ASSIGN, property=DirX, value=1, object_property=1
- ACTUATOR PROPERTY "DROP": mode=ASSIGN, property=DirY, value=-1, object_property=-1
- ACTUATOR PROPERTY "YPlus": mode=ADD, property=Y, value=1, object_property=1
- ACTUATOR PROPERTY "LIFT": mode=ASSIGN, property=DirY, value=1, object_property=1
- ACTUATOR PROPERTY "YMinus": mode=ADD, property=Y, value=-1, object_property=-1
- ACTUATOR PROPERTY "DropStop": mode=ASSIGN, property=DirY, value=0, object_property=0
- ACTUATOR PROPERTY "REVERSE": mode=TOGGLE, property=Reverse
- ACTUATOR RANDOM "SpawnRND": seed=8313, property=Spawn, distribution=BOOL_UNIFORM, chance=0.1, int_mean=0.1, float_value=0.1, float_min=0.1, float_mean=0.1, half_life_time=0.1
- ACTUATOR EDIT_OBJECT "SPAWN": mode=ADDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, object=obj:CubeObstacle, track_object=obj:CubeObstacle, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

## text blocks
### Text  (9 lines)
```
W A S D to move

P key to start game

The complexity of the logic bricks
on the spawners is in keeping the moving
Porbably could have been done with
more spawners and no motion?

```