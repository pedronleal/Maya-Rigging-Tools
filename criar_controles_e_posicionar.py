import maya.cmds as cmds

def criar_controles_e_posicionar(raio=10, cor=13, rotacao=(0, 0, 90), freeze=True):

	selected = cmds.ls(selection=True)

	if selected:
		joint = selected[0]
	
		base_name = joint.replace("_JNT", "")
	
		ctrl_name = f"{base_name}_CTRL"
	
		pos = cmds.xform(joint, query=True, worldSpace=True, translation=True)
	
		ctrl = cmds.circle(name=ctrl_name, radius=raio)[0]
		
		cmds.xform(ctrl_name, translation=pos)
		
		cmds.rotate(*rotacao, ctrl_name)
		
		cmds.setAttr(f"{ctrl_name}.overrideEnabled", 1)
		cmds.setAttr(f"{ctrl_name}.overrideColor", cor)
		
		if freeze:
			cmds.makeIdentity(ctrl_name, apply=True, translate=True, rotate=True, scale=True, normal=False)
		
		print(f"{ctrl_name} Criado com sucesso!")
	else:
		print("Nenhum Joint selecionado, selecione um Joint primeiro")