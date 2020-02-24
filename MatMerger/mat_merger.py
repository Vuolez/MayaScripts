import maya.cmds as cmds
import pymel.core as pm
import time
import os
import sys

start_time = time.clock()

geometry = pm.ls(tr=True)
geometries_poly = cmds.polyListComponentConversion(geometry, tf=True)
materials = pm.ls(mat = True)


###

for object in geometries_poly:
    for mat in materials:
        cmds.hyperShade(objects=str(mat))
        selected = pm.ls(sl = True)
        geometries_poly = cmds.polyListComponentConversion(selected, tf=True)
            
        try:
            cmds.polyChipOff(geometries_poly, kft = False , dup = False)
            print("ChipOff")
        except:
            pass
        
        
obj_name = []
for obj in geometry:
    obj_name.append(obj)


for i in obj_name:
    try:
        cmds.polySeparate(str(i))
        print("Separate: " + str(i))
    except:
        pass
        
            
for mat in materials:
    cmds.hyperShade(objects=str(mat))
    selected = pm.ls(sl = True)
    
    for i in range(len(selected)):
        selected[i] = str(selected[i]).split(".")
        selected[i] = selected[i][0]
    try:
        cmds.polyUnite(selected, ch = 0, n=str(mat)+"_model")
        print("Unite: " + selected[i]) 
    except:
        pass    

print(time.clock() - start_time)



###


filepath = cmds.file(q=True, sn=True)
filename = os.path.basename(filepath)



filepath = os.path.abspath(os.path.join(filepath, os.pardir))
final_directory = os.path.join(filepath , "out")
if not os.path.exists(final_directory):
    os.mkdir(final_directory)
    print("Created Folder")
out_path = os.path.join(final_directory ,filename) 
print(out_path)

cmds.file(out_path, force=True, options="v=0;", typ="FBX export", pr=True,  ea=True)