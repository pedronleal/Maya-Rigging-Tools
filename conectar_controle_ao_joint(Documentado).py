"""
----------------------------------------------------------------------------------------------------------------
SCRIPT: Conectar Controle ao Joint
----------------------------------------------------------------------------------------------------------------

DESCRIÇÃO:
    Conecta automaticamente controles a joints correspondentes usando Parent Constraint.
    Identifica o joint pelo nome do controle (shoulder_CTRL -> shoulder_JNT).

AUTOR: 
    Pedro Leal

DATA DE CRIAÇÃO:
    18/11/2025

VERSÃO:
    1.1.0

DEPENDÊNCIAS:
    - Maya 2020+ (testado em Maya 2024)
    - Python 3.7+

USO:
    1. Selecione um controle (ex: shoulder_CTRL)
    2. Execute a função: conectar_controle_ao_joint()

VALIDAÇÕES:
    ✅ Verifica se há controle selecionado
    ✅ Verifica se joint correspondente existe
    ✅ Mantém offset original (maintainOffset=True)

LICENÇA:
    MIT License - Uso livre para projetos pessoais e comerciais
----------------------------------------------------------------------------------------------------------------
"""
import maya.cmds as cmds

def conectar_controle_ao_joint():
    """
    Conecta um controle ao joint correspondente usando Parent Constraint.

    Como usar:
      . Selecione o controle (ex: shoulder_CTRL)
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

        if cmds.objectExists(joint_name):
            cmds.parentConstraint(ctrl, joint_name, mo=True)

            print(f"Constraint criado: {ctrl} -> {joint_name}")
        else:
            print(f"ERRO: Joint '{joint_name}' não exite no Maya!")
    else:
        print("ERRO: Nenhum Controle selecionado. Selecione primeiro")