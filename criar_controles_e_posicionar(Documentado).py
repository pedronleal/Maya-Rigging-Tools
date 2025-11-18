"""

----------------------------------------------------------------------------------------------------------------
SCRIPT: Criar controles para Joints
----------------------------------------------------------------------------------------------------------------

DESCRIÇÃO:
    Ferramente de rigging que automatiza a criação de controles NURBS para joints selecionados, com customização de tamanho, cor e rotação.


AUTOR: 
    Pedro Leal

DATA DE CRIAÇÃO:
    17/11/2025

VERSÃO:
    1.0.0

DEPENDÊNCIAS:
    - Maya 2020+ (testado em Maya 2024)
    - Python 3.7+

USO:
    1. Selecione um joint no Maya
    2. Execute a função: criar_controles_e_posicionar()
    3. Customize parâmetros conforme necessário

CHANGELOG:
    v1.0.0 (17/11/2025)
        - Versão inicial
        - Criação automática de controles
        - Suporte a customização de raio, cor e rotação

LICENÇA:
    MIT License - Uso livre para projetos pessoais e comerciais
----------------------------------------------------------------------------------------------------------------
"""
import maya.cmds as cmds

def criar_controles_e_posicionar(raio=10, cor=13, rotacao=(0, 90, 0)):
    """
    Cria um controle NURBS circular posicionado em um joint selecionado.

    Esta função automatiza a criação de controles de rigging, gerando um círculo NURBS com nomenclatura baseada no joint, aplicando cor customizada e posicionando/rotacionando automaticamente.

    Args:
        raio (float, optional): Tamanho do controle NURBS. Padrão: 10
        cor (int, optional): Índice de cor do Maya (0-31). Padrão: 13 (vermelho)
        rotacao (tuple, optional): Rotação (X, Y, Z) em graus. Padrão: (0, 90, 0)

    Returns:
        None: Imprime mensagem de sucesso ou erro no console.

    Examples:
        >>> # Criar controle com valores padrão
        >>> criar_controles_e_posicionar()

        >>> # Controle pequeno e azul
        >>> criar_controles_e_posicionar(raio=5, cor=6)

        >>> # Controle grande, amarelo, sem rotação
        >>> criar_controles_e_posicionar(raio=20, cor=17, rotacao=(0, 0, 0))

    Notes:
        - Requer que um joint esteja selecionado no Maya
        - Nomenclatura: joint_JNT -> joint_CTRL
        - Exemplo: shoulder_JNT -> shoulder_CTRL

    Cores comuns do Maya:
        6 = Azul
        13 = Vermelho
        14 = Verde
        17 = Amarelo
        18 = Ciano
    """

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

        print(f"{ctrl_name} Criado com sucesso!")
    else:
        print("Nenhum joint selecionado. Selecione um joint primeiro")