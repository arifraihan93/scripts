#Name: batch_assign_mats_karma
#Label: Batch Assign Mats Karma
#Icon: COMMON_materialx


nodes = hou.node('/stage').selection()
number_of_nodes = sum(1 for _ in nodes)

mat = hou.node('/stage').createNode('assignmaterial')
mat.layoutChildren()
mat.setInput(0, hou.selectedNodes()[0], 0)
mat.setDisplayFlag(True)

mat.parm('nummaterials').set(number_of_nodes)

for id,node in enumerate(nodes):
    
    path = 'primpattern' + str(id + 1)
    matX_path = 'matspecpath' + str(id + 1)
    
    prim_path = mat.parm(path).set(node)
    
    prim_path_parts = mat.parm(path).eval().split('/')
    prim_path_short = '/'.join(prim_path_parts[-3:])
    
    
    mat_path = hou.node(prim_path_short).parm('shop_materialpath').eval()
    mat_path_parts = mat_path.split('/')
    mat_path_short = '/'.join(prim_path_parts[-1:])
    mat_path_materialX = 'MaterialX_' + mat_path_short
    
    mat.parm(matX_path).set(mat_path_materialX)
   
    
    

