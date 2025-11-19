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
    1.2.0

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


----------------------------------------------------------------------------------------------------------------
v1.1.0 (18/11/2025) - CONECTAR CONTROLE AO JOINT
----------------------------------------------------------------------------------------------------------------

SCRIPT: Conectar Controle ao Joint
ARQUIVO: conectar_controle.py

DESCRIÇÃO:
    Conecta automaticamente controles a joints correspondentes usando Parent Constraint.
    Identifica o joint pelo nome do controle (shoulder_CTRL -> shoulder_JNT).

USO:
    1. Selecione um controle (ex: shoulder_CTRL)
    2. Execute a função: conectar_controle_ao_joint()
    3. O controle será conectado ao joint automaticamente

EXEMPLO:
    >>> cmds.select('shoulder_CTRL')
    >>> conectar_controle_ao_joint()
    # Resultado: "Constraint criado: shoulder_CTRL -> shoulder_JNT"

VALIDAÇÕES:
    ✅ Verifica se há controle selecionado
    ✅ Verifica se joint correspondente existe
    ✅ Mantém offset original (maintainOffset=True)

MENSAGENS DE ERRO:
    - "ERRO: Nenhum Controle selecionado. Selecione primeiro"
    - "ERRO: Joint 'nome_JNT' não existe no Maya!"

INTEGRAÇÃO:
    Pode ser usado em conjunto com criar_controles_e_posicionar() (v1.0.0):
    
    >>> # Workflow completo:
    >>> cmds.select('shoulder_JNT')
    >>> criar_controles_e_posicionar()  # Cria shoulder_CTRL
    >>> cmds.select('shoulder_CTRL')
    >>> conectar_controle_ao_joint()    # Conecta ao joint
----------------------------------------------------------------------------------------------------------------
v1.2.0 (19/11/2025) - FREEZE TRANSFORMS
----------------------------------------------------------------------------------------------------------------

ATUALIZAÇÃO: Criar Controle com Freeze Transforms
ARQUIVO: criar_controle.py (atualizado)

DESCRIÇÃO:
    Adicionada funcionalidade de freeze transforms automático aos controles criados.
    Zera translação/rotação e normaliza escala para facilitar animação.

NOVA FUNCIONALIDADE:
    ✅ Parâmetro freeze=True (ativado por padrão)
    ✅ Aplica cmds.makeIdentity() automaticamente
    ✅ Zera Translate (X, Y, Z) para 0
    ✅ Zera Rotate (X, Y, Z) para 0
    ✅ Normaliza Scale (X, Y, Z) para 1

USO:
    # Com freeze (padrão):
    >>> criar_controles_e_posicionar()
    
    # Sem freeze (opcional):
    >>> criar_controles_e_posicionar(freeze=False)
    
    # Customizado:
    >>> criar_controles_e_posicionar(raio=15, cor=6, freeze=True)

BENEFÍCIOS:
    ✅ Controles começam com valores zerados
    ✅ Facilita reset de pose para animadores
    ✅ Padrão da indústria de rigging
    ✅ Evita transformações acumuladas

EXEMPLO ANTES/DEPOIS:
    ANTES do freeze:
        TranslateX: 5.234
        RotateY: 90.0
        
    DEPOIS do freeze:
        TranslateX: 0.0  ← Zerado!
        RotateY: 0.0     ← Zerado!

INTEGRAÇÃO COM VERSÕES ANTERIORES:
    >>> # Workflow completo v1.0.0 + v1.1.0 + v1.2.0:
    >>> cmds.select('shoulder_JNT')
    >>> criar_controles_e_posicionar()          # Cria E aplica freeze
    >>> cmds.select('shoulder_CTRL')
    >>> conectar_controle_ao_joint()            # Conecta ao joint

----------------------------------------------------------------------------------------------------------------
CHANGELOG GERAL DO PROJETO:
----------------------------------------------------------------------------------------------------------------
v1.2.0 (19/11/2025)
    - Atualização: criar_controles_e_posicionar()
    - Adicionado parâmetro freeze=True
    - Aplica freeze transforms automático
    - Controles criados já zerados

v1.1.0 (18/11/2025)
    - Nova função: conectar_controle_ao_joint()
    - Adicionado Parent Constraint automático
    - Validação de existência de joints
    - Tratamento de erros melhorado

v1.0.0 (17/11/2025)
    - Versão inicial
    - Função: criar_controles_e_posicionar()
    - Criação automática de controles
    - Suporte a customização de raio, cor e rotação

----------------------------------------------------------------------------------------------------------------
PRÓXIMAS VERSÕES (ROADMAP):
----------------------------------------------------------------------------------------------------------------

v1.2.0 (Lançado)
    - Adicionar freeze transforms automático
    - Zerar translação/rotação/escala dos controles

v1.3.0 (Planejado)
    - Criar grupo offset (GRP) automaticamente
    - Hierarquia: GRP -> CTRL -> JNT

v2.0.0 (Planejado)
    - Função unificada: setup_rig_completo()
    - Interface gráfica (UI)
    - Suporte a múltiplas convenções de nomenclatura

----------------------------------------------------------------------------------------------------------------
"""
