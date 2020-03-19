import pymel.core as pm
import maya.cmds as cmds
import maya.mel as mel

file_path = ''

def button_export (*arg):
    object = pm.ls(sl=True)[0]  
    
    mel.eval('BakeCustomPivot;')
    mel.eval('performBakeCustomToolPivot 0;')
    
    object.translateX.set(0)
    object.translateY.set(0)
    object.translateZ.set(0)
    
    #find the filename
    filename = file_path.replace('\\','/')
    print(filename)
    mel.eval(('FBXExport -f \"{}\" -s').format(filename))
    
    #cmds.file('D:\\workspace\\learn\\pymel/out', exportSelected = True)






    
def button_accept_path(path):
    if not os.path.exists(path):
        print("path not exists")
        return
    global file_path
    file_path = path + "\\model.fbx"

pm.window(title = "Plunig for Sen'ka", width = 200)
pm.columnLayout(adjustableColumn = True)



pm.button(label = 'export object', command = button_export)
path_field = pm.textField(changeCommand  = button_accept_path)
#pm.textFieldButtonGrp( label='path', buttonLabel='accept', changeCommand  = button_accept_path)

pm.showWindow()