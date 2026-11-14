# CUBE_INVADERS.blend

## scene "Scene"  camera=Camera
game: fps=60 physics=BULLET gravity=9.8

### BottomWall  [MESH]  pos=(0.00, -11.20, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(80.00, 4.00, 2.01)
mesh "Cube.009": 8 verts 6 faces
physics: RIGID_BODY mass=1.0
- prop WALL (STRING) = WALL
- prop BOTTOMWALL (STRING) = BOTTOMWALL

### LeftWall  [MESH]  pos=(-19.56, 97.58, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(3.19, 200.00, 2.01)
mesh "Cube.005": 8 verts 6 faces
physics: RIGID_BODY mass=1.0
- prop WALL (STRING) = WALL

### TopWall  [MESH]  pos=(0.00, 92.40, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(80.00, 4.00, 2.01)
mesh "Cube.008": 8 verts 6 faces
physics: RIGID_BODY mass=1.0
- prop WALL (STRING) = WALL

### Rightwall  [MESH]  pos=(18.97, 97.58, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(3.19, 200.00, 2.01)
mesh "Cube.007": 8 verts 6 faces
physics: RIGID_BODY mass=1.0
- prop WALL (STRING) = WALL

### Light  [LIGHT]  pos=(0.03, 1.01, 5.90) rot_deg=(37.26, 3.16, 106.94) size=(0.00, 0.00, 0.00)
physics: STATIC mass=1.0

### Camera  [CAMERA]  pos=(0.00, -8.79, 12.89) rot_deg=(66.26, 0.00, 0.00) size=(0.00, 0.00, 0.00)
camera: lens=13.0 type=PERSP ortho_scale=7.31
physics: STATIC mass=1.0

### Player  [MESH]  pos=(0.00, 0.00, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 2.00)
mesh "Cube": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=20.3
- prop PLAYER (STRING) = PLAYER
- SENSOR KEYBOARD "Left" -> [LEFT]: controllers=(bpy.data.objects['Player']...AndController,), key=A, modifier_key_1=NONE, modifier_key_2=NONE
- SENSOR KEYBOARD "Right" -> [RIGHT]: controllers=(bpy.data.objects['Player']...AndController,), key=D, modifier_key_1=NONE, modifier_key_2=NONE
- SENSOR COLLISION "Collision" -> [And]: use_tap=True, controllers=(bpy.data.objects['Player']...AndController,), property=InvaderBullet
- SENSOR KEYBOARD "Space" -> [And.001]: controllers=(bpy.data.objects['Player']...AndController,), key=SPACE, modifier_key_1=NONE, modifier_key_2=NONE
- CONTROLLER LOGIC_AND "LEFT" -> [Left]
- CONTROLLER LOGIC_AND "RIGHT" -> [Right]
- CONTROLLER LOGIC_AND "And" -> [Game]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- ACTUATOR MOTION "Left": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_x=-1.0, offset_location=(-1.0, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "Right": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_x=1.0, offset_location=(1.0, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR GAME "Game": mode=RESTART
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ADDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, object=obj:PlayerBullet, track_object=obj:PlayerBullet, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### PlayerBullet  [MESH]  pos=(0.00, 0.00, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(0.50, 0.50, 0.50) (hidden)
mesh "Cube.001": 8 verts 6 faces
physics: RIGID_BODY mass=1.0
- prop PlayerBullet (STRING) = PlayerBullet
- SENSOR ALWAYS "Always" -> [And]: controllers=(bpy.data.objects['PlayerBullet']...AndController,)
- SENSOR COLLISION "WALL" -> [END]: controllers=(bpy.data.objects['PlayerBullet']...OrController,), property=WALL
- SENSOR COLLISION "Collision" -> [END]: controllers=(bpy.data.objects['PlayerBullet']...OrController,), property=ENEMY
- SENSOR NEAR "Near" -> [And.001]: controllers=(bpy.data.objects['PlayerBullet']...AndController,), property=Player, distance=1.0, reset_distance=2.0
- CONTROLLER LOGIC_AND "And" -> [Motion]
- CONTROLLER LOGIC_OR "END" -> [END]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- ACTUATOR MOTION "Motion": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_y=1.0, offset_location=(0.0, 1.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR EDIT_OBJECT "END": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True
- ACTUATOR EDIT_OBJECT "Edit Object": mode=DYNAMICS, dynamic_operation=SUSPENDPHY, up_axis=UPAXISZ, track_axis=TRACKAXISY, object=obj:PlayerBullet, track_object=obj:PlayerBullet, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### SCORE  [FONT]  pos=(0.02, 31.19, 16.65) rot_deg=(90.00, 0.00, 0.00) size=(2.79, 4.45, 0.00)
text: "0"
physics: NO_COLLISION mass=1.0
- prop Text (INT) = 0
- SENSOR MESSAGE "Message" -> [And]: controllers=(bpy.data.objects['SCORE']...AndController,), subject=score
- CONTROLLER LOGIC_AND "And" -> [Property.001]
- ACTUATOR PROPERTY "Property.001": mode=ADD, property=Text, value=100, object_property=100

### Instructions  [FONT]  pos=(0.90, 31.19, 10.93) rot_deg=(90.00, 0.00, 0.00) size=(54.00, 5.85, 0.00)
text: "Press Space To Begin"
physics: NO_COLLISION mass=1.0
- SENSOR KEYBOARD "Message" -> [And]: controllers=(bpy.data.objects['Instructions']...AndController,), key=SPACE, modifier_key_1=NONE, modifier_key_2=NONE
- CONTROLLER LOGIC_AND "And" -> [Property.001]
- ACTUATOR EDIT_OBJECT "Property.001": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### Invader  [MESH]  pos=(0.00, 49.63, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 2.00) (hidden)
mesh "Cube.004": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop DirX (INT) = 0
- prop Shoot (INT) = 0
- prop ENEMY (STRING) = ENEMY
- SENSOR PROPERTY "SHOOT" -> [SHOOT]: controllers=(bpy.data.objects['Invader']...AndController,), evaluation_type=PROPGREATERTHAN, property=Shoot, value=50, value_min=50
- SENSOR DELAY "Delay" -> [Delay]: controllers=(bpy.data.objects['Invader']...AndController,), delay=50, use_repeat=True
- SENSOR COLLISION "WALL" -> [WALL]: use_tap=True, controllers=(bpy.data.objects['Invader']...AndController,), property=WALL
- SENSOR COLLISION "HIT" -> [HIT]: controllers=(bpy.data.objects['Invader']...OrController,), property=PlayerBullet
- SENSOR COLLISION "OffScreen" -> [And]: controllers=(bpy.data.objects['Invader']...AndController,), property=BOTTOMWALL
- CONTROLLER LOGIC_AND "SHOOT" -> [SHOOT]
- CONTROLLER LOGIC_AND "Delay" -> [SHOOTRand]
- CONTROLLER LOGIC_AND "WALL" -> [WALL]
- CONTROLLER LOGIC_OR "HIT" -> [DIE, Refresh, score]
- CONTROLLER LOGIC_AND "And" -> [DIE, Refresh]
- ACTUATOR EDIT_OBJECT "SHOOT": mode=ADDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, object=obj:InvaderBullet, track_object=obj:InvaderBullet, linear_velocity=(0.0, -40.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_object_duplicate=True
- ACTUATOR RANDOM "SHOOTRand": seed=1256, property=Shoot, distribution=INT_UNIFORM, chance=0.1, int_max=100, int_mean=0.1, float_value=0.1, float_min=0.1, float_mean=0.1, half_life_time=0.1
- ACTUATOR MOTION "WALL": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_y=-4.0, offset_location=(0.0, -4.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR EDIT_OBJECT "DIE": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True
- ACTUATOR MESSAGE "score": to_property=SCORE, subject=score, body_type=TEXT, body_message=score, body_property=score
- ACTUATOR MESSAGE "Refresh": to_property=SPAWNER, subject=Refresh, body_type=TEXT, body_message=Refresh, body_property=Refresh

### InvaderBullet  [MESH]  pos=(0.00, 0.00, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(0.50, 0.50, 0.50) (hidden)
mesh "Cube.002": 8 verts 6 faces
physics: RIGID_BODY mass=0.01
- prop InvaderBullet (STRING) = InvaderBullet
- SENSOR ALWAYS "Always" -> [And]: controllers=(bpy.data.objects['InvaderBullet']...AndController,)
- SENSOR COLLISION "WALL" -> [END]: controllers=(bpy.data.objects['InvaderBullet']...AndController,), property=BOTTOMWALL
- CONTROLLER LOGIC_AND "And" -> [Motion]
- CONTROLLER LOGIC_AND "END" -> [END]
- ACTUATOR MOTION "Motion": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, offset_location=(0.0, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR EDIT_OBJECT "END": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### SPAWNER  [EMPTY]  pos=(0.00, 83.76, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(0.00, 0.00, 0.00)
physics: NO_COLLISION mass=1.0
- prop Play (BOOL) = False
- prop Count (INT) = 0
- SENSOR KEYBOARD "SPACE" -> [PLAY]: use_tap=True, controllers=(bpy.data.objects['SPAWNER']...AndController,), key=SPACE, modifier_key_1=NONE, modifier_key_2=NONE
- SENSOR PROPERTY "START" -> [PLAY]: controllers=(bpy.data.objects['SPAWNER']...AndController,), evaluation_type=PROPEQUAL, property=Play, value=FALSE, value_min=FALSE
- SENSOR PROPERTY "ACTIVE" -> [SPAWN]: controllers=(bpy.data.objects['SPAWNER']...AndController,), evaluation_type=PROPEQUAL, property=Play, value=TRUE, value_min=TRUE
- SENSOR DELAY "Delay" -> [SPAWN]: controllers=(bpy.data.objects['SPAWNER']...AndController,), delay=60, use_repeat=True
- SENSOR PROPERTY "COUNT" -> [SPAWN]: controllers=(bpy.data.objects['SPAWNER']...AndController,), evaluation_type=PROPLESSTHAN, property=Count, value=20, value_min=20
- SENSOR MESSAGE "Refresh" -> [And]: controllers=(bpy.data.objects['SPAWNER']...AndController,), subject=Refresh
- SENSOR PROPERTY "NotZero" -> [And]: controllers=(bpy.data.objects['SPAWNER']...AndController,), evaluation_type=PROPGREATERTHAN, property=Count, value=0, value_min=0
- CONTROLLER LOGIC_AND "PLAY" -> [PLAY]
- CONTROLLER LOGIC_AND "SPAWN" -> [SPAWN, Property]
- CONTROLLER LOGIC_AND "And" -> [Property.001]
- ACTUATOR PROPERTY "PLAY": mode=ASSIGN, property=Play, value=TRUE, object_property=TRUE
- ACTUATOR EDIT_OBJECT "SPAWN": mode=ADDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, object=obj:Invader, track_object=obj:Invader, linear_velocity=(20.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True
- ACTUATOR PROPERTY "Property": mode=ADD, property=Count, value=1, object_property=1
- ACTUATOR PROPERTY "Property.001": mode=ADD, property=Count, value=-1, object_property=-1

## text blocks
### Instructions  (6 lines)
```
A & D to move
SPACE to shoot

P key to start game

game resets when player is hit
```