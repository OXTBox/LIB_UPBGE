# Rotation_Shooter.blend

## scene "Scene"  camera=Camera
game: fps=60 physics=BULLET gravity=0.0

### Cubeeroid  [MESH]  pos=(-12.20, 0.00, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(4.17, 4.17, 4.17) (hidden)
mesh "Cube.007": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop SpinZ (BOOL) = False
- SENSOR ALWAYS "Always" -> [And]: controllers=(bpy.data.objects['Cubeeroid']...AndController,)
- SENSOR DELAY "Delay" -> [And.002]: controllers=(bpy.data.objects['Cubeeroid']...AndController,), delay=100, duration=20, use_repeat=True
- SENSOR PROPERTY "Spinz1" -> [And.001]: controllers=(bpy.data.objects['Cubeeroid']...AndController,), evaluation_type=PROPEQUAL, property=SpinZ, value=TRUE, value_min=TRUE
- SENSOR PROPERTY "SpinZ-1" -> [And.003]: controllers=(bpy.data.objects['Cubeeroid']...AndController,), evaluation_type=PROPEQUAL, property=SpinZ, value=FALSE, value_min=FALSE
- SENSOR COLLISION "Collision" -> [And.004]: controllers=(bpy.data.objects['Cubeeroid']...AndController,), property=PlayerBullet
- CONTROLLER LOGIC_AND "And" -> [Motion]
- CONTROLLER LOGIC_AND "And.002" -> [SpinZ]
- CONTROLLER LOGIC_AND "And.001" -> [SpinZ1]
- CONTROLLER LOGIC_AND "And.003" -> [SpinZ-1]
- CONTROLLER LOGIC_AND "And.004" -> [Message, Edit Object]
- ACTUATOR MOTION "Motion": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, offset_location=(0.0, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.5, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_local_linear_velocity=True, use_add_linear_velocity=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR RANDOM "SpinZ": seed=2076, property=SpinZ, distribution=BOOL_UNIFORM, chance=0.1, int_mean=0.1, float_value=0.1, float_min=0.1, float_mean=0.1, half_life_time=0.1
- ACTUATOR MOTION "SpinZ1": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_min_z=0.087, offset_location=(0.0, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.087), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "SpinZ-1": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_min_z=-0.087, offset_location=(0.0, 0.0, 0.0), offset_rotation=(0.0, 0.0, -0.087), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MESSAGE "Message": to_property=Spawner, subject=Refresh, body_type=TEXT, body_message=Refresh, body_property=Refresh
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### Spawner  [MESH]  pos=(25.78, -16.13, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(0.89, 0.89, 0.89)
mesh "Cube.008": 8 verts 6 faces colour=#CCCCCC
physics: NO_COLLISION mass=1.0
- prop MovX (BOOL) = False
- prop Count (FLOAT) = 0.0
- SENSOR DELAY "Delay" -> [And.001]: controllers=(bpy.data.objects['Spawner']...AndController,), delay=100, use_repeat=True
- SENSOR PROPERTY "Count" -> [And.001]: controllers=(bpy.data.objects['Spawner']...AndController,), evaluation_type=PROPLESSTHAN, property=Count, value=10, value_min=10
- SENSOR DELAY "MoveDelay" -> [And.002]: controllers=(bpy.data.objects['Spawner']...AndController,), delay=500, use_repeat=True
- SENSOR PROPERTY "MovXTrue" -> [And.003]: controllers=(bpy.data.objects['Spawner']...AndController,), evaluation_type=PROPEQUAL, property=MovX, value=TRUE, value_min=TRUE
- SENSOR PROPERTY "MovXFalse" -> [And.004]: controllers=(bpy.data.objects['Spawner']...AndController,), evaluation_type=PROPEQUAL, property=MovX, value=FALSE, value_min=FALSE
- SENSOR MESSAGE "Message" -> [And]: controllers=(bpy.data.objects['Spawner']...AndController,), subject=Refresh
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object, Property]
- CONTROLLER LOGIC_AND "And.002" -> [Property.001]
- CONTROLLER LOGIC_AND "And.003" -> [Motion.001]
- CONTROLLER LOGIC_AND "And.004" -> [Motion.002]
- CONTROLLER LOGIC_AND "And" -> [Property.002]
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ADDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, object=obj:Cubeeroid, track_object=obj:Cubeeroid, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_object_duplicate=True
- ACTUATOR PROPERTY "Property": mode=ADD, property=Count, value=1, object_property=1
- ACTUATOR PROPERTY "Property.001": mode=TOGGLE, property=MovX
- ACTUATOR MOTION "Motion.001": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_x=0.1, offset_location=(0.1, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "Motion.002": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_x=-0.1, offset_location=(-0.1, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR PROPERTY "Property.002": mode=ADD, property=Count, value=-1, object_property=-1

### BottomWall  [MESH]  pos=(0.00, -21.01, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(77.59, 0.81, 14.10)
mesh "Cube.004": 8 verts 6 faces
physics: STATIC mass=1.0

### LeftWall  [MESH]  pos=(-36.67, -0.31, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(0.54, 41.72, 13.03)
mesh "Cube.005": 8 verts 6 faces
physics: STATIC mass=1.0

### RightWall  [MESH]  pos=(36.54, -0.31, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(0.54, 41.72, 16.17)
mesh "Cube.006": 8 verts 6 faces
physics: STATIC mass=1.0

### TopWall  [MESH]  pos=(0.00, 20.88, -0.00) rot_deg=(0.00, 0.00, 0.00) size=(77.91, 0.81, 15.06)
mesh "Cube.003": 8 verts 6 faces
physics: STATIC mass=1.0

### TopWall.001  [MESH]  pos=(0.00, 0.00, -0.92) rot_deg=(0.00, 0.00, 0.00) size=(77.91, 44.06, 1.18)
mesh "Cube.002": 8 verts 6 faces colour=#CCCCCC
physics: STATIC mass=1.0

### Player  [MESH]  pos=(0.00, 0.00, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 2.00)
mesh "Cube": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=100.0
- prop Player (STRING) = Player
- SENSOR KEYBOARD "Shoot" -> [And]: controllers=(bpy.data.objects['Player']...AndController,), key=SPACE, modifier_key_1=NONE, modifier_key_2=NONE
- SENSOR KEYBOARD "Thrust" -> [And.001]: controllers=(bpy.data.objects['Player']...AndController,), key=W, modifier_key_1=NONE, modifier_key_2=NONE
- SENSOR KEYBOARD "Left" -> [And.002]: controllers=(bpy.data.objects['Player']...AndController,), key=A, modifier_key_1=NONE, modifier_key_2=NONE
- SENSOR KEYBOARD "Right" -> [And.003]: controllers=(bpy.data.objects['Player']...AndController,), key=D, modifier_key_1=NONE, modifier_key_2=NONE
- SENSOR KEYBOARD "Reverse" -> [And.004]: controllers=(bpy.data.objects['Player']...AndController,), key=S, modifier_key_1=NONE, modifier_key_2=NONE
- CONTROLLER LOGIC_AND "And" -> [SHOOT]
- CONTROLLER LOGIC_AND "And.001" -> [Forward]
- CONTROLLER LOGIC_AND "And.002" -> [Left]
- CONTROLLER LOGIC_AND "And.003" -> [Right]
- CONTROLLER LOGIC_AND "And.004" -> [Reverse]
- ACTUATOR EDIT_OBJECT "SHOOT": mode=ADDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, object=obj:PlayerBullet, track_object=obj:PlayerBullet, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_object_duplicate=True
- ACTUATOR MOTION "Forward": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, offset_location=(0.0, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 1.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_local_linear_velocity=True, use_add_linear_velocity=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "Left": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_min_z=0.035, offset_location=(0.0, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.035), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "Right": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_min_z=-0.035, offset_location=(0.0, 0.0, 0.0), offset_rotation=(0.0, 0.0, -0.035), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "Reverse": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, offset_location=(0.0, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, -1.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_local_linear_velocity=True, use_add_linear_velocity=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True

### PlayerBullet  [MESH]  pos=(0.00, 0.00, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(0.50, 0.50, 0.50) (hidden)
mesh "Cube.001": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop PlayerBullet (STRING) = PlayerBullet
- SENSOR ALWAYS "Always" -> [And]: controllers=(bpy.data.objects['PlayerBullet']...AndController,)
- SENSOR COLLISION "Player" -> [And.001]: controllers=(bpy.data.objects['PlayerBullet']...AndController,), property=Player
- SENSOR COLLISION "Collision" -> [And.002]: invert=True, controllers=(bpy.data.objects['PlayerBullet']...AndController,), property=Player
- SENSOR DELAY "END" -> [END]: use_tap=True, controllers=(bpy.data.objects['PlayerBullet']...AndController,), delay=100
- CONTROLLER LOGIC_AND "And" -> [Motion]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- CONTROLLER LOGIC_AND "And.002" -> [Edit Object.001]
- CONTROLLER LOGIC_AND "END" -> [END]
- ACTUATOR MOTION "Motion": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_y=0.5, offset_location=(0.0, 0.5, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_local_linear_velocity=True, use_add_linear_velocity=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR EDIT_OBJECT "Edit Object": mode=DYNAMICS, dynamic_operation=DISABLERIGIDBODY, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True
- ACTUATOR EDIT_OBJECT "Edit Object.001": mode=DYNAMICS, dynamic_operation=ENABLERIGIDBODY, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True
- ACTUATOR EDIT_OBJECT "END": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### Camera  [CAMERA]  pos=(0.00, 0.00, 100.00) rot_deg=(0.00, 0.00, 0.00) size=(0.00, 0.00, 0.00)
camera: lens=50.0 type=PERSP ortho_scale=74.31
physics: NO_COLLISION mass=1.0

### Light  [LIGHT]  pos=(4.08, 1.01, 69.40) rot_deg=(37.26, 3.16, 106.94) size=(0.00, 0.00, 0.00)
physics: STATIC mass=1.0

## text blocks
### Text  (4 lines)
```
W A S D to move
Space to shoot

P key to start game
```