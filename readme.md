# Sistema Farol de Automação

Sistema de automação para bares e pequenos estabelecimentos. Desenvolvido em **Python 3**, com suporte a **SQLite** e duas interfaces:
- **GUI (Tkinter)**: interface gráfica, quando disponível.
- **CLI (linha de comando)**: alternativa funcional para ambientes sem suporte gráfico (sandbox/servidores/CI).

---

##  Funcionalidades
- **Caixa**: abertura, fechamento com controle de divergência.
- **Estoque**: cadastro de produtos (CRUD completo).
- **Vendas**: registro de vendas com verificação de estoque e transações atômicas.
- **Relatórios**: totais do dia, ticket médio, produtos mais vendidos.
- **Configurações**: espaço reservado para evoluções futuras (usuários, permissões, exportação de relatórios).

---

##  Instalação
Clone o repositório e entre na pasta do projeto:
```bash
git clone https://github.com/seu-usuario/farol-automacao.git
cd farol-automacao
```

Crie e ative um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

Não há dependências externas além do Python 3.x (Tkinter já vem incluído na maioria das distribuições, mas não é obrigatório).

---

## Uso
### Inicialização do banco
```bash
python app.py init-db
```

### Inserir produtos de demonstração
```bash
python app.py seed-demo
```

### Abrir caixa
```bash
python app.py open-caixa --valor 100
```

### Adicionar produto
```bash
python app.py add-produto --nome "Cerveja" --preco 12.5 --estoque 50
```

### Listar produtos
```bash
python app.py listar-produtos
```

### Registrar venda
```bash
python app.py vender --item 1:2 --item 2:1
```

### Relatório do dia
```bash
python app.py rel-dia
```

### Fechar caixa
```bash
python app.py fechar-caixa --informado 162.5
```

### Interface gráfica (se Tkinter disponível)
```bash
python app.py gui
```

### Executar testes automatizados
```bash
python app.py test
```

---

## Testes
A suíte de testes (`unittest`) cobre:
- Inicialização e relatórios sem vendas.
- CRUD de produtos.
- Fluxo de abertura/fechamento de caixa.
- Registro de vendas com verificação de estoque.
- Garantia de atomicidade em transações.
- Detecção de divergências no fechamento de caixa.

---

## Roadmap de Evoluções
- Rotina de ajuste de caixa em divergências.
- Gestão de usuários e permissões.
- Exportação de relatórios (CSV/PDF).
- Interface gráfica mais elaborada com telas customizadas.

---


