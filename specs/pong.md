# pong.blend

## scene "Scene"  camera=Camera
game: fps=60 physics=BULLET gravity=0.0

### Camera  [CAMERA]  pos=(0.07, -2.92, 100.00) rot_deg=(0.00, 0.00, 0.00) size=(0.00, 0.00, 0.00)
camera: lens=50.0 type=ORTHO ortho_scale=169.51
physics: STATIC mass=1.0
- prop SCORE2 (FLOAT) = 0.0

### Light  [LIGHT]  pos=(4.08, 1.01, 34.58) rot_deg=(37.26, 3.16, 106.94) size=(0.00, 0.00, 0.00)
physics: STATIC mass=1.0

### RightWall  [MESH]  pos=(83.38, -7.05, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(2.31, 82.00, 24.36)
mesh "Cube.004": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop Score1 (INT) = 0
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['RightWall']...AndController,), use_material=True, material=Ball
- CONTROLLER LOGIC_AND "And" -> [Message, Property]
- ACTUATOR MESSAGE "Message": to_property=Score1, subject=1up, body_type=TEXT, body_message=1, body_property=1
- ACTUATOR PROPERTY "Property": mode=ADD, property=Score1, value=1, object_property=1

### TopWall  [MESH]  pos=(-0.02, 34.25, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(170.00, 2.26, 24.36)
mesh "Cube.005": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop TopWall (STRING) = TopWall

### LeftWall  [MESH]  pos=(-83.31, -7.04, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(2.31, 82.00, 24.36)
mesh "Cube.003": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop SCORE2 (INT) = 0
- SENSOR COLLISION "Collision" -> [And]: use_tap=True, controllers=(bpy.data.objects['LeftWall']...AndController,), use_material=True, material=Ball
- CONTROLLER LOGIC_AND "And" -> [Score1, Property]
- ACTUATOR MESSAGE "Score1": to_property=Score2, subject=1up, body_type=TEXT, body_message=1, body_property=1
- ACTUATOR PROPERTY "Property": mode=ADD, property=SCORE2, value=1, object_property=1

### BottomWall  [MESH]  pos=(0.18, -48.92, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(170.00, 2.26, 24.36)
mesh "Cube.006": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop BottomWall (STRING) = BottomWall

### CENTER  [EMPTY]  pos=(0.00, -4.41, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(0.00, 0.00, 0.00)
physics: NO_COLLISION mass=1.0

### Left_Paddle  [MESH]  pos=(-74.04, -4.00, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 12.00, 16.17)
mesh "Cube.001": 8 verts 6 faces colour=#CCCCCC
physics: DYNAMIC mass=100.0
- prop LeftPaddle (STRING) = LeftPaddle
- SENSOR KEYBOARD "UP" -> [And]: controllers=(bpy.data.objects['Left_Paddle']...AndController,), key=W, modifier_key_1=NONE, modifier_key_2=NONE
- SENSOR KEYBOARD "DOWN" -> [And.001]: use_pulse_true_level=True, controllers=(bpy.data.objects['Left_Paddle']...AndController,), key=S, modifier_key_1=NONE, modifier_key_2=NONE
- CONTROLLER LOGIC_AND "And" -> [up]
- CONTROLLER LOGIC_AND "And.001" -> [down]
- ACTUATOR MOTION "up": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_y=1.0, offset_location=(0.0, 1.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "down": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_y=-1.0, offset_location=(0.0, -1.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True

### Sphere  [MESH]  pos=(0.00, -4.00, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 2.00)
mesh "Sphere": 482 verts 512 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop Direction (BOOL) = False
- prop Play (BOOL) = False
- prop DirY (INT) = 0
- SENSOR KEYBOARD "SPACE" -> [START, STOP]: use_tap=True, controllers=(bpy.data.objects['Sphere']...AndController, bpy.data.objects['Sphere']...AndController), key=SPACE, modifier_key_1=NONE, modifier_key_2=NONE
- SENSOR PROPERTY "STOPPED" -> [START]: controllers=(bpy.data.objects['Sphere']...AndController,), evaluation_type=PROPEQUAL, property=Play, value=FALSE, value_min=FALSE
- SENSOR PROPERTY "PLAYING" -> [STOP, LEFT, HITTOP]: controllers=(bpy.data.objects['Sphere']...AndController, bpy.data.objects['Sphere']...AndController, bpy.data.objects['Sphere']...AndController), evaluation_type=PROPEQUAL, property=Play, value=TRUE, value_min=TRUE
- SENSOR PROPERTY "RIGHT" -> [RIGHT]: use_tap=True, controllers=(bpy.data.objects['Sphere']...AndController,), evaluation_type=PROPEQUAL, property=Direction, value=TRUE, value_min=TRUE
- SENSOR PROPERTY "LEFT" -> [LEFT]: use_pulse_true_level=True, use_tap=True, controllers=(bpy.data.objects['Sphere']...AndController,), evaluation_type=PROPEQUAL, property=Direction, value=FALSE, value_min=FALSE
- SENSOR COLLISION "HitTop" -> [HITTOP]: controllers=(bpy.data.objects['Sphere']...AndController,), property=TopWall
- SENSOR COLLISION "HitBottom" -> [HITBOTTOM]: controllers=(bpy.data.objects['Sphere']...AndController,), property=BottomWall
- SENSOR COLLISION "LeftPaddle" -> [LEFTPADDLE]: controllers=(bpy.data.objects['Sphere']...AndController,), property=LeftPaddle
- SENSOR COLLISION "RightPaddle" -> [RIGHTPADDLE]: controllers=(bpy.data.objects['Sphere']...AndController,), property=RightPaddle
- SENSOR PROPERTY "DirY-1" -> [DIRY-1]: use_tap=True, controllers=(bpy.data.objects['Sphere']...AndController,), evaluation_type=PROPEQUAL, property=DirY, value=-1, value_min=-1
- SENSOR PROPERTY "DirY1" -> [DIRY1]: use_tap=True, controllers=(bpy.data.objects['Sphere']...AndController,), evaluation_type=PROPEQUAL, property=DirY, value=1, value_min=1
- SENSOR PROPERTY "DirY-2" -> [DIRY-2]: use_tap=True, controllers=(bpy.data.objects['Sphere']...AndController,), evaluation_type=PROPEQUAL, property=DirY, value=-2, value_min=-2
- SENSOR PROPERTY "DirY2" -> [DIRY2]: use_tap=True, controllers=(bpy.data.objects['Sphere']...AndController,), evaluation_type=PROPEQUAL, property=DirY, value=2, value_min=2
- CONTROLLER LOGIC_AND "START" -> [Direction, START]
- CONTROLLER LOGIC_AND "STOP" -> [STOP]
- CONTROLLER LOGIC_AND "RIGHT" -> [RIGHT]
- CONTROLLER LOGIC_AND "LEFT" -> [LEFT]
- CONTROLLER LOGIC_AND "HITTOP" -> [ANGLE]
- CONTROLLER LOGIC_AND "HITBOTTOM" -> [ANGLE]
- CONTROLLER LOGIC_AND "LEFTPADDLE" -> [ANGLE, LeftBoost]
- CONTROLLER LOGIC_AND "RIGHTPADDLE" -> [RightBoost, ANGLE]
- CONTROLLER LOGIC_AND "DIRY-1" -> [DirY-1]
- CONTROLLER LOGIC_AND "DIRY1" -> [DirY1]
- CONTROLLER LOGIC_AND "DIRY-2" -> [DirY-2]
- CONTROLLER LOGIC_AND "DIRY2" -> [DirY2]
- ACTUATOR RANDOM "Direction": seed=1766, property=Direction, distribution=BOOL_UNIFORM, chance=0.1, int_mean=0.1, float_value=0.1, float_min=0.1, float_mean=0.1, half_life_time=0.1
- ACTUATOR PROPERTY "START": mode=ASSIGN, property=Play, value=TRUE, object_property=TRUE
- ACTUATOR SCENE "STOP": mode=RESTART
- ACTUATOR MOTION "RIGHT": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, offset_location=(0.0, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(40.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_local_linear_velocity=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "LEFT": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, offset_location=(0.0, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(-40.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_local_linear_velocity=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR RANDOM "ANGLE": property=DirY, distribution=INT_UNIFORM, chance=0.1, int_value=-2, int_min=-2, int_max=2, int_mean=0.1, float_value=0.1, float_min=0.1, float_mean=0.1, half_life_time=0.1
- ACTUATOR MOTION "LeftBoost": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, offset_location=(0.0, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(2.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_local_linear_velocity=True, use_add_linear_velocity=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "RightBoost": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, offset_location=(0.0, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(-2.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_local_linear_velocity=True, use_add_linear_velocity=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "DirY-1": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, offset_location=(0.0, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, -10.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_local_linear_velocity=True, use_local_angular_velocity=True, use_add_linear_velocity=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "DirY1": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, offset_location=(0.0, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 10.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_local_linear_velocity=True, use_local_angular_velocity=True, use_add_linear_velocity=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "DirY-2": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, offset_location=(0.0, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, -20.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_local_linear_velocity=True, use_add_linear_velocity=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "DirY2": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, offset_location=(0.0, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 20.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_local_linear_velocity=True, use_add_linear_velocity=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True

### Right_Paddel  [MESH]  pos=(73.16, -4.00, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 12.00, 16.17)
mesh "Cube.002": 8 verts 6 faces colour=#CCCCCC
physics: DYNAMIC mass=100.0
- prop RightPaddle (STRING) = RightPaddle
- SENSOR KEYBOARD "Up" -> [And]: controllers=(bpy.data.objects['Right_Paddel']...AndController,), key=UP_ARROW, modifier_key_1=NONE, modifier_key_2=NONE
- SENSOR KEYBOARD "Down" -> [And.001]: controllers=(bpy.data.objects['Right_Paddel']...AndController,), key=DOWN_ARROW, modifier_key_1=NONE, modifier_key_2=NONE
- CONTROLLER LOGIC_AND "And" -> [up]
- CONTROLLER LOGIC_AND "And.001" -> [down]
- ACTUATOR MOTION "up": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_y=1.0, offset_location=(0.0, 1.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "down": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_y=-1.0, offset_location=(0.0, -1.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True

### Score1  [FONT]  pos=(-69.39, 36.81, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(4.40, 7.00, 0.00)
text: "0"
physics: NO_COLLISION mass=1.0
- prop SCORE1 (INT) = 0
- prop Text (STRING) = 
- SENSOR MESSAGE "Message" -> [And]: controllers=(bpy.data.objects['Score1']...AndController,), subject=1up
- SENSOR PROPERTY "Property.001" -> [And.001]: controllers=(bpy.data.objects['Score1']...AndController,), evaluation_type=PROPCHANGED, property=SCORE1
- CONTROLLER LOGIC_AND "And" -> [Property]
- CONTROLLER LOGIC_AND "And.001" -> [Property.001]
- ACTUATOR PROPERTY "Property": mode=ADD, property=SCORE1, value=1, object_property=1
- ACTUATOR PROPERTY "Property.001": mode=COPY, property=Text, value=Score1, object=obj:RightWall, object_property=Score1

### Score2  [FONT]  pos=(64.66, 36.81, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(4.40, 7.00, 0.00)
text: "0"
physics: NO_COLLISION mass=1.0
- prop SCORE2 (INT) = 0
- prop Text (STRING) = 
- SENSOR MESSAGE "Message" -> [And]: controllers=(bpy.data.objects['Score2']...AndController,), subject=1up
- SENSOR PROPERTY "Property.001" -> [And.001]: controllers=(bpy.data.objects['Score2']...AndController,), evaluation_type=PROPCHANGED, property=SCORE2
- CONTROLLER LOGIC_AND "And" -> [Property]
- CONTROLLER LOGIC_AND "And.001" -> [Property.001]
- ACTUATOR PROPERTY "Property": mode=ADD, property=SCORE2, value=1, object_property=1
- ACTUATOR PROPERTY "Property.001": mode=COPY, property=Text, value=SCORE2, object=obj:LeftWall, object_property=SCORE2

### Instructions  [FONT]  pos=(-35.14, 37.97, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(64.68, 7.00, 0.00)
text: "Press Space To Begin"
physics: NO_COLLISION mass=1.0
- prop PLAY (BOOL) = False
- prop Text (STRING) = 
- SENSOR KEYBOARD "SPACE" -> [And, And.001, And.003, And.002]: use_tap=True, controllers=(bpy.data.objects['Instructions']...AndController, bpy.data.objects['Instructions']...AndController, bpy.data.objects['Instructions']...AndController, bpy.data.objects['Instructions']...AndController), key=SPACE, modifier_key_1=NONE, modifier_key_2=NONE
- SENSOR PROPERTY "START" -> [And, And.003]: controllers=(bpy.data.objects['Instructions']...AndController, bpy.data.objects['Instructions']...AndController), evaluation_type=PROPEQUAL, property=PLAY, value=FALSE, value_min=FALSE
- SENSOR PROPERTY "STOP" -> [And.001, And.002]: controllers=(bpy.data.objects['Instructions']...AndController, bpy.data.objects['Instructions']...AndController), evaluation_type=PROPEQUAL, property=PLAY, value=TRUE, value_min=TRUE
- CONTROLLER LOGIC_AND "And" -> [START]
- CONTROLLER LOGIC_AND "And.001" -> [STOP]
- CONTROLLER LOGIC_AND "And.003" -> [Clear]
- CONTROLLER LOGIC_AND "And.002" -> [Instruct]
- ACTUATOR PROPERTY "START": mode=ASSIGN, property=PLAY, value=TRUE, object_property=TRUE
- ACTUATOR PROPERTY "STOP": mode=ASSIGN, property=PLAY, value=FALSE, object_property=FALSE
- ACTUATOR MOTION "Clear": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_y=40.0, offset_location=(0.0, 40.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "Instruct": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_y=-40.0, offset_location=(0.0, -40.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True

## text blocks
### Text  (6 lines)
```
W & S for left player movement
Arrow UP & DOWN for right player movement

Space to start the ball

P key to start the game
```