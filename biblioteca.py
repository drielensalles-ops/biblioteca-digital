import os
import shutil
from datetime import datetime

# Extensoes suportadas
EXTENSOES = ['.pdf', '.epub', '.docx', '.txt', '.mobi']

def listar_documentos(diretorio='.'):
    """Lista todos os documentos organizados por tipo e ano."""
    por_tipo = {}
    por_ano = {}

    for raiz, dirs, arquivos in os.walk(diretorio):
        for arquivo in arquivos:
            ext = os.path.splitext(arquivo)[1].lower()
            if ext in EXTENSOES:
                caminho = os.path.join(raiz, arquivo)
                # Organizar por tipo
                if ext not in por_tipo:
                    por_tipo[ext] = []
                por_tipo[ext].append(arquivo)

                # Organizar por ano (data de modificacao)
                ano = str(datetime.fromtimestamp(os.path.getmtime(caminho)).year)
                if ano not in por_ano:
                    por_ano[ano] = []
                por_ano[ano].append(arquivo)

    return por_tipo, por_ano

def adicionar_documento(origem, destino='.'):
    """Adiciona um documento ao repositorio."""
    if not os.path.exists(origem):
        print(f"Erro: arquivo '{origem}' nao encontrado.")
        return False
    ext = os.path.splitext(origem)[1].lower()
    if ext not in EXTENSOES:
        print(f"Erro: extensao '{ext}' nao suportada.")
        return False
    shutil.copy2(origem, destino)
    print(f"Documento '{os.path.basename(origem)}' adicionado com sucesso!")
    return True

def renomear_documento(nome_atual, novo_nome, diretorio='.'):
    """Renomeia um documento existente."""
    caminho_atual = os.path.join(diretorio, nome_atual)
    caminho_novo = os.path.join(diretorio, novo_nome)
    if not os.path.exists(caminho_atual):
        print(f"Erro: arquivo '{nome_atual}' nao encontrado.")
        return False
    os.rename(caminho_atual, caminho_novo)
    print(f"Documento renomeado para '{novo_nome}' com sucesso!")
    return True

def remover_documento(nome_arquivo, diretorio='.'):
    """Remove um documento do repositorio."""
    caminho = os.path.join(diretorio, nome_arquivo)
    if not os.path.exists(caminho):
        print(f"Erro: arquivo '{nome_arquivo}' nao encontrado.")
        return False
    os.remove(caminho)
    print(f"Documento '{nome_arquivo}' removido com sucesso!")
    return True

def exibir_menu():
    """Exibe o menu principal."""
    print("\n" + "="*50)
    print("  SISTEMA DE BIBLIOTECA DIGITAL")
    print("="*50)
    print("1. Listar documentos por tipo")
    print("2. Listar documentos por ano")
    print("3. Adicionar documento")
    print("4. Renomear documento")
    print("5. Remover documento")
    print("0. Sair")
    print("="*50)

def main():
    """Interface de linha de comando principal."""
    diretorio = input("Digite o diretorio da biblioteca (Enter para usar o atual): ").strip()
    if not diretorio:
        diretorio = '.'
    if not os.path.exists(diretorio):
        print(f"Diretorio '{diretorio}' nao encontrado. Usando diretorio atual.")
        diretorio = '.'

    while True:
        exibir_menu()
        opcao = input("Escolha uma opcao: ").strip()

        if opcao == '1':
            por_tipo, _ = listar_documentos(diretorio)
            if not por_tipo:
                print("\nNenhum documento encontrado.")
            else:
                print("\n--- Documentos por Tipo ---")
                for tipo, arquivos in sorted(por_tipo.items()):
                    print(f"\n{tipo.upper()} ({len(arquivos)} arquivo(s)):")
                    for arq in arquivos:
                        print(f"  - {arq}")

        elif opcao == '2':
            _, por_ano = listar_documentos(diretorio)
            if not por_ano:
                print("\nNenhum documento encontrado.")
            else:
                print("\n--- Documentos por Ano ---")
                for ano, arquivos in sorted(por_ano.items(), reverse=True):
                    print(f"\n{ano} ({len(arquivos)} arquivo(s)):")
                    for arq in arquivos:
                        print(f"  - {arq}")

        elif opcao == '3':
            origem = input("Caminho completo do arquivo a adicionar: ").strip()
            adicionar_documento(origem, diretorio)

        elif opcao == '4':
            nome_atual = input("Nome atual do arquivo: ").strip()
            novo_nome = input("Novo nome do arquivo: ").strip()
            renomear_documento(nome_atual, novo_nome, diretorio)

        elif opcao == '5':
            nome = input("Nome do arquivo a remover: ").strip()
            confirmacao = input(f"Confirma remocao de '{nome}'? (s/n): ").strip().lower()
            if confirmacao == 's':
                remover_documento(nome, diretorio)
            else:
                print("Operacao cancelada.")

        elif opcao == '0':
            print("\nSaindo do sistema. Ate logo!")
            break

        else:
            print("Opcao invalida. Tente novamente.")

if __name__ == "__main__":
    main()
