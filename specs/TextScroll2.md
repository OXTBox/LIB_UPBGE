# TextScroll2.blend

## scene "Scene"  camera=Camera
game: fps=60 physics=BULLET gravity=0.0

### Light  [LIGHT]  pos=(10.68, 1.01, 5.90) rot_deg=(37.26, 3.16, 106.94) size=(0.00, 0.00, 0.00) parent=Camera
physics: STATIC mass=1.0

### Camera  [CAMERA]  pos=(8.98, -16.04, 32.76) rot_deg=(56.33, 0.00, 0.00) size=(0.00, 0.00, 0.00)
camera: lens=70.0 type=PERSP ortho_scale=7.31
physics: NO_COLLISION mass=1.0
- SENSOR ALWAYS "Always" -> [And]: controllers=(bpy.data.objects['Camera']...AndController,)
- CONTROLLER LOGIC_AND "And" -> [Motion]
- ACTUATOR MOTION "Motion": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_y=-0.02, force_max_z=0.02, offset_location=(0.0, -0.02, 0.02), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True

### TextScroll  [FONT]  pos=(-0.14, -2.73, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(17.26, 28.52, 0.00)
text: "A long time ago in a galaxy far far away...

The Bad Guys were being awful and 
the Good Guys were like 
"Oh man, this is so awful!"

A render farmer was reviewing some
addons over at artstation when his
Android malfunctioned.

A big ship was flying around with it's lasers
going "pew pew" another ship was like
"Whoa! watch it with those lasers bruh"

Then some other stuff happened, it was
very exciting, you shoulda been there,
but too bad it was a long long time a ago
and in a galaxy far far away.

I could tell you more about this but it's
way passed your bed time and you have
to get up early to farm moisture
from the desert sky...just like this Jedi
I used to know...but that is another story.
"
physics: NO_COLLISION mass=1.0

### Cube  [MESH]  pos=(9.25, -14.82, 12.52) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 2.00) parent=Camera
mesh "Cube.001": 8 verts 6 faces
physics: NO_COLLISION mass=1.0

### Title  [FONT]  pos=(9.37, 13.41, 1.70) rot_deg=(75.00, 0.00, 0.00) size=(17.72, 4.98, 0.00)
text: "BLENDER
WARS"
physics: NO_COLLISION mass=1.0
- SENSOR ALWAYS "Always" -> [And]: controllers=(bpy.data.objects['Title']...AndController,)
- CONTROLLER LOGIC_AND "And" -> [Motion]
- ACTUATOR MOTION "Motion": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_y=-0.1, force_max_z=-0.2, offset_location=(0.0, -0.1, -0.2), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True

## text blocks