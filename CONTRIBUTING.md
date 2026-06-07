bash

cat /home/claude/CONTRIBUTING.md
Saída

# Guia de Contribuição

Obrigada pelo interesse em contribuir com o Sistema de Biblioteca Digital!

## Como contribuir

### 1. Fork e clone do repositório

```bash
git clone https://github.com/Drileensalles-Ops/biblioteca-digital.git
cd biblioteca-digital
```

### 2. Crie uma branch para sua contribuição

```bash
git checkout -b minha-funcionalidade
```

### 3. Faça suas alterações

Edite os arquivos necessários e teste suas mudanças:

```bash
python test_biblioteca.py
```

### 4. Commit das alterações

Use mensagens de commit claras e descritivas:

```bash
git add .
git commit -m "feat: adiciona busca de documentos por título"
```

**Padrão de commits:**
- `feat:` nova funcionalidade
- `fix:` correção de bug
- `docs:` atualização de documentação
- `test:` adição ou correção de testes

### 5. Push e Pull Request

```bash
git push origin minha-funcionalidade
```

Acesse o repositório no GitHub e clique em **"New Pull Request"**. Descreva o que foi alterado e por quê.

## Boas práticas

- Escreva código limpo e comentado
- Adicione testes para novas funcionalidades
- Mantenha o README atualizado
- Respeite o estilo de código já existente
Concluído
