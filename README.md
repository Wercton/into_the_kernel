# 🎮 Into the Kernel

**Into the Kernel** é um jogo tático em grade em desenvolvimento com Pygame, onde cada ação do jogador ocorre em turnos e exige planejamento estratégico.

Você controla um agente infiltrado em um ambiente hostil, representado por um mapa 15x10. Seu objetivo é:

- alcançar um terminal (`T`)
- realizar o hack
- escapar pelo ponto de saída (`E`) sem ser detectado

Durante a missão:

- guardas patrulham o mapa
- o jogador perde se for visto ou encostar em um inimigo

A dinâmica por turnos transforma cada movimento em uma decisão crítica, combinando elementos de stealth e raciocínio lógico.

---

## 🚀 Tecnologias

- Python 3.11
- Pygame
- GitHub Actions (CI)
- Flake8 (lint)

---

## 🧩 Estrutura do Projeto

```

.
├── src/
│   ├── main.py
│   ├── config.py
│   └── **init**.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── requirements.txt
├── .flake8
|── .gitignore
├── CHANGELOG.md
└── README.md

````

---

## 🗺️ Mapa

O cenário é definido por um array de strings:

- `.` → chão  
- `#` → parede  
- `T` → terminal  
- `E` → saída  

---

## ▶️ Como executar

```bash
python -m venv venv
source venv/bin/activate  # ou Windows equivalente
pip install -r requirements.txt

python -m src.main
````

---

## 🔄 Integração Contínua (CI)

A pipeline executa automaticamente:

* Instalação de dependências
* Verificação de código com **flake8**

Falhas de lint impedem merges na branch principal.

---

# 🧠 Reflexão Técnica

## Decisões técnicas mais relevantes na construção do pipeline

A principal decisão foi adotar uma pipeline simples e determinística, focada em linting com **flake8**. Isso garante padronização de código e detecção precoce de problemas sem introduzir complexidade excessiva.
Também foi adotado o uso de ambiente limpo (`ubuntu-latest`) e instalação explícita de dependências, evitando efeitos colaterais de ambiente local.

---

## Impactos da ausência de testes automatizados

A ausência de testes reduz significativamente a confiabilidade da pipeline. Embora o linting valide aspectos sintáticos e de estilo, não há verificação de comportamento ou regressões.
Isso implica que mudanças podem quebrar funcionalidades sem serem detectadas automaticamente, aumentando o risco em evoluções futuras.

---

## Possibilidades reais de evolução para Entrega Contínua

O projeto pode evoluir para Entrega Contínua com:

* Adição de testes automatizados (ex: pytest)
* Geração de artefatos (builds do jogo)
* Versionamento automatizado (SemVer + tags)
* Pipeline separada para deploy

Isso permitiria que cada alteração validada fosse potencialmente liberada de forma automatizada.

---

## Riscos técnicos mitigados pela Integração Contínua

A CI mitiga principalmente:

* Introdução de código com erros de sintaxe
* Inconsistência de estilo entre commits
* Problemas de ambiente (“funciona na minha máquina”)

Além disso, força uma disciplina mínima de qualidade antes da integração na branch principal.

---

## 📌 Próximos passos

* Implementar movimentação do player
* Adicionar sistema de colisão
* Introduzir testes automatizados
* Evoluir arquitetura do projeto
