import os
import maya.cmds as cmds
import pymel.core as pm

def create_subfolder(name = 'out'):
    filepath = cmds.file(q=True, sn=True)
    filepath = os.path.abspath(os.path.join(filepath,os.pardir))
    final_directory = os.path.join(filepath, name)
    if not os.path.exists(final_directory):
        os.mkdir(final_directory)
        print('Create Folder')
        
        
def get_selected_meshes():
    selected = pm.ls(sl=True, et='transform')
    meshes = []

    if selected:
        for s in selected:
            shape = s.getShape()
            if shape:
                if shape.nodeType() == 'mesh':
                    meshes.append(shape)

    return meshes
    
    
def get_str_until(str, ch):
    result = ''
    for i in str:
        if i == ch:
            return result
        else:
            result += i

    return result