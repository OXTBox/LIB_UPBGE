# breakout_like.blend

## scene "Scene"  camera=Camera
game: fps=60 physics=BULLET gravity=0.0

### Camera  [CAMERA]  pos=(0.07, -2.92, 100.00) rot_deg=(0.00, 0.00, 0.00) size=(0.00, 0.00, 0.00)
camera: lens=50.0 type=ORTHO ortho_scale=169.51
physics: STATIC mass=1.0
- prop SCORE2 (FLOAT) = 0.0

### Light  [LIGHT]  pos=(-46.48, 13.73, 34.58) rot_deg=(37.26, 3.16, 106.94) size=(0.00, 0.00, 0.00)
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

### Floor  [MESH]  pos=(-0.02, -7.64, -0.66) rot_deg=(0.00, 0.00, 0.00) size=(170.00, 81.22, 1.33)
mesh "Cube.007": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop Floor (STRING) = TopWall

### Left_Paddle  [MESH]  pos=(-74.04, -4.00, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 12.00, 16.17) (hidden)
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
- prop VelY (FLOAT) = 0.0
- prop Score (INT) = 0
- SENSOR KEYBOARD "SPACE" -> [START, STOP]: use_tap=True, controllers=(bpy.data.objects['Sphere']...AndController, bpy.data.objects['Sphere']...AndController), key=SPACE, modifier_key_1=NONE, modifier_key_2=NONE
- SENSOR PROPERTY "STOPPED" -> [START]: controllers=(bpy.data.objects['Sphere']...AndController,), evaluation_type=PROPEQUAL, property=Play, value=FALSE, value_min=FALSE
- SENSOR PROPERTY "PLAYING" -> [STOP, LEFT, HITTOP]: controllers=(bpy.data.objects['Sphere']...AndController, bpy.data.objects['Sphere']...AndController, bpy.data.objects['Sphere']...AndController), evaluation_type=PROPEQUAL, property=Play, value=True, value_min=True
- SENSOR PROPERTY "DOWN" -> [RIGHT]: use_tap=True, controllers=(bpy.data.objects['Sphere']...AndController,), evaluation_type=PROPEQUAL, property=Direction, value=True, value_min=True
- SENSOR PROPERTY "UP" -> [LEFT]: use_pulse_true_level=True, use_tap=True, controllers=(bpy.data.objects['Sphere']...AndController,), evaluation_type=PROPEQUAL, property=Direction, value=False, value_min=False
- SENSOR COLLISION "HitTop" -> [HITTOP]: controllers=(bpy.data.objects['Sphere']...AndController,), property=TopWall
- SENSOR COLLISION "HitBottom" -> [HITBOTTOM]: controllers=(bpy.data.objects['Sphere']...PythonController,), property=BottomWall
- SENSOR COLLISION "LeftPaddle" -> [LEFTPADDLE]: controllers=(bpy.data.objects['Sphere']...AndController,), property=LeftPaddle
- SENSOR COLLISION "RightPaddle" -> [RIGHTPADDLE]: controllers=(bpy.data.objects['Sphere']...AndController,), property=RightPaddle
- SENSOR PROPERTY "DirY-1" -> [DIRY-1]: use_tap=True, controllers=(bpy.data.objects['Sphere']...AndController,), evaluation_type=PROPEQUAL, property=DirY, value=-1, value_min=-1
- SENSOR PROPERTY "DirY1" -> [DIRY1]: use_tap=True, controllers=(bpy.data.objects['Sphere']...AndController,), evaluation_type=PROPEQUAL, property=DirY, value=1, value_min=1
- SENSOR PROPERTY "DirY-2" -> [DIRY-2]: use_tap=True, controllers=(bpy.data.objects['Sphere']...AndController,), evaluation_type=PROPEQUAL, property=DirY, value=-2, value_min=-2
- SENSOR PROPERTY "DirY2" -> [DIRY2]: use_tap=True, controllers=(bpy.data.objects['Sphere']...AndController,), evaluation_type=PROPEQUAL, property=DirY, value=2, value_min=2
- SENSOR NEAR "near" -> [Python]: invert=True, use_pulse_true_level=True, controllers=(bpy.data.objects['Sphere']...PythonController,), property=LeftPaddle, distance=0.5, reset_distance=1.0
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['Sphere']...AndController,), property=Brick
- CONTROLLER LOGIC_AND "START" -> [Direction, START]
- CONTROLLER LOGIC_AND "STOP" -> [STOP]
- CONTROLLER LOGIC_AND "RIGHT" -> [DOWN]
- CONTROLLER LOGIC_AND "LEFT" -> [UP]
- CONTROLLER LOGIC_AND "HITTOP" -> [ANGLE]
- CONTROLLER PYTHON "HITBOTTOM" script=BallReset.py -> [DirectioNT]
- CONTROLLER LOGIC_AND "LEFTPADDLE" -> [ANGLE, LeftBoost]
- CONTROLLER LOGIC_AND "RIGHTPADDLE" -> [RightBoost, ANGLE]
- CONTROLLER LOGIC_AND "DIRY-1" -> [DirY-1]
- CONTROLLER LOGIC_AND "DIRY1" -> [DirY1]
- CONTROLLER LOGIC_AND "DIRY-2" -> [DirY-2]
- CONTROLLER LOGIC_AND "DIRY2" -> [DirY2]
- CONTROLLER PYTHON "Python" script=fix_ball.check_vel -> []
- CONTROLLER LOGIC_AND "And" -> [Property, Message]
- ACTUATOR RANDOM "Direction": seed=2081, property=Direction, distribution=BOOL_UNIFORM, chance=0.1, int_mean=0.1, float_value=0.1, float_min=0.1, float_mean=0.1, half_life_time=0.1
- ACTUATOR PROPERTY "START": mode=ASSIGN, property=Play, value=True, object_property=True
- ACTUATOR SCENE "STOP": mode=RESTART
- ACTUATOR MOTION "DOWN": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, offset_location=(0.0, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, -40.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_local_linear_velocity=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "UP": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, offset_location=(0.0, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 40.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_local_linear_velocity=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR PROPERTY "DirectioNT": mode=ASSIGN, property=Direction, value=True, object_property=True
- ACTUATOR RANDOM "ANGLE": property=DirY, distribution=INT_UNIFORM, chance=0.1, int_value=-2, int_min=-2, int_max=2, int_mean=0.1, float_value=0.1, float_min=0.1, float_mean=0.1, half_life_time=0.1
- ACTUATOR MOTION "LeftBoost": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, offset_location=(0.0, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(4.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_local_linear_velocity=True, use_add_linear_velocity=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "RightBoost": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, offset_location=(0.0, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(-4.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_local_linear_velocity=True, use_add_linear_velocity=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "DirY-1": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, offset_location=(0.0, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, -40.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_local_linear_velocity=True, use_local_angular_velocity=True, use_add_linear_velocity=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "DirY1": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, offset_location=(0.0, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 40.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_local_linear_velocity=True, use_local_angular_velocity=True, use_add_linear_velocity=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "DirY-2": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, offset_location=(0.0, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, -50.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_local_linear_velocity=True, use_add_linear_velocity=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "DirY2": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, offset_location=(0.0, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 50.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_local_linear_velocity=True, use_add_linear_velocity=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR PROPERTY "Property": mode=ADD, property=Score, value=10, object_property=10
- ACTUATOR MESSAGE "Message": to_property=Score1, subject=Score, body_type=TEXT, body_message=Score, body_property=Score

### Right_Paddel  [MESH]  pos=(73.16, -4.00, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 12.00, 16.17) (hidden)
mesh "Cube.002": 8 verts 6 faces colour=#CCCCCC
physics: DYNAMIC mass=100.0
- prop RightPaddle (STRING) = RightPaddle
- SENSOR KEYBOARD "Up" -> [And]: controllers=(bpy.data.objects['Right_Paddel']...AndController,), key=UP_ARROW, modifier_key_1=NONE, modifier_key_2=NONE
- SENSOR KEYBOARD "Down" -> [And.001]: controllers=(bpy.data.objects['Right_Paddel']...AndController,), key=DOWN_ARROW, modifier_key_1=NONE, modifier_key_2=NONE
- CONTROLLER LOGIC_AND "And" -> [up]
- CONTROLLER LOGIC_AND "And.001" -> [down]
- ACTUATOR MOTION "up": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_y=1.0, offset_location=(0.0, 1.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "down": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_y=-1.0, offset_location=(0.0, -1.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True

### Score1  [FONT]  pos=(0.00, 36.81, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(4.40, 7.00, 0.00)
text: "0"
physics: NO_COLLISION mass=1.0
- prop SCORE1 (INT) = 0
- prop Text (STRING) = 
- SENSOR MESSAGE "Message" -> [And]: controllers=(bpy.data.objects['Score1']...AndController,), subject=Score
- SENSOR PROPERTY "Property.001" -> [And.001]: controllers=(bpy.data.objects['Score1']...AndController,), evaluation_type=PROPGREATERTHAN, property=SCORE1, value=0, value_min=0
- SENSOR PROPERTY "Property" -> [And.002]: controllers=(bpy.data.objects['Score1']...AndController,), evaluation_type=PROPLESSTHAN, property=SCORE1, value=1, value_min=1
- CONTROLLER LOGIC_AND "And" -> [SCORE+1, Edit Object]
- CONTROLLER LOGIC_AND "And.001" -> [Show]
- CONTROLLER LOGIC_AND "And.002" -> [Hide]
- ACTUATOR PROPERTY "SCORE+1": mode=COPY, property=SCORE1, value=Score, object=obj:Sphere, object_property=Score
- ACTUATOR PROPERTY "Edit Object": mode=COPY, property=Text, value=Score, object=obj:Sphere, object_property=Score
- ACTUATOR VISIBILITY "Show": use_visible=True
- ACTUATOR VISIBILITY "Hide": 

### Score2  [FONT]  pos=(64.66, 36.81, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(4.40, 7.00, 0.00) (hidden)
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

### Paddle  [MESH]  pos=(0.00, -40.00, 5.00) rot_deg=(0.00, 0.00, 0.00) size=(26.69, 2.00, 16.88)
mesh "Cube.008": 8 verts 6 faces colour=#CCCCCC
physics: DYNAMIC mass=100.0
- prop LeftPaddle (STRING) = LeftPaddle
- prop x (FLOAT) = 0.0
- prop y (FLOAT) = 0.0
- prop z (FLOAT) = 0.0
- prop mx (FLOAT) = 0.0
- prop my (FLOAT) = 0.0
- SENSOR KEYBOARD "UP" -> [And]: controllers=(bpy.data.objects['Paddle']...AndController,), key=A, modifier_key_1=NONE, modifier_key_2=NONE
- SENSOR KEYBOARD "DOWN" -> [And.001]: use_pulse_true_level=True, controllers=(bpy.data.objects['Paddle']...AndController,), key=D, modifier_key_1=NONE, modifier_key_2=NONE
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['Paddle']...PythonController,), mouse_event=MOUSEOVERANY, use_material=PROPERTY, property=Floor, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER LOGIC_AND "And" -> [LEFT]
- CONTROLLER LOGIC_AND "And.001" -> [RIGHT]
- CONTROLLER PYTHON "Python" script=MousePaddle_L_R.main -> []
- ACTUATOR MOTION "LEFT": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_x=-1.0, force_max_z=-0.1, offset_location=(-1.0, 0.0, -0.1), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "RIGHT": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_x=1.0, offset_location=(1.0, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True

### Brick  [MESH]  pos=(-50.16, 9.21, 0.00) rot_deg=(0.00, -0.00, 0.00) size=(9.14, 3.21, 14.95)
mesh "Cube.009": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop Brick (BOOL) = False
- prop HitCount (INT) = 0
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['Brick']...AndController,), use_material=True, material=Ball
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Brick']...AndController,), evaluation_type=PROPGREATERTHAN, property=HitCount, value=2, value_min=2
- CONTROLLER LOGIC_AND "And" -> [HIT]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- ACTUATOR PROPERTY "HIT": mode=ADD, property=HitCount, value=1, object_property=1
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### Brick.001  [MESH]  pos=(-40.16, 9.21, 0.00) rot_deg=(0.00, -0.00, 0.00) size=(9.14, 3.21, 14.95)
mesh "Cube.065": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop Brick (BOOL) = False
- prop HitCount (INT) = 0
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['Brick.001']...AndController,), use_material=True, material=Ball
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Brick.001']...AndController,), evaluation_type=PROPGREATERTHAN, property=HitCount, value=2, value_min=2
- CONTROLLER LOGIC_AND "And" -> [HIT]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- ACTUATOR PROPERTY "HIT": mode=ADD, property=HitCount, value=1, object_property=1
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### Brick.002  [MESH]  pos=(-30.16, 9.21, 0.00) rot_deg=(0.00, -0.00, 0.00) size=(9.14, 3.21, 14.95)
mesh "Cube.066": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop Brick (BOOL) = False
- prop HitCount (INT) = 0
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['Brick.002']...AndController,), use_material=True, material=Ball
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Brick.002']...AndController,), evaluation_type=PROPGREATERTHAN, property=HitCount, value=2, value_min=2
- CONTROLLER LOGIC_AND "And" -> [HIT]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- ACTUATOR PROPERTY "HIT": mode=ADD, property=HitCount, value=1, object_property=1
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### Brick.003  [MESH]  pos=(-20.16, 9.21, 0.00) rot_deg=(0.00, -0.00, 0.00) size=(9.14, 3.21, 14.95)
mesh "Cube.067": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop Brick (BOOL) = False
- prop HitCount (INT) = 0
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['Brick.003']...AndController,), use_material=True, material=Ball
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Brick.003']...AndController,), evaluation_type=PROPGREATERTHAN, property=HitCount, value=2, value_min=2
- CONTROLLER LOGIC_AND "And" -> [HIT]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- ACTUATOR PROPERTY "HIT": mode=ADD, property=HitCount, value=1, object_property=1
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### Brick.004  [MESH]  pos=(-10.16, 9.21, 0.00) rot_deg=(0.00, -0.00, 0.00) size=(9.14, 3.21, 14.95)
mesh "Cube.068": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop Brick (BOOL) = False
- prop HitCount (INT) = 0
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['Brick.004']...AndController,), use_material=True, material=Ball
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Brick.004']...AndController,), evaluation_type=PROPGREATERTHAN, property=HitCount, value=2, value_min=2
- CONTROLLER LOGIC_AND "And" -> [HIT]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- ACTUATOR PROPERTY "HIT": mode=ADD, property=HitCount, value=1, object_property=1
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### Brick.005  [MESH]  pos=(-50.16, 13.73, 0.00) rot_deg=(0.00, -0.00, 0.00) size=(9.14, 3.21, 14.95)
mesh "Cube.069": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop Brick (BOOL) = False
- prop HitCount (INT) = 0
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['Brick.005']...AndController,), use_material=True, material=Ball
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Brick.005']...AndController,), evaluation_type=PROPGREATERTHAN, property=HitCount, value=2, value_min=2
- CONTROLLER LOGIC_AND "And" -> [HIT]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- ACTUATOR PROPERTY "HIT": mode=ADD, property=HitCount, value=1, object_property=1
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### Brick.006  [MESH]  pos=(-40.16, 13.73, 0.00) rot_deg=(0.00, -0.00, 0.00) size=(9.14, 3.21, 14.95)
mesh "Cube.070": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop Brick (BOOL) = False
- prop HitCount (INT) = 0
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['Brick.006']...AndController,), use_material=True, material=Ball
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Brick.006']...AndController,), evaluation_type=PROPGREATERTHAN, property=HitCount, value=2, value_min=2
- CONTROLLER LOGIC_AND "And" -> [HIT]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- ACTUATOR PROPERTY "HIT": mode=ADD, property=HitCount, value=1, object_property=1
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### Brick.007  [MESH]  pos=(-30.16, 13.73, 0.00) rot_deg=(0.00, -0.00, 0.00) size=(9.14, 3.21, 14.95)
mesh "Cube.071": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop Brick (BOOL) = False
- prop HitCount (INT) = 0
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['Brick.007']...AndController,), use_material=True, material=Ball
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Brick.007']...AndController,), evaluation_type=PROPGREATERTHAN, property=HitCount, value=2, value_min=2
- CONTROLLER LOGIC_AND "And" -> [HIT]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- ACTUATOR PROPERTY "HIT": mode=ADD, property=HitCount, value=1, object_property=1
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### Brick.008  [MESH]  pos=(-20.16, 13.73, 0.00) rot_deg=(0.00, -0.00, 0.00) size=(9.14, 3.21, 14.95)
mesh "Cube.072": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop Brick (BOOL) = False
- prop HitCount (INT) = 0
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['Brick.008']...AndController,), use_material=True, material=Ball
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Brick.008']...AndController,), evaluation_type=PROPGREATERTHAN, property=HitCount, value=2, value_min=2
- CONTROLLER LOGIC_AND "And" -> [HIT]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- ACTUATOR PROPERTY "HIT": mode=ADD, property=HitCount, value=1, object_property=1
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### Brick.009  [MESH]  pos=(-10.16, 13.73, 0.00) rot_deg=(0.00, -0.00, 0.00) size=(9.14, 3.21, 14.95)
mesh "Cube.073": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop Brick (BOOL) = False
- prop HitCount (INT) = 0
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['Brick.009']...AndController,), use_material=True, material=Ball
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Brick.009']...AndController,), evaluation_type=PROPGREATERTHAN, property=HitCount, value=2, value_min=2
- CONTROLLER LOGIC_AND "And" -> [HIT]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- ACTUATOR PROPERTY "HIT": mode=ADD, property=HitCount, value=1, object_property=1
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### Brick.010  [MESH]  pos=(0.00, 9.21, 0.00) rot_deg=(0.00, -0.00, 0.00) size=(9.14, 3.21, 14.95)
mesh "Cube.074": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop Brick (BOOL) = False
- prop HitCount (INT) = 0
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['Brick.010']...AndController,), use_material=True, material=Ball
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Brick.010']...AndController,), evaluation_type=PROPGREATERTHAN, property=HitCount, value=2, value_min=2
- CONTROLLER LOGIC_AND "And" -> [HIT]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- ACTUATOR PROPERTY "HIT": mode=ADD, property=HitCount, value=1, object_property=1
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### Brick.011  [MESH]  pos=(10.00, 9.21, 0.00) rot_deg=(0.00, -0.00, 0.00) size=(9.14, 3.21, 14.95)
mesh "Cube.075": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop Brick (BOOL) = False
- prop HitCount (INT) = 0
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['Brick.011']...AndController,), use_material=True, material=Ball
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Brick.011']...AndController,), evaluation_type=PROPGREATERTHAN, property=HitCount, value=2, value_min=2
- CONTROLLER LOGIC_AND "And" -> [HIT]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- ACTUATOR PROPERTY "HIT": mode=ADD, property=HitCount, value=1, object_property=1
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### Brick.012  [MESH]  pos=(20.00, 9.21, 0.00) rot_deg=(0.00, -0.00, 0.00) size=(9.14, 3.21, 14.95)
mesh "Cube.076": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop Brick (BOOL) = False
- prop HitCount (INT) = 0
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['Brick.012']...AndController,), use_material=True, material=Ball
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Brick.012']...AndController,), evaluation_type=PROPGREATERTHAN, property=HitCount, value=2, value_min=2
- CONTROLLER LOGIC_AND "And" -> [HIT]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- ACTUATOR PROPERTY "HIT": mode=ADD, property=HitCount, value=1, object_property=1
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### Brick.013  [MESH]  pos=(30.00, 9.21, 0.00) rot_deg=(0.00, -0.00, 0.00) size=(9.14, 3.21, 14.95)
mesh "Cube.077": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop Brick (BOOL) = False
- prop HitCount (INT) = 0
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['Brick.013']...AndController,), use_material=True, material=Ball
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Brick.013']...AndController,), evaluation_type=PROPGREATERTHAN, property=HitCount, value=2, value_min=2
- CONTROLLER LOGIC_AND "And" -> [HIT]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- ACTUATOR PROPERTY "HIT": mode=ADD, property=HitCount, value=1, object_property=1
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### Brick.014  [MESH]  pos=(40.00, 9.21, 0.00) rot_deg=(0.00, -0.00, 0.00) size=(9.14, 3.21, 14.95)
mesh "Cube.078": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop Brick (BOOL) = False
- prop HitCount (INT) = 0
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['Brick.014']...AndController,), use_material=True, material=Ball
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Brick.014']...AndController,), evaluation_type=PROPGREATERTHAN, property=HitCount, value=2, value_min=2
- CONTROLLER LOGIC_AND "And" -> [HIT]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- ACTUATOR PROPERTY "HIT": mode=ADD, property=HitCount, value=1, object_property=1
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### Brick.015  [MESH]  pos=(0.00, 13.73, 0.00) rot_deg=(0.00, -0.00, 0.00) size=(9.14, 3.21, 14.95)
mesh "Cube.079": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop Brick (BOOL) = False
- prop HitCount (INT) = 0
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['Brick.015']...AndController,), use_material=True, material=Ball
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Brick.015']...AndController,), evaluation_type=PROPGREATERTHAN, property=HitCount, value=2, value_min=2
- CONTROLLER LOGIC_AND "And" -> [HIT]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- ACTUATOR PROPERTY "HIT": mode=ADD, property=HitCount, value=1, object_property=1
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### Brick.016  [MESH]  pos=(10.00, 13.73, 0.00) rot_deg=(0.00, -0.00, 0.00) size=(9.14, 3.21, 14.95)
mesh "Cube.080": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop Brick (BOOL) = False
- prop HitCount (INT) = 0
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['Brick.016']...AndController,), use_material=True, material=Ball
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Brick.016']...AndController,), evaluation_type=PROPGREATERTHAN, property=HitCount, value=2, value_min=2
- CONTROLLER LOGIC_AND "And" -> [HIT]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- ACTUATOR PROPERTY "HIT": mode=ADD, property=HitCount, value=1, object_property=1
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### Brick.017  [MESH]  pos=(20.00, 13.73, 0.00) rot_deg=(0.00, -0.00, 0.00) size=(9.14, 3.21, 14.95)
mesh "Cube.081": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop Brick (BOOL) = False
- prop HitCount (INT) = 0
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['Brick.017']...AndController,), use_material=True, material=Ball
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Brick.017']...AndController,), evaluation_type=PROPGREATERTHAN, property=HitCount, value=2, value_min=2
- CONTROLLER LOGIC_AND "And" -> [HIT]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- ACTUATOR PROPERTY "HIT": mode=ADD, property=HitCount, value=1, object_property=1
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### Brick.018  [MESH]  pos=(30.00, 13.73, 0.00) rot_deg=(0.00, -0.00, 0.00) size=(9.14, 3.21, 14.95)
mesh "Cube.082": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop Brick (BOOL) = False
- prop HitCount (INT) = 0
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['Brick.018']...AndController,), use_material=True, material=Ball
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Brick.018']...AndController,), evaluation_type=PROPGREATERTHAN, property=HitCount, value=2, value_min=2
- CONTROLLER LOGIC_AND "And" -> [HIT]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- ACTUATOR PROPERTY "HIT": mode=ADD, property=HitCount, value=1, object_property=1
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### Brick.019  [MESH]  pos=(40.00, 13.73, 0.00) rot_deg=(0.00, -0.00, 0.00) size=(9.14, 3.21, 14.95)
mesh "Cube.083": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop Brick (BOOL) = False
- prop HitCount (INT) = 0
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['Brick.019']...AndController,), use_material=True, material=Ball
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Brick.019']...AndController,), evaluation_type=PROPGREATERTHAN, property=HitCount, value=2, value_min=2
- CONTROLLER LOGIC_AND "And" -> [HIT]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- ACTUATOR PROPERTY "HIT": mode=ADD, property=HitCount, value=1, object_property=1
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### Brick.020  [MESH]  pos=(50.24, 13.73, 0.00) rot_deg=(0.00, -0.00, 0.00) size=(9.14, 3.21, 14.95)
mesh "Cube.084": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop Brick (BOOL) = False
- prop HitCount (INT) = 0
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['Brick.020']...AndController,), use_material=True, material=Ball
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Brick.020']...AndController,), evaluation_type=PROPGREATERTHAN, property=HitCount, value=2, value_min=2
- CONTROLLER LOGIC_AND "And" -> [HIT]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- ACTUATOR PROPERTY "HIT": mode=ADD, property=HitCount, value=1, object_property=1
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### Brick.021  [MESH]  pos=(60.24, 13.73, 0.00) rot_deg=(0.00, -0.00, 0.00) size=(9.14, 3.21, 14.95)
mesh "Cube.085": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop Brick (BOOL) = False
- prop HitCount (INT) = 0
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['Brick.021']...AndController,), use_material=True, material=Ball
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Brick.021']...AndController,), evaluation_type=PROPGREATERTHAN, property=HitCount, value=2, value_min=2
- CONTROLLER LOGIC_AND "And" -> [HIT]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- ACTUATOR PROPERTY "HIT": mode=ADD, property=HitCount, value=1, object_property=1
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### Brick.022  [MESH]  pos=(50.24, 9.21, 0.00) rot_deg=(0.00, -0.00, 0.00) size=(9.14, 3.21, 14.95)
mesh "Cube.086": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop Brick (BOOL) = False
- prop HitCount (INT) = 0
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['Brick.022']...AndController,), use_material=True, material=Ball
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Brick.022']...AndController,), evaluation_type=PROPGREATERTHAN, property=HitCount, value=2, value_min=2
- CONTROLLER LOGIC_AND "And" -> [HIT]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- ACTUATOR PROPERTY "HIT": mode=ADD, property=HitCount, value=1, object_property=1
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### Brick.023  [MESH]  pos=(60.24, 9.21, 0.00) rot_deg=(0.00, -0.00, 0.00) size=(9.14, 3.21, 14.95)
mesh "Cube.087": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop Brick (BOOL) = False
- prop HitCount (INT) = 0
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['Brick.023']...AndController,), use_material=True, material=Ball
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Brick.023']...AndController,), evaluation_type=PROPGREATERTHAN, property=HitCount, value=2, value_min=2
- CONTROLLER LOGIC_AND "And" -> [HIT]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- ACTUATOR PROPERTY "HIT": mode=ADD, property=HitCount, value=1, object_property=1
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### Brick.024  [MESH]  pos=(-50.16, 18.26, 0.00) rot_deg=(0.00, -0.00, 0.00) size=(9.14, 3.21, 14.95)
mesh "Cube.089": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop Brick (BOOL) = False
- prop HitCount (INT) = 0
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['Brick.024']...AndController,), use_material=True, material=Ball
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Brick.024']...AndController,), evaluation_type=PROPGREATERTHAN, property=HitCount, value=2, value_min=2
- CONTROLLER LOGIC_AND "And" -> [HIT]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- ACTUATOR PROPERTY "HIT": mode=ADD, property=HitCount, value=1, object_property=1
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### Brick.025  [MESH]  pos=(-40.16, 18.26, 0.00) rot_deg=(0.00, -0.00, 0.00) size=(9.14, 3.21, 14.95)
mesh "Cube.090": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop Brick (BOOL) = False
- prop HitCount (INT) = 0
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['Brick.025']...AndController,), use_material=True, material=Ball
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Brick.025']...AndController,), evaluation_type=PROPGREATERTHAN, property=HitCount, value=2, value_min=2
- CONTROLLER LOGIC_AND "And" -> [HIT]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- ACTUATOR PROPERTY "HIT": mode=ADD, property=HitCount, value=1, object_property=1
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### Brick.026  [MESH]  pos=(-30.16, 18.26, 0.00) rot_deg=(0.00, -0.00, 0.00) size=(9.14, 3.21, 14.95)
mesh "Cube.091": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop Brick (BOOL) = False
- prop HitCount (INT) = 0
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['Brick.026']...AndController,), use_material=True, material=Ball
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Brick.026']...AndController,), evaluation_type=PROPGREATERTHAN, property=HitCount, value=2, value_min=2
- CONTROLLER LOGIC_AND "And" -> [HIT]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- ACTUATOR PROPERTY "HIT": mode=ADD, property=HitCount, value=1, object_property=1
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### Brick.027  [MESH]  pos=(-20.16, 18.26, 0.00) rot_deg=(0.00, -0.00, 0.00) size=(9.14, 3.21, 14.95)
mesh "Cube.092": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop Brick (BOOL) = False
- prop HitCount (INT) = 0
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['Brick.027']...AndController,), use_material=True, material=Ball
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Brick.027']...AndController,), evaluation_type=PROPGREATERTHAN, property=HitCount, value=2, value_min=2
- CONTROLLER LOGIC_AND "And" -> [HIT]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- ACTUATOR PROPERTY "HIT": mode=ADD, property=HitCount, value=1, object_property=1
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### Brick.028  [MESH]  pos=(-10.16, 18.26, 0.00) rot_deg=(0.00, -0.00, 0.00) size=(9.14, 3.21, 14.95)
mesh "Cube.093": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop Brick (BOOL) = False
- prop HitCount (INT) = 0
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['Brick.028']...AndController,), use_material=True, material=Ball
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Brick.028']...AndController,), evaluation_type=PROPGREATERTHAN, property=HitCount, value=2, value_min=2
- CONTROLLER LOGIC_AND "And" -> [HIT]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- ACTUATOR PROPERTY "HIT": mode=ADD, property=HitCount, value=1, object_property=1
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### Brick.029  [MESH]  pos=(-50.16, 22.78, 0.00) rot_deg=(0.00, -0.00, 0.00) size=(9.14, 3.21, 14.95)
mesh "Cube.094": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop Brick (BOOL) = False
- prop HitCount (INT) = 0
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['Brick.029']...AndController,), use_material=True, material=Ball
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Brick.029']...AndController,), evaluation_type=PROPGREATERTHAN, property=HitCount, value=2, value_min=2
- CONTROLLER LOGIC_AND "And" -> [HIT]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- ACTUATOR PROPERTY "HIT": mode=ADD, property=HitCount, value=1, object_property=1
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### Brick.030  [MESH]  pos=(-40.16, 22.78, 0.00) rot_deg=(0.00, -0.00, 0.00) size=(9.14, 3.21, 14.95)
mesh "Cube.095": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop Brick (BOOL) = False
- prop HitCount (INT) = 0
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['Brick.030']...AndController,), use_material=True, material=Ball
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Brick.030']...AndController,), evaluation_type=PROPGREATERTHAN, property=HitCount, value=2, value_min=2
- CONTROLLER LOGIC_AND "And" -> [HIT]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- ACTUATOR PROPERTY "HIT": mode=ADD, property=HitCount, value=1, object_property=1
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### Brick.031  [MESH]  pos=(-30.16, 22.78, 0.00) rot_deg=(0.00, -0.00, 0.00) size=(9.14, 3.21, 14.95)
mesh "Cube.096": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop Brick (BOOL) = False
- prop HitCount (INT) = 0
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['Brick.031']...AndController,), use_material=True, material=Ball
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Brick.031']...AndController,), evaluation_type=PROPGREATERTHAN, property=HitCount, value=2, value_min=2
- CONTROLLER LOGIC_AND "And" -> [HIT]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- ACTUATOR PROPERTY "HIT": mode=ADD, property=HitCount, value=1, object_property=1
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### Brick.032  [MESH]  pos=(-20.16, 22.78, 0.00) rot_deg=(0.00, -0.00, 0.00) size=(9.14, 3.21, 14.95)
mesh "Cube.097": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop Brick (BOOL) = False
- prop HitCount (INT) = 0
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['Brick.032']...AndController,), use_material=True, material=Ball
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Brick.032']...AndController,), evaluation_type=PROPGREATERTHAN, property=HitCount, value=2, value_min=2
- CONTROLLER LOGIC_AND "And" -> [HIT]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- ACTUATOR PROPERTY "HIT": mode=ADD, property=HitCount, value=1, object_property=1
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### Brick.033  [MESH]  pos=(-10.16, 22.78, 0.00) rot_deg=(0.00, -0.00, 0.00) size=(9.14, 3.21, 14.95)
mesh "Cube.098": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop Brick (BOOL) = False
- prop HitCount (INT) = 0
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['Brick.033']...AndController,), use_material=True, material=Ball
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Brick.033']...AndController,), evaluation_type=PROPGREATERTHAN, property=HitCount, value=2, value_min=2
- CONTROLLER LOGIC_AND "And" -> [HIT]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- ACTUATOR PROPERTY "HIT": mode=ADD, property=HitCount, value=1, object_property=1
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### Brick.034  [MESH]  pos=(0.00, 18.26, 0.00) rot_deg=(0.00, -0.00, 0.00) size=(9.14, 3.21, 14.95)
mesh "Cube.099": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop Brick (BOOL) = False
- prop HitCount (INT) = 0
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['Brick.034']...AndController,), use_material=True, material=Ball
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Brick.034']...AndController,), evaluation_type=PROPGREATERTHAN, property=HitCount, value=2, value_min=2
- CONTROLLER LOGIC_AND "And" -> [HIT]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- ACTUATOR PROPERTY "HIT": mode=ADD, property=HitCount, value=1, object_property=1
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### Brick.035  [MESH]  pos=(10.00, 18.26, 0.00) rot_deg=(0.00, -0.00, 0.00) size=(9.14, 3.21, 14.95)
mesh "Cube.100": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop Brick (BOOL) = False
- prop HitCount (INT) = 0
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['Brick.035']...AndController,), use_material=True, material=Ball
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Brick.035']...AndController,), evaluation_type=PROPGREATERTHAN, property=HitCount, value=2, value_min=2
- CONTROLLER LOGIC_AND "And" -> [HIT]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- ACTUATOR PROPERTY "HIT": mode=ADD, property=HitCount, value=1, object_property=1
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### Brick.036  [MESH]  pos=(20.00, 18.26, 0.00) rot_deg=(0.00, -0.00, 0.00) size=(9.14, 3.21, 14.95)
mesh "Cube.101": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop Brick (BOOL) = False
- prop HitCount (INT) = 0
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['Brick.036']...AndController,), use_material=True, material=Ball
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Brick.036']...AndController,), evaluation_type=PROPGREATERTHAN, property=HitCount, value=2, value_min=2
- CONTROLLER LOGIC_AND "And" -> [HIT]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- ACTUATOR PROPERTY "HIT": mode=ADD, property=HitCount, value=1, object_property=1
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### Brick.037  [MESH]  pos=(30.00, 18.26, 0.00) rot_deg=(0.00, -0.00, 0.00) size=(9.14, 3.21, 14.95)
mesh "Cube.102": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop Brick (BOOL) = False
- prop HitCount (INT) = 0
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['Brick.037']...AndController,), use_material=True, material=Ball
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Brick.037']...AndController,), evaluation_type=PROPGREATERTHAN, property=HitCount, value=2, value_min=2
- CONTROLLER LOGIC_AND "And" -> [HIT]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- ACTUATOR PROPERTY "HIT": mode=ADD, property=HitCount, value=1, object_property=1
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### Brick.038  [MESH]  pos=(40.00, 18.26, 0.00) rot_deg=(0.00, -0.00, 0.00) size=(9.14, 3.21, 14.95)
mesh "Cube.103": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop Brick (BOOL) = False
- prop HitCount (INT) = 0
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['Brick.038']...AndController,), use_material=True, material=Ball
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Brick.038']...AndController,), evaluation_type=PROPGREATERTHAN, property=HitCount, value=2, value_min=2
- CONTROLLER LOGIC_AND "And" -> [HIT]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- ACTUATOR PROPERTY "HIT": mode=ADD, property=HitCount, value=1, object_property=1
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### Brick.039  [MESH]  pos=(0.00, 22.78, 0.00) rot_deg=(0.00, -0.00, 0.00) size=(9.14, 3.21, 14.95)
mesh "Cube.104": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop Brick (BOOL) = False
- prop HitCount (INT) = 0
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['Brick.039']...AndController,), use_material=True, material=Ball
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Brick.039']...AndController,), evaluation_type=PROPGREATERTHAN, property=HitCount, value=2, value_min=2
- CONTROLLER LOGIC_AND "And" -> [HIT]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- ACTUATOR PROPERTY "HIT": mode=ADD, property=HitCount, value=1, object_property=1
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### Brick.040  [MESH]  pos=(10.00, 22.78, 0.00) rot_deg=(0.00, -0.00, 0.00) size=(9.14, 3.21, 14.95)
mesh "Cube.105": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop Brick (BOOL) = False
- prop HitCount (INT) = 0
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['Brick.040']...AndController,), use_material=True, material=Ball
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Brick.040']...AndController,), evaluation_type=PROPGREATERTHAN, property=HitCount, value=2, value_min=2
- CONTROLLER LOGIC_AND "And" -> [HIT]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- ACTUATOR PROPERTY "HIT": mode=ADD, property=HitCount, value=1, object_property=1
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### Brick.041  [MESH]  pos=(20.00, 22.78, 0.00) rot_deg=(0.00, -0.00, 0.00) size=(9.14, 3.21, 14.95)
mesh "Cube.106": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop Brick (BOOL) = False
- prop HitCount (INT) = 0
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['Brick.041']...AndController,), use_material=True, material=Ball
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Brick.041']...AndController,), evaluation_type=PROPGREATERTHAN, property=HitCount, value=2, value_min=2
- CONTROLLER LOGIC_AND "And" -> [HIT]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- ACTUATOR PROPERTY "HIT": mode=ADD, property=HitCount, value=1, object_property=1
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### Brick.042  [MESH]  pos=(30.00, 22.78, 0.00) rot_deg=(0.00, -0.00, 0.00) size=(9.14, 3.21, 14.95)
mesh "Cube.107": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop Brick (BOOL) = False
- prop HitCount (INT) = 0
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['Brick.042']...AndController,), use_material=True, material=Ball
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Brick.042']...AndController,), evaluation_type=PROPGREATERTHAN, property=HitCount, value=2, value_min=2
- CONTROLLER LOGIC_AND "And" -> [HIT]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- ACTUATOR PROPERTY "HIT": mode=ADD, property=HitCount, value=1, object_property=1
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### Brick.043  [MESH]  pos=(40.00, 22.78, 0.00) rot_deg=(0.00, -0.00, 0.00) size=(9.14, 3.21, 14.95)
mesh "Cube.108": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop Brick (BOOL) = False
- prop HitCount (INT) = 0
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['Brick.043']...AndController,), use_material=True, material=Ball
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Brick.043']...AndController,), evaluation_type=PROPGREATERTHAN, property=HitCount, value=2, value_min=2
- CONTROLLER LOGIC_AND "And" -> [HIT]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- ACTUATOR PROPERTY "HIT": mode=ADD, property=HitCount, value=1, object_property=1
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### Brick.044  [MESH]  pos=(50.24, 22.78, 0.00) rot_deg=(0.00, -0.00, 0.00) size=(9.14, 3.21, 14.95)
mesh "Cube.109": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop Brick (BOOL) = False
- prop HitCount (INT) = 0
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['Brick.044']...AndController,), use_material=True, material=Ball
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Brick.044']...AndController,), evaluation_type=PROPGREATERTHAN, property=HitCount, value=2, value_min=2
- CONTROLLER LOGIC_AND "And" -> [HIT]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- ACTUATOR PROPERTY "HIT": mode=ADD, property=HitCount, value=1, object_property=1
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### Brick.045  [MESH]  pos=(60.24, 22.78, 0.00) rot_deg=(0.00, -0.00, 0.00) size=(9.14, 3.21, 14.95)
mesh "Cube.110": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop Brick (BOOL) = False
- prop HitCount (INT) = 0
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['Brick.045']...AndController,), use_material=True, material=Ball
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Brick.045']...AndController,), evaluation_type=PROPGREATERTHAN, property=HitCount, value=2, value_min=2
- CONTROLLER LOGIC_AND "And" -> [HIT]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- ACTUATOR PROPERTY "HIT": mode=ADD, property=HitCount, value=1, object_property=1
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### Brick.046  [MESH]  pos=(50.24, 18.26, 0.00) rot_deg=(0.00, -0.00, 0.00) size=(9.14, 3.21, 14.95)
mesh "Cube.111": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop Brick (BOOL) = False
- prop HitCount (INT) = 0
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['Brick.046']...AndController,), use_material=True, material=Ball
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Brick.046']...AndController,), evaluation_type=PROPGREATERTHAN, property=HitCount, value=2, value_min=2
- CONTROLLER LOGIC_AND "And" -> [HIT]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- ACTUATOR PROPERTY "HIT": mode=ADD, property=HitCount, value=1, object_property=1
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### Brick.047  [MESH]  pos=(60.24, 18.26, 0.00) rot_deg=(0.00, -0.00, 0.00) size=(9.14, 3.21, 14.95)
mesh "Cube.112": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop Brick (BOOL) = False
- prop HitCount (INT) = 0
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['Brick.047']...AndController,), use_material=True, material=Ball
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Brick.047']...AndController,), evaluation_type=PROPGREATERTHAN, property=HitCount, value=2, value_min=2
- CONTROLLER LOGIC_AND "And" -> [HIT]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- ACTUATOR PROPERTY "HIT": mode=ADD, property=HitCount, value=1, object_property=1
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

## text blocks
### BallReset.py  (11 lines)
```
import bge


## Reset the ball if it hits the bottom wall
loc = [0,-4,0]
scene = bge.logic.getCurrentScene()
#cont = bge.logic.getCurrentController()
ball = scene.objects["Sphere"]
ball.worldPosition = loc
    
 
```
### fix_ball.py  (26 lines)
```
import bge
## Make sure the ball doesn't get stuck in a horizontal loop

def check_vel():
    scene = bge.logic.getCurrentScene()
    cont = bge.logic.getCurrentController()
    own = cont.owner
    velchk = own['VelY']
    play = own['Play']
    
    ball = scene.objects["Sphere"]
    loc = ball.worldPosition 
    if loc.z != 0:
        loc.z = 0
        ball.worldPosition = loc
        
    linearVel = ball.localLinearVelocity 
    
    own['VelY'] = linearVel.y
    # if the absolute vertical velocity less than or equal 30, push it to 40 (up)
    if abs(linearVel.y) <= 30 and play == True:           
        linearVel.y = 40
        ball.localLinearVelocity = linearVel
        

             
```
### Instructions  (16 lines)
```
W & S for left player movement
Arrow UP & DOWN for right player movement

Space to start the ball

P key to start the game

This one has extra scripts:
    Ballreset.py set the ball back center screen if player misses a bounce
    
    pfix_ball.py makes sure the ball does not get caught in horizontal loop
    
    Mouse_Tracker_L_R.py moves the paddle left or right, this
    disables /interferes with the keyboard logic on the paddle though.
    

```
### MousePaddle_L_R.py  (47 lines)
```
import bge

####
## MOUSE paddle
## FROM https://youtu.be/-IeNnw6zzvQ
## CLICK AND DRAG TO MOVE paddle
####

def main():
    
    loc = [0,0,0]
    scene = bge.logic.getCurrentScene()
    cont = bge.logic.getCurrentController()
    own = cont.owner
    m = bge.logic.mouse.position
    
     ## checking values of mouse/paddle screen activity
    
    own['mx'] = m[0]
    own['my'] = m[1]
    mx = m[0]
       
   ## if mouse X > .95 or < .095 freeze the mouse there
    if m[0] < 0.095:
       mx = 0.1
    if m[0] > 0.95:
       mx = 0.94
    # keep mouse in screen
    bge.logic.mouse.position = (mx, 0.5)   
    
    mouse_over = cont.sensors["mouse_over"]
    xyz = mouse_over.hitPosition
    own['x'] = xyz.x
    own['y'] = xyz.y
    own['z'] = xyz.z

    if mouse_over.positive:
        paddle = scene.objects["Paddle"]
        
        xyz.y = -40
        xyz.z = 0
        
        # set the position of the paddle
        paddle.worldPosition = xyz

        
        
```