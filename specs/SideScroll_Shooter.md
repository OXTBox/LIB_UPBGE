# SideScroll_Shooter.blend

## scene "Scene"  camera=Camera
game: fps=60 physics=BULLET gravity=0.0

### Score  [FONT]  pos=(5.05, 1.53, 10.92) rot_deg=(90.00, -0.00, 0.00) size=(1.21, 1.92, 0.00)
text: "0"
physics: NO_COLLISION mass=1.0
- prop Text (STRING) = 
- prop Score (INT) = 0
- SENSOR MESSAGE "Message" -> [And]: controllers=(bpy.data.objects['Score']...AndController,), subject=Score
- CONTROLLER LOGIC_AND "And" -> [Property]
- ACTUATOR PROPERTY "Property": mode=COPY, property=Text, value=Score, object=obj:Player, object_property=Score

### TestScore  [EMPTY]  pos=(0.00, 0.00, 0.00) rot_deg=(0.00, -0.00, 0.00) size=(0.00, 0.00, 0.00)
physics: NO_COLLISION mass=1.0
- SENSOR KEYBOARD "1Key" -> [And]: controllers=(bpy.data.objects['TestScore']...AndController,), key=ONE, modifier_key_1=NONE, modifier_key_2=NONE
- CONTROLLER LOGIC_AND "And" -> [Message]
- ACTUATOR MESSAGE "Message": to_property=Player, subject=Score, body_type=TEXT, body_message=Score, body_property=Score

### Player  [MESH]  pos=(-1.00, 0.00, 0.46) rot_deg=(0.00, -0.00, 0.00) size=(2.00, 2.00, 0.77)
mesh "Cube": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=100.0
- prop Player (STRING) = Player
- prop Score (INT) = 0
- SENSOR KEYBOARD "UP" -> [And]: controllers=(bpy.data.objects['Player']...AndController,), key=W, modifier_key_1=NONE, modifier_key_2=NONE
- SENSOR KEYBOARD "DOWN" -> [And.001]: controllers=(bpy.data.objects['Player']...AndController,), key=S, modifier_key_1=NONE, modifier_key_2=NONE
- SENSOR KEYBOARD "Keyboard" -> [And.002]: use_tap=True, controllers=(bpy.data.objects['Player']...AndController,), key=SPACE, modifier_key_1=NONE, modifier_key_2=NONE
- SENSOR MESSAGE "Message" -> [And.003]: controllers=(bpy.data.objects['Player']...AndController,), subject=Score
- SENSOR PROPERTY "Property" -> [And.004]: controllers=(bpy.data.objects['Player']...AndController,), evaluation_type=PROPCHANGED, property=Score
- CONTROLLER LOGIC_AND "And" -> [UP]
- CONTROLLER LOGIC_AND "And.001" -> [DOWN]
- CONTROLLER LOGIC_AND "And.002" -> [Edit Object]
- CONTROLLER LOGIC_AND "And.003" -> [Property]
- CONTROLLER LOGIC_AND "And.004" -> [Message]
- ACTUATOR MOTION "UP": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, offset_location=(0.0, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 1.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_local_linear_velocity=True, use_add_linear_velocity=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "DOWN": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, offset_location=(0.0, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, -1.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_local_linear_velocity=True, use_add_linear_velocity=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ADDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, object=obj:PlayerBullet, track_object=obj:PlayerBullet, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_object_duplicate=True
- ACTUATOR PROPERTY "Property": mode=ADD, property=Score, value=100, object_property=100
- ACTUATOR MESSAGE "Message": to_property=Score, subject=Score, body_type=TEXT, body_message=Score, body_property=Score

### PlayerBullet  [MESH]  pos=(1.01, 0.00, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(0.31, 0.31, 0.31) (hidden)
mesh "Cube.002": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=0.01
- prop PlayerBullet (STRING) = PlayerBullet
- SENSOR ALWAYS "ALWAYS" -> [ACTIVE]: controllers=(bpy.data.objects['PlayerBullet']...AndController,)
- SENSOR COLLISION "RightWall" -> [END]: controllers=(bpy.data.objects['PlayerBullet']...OrController,), property=RightWall
- SENSOR COLLISION "Enemy" -> [END, And]: controllers=(bpy.data.objects['PlayerBullet']...OrController, bpy.data.objects['PlayerBullet']...AndController), property=Enemy
- SENSOR DELAY "END" -> [END]: use_tap=True, controllers=(bpy.data.objects['PlayerBullet']...OrController,), delay=100
- SENSOR NEAR "Near" -> [And.001]: controllers=(bpy.data.objects['PlayerBullet']...AndController,), property=Player, distance=2.0, reset_distance=3.0
- CONTROLLER LOGIC_AND "ACTIVE" -> [ACTIVE]
- CONTROLLER LOGIC_OR "END" -> [END]
- CONTROLLER LOGIC_AND "And" -> [Score]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- ACTUATOR MOTION "ACTIVE": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_x=0.1, offset_location=(0.1, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.3, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_local_linear_velocity=True, use_add_linear_velocity=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR EDIT_OBJECT "END": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True
- ACTUATOR MESSAGE "Score": to_property=Player, subject=Score, body_type=TEXT, body_message=Score, body_property=Score
- ACTUATOR EDIT_OBJECT "Edit Object": mode=DYNAMICS, dynamic_operation=DISABLERIGIDBODY, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### LeftWall  [MESH]  pos=(-6.92, 0.00, -0.97) rot_deg=(0.00, -0.00, 0.00) size=(0.70, 2.00, 22.00)
mesh "Cube.003": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop LeftWall (STRING) = LeftWall

### RightWall  [MESH]  pos=(55.72, 0.00, -1.02) rot_deg=(0.00, -0.00, 0.00) size=(0.70, 2.00, 22.32)
mesh "Cube.004": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop RightWall (STRING) = RightWall

### ToPwall  [MESH]  pos=(24.51, 0.00, 10.10) rot_deg=(0.00, -0.00, 0.00) size=(62.50, 2.00, 0.49)
mesh "Cube.005": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop TopWall (STRING) = TopWall

### BottomWall  [MESH]  pos=(24.74, 0.00, -12.71) rot_deg=(0.00, -0.00, 0.00) size=(64.56, 2.00, 0.95)
mesh "Cube.006": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop BottomWall (STRING) = BottomWall

### Camera  [CAMERA]  pos=(17.46, -0.23, 0.00) rot_deg=(90.00, -0.00, 0.00) size=(0.00, 0.00, 0.00)
camera: lens=9.0 type=ORTHO ortho_scale=48.1
physics: STATIC mass=1.0

### Light  [LIGHT]  pos=(18.08, -26.59, -0.12) rot_deg=(127.62, 105.43, 369.16) size=(0.00, 0.00, 0.00)
physics: STATIC mass=1.0

### Enemy  [MESH]  pos=(40.39, 0.00, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 1.53) (hidden)
mesh "Cube.010": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=53.11
- prop Enemy (STRING) = Enemy
- prop Angle (INT) = 0
- prop bShoot (BOOL) = False
- SENSOR ALWAYS "Always" -> [And]: controllers=(bpy.data.objects['Enemy']...AndController,)
- SENSOR COLLISION "LeftWall" -> [End]: controllers=(bpy.data.objects['Enemy']...OrController,), property=LeftWall
- SENSOR COLLISION "PlayerBUllet" -> [End]: controllers=(bpy.data.objects['Enemy']...OrController,), property=PlayerBullet
- SENSOR DELAY "DieTime" -> [End]: use_tap=True, controllers=(bpy.data.objects['Enemy']...OrController,), delay=3000
- SENSOR COLLISION "Player" -> [End]: controllers=(bpy.data.objects['Enemy']...OrController,), property=Player
- SENSOR NEAR "Near" -> [And.001]: controllers=(bpy.data.objects['Enemy']...AndController,), property=Spawner, distance=4.0, reset_distance=5.0
- SENSOR DELAY "AngleDelay" -> [And.002]: controllers=(bpy.data.objects['Enemy']...AndController,), delay=10, duration=5, use_repeat=True
- SENSOR PROPERTY "Angle1" -> [And.003]: use_tap=True, controllers=(bpy.data.objects['Enemy']...AndController,), evaluation_type=PROPEQUAL, property=Angle, value=1, value_min=1
- SENSOR PROPERTY "Angle-1" -> [And.004]: use_tap=True, controllers=(bpy.data.objects['Enemy']...AndController,), evaluation_type=PROPEQUAL, property=Angle, value=-1, value_min=-1
- SENSOR PROPERTY "Angle2" -> [And.005]: use_tap=True, controllers=(bpy.data.objects['Enemy']...AndController,), evaluation_type=PROPEQUAL, property=Angle, value=2, value_min=2
- SENSOR PROPERTY "Angle-2" -> [And.006]: use_tap=True, controllers=(bpy.data.objects['Enemy']...AndController,), evaluation_type=PROPEQUAL, property=Angle, value=-2, value_min=-2
- SENSOR DELAY "SHOOT" -> [ShootRand]: controllers=(bpy.data.objects['Enemy']...AndController,), delay=10, use_repeat=True
- SENSOR PROPERTY "Property" -> [SHOOT]: use_tap=True, controllers=(bpy.data.objects['Enemy']...AndController,), evaluation_type=PROPEQUAL, property=bShoot, value=TRUE, value_min=TRUE
- CONTROLLER LOGIC_AND "And" -> [Motion]
- CONTROLLER LOGIC_OR "End" -> [End]
- CONTROLLER LOGIC_AND "And.001" -> [NoRigide]
- CONTROLLER LOGIC_AND "And.002" -> [Random]
- CONTROLLER LOGIC_AND "And.003" -> [Angle1]
- CONTROLLER LOGIC_AND "And.004" -> [Angle-1]
- CONTROLLER LOGIC_AND "And.005" -> [Angle2]
- CONTROLLER LOGIC_AND "And.006" -> [Angle-2]
- CONTROLLER LOGIC_AND "ShootRand" -> [ShootRand]
- CONTROLLER LOGIC_AND "SHOOT" -> [SHOOT]
- ACTUATOR MOTION "Motion": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, offset_location=(0.0, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(-1.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_local_linear_velocity=True, use_add_linear_velocity=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR EDIT_OBJECT "End": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True
- ACTUATOR EDIT_OBJECT "NoRigide": mode=DYNAMICS, dynamic_operation=DISABLERIGIDBODY, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True
- ACTUATOR RANDOM "Random": property=Angle, distribution=INT_UNIFORM, chance=0.1, int_value=-2, int_min=-2, int_max=2, int_mean=0.1, float_value=0.1, float_min=0.1, float_mean=0.1, half_life_time=0.1
- ACTUATOR MOTION "Angle1": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, offset_location=(0.0, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 1.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_local_linear_velocity=True, use_add_linear_velocity=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "Angle-1": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, offset_location=(0.0, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, -1.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_local_linear_velocity=True, use_add_linear_velocity=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "Angle2": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, offset_location=(0.0, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 4.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_local_linear_velocity=True, use_add_linear_velocity=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "Angle-2": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, offset_location=(0.0, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, -4.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_local_linear_velocity=True, use_add_linear_velocity=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR RANDOM "ShootRand": property=bShoot, distribution=BOOL_UNIFORM, chance=0.1, int_mean=0.1, float_value=0.1, float_min=0.1, float_mean=0.1, half_life_time=0.1
- ACTUATOR EDIT_OBJECT "SHOOT": mode=ADDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, object=obj:Enemy_Bullet, track_object=obj:Enemy_Bullet, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_object_duplicate=True

### Enemy_Bullet  [MESH]  pos=(1.01, 0.00, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(0.31, 0.31, 0.31) (hidden)
mesh "Cube.009": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=0.01
- prop EnemyBullet (STRING) = EnemyBullet
- SENSOR ALWAYS "ALWAYS" -> [ACTIVE]: controllers=(bpy.data.objects['Enemy_Bullet']...AndController,)
- SENSOR COLLISION "RightWall" -> [END]: controllers=(bpy.data.objects['Enemy_Bullet']...AndController,), property=RightWall
- SENSOR DELAY "EndBullet" -> [End]: controllers=(bpy.data.objects['Enemy_Bullet']...AndController,), delay=200
- SENSOR NEAR "Near" -> [And]: controllers=(bpy.data.objects['Enemy_Bullet']...AndController,), property=Enemy, distance=2.0, reset_distance=3.0
- CONTROLLER LOGIC_AND "ACTIVE" -> [ACTIVE]
- CONTROLLER LOGIC_AND "END" -> [END]
- CONTROLLER LOGIC_AND "End" -> [End]
- CONTROLLER LOGIC_AND "And" -> [NoRigd]
- ACTUATOR MOTION "ACTIVE": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_x=-1.0, offset_location=(-1.0, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(-1.5, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_local_linear_velocity=True, use_add_linear_velocity=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR EDIT_OBJECT "END": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True
- ACTUATOR EDIT_OBJECT "End": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True
- ACTUATOR EDIT_OBJECT "NoRigd": mode=DYNAMICS, dynamic_operation=DISABLERIGIDBODY, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### Spawner  [MESH]  pos=(46.70, 0.03, 0.30) rot_deg=(0.00, -0.00, 0.00) size=(1.41, 1.41, 1.41)
mesh "SpawnerCub": 8 verts 6 faces colour=#CCCCCC
physics: NO_COLLISION mass=1.0
- prop Spawn (BOOL) = False
- prop Spawner (STRING) = Spawner
- prop DirZ (BOOL) = False
- prop DirX (BOOL) = False
- SENSOR DELAY "Spawn" -> [And]: controllers=(bpy.data.objects['Spawner']...AndController,), delay=30, duration=5, use_repeat=True
- SENSOR PROPERTY "SPAWN" -> [Spawn]: controllers=(bpy.data.objects['Spawner']...AndController,), evaluation_type=PROPEQUAL, property=Spawn, value=TRUE, value_min=TRUE
- SENSOR DELAY "DelayZ" -> [And.005]: use_tap=True, controllers=(bpy.data.objects['Spawner']...AndController,), delay=40, duration=50, use_repeat=True
- SENSOR PROPERTY "PlusZ" -> [And.004]: controllers=(bpy.data.objects['Spawner']...AndController,), evaluation_type=PROPEQUAL, property=DirZ, value=TRUE, value_min=TRUE
- SENSOR PROPERTY "MinuxZ" -> [And.006]: controllers=(bpy.data.objects['Spawner']...AndController,), evaluation_type=PROPEQUAL, property=DirZ, value=FALSE, value_min=FALSE
- CONTROLLER LOGIC_AND "And" -> [TOGGLE]
- CONTROLLER LOGIC_AND "Spawn" -> [Spawn]
- CONTROLLER LOGIC_AND "And.005" -> [DIRZToggle]
- CONTROLLER LOGIC_AND "And.004" -> [ZPlus]
- CONTROLLER LOGIC_AND "And.006" -> [ZMinus]
- ACTUATOR PROPERTY "TOGGLE": mode=TOGGLE, property=Spawn
- ACTUATOR EDIT_OBJECT "Spawn": mode=ADDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, object=obj:Enemy, track_object=obj:Enemy, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_object_duplicate=True
- ACTUATOR PROPERTY "DIRZToggle": mode=TOGGLE, property=DirZ
- ACTUATOR MOTION "ZPlus": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_z=0.15, offset_location=(0.0, 0.0, 0.15), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "ZMinus": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_z=-0.15, offset_location=(0.0, 0.0, -0.15), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True

## text blocks
### Text  (4 lines)
```
W & S to move 
Space bar to shoot

P key to start game
```