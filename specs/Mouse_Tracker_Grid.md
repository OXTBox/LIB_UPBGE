# Mouse_Tracker_Grid.blend

## scene "Scene"  camera=Camera
game: fps=60 physics=BULLET gravity=9.8

### Light  [LIGHT]  pos=(4.08, 1.01, 5.90) rot_deg=(37.26, 3.16, 106.94) size=(0.00, 0.00, 0.00)
physics: STATIC mass=1.0

### Camera  [CAMERA]  pos=(7.36, -6.93, 4.96) rot_deg=(63.56, 0.00, 46.69) size=(0.00, 0.00, 0.00)
camera: lens=50.0 type=PERSP ortho_scale=7.31
physics: STATIC mass=1.0

### Plane  [MESH]  pos=(0.00, 0.00, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(32.89, 32.89, 0.00) (hidden)
mesh "Plane": 4 verts 1 faces colour=#CCCCCC
physics: STATIC mass=1.0

### Cube  [MESH]  pos=(0.00, 0.00, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(0.70, 0.70, 0.70) (hidden)
mesh "Cube.001": 8 verts 6 faces
physics: DYNAMIC mass=10.0

### ScriptedTracker  [MESH]  pos=(-0.00, -0.00, 0.03) rot_deg=(0.00, 180.00, 0.00) size=(2.00, 2.00, 2.00)
mesh "Cone": 33 verts 33 faces colour=#CCCCCC
physics: NO_COLLISION mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['ScriptedTracker']...PythonController,), mouse_event=MOUSEOVERANY, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- SENSOR MOUSE "mouse_leftclick" -> []: use_tap=True, controllers=(), mouse_event=LEFTCLICK, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- SENSOR MOUSE "Mouse" -> [and]: tick_skip=10, use_tap=True, controllers=(bpy.data.objects['ScriptedTracker']...AndController,), mouse_event=LEFTCLICK, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []
- CONTROLLER LOGIC_AND "and" -> [Edit Object]
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ADDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, object=obj:Cube, track_object=obj:Cube, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### Tracker  [MESH]  pos=(-0.00, -6.84, 0.03) rot_deg=(0.00, 180.00, 0.00) size=(2.00, 2.00, 2.00) (hidden)
mesh "Cone.001": 33 verts 33 faces colour=#CCCCCC
physics: NO_COLLISION mass=1.0

### RTSUnit  [MESH]  pos=(-0.00, -0.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.001": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.001  [MESH]  pos=(-0.00, 2.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.026": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.001']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.002  [MESH]  pos=(-0.00, 4.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.027": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.002']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.003  [MESH]  pos=(-0.00, 6.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.028": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.003']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.004  [MESH]  pos=(-0.00, 8.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.029": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.004']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.005  [MESH]  pos=(-0.00, 10.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.030": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.005']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.006  [MESH]  pos=(-0.00, 12.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.031": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.006']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.007  [MESH]  pos=(-0.00, 14.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.032": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.007']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.008  [MESH]  pos=(2.00, -0.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.033": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.008']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.009  [MESH]  pos=(2.00, 2.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.034": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.009']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.010  [MESH]  pos=(2.00, 4.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.035": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.010']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.011  [MESH]  pos=(2.00, 6.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.036": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.011']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.012  [MESH]  pos=(2.00, 8.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.037": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.012']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.013  [MESH]  pos=(2.00, 10.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.038": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.013']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.014  [MESH]  pos=(2.00, 12.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.039": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.014']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.015  [MESH]  pos=(2.00, 14.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.040": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.015']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.016  [MESH]  pos=(4.00, -0.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.041": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.016']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.017  [MESH]  pos=(4.00, 2.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.042": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.017']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.018  [MESH]  pos=(4.00, 4.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.043": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.018']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.019  [MESH]  pos=(4.00, 6.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.044": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.019']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.020  [MESH]  pos=(4.00, 8.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.045": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.020']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.021  [MESH]  pos=(4.00, 10.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.046": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.021']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.022  [MESH]  pos=(4.00, 12.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.047": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.022']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.023  [MESH]  pos=(4.00, 14.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.048": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.023']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.024  [MESH]  pos=(6.00, -0.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.049": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.024']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.025  [MESH]  pos=(6.00, 2.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.050": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.025']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.026  [MESH]  pos=(6.00, 4.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.051": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.026']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.027  [MESH]  pos=(6.00, 6.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.052": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.027']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.028  [MESH]  pos=(6.00, 8.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.053": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.028']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.029  [MESH]  pos=(6.00, 10.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.054": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.029']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.030  [MESH]  pos=(6.00, 12.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.055": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.030']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.031  [MESH]  pos=(6.00, 14.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.056": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.031']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.032  [MESH]  pos=(8.00, -0.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.057": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.032']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.033  [MESH]  pos=(8.00, 2.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.058": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.033']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.034  [MESH]  pos=(8.00, 4.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.059": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.034']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.035  [MESH]  pos=(8.00, 6.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.060": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.035']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.036  [MESH]  pos=(8.00, 8.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.061": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.036']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.037  [MESH]  pos=(8.00, 10.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.062": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.037']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.038  [MESH]  pos=(8.00, 12.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.063": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.038']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.039  [MESH]  pos=(8.00, 14.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.064": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.039']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.040  [MESH]  pos=(10.00, -0.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.065": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.040']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.041  [MESH]  pos=(10.00, 2.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.066": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.041']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.042  [MESH]  pos=(10.00, 4.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.067": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.042']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.043  [MESH]  pos=(10.00, 6.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.068": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.043']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.044  [MESH]  pos=(10.00, 8.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.069": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.044']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.045  [MESH]  pos=(10.00, 10.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.070": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.045']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.046  [MESH]  pos=(10.00, 12.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.071": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.046']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.047  [MESH]  pos=(10.00, 14.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.072": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.047']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.048  [MESH]  pos=(12.00, -0.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.073": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.048']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.049  [MESH]  pos=(12.00, 2.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.074": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.049']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.050  [MESH]  pos=(12.00, 4.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.075": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.050']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.051  [MESH]  pos=(12.00, 6.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.076": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.051']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.052  [MESH]  pos=(12.00, 8.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.077": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.052']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.053  [MESH]  pos=(12.00, 10.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.078": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.053']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.054  [MESH]  pos=(12.00, 12.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.079": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.054']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.055  [MESH]  pos=(12.00, 14.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.080": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.055']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.056  [MESH]  pos=(14.00, -0.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.081": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.056']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.057  [MESH]  pos=(14.00, 2.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.082": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.057']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.058  [MESH]  pos=(14.00, 4.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.083": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.058']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.059  [MESH]  pos=(14.00, 6.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.084": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.059']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.060  [MESH]  pos=(14.00, 8.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.085": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.060']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.061  [MESH]  pos=(14.00, 10.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.086": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.061']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.062  [MESH]  pos=(14.00, 12.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.087": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.062']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

### RTSUnit.063  [MESH]  pos=(14.00, 14.00, 0.03) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Plane.088": 4 verts 1 faces
physics: STATIC mass=1.0
- SENSOR MOUSE "mouse_over" -> [Python]: use_pulse_true_level=True, controllers=(bpy.data.objects['RTSUnit.063']...PythonController,), mouse_event=MOUSEOVER, use_material=PROPERTY, mask=(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True)
- CONTROLLER PYTHON "Python" script=mouse_tracker_Grid.main -> []

## text blocks
### mouse_tracker.py  (27 lines)
```
import bpy
import bge
from pycl import print
####
## MOUSE TRACKER
## FROM https://youtu.be/-IeNnw6zzvQ
## CLICK AND DRAG TO MOVE TRACKER
####

def main():
    loc = [0,0,0]
    scene = bge.logic.getCurrentScene()
    cont = bge.logic.getCurrentController()

    mouse_over = cont.sensors["mouse_over"]
    mouse_click = cont.sensors["mouse_leftclick"]

    if mouse_over.positive and mouse_click.positive:
        tracker = scene.objects["Tracker"]
        xyz = mouse_over.hitPosition
        tracker.worldPosition = xyz 
        # print("working?", xyz[0],xyz[1],xyz[2])
        



        
```
### mouse_tracker_Grid.py  (23 lines)
```

import bge
####
## MOUSE TRACKER  GRID UNITS
## FROM https://youtu.be/-IeNnw6zzvQ
## CLICK AND DRAG TO MOVE TRACKER
## Tracker moves only to grid location of FPSUnit plane
## Click drops cubes at mouse location
####

def main():
    scene = bge.logic.getCurrentScene()
    cont = bge.logic.getCurrentController()
    own = cont.owner

    mouse_over = cont.sensors["mouse_over"]
    #mouse_click = cont.sensors["mouse_leftclick"]

    if mouse_over.positive:
        tracker = scene.objects["ScriptedTracker"]
        tracker.worldPosition =  own.worldPosition
        tracker.worldPosition.z += .1

```