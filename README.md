#  Sistema de Biblioteca Digital

Sistema de gerenciamento de documentos digitais desenvolvido em Python para a biblioteca universitária.

## Funcionalidades

- Listar documentos por tipo de arquivo (PDF, ePUB, DOCX, TXT, MOBI)
- Listar documentos por ano de publicação
- Adicionar novos documentos ao repositório
- Renomear documentos existentes
- Remover documentos

## Como usar

### Pré-requisitos

- Python 3.7 ou superior
- Sem dependências externas — usa apenas bibliotecas padrão do Python

### Executar o sistema

```bash
python biblioteca.py
```

Ao iniciar, o sistema vai pedir o diretório onde estão os documentos. Pressione Enter para usar o diretório atual.

### Menu de opções

```
1. Listar documentos por tipo
2. Listar documentos por ano
3. Adicionar documento
4. Renomear documento
5. Remover documento
0. Sair
```

### Formatos suportados

| Extensão | Tipo |
|----------|------|
| .pdf | Artigos, teses, livros |
| .epub | Livros digitais |
| .docx | Documentos Word |
| .txt | Arquivos de texto |
| .mobi | E-books Kindle |

## Executar os testes

```bash
python test_biblioteca.py
```

## Estrutura do projeto

```
biblioteca-digital/
├── biblioteca.py         # Sistema principal
├── test_biblioteca.py    # Testes automatizados
├── CONTRIBUTING.md       # Guia de contribuição
└── README.md             # Esta documentação
```

## Como contribuir

Veja o arquivo [CONTRIBUTING.md](CONTRIBUTING.md) para detalhes sobre como contribuir com o projeto.
