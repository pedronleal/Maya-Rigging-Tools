# 🎮 Rigging Tools - Maya Python Automation

![Maya Version](https://img.shields.io/badge/Maya-2024-blue)
![Python Version](https://img.shields.io/badge/Python-3.7+-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Active-success)

> Ferramentas de rigging automatizadas para Autodesk Maya, desenvolvidas com foco em produtividade e pipeline profissional.

---

## 📋 Índice

- [Sobre](#sobre)
- [Funcionalidades](#funcionalidades)
- [Instalação](#instalação)
- [Uso](#uso)
- [Exemplos](#exemplos)
- [Parâmetros](#parâmetros)
- [Roadmap](#roadmap)
- [Contribuindo](#contribuindo)
- [Licença](#licença)
- [Contato](#contato)

---

## 🎯 Sobre

Este projeto nasceu da necessidade de **automatizar tarefas repetitivas** no processo de rigging. A ferramenta permite criar controles NURBS para joints de forma rápida e consistente, com customização total de aparência e orientação.

### Por que este projeto existe?

- ⏱️ **Economia de tempo**: Reduz criação manual de controles de minutos para segundos
- 🎨 **Consistência visual**: Todos os controles seguem o mesmo padrão de nomenclatura e cor
- 🔧 **Flexibilidade**: Parâmetros customizáveis para diferentes necessidades
- 📚 **Aprendizado**: Código documentado para estudantes e profissionais

---

## ✨ Funcionalidades

### v1.0.0 (Atual)

- ✅ Criação automática de controles NURBS circulares
- ✅ Nomenclatura inteligente baseada nos joints (`joint_JNT` → `joint_CTRL`)
- ✅ Posicionamento automático na localização exata do joint
- ✅ Customização de tamanho (raio)
- ✅ Sistema de cores com 31 opções do Maya
- ✅ Rotação customizável em qualquer eixo
- ✅ Tratamento de erros com mensagens claras
- ✅ Código totalmente documentado

---

## 💾 Instalação

### Método 1: Copiar e Colar (Mais Rápido)

1. Abra o **Script Editor** do Maya (`Windows → General Editors → Script Editor`)
2. Crie uma nova aba **Python**
3. Cole o código de `criar_controle.py`
4. Execute ou salve como shelf button

### Método 2: Arquivo Externo (Recomendado)

1. Salve `criar_controle.py` em uma pasta de scripts do Maya:
```
   Windows: C:/Users/SEU_USUARIO/Documents/maya/scripts/
   Mac: ~/Library/Preferences/Autodesk/maya/scripts/
   Linux: ~/maya/scripts/
```

2. No Maya, execute:
```python
   import criar_controle
   criar_controle.criar_controles_e_posicionar()
```

3. **(Opcional)** Adicione à shelf para acesso rápido

---

## 🚀 Uso

### Uso Básico
```python
# 1. Selecione um joint no Maya
# 2. Execute:
criar_controles_e_posicionar()

# Resultado: Controle vermelho, raio 10, rotacionado 90° em Y
```

### Uso Avançado
```python
# Controle pequeno e azul
criar_controles_e_posicionar(raio=5, cor=6)

# Controle grande, amarelo, sem rotação
criar_controles_e_posicionar(raio=20, cor=17, rotacao=(0, 0, 0))

# Controle médio, verde, rotacionado 90° em X
criar_controles_e_posicionar(raio=12, cor=14, rotacao=(90, 0, 0))
```


---

## 📸 Exemplos

### Exemplo 1: Rig de Braço
```python
# Criar controles para clavícula, ombro, cotovelo e pulso
# Com tamanhos diferentes para hierarquia visual

# Clavícula (grande)
# Selecione clavicle_JNT
criar_controles_e_posicionar(raio=15, cor=13)

# Ombro (médio)
# Selecione shoulder_JNT
criar_controles_e_posicionar(raio=12, cor=13)

# Cotovelo (médio)
# Selecione elbow_JNT
criar_controles_e_posicionar(raio=10, cor=13)

# Pulso (pequeno)
# Selecione wrist_JNT
criar_controles_e_posicionar(raio=8, cor=13)
```

### Exemplo 2: Rig de Mão
```python
# Controles pequenos e azuis para dedos
# Selecione todos os joints dos dedos

criar_controles_e_posicionar(raio=3, cor=6, rotacao=(0, 0, 90))
```

## 📸 Galeria

### Controles criados automaticamente
![Exemplo 1] (screenshots)

### Controles tamanhos e cores]
![Exemplo 2] (screenshots)

### Código em ação
![Exemplo 3] (screenshots)



---

## ⚙️ Parâmetros

| Parâmetro | Tipo | Padrão | Descrição |
|-----------|------|--------|-----------|
| `raio` | float | 10 | Tamanho do controle NURBS |
| `cor` | int | 13 | Índice de cor do Maya (0-31) |
| `rotacao` | tuple | (0, 90, 0) | Rotação (X, Y, Z) em graus |

### 🎨 Tabela de Cores do Maya

| Índice | Cor | Uso Comum |
|--------|-----|-----------|
| 6 | Azul | Controles do lado direito |
| 13 | Vermelho | Controles do lado esquerdo |
| 14 | Verde | Controles do centro |
| 17 | Amarelo | Controles principais/raiz |
| 18 | Ciano | Controles IK |

---

## 🗺️ Roadmap

### v1.1.0 (Próxima versão)
- [ ] Suporte para múltiplos joints simultaneamente (loop)
- [ ] Shapes customizadas (quadrado, triângulo, estrela)
- [ ] Presets de cores por tipo de controle
- [ ] Função deundo/redo integrada

### v1.2.0 (Futuro)
- [ ] Interface gráfica (GUI) no Maya
- [ ] Criação automática de hierarquia de controles
- [ ] Parent constraints automatizados
- [ ] Lock & Hide atributos desnecessários

### v2.0.0 (Visão de longo prazo)
- [ ] Pipeline completo de auto-rigging
- [ ] Suporte para FK/IK switching
- [ ] Templates de rigs pré-configurados
- [ ] Integração com Motion Capture

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Se você quer melhorar este projeto:

1. Fork o repositório
2. Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

### Guidelines

- Mantenha a documentação atualizada
- Adicione testes quando possível
- Siga o padrão de código existente
- Atualize o CHANGELOG

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
```
MIT License

Copyright (c) 2025 Pedro Leal

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software...
```

---

## 👤 Contato

**Pedro Leal**

- Portfolio: [pedronleal] https://www.artstation.com/pedronleal
- LinkedIn: https://www.linkedin.com/in/pedronleal12/
- Email: pedronaimayer@outlook.com
- GitHub: [pedronleal] https://github.com/pedronleal

---

## 🙏 Agradecimentos

- Comunidade Maya Python
- Feedback de colegas riggers

---

## 📊 Estatísticas do Projeto

![GitHub stars](https://img.shields.io/github/stars/seu-usuario/maya-rigging-tools?style=social)
![GitHub forks](https://img.shields.io/github/forks/seu-usuario/maya-rigging-tools?style=social)
![GitHub issues](https://img.shields.io/github/issues/seu-usuario/maya-rigging-tools)

---

<div align="center">

**Feito com ❤️ e ☕ por Pedro Leal**

[⬆ Voltar ao topo](#-rigging-tools---maya-python-automation)


</div>
