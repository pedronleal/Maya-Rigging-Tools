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
    
    Esta função identifica automaticamente o joint baseado no nome do controle, cria um Parent Constraint
    e mantém o offset original (maintain offset)
    
    Args:
    	Nenhum - A função usa o objeto atualmente selecionado no Maya
    	
    Returns:
    	None: Imprime mensagem de sucesso ou erro no console.

    Como usar:
        Selecione o controle (ex: shoulder_CTRL)
        2. Execute: conectar_controle_ao_joint()
        3. O controle será conectado ao joint (shoulder_JNT)
        
    Exemplo:
        Selecionar e conectar um controle
        cmds.select('shoulder_CTRL')
        conectar_controle_ao_joint()
        # ✓ Resultado: shoulder_CTRL -> shoulder_JNT conectados

        Tentar conectar sem seleção
        cmds.select(clear=True)
        conectar_controle_ao_joint()
        # ❌ ERRO: Nenhum controle selecionado

    Notes:
        - Requer que um controle esteja selecionado no Maya
        - Nomenclatura: controle_CTRL -> joint_JNT correspondente
        - Usa maintainOffset=True para preservar posição relativa
        - Se o joint não existir, exibe mensagem de erro clara

    Workflow típico:
        1. Cria controles: criar_controles_e_posicionar()
        2. Conecta com esta função
        3. Resultado: Controles animáveis que movem os joints
    """  

    selected = cmds.ls(selection=True)

    if selected:
        ctrl = selected[0]
        joint_name = ctrl.replace("_CTRL", "_JNT")

        if cmds.objectExists(joint_name):
            cmds.parentConstraint(ctrl, joint_name, mo=True)

            print(f"✓ Constraint criado: {ctrl} -> {joint_name}")
        else:
            print(f"❌ERRO: Joint '{joint_name}' não existe no Maya!")
    else:
        print("❌ERRO: Nenhum Controle selecionado. Selecione primeiro")