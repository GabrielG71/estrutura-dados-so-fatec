---
name: fatec-estudo-pdf
description: >
  Use this skill whenever Gabriel asks to create a study PDF, educational document, or simulado
  (mock exam) for any topic from his FATEC Ourinhos coursework — Estrutura de Dados (C99) or
  Sistemas Operacionais (Tanenbaum-based theory). Triggers on Portuguese phrases like "cria um
  PDF de", "me faz um material de", "gera um PDF explicando", "faz um simulado sobre", "quero
  estudar [tópico]", "resumo em PDF", "material de estudo", "apostila de", as well as English
  equivalents. Also use when Gabriel asks for exam prep, printed study guides, or concept
  explanations that should be saved as a document — not just answered in chat. The whole point
  of this skill is producing an actual .pdf file; if the user wants a PDF, use this skill rather
  than writing markdown.
---

# FATEC Estudo PDF

Skill para gerar PDFs didáticos e bonitos para estudo das disciplinas de **Estrutura de Dados** (C99)
e **Sistemas Operacionais** (teórico, base Tanenbaum) do curso de ADS — FATEC Ourinhos.

## Contexto do usuário

Gabriel é engenheiro de software profissional (TypeScript, PHP, Python), no 3.º semestre de ADS.
**Não explicar o básico de programação.** Ir direto aos conceitos do curso. Nível: intermediário-
avançado em CS, mas iniciante nos tópicos acadêmicos específicos que o semestre está cobrindo.

---

## Fluxo de execução

1. **Identificar** tópico e disciplina (ED ou SO)
2. **Confirmar escopo** se ambíguo (ex: "quer toda a BST ou só inserção/busca?")
3. **Ler a referência** relevante: `references/ed_topicos.md` para ED, `references/so_topicos.md`
   para SO — os pontos cobrados em prova estão lá
4. **Compor o dict `dados`** com toda a estrutura abaixo (seções de conteúdo + simulado)
5. **Chamar o gerador**:
   ```python
   import sys
   sys.path.insert(0, '.claude/skills/fatec-estudo-pdf/scripts')
   from gerar_pdf import gerar_pdf
   caminho = gerar_pdf(dados, "estrutura-de-dados/aa10/bst.pdf")
   print(f"PDF gerado: {caminho}")
   ```
6. **Salvar** em `estrutura-de-dados/<aa0X>/` ou `sistemas-operacionais/<aa0X>/` conforme o tópico
7. **Reportar** o caminho do arquivo gerado ao usuário

> O script em `scripts/gerar_pdf.py` cuida de toda a formatação reportlab (capa, cores, fontes,
> caixas de código, simulado). Seu trabalho é produzir o dict `dados` com conteúdo rico.

---

## Estrutura do dict `dados`

```python
dados = {
  "topico": "Árvore Binária de Busca (BST)",   # aparece na capa e no cabeçalho
  "disciplina": "Estrutura de Dados",            # "Estrutura de Dados" ou "Sistemas Operacionais"
  "data": "Março 2026",

  "secoes": [
    {
      "titulo": "Contexto / Motivação",          # nome da seção (H1 no PDF)
      "conteudo": [
        # --- Tipos de item disponíveis ---
        {"tipo": "texto",     "body": "Texto corrido justificado..."},
        {"tipo": "subtitulo", "body": "Subtítulo da subseção"},
        {"tipo": "codigo",    "body": "int x = 42;\n// comentário", "legenda": "Código 1 — descrição"},
        {"tipo": "diagrama",  "body": "ASCII art aqui",             "legenda": "Figura 1 — descrição"},
        {"tipo": "dica",      "body": "Texto da dica (caixa âmbar)"},
        {"tipo": "lista",     "items": ["item 1", "item 2", "item 3"]},
        {"tipo": "tabela",
         "cabecalho": ["Operação", "Complexidade", "Observação"],
         "linhas":    [["Inserir", "O(log n)", "médio"], ["Buscar", "O(log n)", "médio"]]},
      ]
    },
    # ... mais seções ...
  ],

  "simulado": [
    {
      "numero": 1,
      "tipo": "conceitual",    # conceitual | codigo | raciocinio | dissertativa | multipla
      "enunciado": "Pergunta ou código a analisar...",
      "gabarito": "Resposta comentada que aparece no gabarito ao final"
    },
    # ... mais questões ...
  ]
}
```

---

## Estrutura obrigatória das seções

Todo PDF deve cobrir esta progressão — adapte os títulos ao tópico:

1. **Contexto / Motivação** — Qual problema essa estrutura/conceito resolve? Por que existe?
2. **Como funciona** — Explicação técnica com diagramas ASCII quando útil
3. **Implementação / Exemplo concreto**
   - ED: código C99 comentado (estilo do repositório — veja CLAUDE.md seção 7)
   - SO: exemplo real no Linux (comandos, syscalls, pseudocódigo com `pthread`, etc.)
4. **Complexidade e trade-offs** — Big-O para ED; implicações de design para SO
5. **Comparativo** — Relacionar com estruturas/conceitos já vistos (quando relevante)
6. **Simulado** — ver seção abaixo

---

## Simulado (sempre incluir)

### Para Estrutura de Dados:
- 3–4 questões `conceitual` — diferença entre estruturas, complexidade, ponteiros
- 2–3 questões `codigo` — completar função em C, identificar bug, escrever trecho
- 1–2 questões `raciocinio` — traçar execução de operação, desenhar estado da memória
- Gabarito comentado (gerado automaticamente pela seção `"gabarito"` de cada questão)

### Para Sistemas Operacionais:
- 3–4 questões `dissertativa` — 3 a 5 linhas de resposta esperada
- 2–3 questões `multipla` — alternativas já no enunciado (ex: "a) ... b) ... c) ...")
- 1 questão sobre problema clássico quando o tema tocar concorrência/sincronização

---

## Diagramas ASCII para ED

Incluir pelo menos um diagrama mostrando estado da memória. Padrões:

```
Lista:   [dado|*] --> [dado|*] --> [dado|NULL]
           ^
         cabeca

Pilha:   TOP → | 30 |
               | 20 |
               | 10 |
               └────┘

BST:         [50]
            /    \
         [30]    [70]
         /  \    /  \
       [20][40][60][80]
```

Adapte o diagrama ao estado específico explicado (após inserção, após remoção, etc.).

---

## Tratamento de erros

- `reportlab` não instalado: `pip install reportlab`
- Não usar Unicode de subscript/superscript (₀¹²) — escrever por extenso (ex: "O(n^2)")
- Código C longo: dividir em múltiplos blocos `{"tipo": "codigo", ...}` com legendas sequenciais
- Caminho de saída: sempre passar o diretório correto da AA correspondente ao tópico