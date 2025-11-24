import maya.cmds as cmds

def criar_controles_e_posicionar(raio=10, cor=13, rotacao=(0, 0, 90), freeze=True):

	selected = cmds.ls(selection=True)

	if selected:
		
		joint = selected[0]
		base_name = joint.replace("_JNT", "")
		ctrl_name = f"{base_name}_CTRL"
		grp_name = f"{base_name}_GRP"
	
		pos = cmds.xform(joint, query=True, worldSpace=True, translation=True)
		
		grp = cmds.group(empty=True, name=grp_name)
		cmds.xform(grp, translation=pos)
	
		ctrl = cmds.circle(name=ctrl_name, radius=raio)[0]
		
		cmds.xform(ctrl_name, translation=pos)
		
		cmds.parent(ctrl_name, grp_name)
		
		cmds.rotate(*rotacao, ctrl_name)
		
		if freeze:
			cmds.makeIdentity(ctrl_name, apply=True, translate=True, rotate=True, scale=True, normal=False)
		
		cmds.setAttr(f"{ctrl_name}.overrideEnabled", 1)
		cmds.setAttr(f"{ctrl_name}.overrideColor", cor)
		
		print(f"Controle criado com Sucesso: {ctrl_name}")
		print(f"Grupo criado com Sucesso: {grp_name}")
		print(f"Hierarquia criada com Sucesso: {grp_name} -> {ctrl_name}")
	else:
		print("Nenhum Joint selecionado, selecione um Joint primeiro")

def conectar_controle_ao_joint():
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



def abrir_rigging_tools():
	"""Abre a janela de Rigging Tools."""
	
	cores = {
		"Vermelho": 13,
		"Azul": 6,
		"Amarelo": 17, 
		"Verde": 14
	}	
	
	
		
	if cmds.window("riggingToolsWin", exists=True):
		cmds.deleteUI("riggingToolsWin")
		
	janela = cmds.window("riggingToolsWin", title="Rigging Tools v1.4.0", widthHeight=(300, 250))
	layout_principal = cmds.columnLayout(adjustableColumn=True)
		
	cmds.separator(height=10, style='none')
	cmds.text(label="Selecione objetos e clique na função desejada:", align='center')
	cmds.separator(height=10, style='none')
	
	cmds.intSliderGrp("tamanhoSlider", label="Tamanho:", minValue=1, maxValue=50, value=10, field=True)
	
	cmds.optionMenu("corMenu", label="Cor:")
	cmds.menuItem(label="Vermelho", )
	cmds.menuItem(label="Azul", )
	cmds.menuItem(label="Amarelo", )
	cmds.menuItem(label="Verde", )
	
	cmds.checkBox("freezeCheck", label="Aplicar Freeze Transforms", value=True)
	
	cmds.separator(height=15, style='single')
		
	cmds.button(label="Criar Controles", command=lambda *args: criar_controles_e_posicionar(raio=cmds.intSliderGrp("tamanhoSlider", query=True, value=True), cor=cores[cmds.optionMenu("corMenu", query=True, value=True)], freeze=cmds.checkBox("freezeCheck", query=True, value=True)), backgroundColor=(0.3, 0.5, 0.7))
	cmds.button(label="Conectar Controle ao Joint", command=lambda *args: conectar_controle_ao_joint(), backgroundColor=(0.5, 0.6, 0.3))
	cmds.separator(height=15, style='single')
	cmds.button(label="Fechar", command=lambda *args: cmds.deleteUI("riggingToolsWin", window=True))
		
	cmds.showWindow(janela)