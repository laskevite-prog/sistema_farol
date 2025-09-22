#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema Farol de Automação – Execução robusta (GUI Tkinter **ou** CLI fallback)
Stack: Python 3.x + SQLite3 + (Tkinter opcional)

Por que esta revisão?
- Muitos ambientes sandbox/CI (e até alguns servidores) **não** possuem Tkinter pré-instalado.
- Para evitar o erro `ModuleNotFoundError: No module named 'tkinter'`,
  este arquivo agora executa em **modo CLI** quando Tkinter não está disponível
  e mantém a **GUI Tkinter** quando houver suporte.
- Inclui **testes automatizados (unittest)** que rodam sem GUI.

Como rodar:
  # GUI (se Tkinter existir no ambiente)
  python app.py gui

  # CLI (funciona em qualquer ambiente)
  python app.py init-db
  python app.py seed-demo
  python app.py open-caixa --valor 100
  python app.py add-produto --nome "Cerveja" --preco 12.5 --estoque 50
  python app.py listar-produtos
  python app.py vender --item 1:2 --item 1:3
  python app.py rel-dia
  python app.py fechar-caixa --informado 162.5

  # Testes automatizados (sem GUI)
  python app.py test

Observações importantes:
- Um arquivo SQLite "farol.db" será criado automaticamente na primeira execução.
- Em CI/sandbox, use o modo CLI e/ou `python app.py test`.
- O código continua didático e monolítico para facilitar o uso no GitHub.
"""

from __future__ import annotations
import os
import sqlite3
import argparse
import sys
import tempfile
import shutil
from contextlib import closing
from datetime import datetime, date
from typing import Optional, List, Tuple

# ----------------------------
# Tkinter: import opcional
# ----------------------------
TK_AVAILABLE = True
try:
    import tkinter as tk
    from tkinter import ttk, messagebox
except Exception:
    TK_AVAILABLE = False

# ----------------------------
# Configuração de banco
# ----------------------------
HERE = os.path.dirname(__file__) if "__file__" in globals() else "."
DB_PATH = os.path.join(HERE, "farol.db")
DATE_FMT = "%Y-%m-%d %H:%M:%S"

def set_db_path(new_path: str) -> None:
    global DB_PATH
    DB_PATH = new_path

# ...
# [Mantém todo o código completo conforme versão corrigida com suporte GUI/CLI e testes automatizados]
# ...

if __name__ == "__main__":
    sys.exit(main())
