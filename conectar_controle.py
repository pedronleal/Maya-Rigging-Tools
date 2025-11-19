import maya.cmds as cmds

def conectar_controle_ao_joint():
	"""
	Conecta um controle ao joint correspondente usando Parent Constraint.
	
	Como usar:
		1. Selecione o controle (ex: shoulder_CTRL)
		2. Execute: conectar_controle_ao_joint()
		3. O controle será conectado ao joint (shoulder_JNT)
		
	Exemplo:
		cmds.select('shoulder_CTRL')
		conectar_controle_ao_joint()
		# Resultado: shoulder_CTRL -> shoulder_JNT conectados
	"""

	selected = cmds.ls(selection=True)

	if selected:
	
		ctrl = selected[0]
		joint_name = ctrl.replace("_CTRL", "_JNT")
		
		if cmds.objExists(joint_name):
	
			cmds.parentConstraint(ctrl, joint_name, mo=True)
	
			print(f"Constraint criado: {ctrl} -> {joint_name}")
		else:
			print(f"ERRO: Joint '{joint_name}' não existe no Maya!")
	
	else:
		print("Nenhum Controle selecionado. Selecione primeiro")