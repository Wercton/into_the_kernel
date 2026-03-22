# 🎮 Into the Kernel

**Into the Kernel** é um jogo tático em grade desenvolvido com Pygame, onde cada ação ocorre em turnos e exige planejamento estratégico.

Você controla um agente infiltrado em um ambiente hostil. Seu objetivo é:

- alcançar um terminal (`T`)
- realizar o hack
- escapar pelo ponto de saída (`E`) sem ser detectado

Durante a missão:

- guardas patrulham o mapa
- o jogador perde ao ser visto ou ao colidir com um inimigo

A proposta do jogo combina **stealth**, **raciocínio lógico** e **tomada de decisão por turnos**.

---

## 🚀 Tecnologias

- Python 3.11
- Pygame
- GitHub Actions (CI)
- Flake8 (lint)
- Black (code formatter)

---

## 🧩 Estrutura do Projeto

```

.
├── src/
│   ├── main.py
│   ├── config.py
│   ├── game/
│   │   ├── game.py
│   │   ├── renderer.py
│   │   └── **init**.py
│   └── **init**.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── pyproject.toml
├── requirements.txt
├── CHANGELOG.md
└── README.md

````

### 📌 Organização

- `main.py` → ponto de entrada
- `game.py` → loop principal e controle do jogo
- `renderer.py` → renderização do mapa
- `config.py` → constantes globais

Separação pensada para facilitar evolução (player, IA, sistema de turnos).

---

## 🗺️ Mapa

O cenário é definido por um array de strings:

| Símbolo | Significado |
|--------|------------|
| `.` | chão |
| `#` | parede |
| `T` | terminal |
| `E` | saída |

## ▶️ Como executar

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt

python -m src.main
````

---

## 🎨 Padronização de Código

O projeto utiliza **Black** para formatação automática.

### Rodar localmente:

```bash
black src
```

### Verificar (modo CI):

```bash
black --check src
```

---

## 🔍 Qualidade de Código

Lint com **flake8**:

```bash
flake8 src
```

---

## 🔄 Integração Contínua (CI)

A pipeline executa automaticamente:

* Instalação de dependências
* Verificação de formatação (**black**)
* Análise estática (**flake8**)

Falhas impedem integração na branch principal.

---

## 🌿 Estratégia de Branches

O projeto adota um fluxo simples inspirado em Git Flow:

- `main` → branch estável (produção)
- `develop` → branch de integração

### 🔄 Fluxo de trabalho

1. Desenvolvimento é feito na branch `develop`
2. Cada alteração passa pela pipeline de CI:
   - formatação (black)
   - lint (flake8)
3. Após validação, é aberto um Pull Request para `main`
4. O código só é integrado à `main` após aprovação

Esse fluxo garante que a branch principal permaneça sempre estável e validada.

---

# 🧠 Reflexão Técnica

## Decisões técnicas mais relevantes na construção do pipeline

Foi adotada uma pipeline enxuta com foco em qualidade de código, utilizando **flake8** e **black**.
A separação entre verificação de estilo e formatação automática garante consistência sem introduzir complexidade excessiva.

Além disso, a execução em ambiente limpo (GitHub Actions) assegura reprodutibilidade e elimina dependência de configurações locais.

---

## Impactos da ausência de testes automatizados

A ausência de testes limita a validação ao nível sintático e estrutural.
Isso implica que erros de lógica ou regressões não são detectados automaticamente, aumentando o risco conforme o projeto cresce.

---

## Possibilidades reais de evolução para Entrega Contínua

O projeto pode evoluir com:

* adoção de testes automatizados (pytest)
* pipeline de build
* versionamento automatizado (SemVer + tags)
* validação de regras de jogo

Isso permitiria transformar a pipeline em um fluxo completo de entrega contínua.

---

## Riscos técnicos mitigados pela Integração Contínua

A CI mitiga:

* inconsistência de código entre desenvolvedores
* erros de sintaxe e estilo
* dependência de ambiente local

Também impõe disciplina mínima antes da integração.

---

## 📌 Próximos passos

* Sistema de player
* Movimento por turnos
* IA de guardas
* Sistema de detecção (campo de visão)
* Testes automatizados

---

Se quiser dar um próximo salto, o README pode incluir:

- GIF do jogo rodando  
- badge do GitHub Actions  
- seção de arquitetura mais detalhada  

Mas, para contexto acadêmico, esse já está bem sólido.
