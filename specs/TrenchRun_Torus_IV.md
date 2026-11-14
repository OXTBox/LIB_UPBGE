# TrenchRun_Torus_IV.blend

## scene "Scene"  camera=Camera
game: fps=60 physics=BULLET gravity=0.0

### Light  [LIGHT]  pos=(0.00, 11.85, 0.00) rot_deg=(37.26, 3.16, 106.94) size=(0.00, 0.00, 0.00)
physics: STATIC mass=1.0

### Camera  [CAMERA]  pos=(0.00, -0.76, 1.42) rot_deg=(71.90, 0.00, 0.00) size=(0.00, 0.00, 0.00) parent=Player
camera: lens=15.0 type=PERSP ortho_scale=7.31
physics: STATIC mass=1.0
- prop Player (FLOAT) = 0.0
- prop prop (FLOAT) = 0.0

### Torus  [MESH]  pos=(0.00, 0.00, 0.00) rot_deg=(0.00, 90.00, 0.00) size=(3.43, 3.43, 0.30) parent=DeathCube
mesh "Torus": 31923 verts 68792 faces colour=#CCCCCC
physics: RIGID_BODY mass=539.4

### DeathCube  [MESH]  pos=(0.00, 0.00, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 2.00)
mesh "Cube.001": 8 verts 0 faces
physics: NO_COLLISION mass=1.0
- SENSOR ALWAYS "Always" -> [And]: controllers=(bpy.data.objects['DeathCube']...AndController,)
- CONTROLLER LOGIC_AND "And" -> [Motion]
- ACTUATOR MOTION "Motion": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_min_x=0.009, offset_location=(0.0, 0.0, 0.0), offset_rotation=(0.009, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True

### Pillbox  [MESH]  pos=(0.00, 0.00, -0.18) rot_deg=(0.00, -0.00, 0.00) size=(0.15, 0.15, 0.15) parent=PillBoxControl
mesh "Cube": 8 verts 6 faces
physics: STATIC mass=1.0
- prop shoot (BOOL) = False
- SENSOR NEAR "Near" -> [And]: controllers=(bpy.data.objects['Pillbox']...AndController,), property=Player, distance=8.0, reset_distance=2.0
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Pillbox']...AndController,), evaluation_type=PROPEQUAL, property=shoot, value=True, value_min=True
- SENSOR COLLISION "Collision" -> [And.002]: controllers=(bpy.data.objects['Pillbox']...AndController,), property=playerShot
- CONTROLLER LOGIC_AND "And" -> [Property]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- CONTROLLER LOGIC_AND "And.002" -> [Visibility]
- ACTUATOR PROPERTY "Property": mode=ASSIGN, property=shoot, value=True, object_property=True
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ADDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, object=obj:shot, track_object=obj:shot, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True
- ACTUATOR VISIBILITY "Visibility": 

### Center  [EMPTY]  pos=(0.00, 0.00, 0.00) rot_deg=(0.00, 0.00, 30.00) size=(0.00, 0.00, 0.00)
physics: NO_COLLISION mass=1.0

### shot  [MESH]  pos=(0.00, 0.00, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(0.10, 0.10, 0.10) (hidden)
mesh "Cube.002": 8 verts 6 faces
physics: STATIC mass=1.0
- prop EnemyShot (FLOAT) = 0.0
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['shot']...AndController,), property=Player
- SENSOR ALWAYS "Always" -> [And.001]: controllers=(bpy.data.objects['shot']...AndController,)
- CONTROLLER LOGIC_AND "And" -> [Edit Object]
- CONTROLLER LOGIC_AND "And.001" -> [Steering]
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True
- ACTUATOR MOTION "Motion": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_y=-0.1, offset_location=(0.0, -0.1, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR STEERING "Steering": mode=SEEK, velocity=8.0, acceleration=3.0, turn_speed=120.0, distance=0.1, target=obj:Camera, facing=True, facing_axis=X, lock_z_velocity=True

### Pillbox.001  [MESH]  pos=(0.00, 0.00, -0.18) rot_deg=(0.00, -0.00, 0.00) size=(0.20, 0.20, 0.15) parent=PillBoxControl
mesh "Cube.003": 8 verts 6 faces
physics: STATIC mass=1.0
- prop shoot (BOOL) = False
- SENSOR NEAR "Near" -> [And]: controllers=(bpy.data.objects['Pillbox.001']...AndController,), property=Player, distance=8.0, reset_distance=2.0
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Pillbox.001']...AndController,), evaluation_type=PROPEQUAL, property=shoot, value=True, value_min=True
- SENSOR COLLISION "Collision" -> [And.002]: controllers=(bpy.data.objects['Pillbox.001']...AndController,), property=playerShot
- CONTROLLER LOGIC_AND "And" -> [Property]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- CONTROLLER LOGIC_AND "And.002" -> [Visibility]
- ACTUATOR PROPERTY "Property": mode=ASSIGN, property=shoot, value=True, object_property=True
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ADDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, object=obj:shot, track_object=obj:shot, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True
- ACTUATOR VISIBILITY "Visibility": 

### Pillbox.002  [MESH]  pos=(0.00, 0.00, -0.18) rot_deg=(0.00, -0.00, 0.00) size=(0.20, 0.20, 0.15) parent=PillBoxControl
mesh "Cube.004": 8 verts 6 faces
physics: STATIC mass=1.0
- prop shoot (BOOL) = False
- SENSOR NEAR "Near" -> [And]: controllers=(bpy.data.objects['Pillbox.002']...AndController,), property=Player, distance=8.0, reset_distance=2.0
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Pillbox.002']...AndController,), evaluation_type=PROPEQUAL, property=shoot, value=True, value_min=True
- SENSOR COLLISION "Collision" -> [And.002]: controllers=(bpy.data.objects['Pillbox.002']...AndController,), property=playerShot
- CONTROLLER LOGIC_AND "And" -> [Property]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- CONTROLLER LOGIC_AND "And.002" -> [Visibility]
- ACTUATOR PROPERTY "Property": mode=ASSIGN, property=shoot, value=True, object_property=True
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ADDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, object=obj:shot, track_object=obj:shot, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True
- ACTUATOR VISIBILITY "Visibility": 

### Pillbox.003  [MESH]  pos=(0.00, 0.00, -0.18) rot_deg=(0.00, -0.00, 0.00) size=(0.15, 0.15, 0.15) parent=PillBoxControl
mesh "Cube.005": 8 verts 6 faces
physics: STATIC mass=1.0
- prop shoot (BOOL) = False
- SENSOR NEAR "Near" -> [And]: controllers=(bpy.data.objects['Pillbox.003']...AndController,), property=Player, distance=8.0, reset_distance=2.0
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Pillbox.003']...AndController,), evaluation_type=PROPEQUAL, property=shoot, value=True, value_min=True
- SENSOR COLLISION "Collision" -> [And.002]: controllers=(bpy.data.objects['Pillbox.003']...AndController,), property=playerShot
- CONTROLLER LOGIC_AND "And" -> [Property]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- CONTROLLER LOGIC_AND "And.002" -> [Visibility]
- ACTUATOR PROPERTY "Property": mode=ASSIGN, property=shoot, value=True, object_property=True
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ADDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, object=obj:shot, track_object=obj:shot, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True
- ACTUATOR VISIBILITY "Visibility": 

### Pillbox.004  [MESH]  pos=(0.00, 0.00, -0.18) rot_deg=(0.00, -0.00, 0.00) size=(0.20, 0.20, 0.15) parent=PillBoxControl
mesh "Cube.006": 8 verts 6 faces
physics: STATIC mass=1.0
- prop shoot (BOOL) = False
- SENSOR NEAR "Near" -> [And]: controllers=(bpy.data.objects['Pillbox.004']...AndController,), property=Player, distance=8.0, reset_distance=2.0
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Pillbox.004']...AndController,), evaluation_type=PROPEQUAL, property=shoot, value=True, value_min=True
- SENSOR COLLISION "Collision" -> [And.002]: controllers=(bpy.data.objects['Pillbox.004']...AndController,), property=playerShot
- CONTROLLER LOGIC_AND "And" -> [Property]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- CONTROLLER LOGIC_AND "And.002" -> [Visibility]
- ACTUATOR PROPERTY "Property": mode=ASSIGN, property=shoot, value=True, object_property=True
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ADDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, object=obj:shot, track_object=obj:shot, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True
- ACTUATOR VISIBILITY "Visibility": 

### Pillbox.005  [MESH]  pos=(0.00, 0.00, -0.18) rot_deg=(0.00, -0.00, 0.00) size=(0.20, 0.20, 0.15) parent=PillBoxControl
mesh "Cube.007": 8 verts 6 faces
physics: STATIC mass=1.0
- prop shoot (BOOL) = False
- SENSOR NEAR "Near" -> [And]: controllers=(bpy.data.objects['Pillbox.005']...AndController,), property=Player, distance=8.0, reset_distance=2.0
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Pillbox.005']...AndController,), evaluation_type=PROPEQUAL, property=shoot, value=True, value_min=True
- SENSOR COLLISION "Collision" -> [And.002]: controllers=(bpy.data.objects['Pillbox.005']...AndController,), property=playerShot
- CONTROLLER LOGIC_AND "And" -> [Property]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- CONTROLLER LOGIC_AND "And.002" -> [Visibility]
- ACTUATOR PROPERTY "Property": mode=ASSIGN, property=shoot, value=True, object_property=True
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ADDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, object=obj:shot, track_object=obj:shot, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True
- ACTUATOR VISIBILITY "Visibility": 

### Pillbox.006  [MESH]  pos=(0.00, 0.00, -0.18) rot_deg=(0.00, -0.00, 0.00) size=(0.15, 0.15, 0.15) parent=PillBoxControl
mesh "Cube.008": 8 verts 6 faces
physics: STATIC mass=1.0
- prop shoot (BOOL) = False
- SENSOR NEAR "Near" -> [And]: controllers=(bpy.data.objects['Pillbox.006']...AndController,), property=Player, distance=8.0, reset_distance=2.0
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Pillbox.006']...AndController,), evaluation_type=PROPEQUAL, property=shoot, value=True, value_min=True
- SENSOR COLLISION "Collision" -> [And.002]: controllers=(bpy.data.objects['Pillbox.006']...AndController,), property=playerShot
- CONTROLLER LOGIC_AND "And" -> [Property]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- CONTROLLER LOGIC_AND "And.002" -> [Visibility]
- ACTUATOR PROPERTY "Property": mode=ASSIGN, property=shoot, value=True, object_property=True
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ADDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, object=obj:shot, track_object=obj:shot, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True
- ACTUATOR VISIBILITY "Visibility": 

### Pillbox.007  [MESH]  pos=(0.00, 0.00, -0.18) rot_deg=(0.00, -0.00, 0.00) size=(0.20, 0.20, 0.15) parent=PillBoxControl
mesh "Cube.009": 8 verts 6 faces
physics: STATIC mass=1.0
- prop shoot (BOOL) = False
- SENSOR NEAR "Near" -> [And]: controllers=(bpy.data.objects['Pillbox.007']...AndController,), property=Player, distance=8.0, reset_distance=2.0
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Pillbox.007']...AndController,), evaluation_type=PROPEQUAL, property=shoot, value=True, value_min=True
- SENSOR COLLISION "Collision" -> [And.002]: controllers=(bpy.data.objects['Pillbox.007']...AndController,), property=playerShot
- CONTROLLER LOGIC_AND "And" -> [Property]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- CONTROLLER LOGIC_AND "And.002" -> [Visibility]
- ACTUATOR PROPERTY "Property": mode=ASSIGN, property=shoot, value=True, object_property=True
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ADDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, object=obj:shot, track_object=obj:shot, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True
- ACTUATOR VISIBILITY "Visibility": 

### Pillbox.008  [MESH]  pos=(0.00, 0.00, -0.18) rot_deg=(0.00, -0.00, 0.00) size=(0.20, 0.20, 0.15) parent=PillBoxControl
mesh "Cube.010": 8 verts 6 faces
physics: STATIC mass=1.0
- prop shoot (BOOL) = False
- SENSOR NEAR "Near" -> [And]: controllers=(bpy.data.objects['Pillbox.008']...AndController,), property=Player, distance=8.0, reset_distance=2.0
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Pillbox.008']...AndController,), evaluation_type=PROPEQUAL, property=shoot, value=True, value_min=True
- SENSOR COLLISION "Collision" -> [And.002]: controllers=(bpy.data.objects['Pillbox.008']...AndController,), property=playerShot
- CONTROLLER LOGIC_AND "And" -> [Property]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- CONTROLLER LOGIC_AND "And.002" -> [Visibility]
- ACTUATOR PROPERTY "Property": mode=ASSIGN, property=shoot, value=True, object_property=True
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ADDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, object=obj:shot, track_object=obj:shot, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True
- ACTUATOR VISIBILITY "Visibility": 

### Pillbox.009  [MESH]  pos=(0.00, 0.00, -0.18) rot_deg=(0.00, -0.00, 0.00) size=(0.15, 0.15, 0.15) parent=PillBoxControl
mesh "Cube.011": 8 verts 6 faces
physics: STATIC mass=1.0
- prop shoot (BOOL) = False
- SENSOR NEAR "Near" -> [And]: controllers=(bpy.data.objects['Pillbox.009']...AndController,), property=Player, distance=8.0, reset_distance=2.0
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Pillbox.009']...AndController,), evaluation_type=PROPEQUAL, property=shoot, value=True, value_min=True
- SENSOR COLLISION "Collision" -> [And.002]: controllers=(bpy.data.objects['Pillbox.009']...AndController,), property=playerShot
- CONTROLLER LOGIC_AND "And" -> [Property]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- CONTROLLER LOGIC_AND "And.002" -> [Visibility]
- ACTUATOR PROPERTY "Property": mode=ASSIGN, property=shoot, value=True, object_property=True
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ADDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, object=obj:shot, track_object=obj:shot, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True
- ACTUATOR VISIBILITY "Visibility": 

### Pillbox.010  [MESH]  pos=(0.00, 0.00, -0.18) rot_deg=(0.00, -0.00, 0.00) size=(0.20, 0.20, 0.15) parent=PillBoxControl
mesh "Cube.012": 8 verts 6 faces
physics: STATIC mass=1.0
- prop shoot (BOOL) = False
- SENSOR NEAR "Near" -> [And]: controllers=(bpy.data.objects['Pillbox.010']...AndController,), property=Player, distance=8.0, reset_distance=2.0
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Pillbox.010']...AndController,), evaluation_type=PROPEQUAL, property=shoot, value=True, value_min=True
- SENSOR COLLISION "Collision" -> [And.002]: controllers=(bpy.data.objects['Pillbox.010']...AndController,), property=playerShot
- CONTROLLER LOGIC_AND "And" -> [Property]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- CONTROLLER LOGIC_AND "And.002" -> [Visibility]
- ACTUATOR PROPERTY "Property": mode=ASSIGN, property=shoot, value=True, object_property=True
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ADDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, object=obj:shot, track_object=obj:shot, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True
- ACTUATOR VISIBILITY "Visibility": 

### Pillbox.011  [MESH]  pos=(0.00, 0.00, -0.18) rot_deg=(0.00, -0.00, 0.00) size=(0.20, 0.20, 0.15) parent=PillBoxControl
mesh "Cube.013": 8 verts 6 faces
physics: STATIC mass=1.0
- prop shoot (BOOL) = False
- SENSOR NEAR "Near" -> [And]: controllers=(bpy.data.objects['Pillbox.011']...AndController,), property=Player, distance=8.0, reset_distance=2.0
- SENSOR PROPERTY "Property" -> [And.001]: controllers=(bpy.data.objects['Pillbox.011']...AndController,), evaluation_type=PROPEQUAL, property=shoot, value=True, value_min=True
- SENSOR COLLISION "Collision" -> [And.002]: controllers=(bpy.data.objects['Pillbox.011']...AndController,), property=playerShot
- CONTROLLER LOGIC_AND "And" -> [Property]
- CONTROLLER LOGIC_AND "And.001" -> [Edit Object]
- CONTROLLER LOGIC_AND "And.002" -> [Visibility]
- ACTUATOR PROPERTY "Property": mode=ASSIGN, property=shoot, value=True, object_property=True
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ADDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, object=obj:shot, track_object=obj:shot, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True
- ACTUATOR VISIBILITY "Visibility": 

### PillBoxControl  [EMPTY]  pos=(0.00, 0.00, 0.00) rot_deg=(0.00, 90.00, 0.00) size=(0.00, 0.00, 0.00) parent=DeathCube
physics: NO_COLLISION mass=1.0

### Empty  [EMPTY]  pos=(0.00, -0.73, 1.02) rot_deg=(0.00, 0.00, 0.00) size=(0.00, 0.00, 0.00)
physics: NO_COLLISION mass=1.0
- prop Player (BOOL) = False

### Player  [MESH]  pos=(0.01, -0.55, 1.32) rot_deg=(0.00, 0.00, 0.00) size=(0.11, 0.11, 0.11)
mesh "Cube.014": 8 verts 5 faces
physics: RIGID_BODY mass=251.8
- prop Player (BOOL) = False
- SENSOR KEYBOARD "A" -> [And]: controllers=(bpy.data.objects['Player']...AndController,), key=A, modifier_key_1=NONE, modifier_key_2=NONE
- SENSOR KEYBOARD "D" -> [And.001]: controllers=(bpy.data.objects['Player']...AndController,), key=D, modifier_key_1=NONE, modifier_key_2=NONE
- SENSOR KEYBOARD "W" -> [And.002]: controllers=(bpy.data.objects['Player']...AndController,), key=W, modifier_key_1=NONE, modifier_key_2=NONE
- SENSOR KEYBOARD "D.001" -> [And.003]: controllers=(bpy.data.objects['Player']...AndController,), key=S, modifier_key_1=NONE, modifier_key_2=NONE
- SENSOR MOUSE "Mouse" -> [And.004]: controllers=(bpy.data.objects['Player']...AndController,), mouse_event=MOVEMENT, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER LOGIC_AND "And" -> [RollLeft]
- CONTROLLER LOGIC_AND "And.001" -> [RollRight]
- CONTROLLER LOGIC_AND "And.002" -> [Motion.002]
- CONTROLLER LOGIC_AND "And.003" -> [Motion.003]
- CONTROLLER LOGIC_AND "And.004" -> [Motion.004]
- ACTUATOR MOTION "RollLeft": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_min_y=0.007, offset_location=(0.0, 0.0, 0.0), offset_rotation=(0.0, 0.007, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "RollRight": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_min_y=-0.007, offset_location=(0.0, 0.0, 0.0), offset_rotation=(0.0, -0.007, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "Motion.002": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_z=0.01, offset_location=(0.0, 0.0, 0.01), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "Motion.003": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_z=-0.01, offset_location=(0.0, 0.0, -0.01), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOUSE "Motion.004": mode=LOOK, visible=True, use_axis_x=True, use_axis_y=True, reset_x=True, reset_y=True, local_y=True, object_axis_x=OBJECT_AXIS_Z, object_axis_y=OBJECT_AXIS_X, sensitivity_x=2.0, sensitivity_y=2.0, min_y=-1.571, max_y=1.571

### Point  [LIGHT]  pos=(0.01, -0.40, 1.50) rot_deg=(0.00, 0.00, 0.00) size=(0.00, 0.00, 0.00)
physics: NO_COLLISION mass=1.0

### Plane  [MESH]  pos=(0.00, -0.52, 1.71) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane": 4 verts 1 faces colour=#CCCCCC
physics: STATIC mass=1.0

## text blocks