# FPS+Enemies+WallRun.blend

## scene "Scene"  camera=PlayerCam
game: fps=60 physics=BULLET gravity=9.8

### Camera  [CAMERA]  pos=(7.36, -6.93, 4.96) rot_deg=(63.56, 0.00, 46.69) size=(0.00, 0.00, 0.00)
camera: lens=50.0 type=PERSP ortho_scale=7.31
physics: STATIC mass=1.0

### PlayerCam  [CAMERA]  pos=(-0.73, 0.58, 2.27) rot_deg=(90.00, 0.00, 0.00) size=(0.00, 0.00, 0.00) parent=PlayerCube
camera: lens=20.0 type=PERSP ortho_scale=6.0
physics: NO_COLLISION mass=1.0
- SENSOR MOUSE "Mouse" -> [And]: controllers=(bpy.data.objects['PlayerCam']...AndController,), mouse_event=MOVEMENT, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER LOGIC_AND "And" -> [Mouse]
- ACTUATOR MOUSE "Mouse": mode=LOOK, visible=True, use_axis_y=True, reset_x=True, reset_y=True, local_y=True, object_axis_x=OBJECT_AXIS_Z, object_axis_y=OBJECT_AXIS_X, sensitivity_x=2.0, sensitivity_y=2.0, min_y=-1.571, max_y=1.571

### PlayerCube  [MESH]  pos=(-0.67, 0.63, 1.56) rot_deg=(0.00, -0.00, 180.00) size=(2.00, 2.00, 3.01)
mesh "Cube.002": 8 verts 0 faces
physics: CHARACTER mass=1.0
- prop Jump (INT) = 0
- prop Player (BOOL) = True
- prop Health (INT) = 100
- SENSOR KEYBOARD "Forward" -> [And, And.009]: controllers=(bpy.data.objects['PlayerCube']...AndController, bpy.data.objects['PlayerCube']...AndController), key=W, modifier_key_1=NONE, modifier_key_2=NONE
- SENSOR KEYBOARD "Left" -> [And.001, And.009]: controllers=(bpy.data.objects['PlayerCube']...AndController, bpy.data.objects['PlayerCube']...AndController), key=A, modifier_key_1=NONE, modifier_key_2=NONE
- SENSOR KEYBOARD "Right" -> [And.002, And.009]: use_pulse_true_level=True, controllers=(bpy.data.objects['PlayerCube']...AndController, bpy.data.objects['PlayerCube']...AndController), key=D, modifier_key_1=NONE, modifier_key_2=NONE
- SENSOR KEYBOARD "Back" -> [And.003]: controllers=(bpy.data.objects['PlayerCube']...AndController,), key=S, modifier_key_1=NONE, modifier_key_2=NONE
- SENSOR COLLISION "WALL" -> [And.010]: controllers=(bpy.data.objects['PlayerCube']...AndController,), use_material=True, material=Wall
- SENSOR COLLISION "JUMPPAD" -> [And.008]: controllers=(bpy.data.objects['PlayerCube']...AndController,), property=Jumppad
- SENSOR MOUSE "Look" -> [And.004]: controllers=(bpy.data.objects['PlayerCube']...AndController,), mouse_event=MOVEMENT, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- SENSOR MOUSE "Shoot" -> [And.011]: controllers=(bpy.data.objects['PlayerCube']...AndController,), mouse_event=LEFTCLICK, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- SENSOR KEYBOARD "Jump" -> [And.005, And.006]: controllers=(bpy.data.objects['PlayerCube']...AndController, bpy.data.objects['PlayerCube']...AndController), key=SPACE, modifier_key_1=NONE, modifier_key_2=NONE, target=Player, log=Jump
- SENSOR PROPERTY "JUMP_Prop" -> [And.006]: controllers=(bpy.data.objects['PlayerCube']...AndController,), evaluation_type=PROPINTERVAL, property=Jump, value=0, value_min=0, value_max=1
- SENSOR COLLISION "GROUND" -> [And.007]: controllers=(bpy.data.objects['PlayerCube']...AndController,), property=ground
- CONTROLLER LOGIC_AND "And" -> [FORWARD]
- CONTROLLER LOGIC_AND "And.001" -> [LEFT]
- CONTROLLER LOGIC_AND "And.002" -> [RIGHT]
- CONTROLLER LOGIC_AND "And.003" -> [BACK]
- CONTROLLER LOGIC_AND "And.009" -> [WALL_CLIMB]
- CONTROLLER LOGIC_AND "And.010" -> [WALL_CLIMB]
- CONTROLLER LOGIC_AND "And.008" -> [pad_boost]
- CONTROLLER LOGIC_AND "And.004" -> [Mouse]
- CONTROLLER LOGIC_AND "And.011" -> [BULLET]
- CONTROLLER LOGIC_AND "And.005" -> [JUMP]
- CONTROLLER LOGIC_AND "And.006" -> [JUMP_Start, JUMP]
- CONTROLLER LOGIC_AND "And.007" -> [JUMP_Stop]
- ACTUATOR MOTION "FORWARD": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_y=0.2, offset_location=(0.0, 0.2, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "LEFT": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_x=-0.2, offset_location=(-0.2, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "RIGHT": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_x=0.2, offset_location=(0.2, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "BACK": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_y=-0.2, offset_location=(0.0, -0.2, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "WALL_CLIMB": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_z=1.0, offset_location=(0.0, 0.0, 1.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 20.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "pad_boost": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_x=2.0, offset_location=(2.0, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 12.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOUSE "Mouse": mode=LOOK, visible=True, use_axis_x=True, reset_x=True, reset_y=True, local_y=True, object_axis_x=OBJECT_AXIS_Z, object_axis_y=OBJECT_AXIS_X, sensitivity_x=2.0, sensitivity_y=2.0, min_y=-1.571, max_y=1.571
- ACTUATOR EDIT_OBJECT "BULLET": mode=ADDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, object=obj:Bullet, track_object=obj:Bullet, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True
- ACTUATOR PROPERTY "JUMP_Start": mode=ADD, property=Jump, value=1, object_property=1
- ACTUATOR MOTION "JUMP": mode=OBJECT_CHARACTER, servo_mode=SERVO_LINEAR, offset_location=(0.0, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_servo_limit_y=True, use_servo_limit_z=True, use_character_jump=True
- ACTUATOR PROPERTY "JUMP_Stop": mode=ASSIGN, property=Jump, value=0, object_property=0

### Floor  [MESH]  pos=(0.00, 0.00, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(227.75, 227.75, 0.00)
mesh "Plane": 4 verts 1 faces colour=#CCCCCC
physics: STATIC mass=1.0
- prop ground (FLOAT) = 0.0

### EnemySpawner  [MESH]  pos=(-0.67, 47.74, 2.62) rot_deg=(0.00, 0.00, 0.00) size=(1.89, 0.95, 5.07)
mesh "Cube.003": 8 verts 6 faces
physics: STATIC mass=1.0
- prop counter (INT) = 0
- SENSOR DELAY "CounterDelay" -> [And]: controllers=(bpy.data.objects['EnemySpawner']...AndController,), delay=1, duration=1, use_repeat=True
- SENSOR PROPERTY "COUNTER" -> [And.001]: controllers=(bpy.data.objects['EnemySpawner']...AndController,), evaluation_type=PROPGREATERTHAN, property=counter, value=100, value_min=100
(no game logic: 'NoneType' object has no attribute 'name')

### Platform  [MESH]  pos=(-41.64, -35.06, 4.58) rot_deg=(0.00, 0.00, 0.00) size=(59.19, 73.85, 9.23)
mesh "Cube.006": 48 verts 46 faces colour=#CCCCCC
physics: STATIC mass=1.0
- prop Floor (FLOAT) = 0.0

### stairs  [MESH]  pos=(19.46, -3.77, 0.35) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 9.21, 3.64)
mesh "Cube.008": 40 verts 38 faces
physics: STATIC mass=1.0

### Enemy  [MESH]  pos=(0.00, 0.00, 1.44) rot_deg=(0.00, 0.00, 0.00) size=(1.86, 1.86, 2.78) (hidden)
mesh "Cube.010": 8 verts 6 faces colour=#CCCCCC
physics: DYNAMIC mass=1.0
- prop Health (INT) = 100
- SENSOR NEAR "Near" -> [And]: controllers=(bpy.data.objects['Enemy']...AndController,), property=Player, distance=1000.0, reset_distance=2000.0
- SENSOR COLLISION "Collision" -> [And.001]: controllers=(bpy.data.objects['Enemy']...AndController,), use_material=True, property=Bullet, material=Bullet
- SENSOR PROPERTY "Property" -> [And.002]: controllers=(bpy.data.objects['Enemy']...AndController,), evaluation_type=PROPLESSTHAN, property=Health, value=0, value_min=0
- CONTROLLER LOGIC_AND "And" -> [SeekPlayer]
- CONTROLLER LOGIC_AND "And.001" -> [Health-20]
- CONTROLLER LOGIC_AND "And.002" -> [DIE]
- ACTUATOR STEERING "SeekPlayer": mode=SEEK, velocity=3.0, acceleration=3.0, turn_speed=120.0, distance=1.0, target=obj:PlayerCube, facing=True, facing_axis=X, lock_z_velocity=True
- ACTUATOR PROPERTY "Health-20": mode=ASSIGN, property=Health, value=-20, object_property=-20
- ACTUATOR EDIT_OBJECT "DIE": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### Bullet  [MESH]  pos=(-5.44, 0.54, 3.61) rot_deg=(0.00, 0.00, 0.00) size=(0.19, 0.51, 0.24) (hidden)
mesh "Cube.012": 8 verts 6 faces colour=#CCCCCC
physics: DYNAMIC mass=0.01
- prop Bullet (FLOAT) = 0.0
- SENSOR ALWAYS "Always" -> [And]: controllers=(bpy.data.objects['Bullet']...AndController,)
- SENSOR COLLISION "Collision" -> [And.001]: controllers=(bpy.data.objects['Bullet']...AndController,), use_material=True, material=Enemy
- CONTROLLER LOGIC_AND "And" -> [Motion]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- ACTUATOR MOTION "Motion": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_y=0.4, offset_location=(0.0, 0.4, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### Instructions  [FONT]  pos=(-0.49, -12.98, 6.14) rot_deg=(90.00, 0.00, 180.00) size=(17.75, 7.10, 0.00)
text: "Simple Logic Bricks FPS Example 
With Enemy and Bullet spawning
WASD to move
Click to Shoot
Space to Jump
Also run along walls for wall running"
physics: NO_COLLISION mass=1.0

### EnemyText  [FONT]  pos=(1.05, 0.09, 1.41) rot_deg=(90.00, -0.00, 90.00) size=(1.90, 0.42, 0.00) parent=Enemy (hidden)
text: "ENEMY"
physics: NO_COLLISION mass=1.0

### platform  [MESH]  pos=(28.01, -19.80, 9.86) rot_deg=(0.00, -0.00, 90.00) size=(45.83, 3.61, 2.83)
mesh "Cube.005": 8 verts 6 faces colour=#CCCCCC
physics: STATIC mass=1.0
- prop prop (FLOAT) = 0.0

### Light  [LIGHT]  pos=(4.08, 1.01, 5.90) rot_deg=(37.26, 3.16, 106.94) size=(0.00, 0.00, 0.00)
physics: STATIC mass=1.0

### Wall  [MESH]  pos=(-33.24, 19.35, 5.31) rot_deg=(0.00, 0.00, 0.00) size=(45.83, 0.20, 11.24)
mesh "Cube.009": 8 verts 6 faces colour=#CCCCCC
physics: STATIC mass=1.0
- prop prop (FLOAT) = 0.0

### Wall.001  [MESH]  pos=(26.17, -18.88, 5.63) rot_deg=(0.00, -0.00, 90.00) size=(45.83, 0.20, 11.24)
mesh "Cube.001": 8 verts 6 faces colour=#CCCCCC
physics: STATIC mass=1.0
- prop prop (FLOAT) = 0.0

### Wall.002  [MESH]  pos=(30.08, -20.17, 5.36) rot_deg=(0.00, -0.00, 90.00) size=(45.83, 0.20, 11.24)
mesh "Cube.004": 8 verts 6 faces colour=#CCCCCC
physics: STATIC mass=1.0
- prop prop (FLOAT) = 0.0

## text blocks
### Instructions  (11 lines)
```
Simple Logic Bricks FPS Example
With Enemy and Bullet Spawning

WASD to move
Click to Shoot
Space to jump

See Tutorial 
https://youtu.be/7mmm3FPuj1k


```