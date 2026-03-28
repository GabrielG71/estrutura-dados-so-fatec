#!/usr/bin/env python3
"""
gerar_pdf.py — Gerador de PDFs didáticos para FATEC Ourinhos
Usado pela skill fatec-estudo-pdf do Claude Code.

Uso via CLI:
    python3 gerar_pdf.py conteudo.json output.pdf

Uso via import:
    from gerar_pdf import gerar_pdf
    gerar_pdf(dados, "output/lista_encadeada.pdf")

Estrutura esperada do JSON de entrada:
{
  "topico": "Lista Encadeada Simples",
  "disciplina": "Estrutura de Dados",
  "data": "Março 2026",
  "secoes": [
    {
      "titulo": "Contexto / Motivação",
      "conteudo": [
        {"tipo": "texto",    "body": "..."},
        {"tipo": "subtitulo","body": "..."},
        {"tipo": "codigo",   "body": "...", "legenda": "opcional"},
        {"tipo": "diagrama", "body": "...", "legenda": "opcional"},
        {"tipo": "dica",     "body": "..."},
        {"tipo": "lista",    "items": ["item1", "item2"]},
        {"tipo": "tabela",   "cabecalho": ["Col1","Col2"], "linhas": [["a","b"],["c","d"]]}
      ]
    }
  ],
  "simulado": [
    {
      "numero": 1,
      "tipo": "conceitual",
      "enunciado": "...",
      "gabarito": "..."
    }
  ]
}
"""

import json
import sys
import os
from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm, cm
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Preformatted,
    Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.platypus.flowables import Flowable


# ─── Paleta de cores ───────────────────────────────────────────────────────────
COR_PRIMARIA      = colors.HexColor("#1A237E")   # azul escuro — cabeçalhos, capa
COR_SECUNDARIA    = colors.HexColor("#283593")   # azul médio — subtítulos
COR_DESTAQUE_BG   = colors.HexColor("#E8EAF6")   # lavanda — fundo de código
COR_DESTAQUE_BOR  = colors.HexColor("#3F51B5")   # azul — borda de código
COR_ALERTA_BG     = colors.HexColor("#FFF8E1")   # amarelo claro — dicas
COR_ALERTA_BOR    = colors.HexColor("#FF6F00")   # âmbar — borda de dicas
COR_SIMULADO_BG   = colors.HexColor("#F3E5F5")   # lilás claro — fundo simulado
COR_SIMULADO_BOR  = colors.HexColor("#7B1FA2")   # roxo — borda simulado
COR_TEXTO         = colors.HexColor("#212121")
COR_BRANCO        = colors.white
COR_CINZA_CLARO   = colors.HexColor("#ECEFF1")


# ─── Estilos de parágrafo ──────────────────────────────────────────────────────
def criar_estilos():
    estilos = getSampleStyleSheet()

    base = dict(
        fontName="Helvetica",
        fontSize=11,
        textColor=COR_TEXTO,
        leading=16,
        spaceAfter=6,
    )

    estilos.add(ParagraphStyle(
        name="CorpoTexto",
        alignment=TA_JUSTIFY,
        **base,
    ))
    estilos.add(ParagraphStyle(
        name="Secao",
        fontName="Helvetica-Bold",
        fontSize=16,
        textColor=COR_PRIMARIA,
        spaceBefore=18,
        spaceAfter=8,
        leading=20,
    ))
    estilos.add(ParagraphStyle(
        name="Subsecao",
        fontName="Helvetica-Bold",
        fontSize=13,
        textColor=COR_SECUNDARIA,
        spaceBefore=12,
        spaceAfter=6,
        leading=17,
    ))
    estilos.add(ParagraphStyle(
        name="Legenda",
        fontName="Helvetica-Oblique",
        fontSize=8,
        textColor=colors.HexColor("#555555"),
        alignment=TA_CENTER,
        spaceAfter=8,
    ))
    estilos.add(ParagraphStyle(
        name="ItemLista",
        fontName="Helvetica",
        fontSize=11,
        textColor=COR_TEXTO,
        leading=16,
        leftIndent=16,
        spaceAfter=3,
    ))
    estilos.add(ParagraphStyle(
        name="QuestaoNum",
        fontName="Helvetica-Bold",
        fontSize=11,
        textColor=COR_PRIMARIA,
        spaceBefore=10,
        spaceAfter=4,
    ))
    estilos.add(ParagraphStyle(
        name="QuestaoTexto",
        fontName="Helvetica",
        fontSize=11,
        textColor=COR_TEXTO,
        leading=16,
        spaceAfter=6,
        alignment=TA_JUSTIFY,
    ))
    estilos.add(ParagraphStyle(
        name="Gabarito",
        fontName="Helvetica",
        fontSize=10,
        textColor=colors.HexColor("#1B5E20"),
        leading=15,
        leftIndent=12,
        spaceAfter=4,
        alignment=TA_JUSTIFY,
    ))
    estilos.add(ParagraphStyle(
        name="Rodape",
        fontName="Helvetica",
        fontSize=8,
        textColor=colors.HexColor("#757575"),
        alignment=TA_CENTER,
    ))

    return estilos


# ─── Caixa de código ───────────────────────────────────────────────────────────
def bloco_codigo(body: str, legenda: str = "") -> list:
    """Retorna lista de flowables para um bloco de código estilizado."""
    flowables = []

    # Normaliza indentação (tabs → 4 espaços)
    body = body.replace("\t", "    ")

    # Caixa com fundo e borda esquerda
    data = [[Preformatted(body, ParagraphStyle(
        name="Codigo",
        fontName="Courier",
        fontSize=9,
        textColor=COR_TEXTO,
        leading=13,
        leftIndent=8,
        rightIndent=8,
    ))]]

    t = Table(data, colWidths=[165 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), COR_DESTAQUE_BG),
        ("LEFTPADDING",  (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING",   (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING",(0, 0), (-1, -1), 8),
        ("LINEBEFORE", (0, 0), (0, -1), 3, COR_DESTAQUE_BOR),
    ]))

    flowables.append(t)
    if legenda:
        estilos = criar_estilos()
        flowables.append(Paragraph(legenda, estilos["Legenda"]))
    flowables.append(Spacer(1, 4))
    return flowables


# ─── Caixa de dica / atenção ───────────────────────────────────────────────────
def bloco_dica(body: str) -> list:
    estilos = criar_estilos()
    data = [[Paragraph(f"<b>Dica:</b> {body}", estilos["CorpoTexto"])]]
    t = Table(data, colWidths=[165 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), COR_ALERTA_BG),
        ("LEFTPADDING",  (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING",   (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING",(0, 0), (-1, -1), 8),
        ("LINEBEFORE", (0, 0), (0, -1), 3, COR_ALERTA_BOR),
    ]))
    return [t, Spacer(1, 4)]


# ─── Tabela de conteúdo ────────────────────────────────────────────────────────
def bloco_tabela(cabecalho: list, linhas: list) -> list:
    data = [cabecalho] + linhas
    largura_col = 165 * mm / len(cabecalho)
    t = Table(data, colWidths=[largura_col] * len(cabecalho))
    t.setStyle(TableStyle([
        # Cabeçalho
        ("BACKGROUND",   (0, 0), (-1, 0),  COR_PRIMARIA),
        ("TEXTCOLOR",    (0, 0), (-1, 0),  COR_BRANCO),
        ("FONTNAME",     (0, 0), (-1, 0),  "Helvetica-Bold"),
        ("FONTSIZE",     (0, 0), (-1, 0),  10),
        ("ALIGN",        (0, 0), (-1, 0),  "CENTER"),
        # Corpo
        ("FONTNAME",     (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE",     (0, 1), (-1, -1), 10),
        ("ROWBACKGROUNDS",(0, 1),(-1, -1), [COR_BRANCO, COR_CINZA_CLARO]),
        ("ALIGN",        (0, 1), (-1, -1), "LEFT"),
        ("VALIGN",       (0, 0), (-1, -1), "MIDDLE"),
        # Grid
        ("GRID",         (0, 0), (-1, -1), 0.5, colors.HexColor("#B0BEC5")),
        ("TOPPADDING",   (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING",(0, 0), (-1, -1), 6),
        ("LEFTPADDING",  (0, 0), (-1, -1), 8),
    ]))
    return [t, Spacer(1, 8)]


# ─── Capa ──────────────────────────────────────────────────────────────────────
def construir_capa(canvas, doc, topico: str, disciplina: str, data: str):
    canvas.saveState()
    w, h = A4

    # Fundo azul escuro
    canvas.setFillColor(COR_PRIMARIA)
    canvas.rect(0, 0, w, h, fill=True, stroke=False)

    # Faixa inferior decorativa
    canvas.setFillColor(COR_SECUNDARIA)
    canvas.rect(0, 0, w, 60, fill=True, stroke=False)

    # Logo / instituição
    canvas.setFont("Helvetica-Bold", 14)
    canvas.setFillColor(COR_BRANCO)
    canvas.drawCentredString(w / 2, h - 80, "FATEC Ourinhos")
    canvas.setFont("Helvetica", 11)
    canvas.drawCentredString(w / 2, h - 100, "Análise e Desenvolvimento de Sistemas — 3.º Semestre")

    # Linha separadora
    canvas.setStrokeColor(colors.HexColor("#5C6BC0"))
    canvas.setLineWidth(1.5)
    canvas.line(50, h - 115, w - 50, h - 115)

    # Disciplina
    canvas.setFont("Helvetica", 16)
    canvas.setFillColor(colors.HexColor("#C5CAE9"))
    canvas.drawCentredString(w / 2, h / 2 + 80, disciplina.upper())

    # Título principal (tópico)
    canvas.setFont("Helvetica-Bold", 28)
    canvas.setFillColor(COR_BRANCO)
    # Quebra de linha automática simples para títulos longos
    palavras = topico.split()
    linhas = []
    linha_atual = []
    for p in palavras:
        linha_atual.append(p)
        if len(" ".join(linha_atual)) > 28:
            linhas.append(" ".join(linha_atual[:-1]))
            linha_atual = [p]
    linhas.append(" ".join(linha_atual))
    y = h / 2 + 30 + (len(linhas) - 1) * 20
    for linha in linhas:
        canvas.drawCentredString(w / 2, y, linha)
        y -= 40

    # Subtítulo "Material de Estudo"
    canvas.setFont("Helvetica", 13)
    canvas.setFillColor(colors.HexColor("#9FA8DA"))
    canvas.drawCentredString(w / 2, h / 2 - 30, "Material de Estudo com Simulado")

    # Data na faixa inferior
    canvas.setFont("Helvetica", 11)
    canvas.setFillColor(COR_BRANCO)
    canvas.drawCentredString(w / 2, 22, data)

    canvas.restoreState()


# ─── Cabeçalho e rodapé por página ────────────────────────────────────────────
def construir_header_footer(canvas, doc, topico: str, disciplina: str):
    canvas.saveState()
    w, h = A4

    # Cabeçalho
    canvas.setFillColor(COR_PRIMARIA)
    canvas.rect(0, h - 28, w, 28, fill=True, stroke=False)
    canvas.setFont("Helvetica", 9)
    canvas.setFillColor(COR_BRANCO)
    canvas.drawString(15, h - 18, f"{disciplina} — {topico}")
    canvas.drawRightString(w - 15, h - 18, f"Página {doc.page}")

    # Rodapé
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#757575"))
    canvas.drawCentredString(w / 2, 12, "FATEC Ourinhos · Material gerado via Claude Code")
    canvas.setStrokeColor(colors.HexColor("#E0E0E0"))
    canvas.line(15, 22, w - 15, 22)

    canvas.restoreState()


# ─── Seção de simulado ────────────────────────────────────────────────────────
def construir_simulado(questoes: list, estilos: dict) -> list:
    flowables = [PageBreak()]

    # Título do simulado
    titulo_data = [[Paragraph("SIMULADO", ParagraphStyle(
        name="TituloSim",
        fontName="Helvetica-Bold",
        fontSize=18,
        textColor=COR_BRANCO,
        alignment=TA_CENTER,
    ))]]
    t_titulo = Table(titulo_data, colWidths=[165 * mm])
    t_titulo.setStyle(TableStyle([
        ("BACKGROUND",   (0, 0), (-1, -1), COR_SIMULADO_BOR),
        ("TOPPADDING",   (0, 0), (-1, -1), 12),
        ("BOTTOMPADDING",(0, 0), (-1, -1), 12),
    ]))
    flowables.append(t_titulo)
    flowables.append(Spacer(1, 12))

    gabaritos = []

    for q in questoes:
        num = q.get("numero", "?")
        tipo = q.get("tipo", "")
        enunciado = q.get("enunciado", "")
        gabarito = q.get("gabarito", "")

        tipo_label = {
            "conceitual": "Conceitual",
            "codigo": "Código",
            "raciocinio": "Raciocínio",
            "dissertativa": "Dissertativa",
            "multipla": "Múltipla Escolha",
        }.get(tipo, tipo.capitalize())

        bloco_q = []
        bloco_q.append(Paragraph(
            f"Questão {num} <font color='#7B1FA2' size='9'>({tipo_label})</font>",
            estilos["QuestaoNum"]
        ))
        bloco_q.append(Paragraph(enunciado, estilos["QuestaoTexto"]))

        if tipo == "codigo":
            # Espaço para resposta em código
            bloco_q.append(Spacer(1, 4))
            bloco_q += bloco_codigo("// Escreva sua resposta aqui:\n\n\n\n")
        elif tipo in ("dissertativa", "conceitual", "raciocinio"):
            # Linhas para resposta escrita
            linhas_resp = "\n".join(["_" * 80] * 4)
            bloco_q += bloco_codigo(linhas_resp)
        elif tipo == "multipla":
            # Alternativas já vêm no enunciado; só espaço para marcar
            bloco_q.append(Spacer(1, 6))

        # Envolve em caixa lilás
        inner_table = Table(
            [[item] for item in bloco_q],
            colWidths=[155 * mm]
        )
        inner_table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), COR_SIMULADO_BG),
            ("LEFTPADDING",  (0, 0), (-1, -1), 10),
            ("RIGHTPADDING", (0, 0), (-1, -1), 8),
            ("TOPPADDING",   (0, 0), (-1, -1), 2),
            ("BOTTOMPADDING",(0, 0), (-1, -1), 2),
            ("LINEBEFORE", (0, 0), (0, -1), 3, COR_SIMULADO_BOR),
        ]))
        flowables.append(inner_table)
        flowables.append(Spacer(1, 8))

        if gabarito:
            gabaritos.append((num, tipo_label, gabarito))

    # ── Gabarito ──
    if gabaritos:
        flowables.append(Spacer(1, 16))
        flowables.append(HRFlowable(width="100%", thickness=1.5,
                                    color=COR_SIMULADO_BOR, spaceAfter=12))
        flowables.append(Paragraph(
            "GABARITO COMENTADO",
            ParagraphStyle(
                name="TituloGab",
                fontName="Helvetica-Bold",
                fontSize=14,
                textColor=COR_SIMULADO_BOR,
                spaceAfter=8,
            )
        ))
        for num, tipo_label, resp in gabaritos:
            flowables.append(Paragraph(
                f"<b>Questão {num}</b> ({tipo_label}):",
                estilos["QuestaoNum"]
            ))
            flowables.append(Paragraph(resp, estilos["Gabarito"]))
            flowables.append(Spacer(1, 6))

    return flowables


# ─── Construtor principal ──────────────────────────────────────────────────────
def gerar_pdf(dados: dict, caminho_saida: str) -> str:
    """
    Gera o PDF didático a partir do dict `dados` e salva em `caminho_saida`.
    Retorna o caminho absoluto do arquivo gerado.
    """
    topico     = dados.get("topico", "Tópico")
    disciplina = dados.get("disciplina", "Disciplina")
    data_str   = dados.get("data", datetime.now().strftime("%B %Y"))
    secoes     = dados.get("secoes", [])
    simulado   = dados.get("simulado", [])

    os.makedirs(os.path.dirname(os.path.abspath(caminho_saida)), exist_ok=True)

    doc = SimpleDocTemplate(
        caminho_saida,
        pagesize=A4,
        topMargin=35 * mm,
        bottomMargin=20 * mm,
        leftMargin=22 * mm,
        rightMargin=22 * mm,
        title=f"{disciplina} — {topico}",
        author="FATEC Ourinhos / Claude Code",
    )

    estilos = criar_estilos()
    story = []

    # ── Capa (página especial) ──
    # Ocupa a página 1 — o conteúdo real da capa é desenhado em onFirstPage
    story.append(Spacer(1, 1))
    story.append(PageBreak())

    # ── Seções de conteúdo ──
    for secao in secoes:
        titulo_sec = secao.get("titulo", "")
        conteudo   = secao.get("conteudo", [])

        bloco_sec = [Paragraph(titulo_sec, estilos["Secao"]),
                     HRFlowable(width="100%", thickness=1,
                                color=COR_PRIMARIA, spaceAfter=8)]

        for item in conteudo:
            tipo = item.get("tipo", "texto")
            body = item.get("body", "")

            if tipo == "texto":
                bloco_sec.append(Paragraph(body, estilos["CorpoTexto"]))

            elif tipo == "subtitulo":
                bloco_sec.append(Paragraph(body, estilos["Subsecao"]))

            elif tipo in ("codigo", "diagrama"):
                legenda = item.get("legenda", "")
                bloco_sec += bloco_codigo(body, legenda)

            elif tipo == "dica":
                bloco_sec += bloco_dica(body)

            elif tipo == "lista":
                items = item.get("items", [])
                for it in items:
                    bloco_sec.append(Paragraph(f"• {it}", estilos["ItemLista"]))
                bloco_sec.append(Spacer(1, 4))

            elif tipo == "tabela":
                cabecalho = item.get("cabecalho", [])
                linhas    = item.get("linhas", [])
                if cabecalho and linhas:
                    bloco_sec += bloco_tabela(cabecalho, linhas)

        story += bloco_sec
        story.append(Spacer(1, 8))

    # ── Simulado ──
    if simulado:
        story += construir_simulado(simulado, estilos)

    # ── Build com callbacks de página ──
    pagina_atual = [0]

    def on_page(canvas, doc):
        pagina_atual[0] += 1
        if pagina_atual[0] == 1:
            construir_capa(canvas, doc, topico, disciplina, data_str)
        else:
            construir_header_footer(canvas, doc, topico, disciplina)

    doc.build(story, onFirstPage=on_page, onLaterPages=on_page)

    return os.path.abspath(caminho_saida)


# ─── CLI ───────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python3 gerar_pdf.py <conteudo.json> <saida.pdf>")
        sys.exit(1)

    json_path = sys.argv[1]
    pdf_path  = sys.argv[2]

    with open(json_path, "r", encoding="utf-8") as f:
        dados = json.load(f)

    caminho = gerar_pdf(dados, pdf_path)
    print(f"PDF gerado: {caminho}")
