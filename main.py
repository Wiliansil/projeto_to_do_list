import argparse
from gerenciador import GerenciadorDeTarefas

def main():
    parser = argparse.ArgumentParser(description="Gerenciador de tarefas CLI em Python!")
    
    subparses = parser.add_subparsers(dest="comando", help="Comandos disponiveis")
    
    # Adicionar uma nova tarefa
    parser_adicionar = subparses.add_parser("adicionar", help="Adicionar uma nova tarefa")
    parser_adicionar.add_argument("titulo", type=str, help="Titulo da tarefa")
    parser_adicionar.add_argument("descricao", type=str, help="Descrição da tarefa")
    parser_adicionar.add_argument("data_vencimento", type=str, help="Data de vencimento no formato DD/MM/AAAA")
    
    # lISTAR TAREFAS
    parser_listar = subparses.add_parser("listar", help="Listar todas as tarefas")
    parser_listar.add_argument("--status", choices=["Pendente", "Concluida"], help="Filtrar por status da tarefa")
    
    # Editar tarefa
    parser_editar = subparses.add_parser("editar", help="Editar uma tarefa")
    parser_editar.add_argument("indice", type=int, help="Indice da tarefa a ser atualizada")
    parser_editar.add_argument("--tituto", type=str, help="Novo titulo da tarefa")
    parser_editar.add_argument("--descricao", type=str, help="Nova descrição da tarefa")
    parser_editar.add_argument("--data_vencimento", type=str, help="Nova data de vencimento no formato DD/MM/AAAA")
    
    # Remover tarefa
    parser_remover = subparses.add_parser("remover", help="Remover uma tarefa")
    parser_remover.add_argument("indice", type=int, help="Indice da tarefa a ser removida")
    
    # Marcar Tarefa como concluida
    parser_marcar_concluida = subparses.add_parser("concluir", help="Concluir uma tarefa")
    parser_marcar_concluida.add_argument("indice", type=int, help="Indice da tarefa a ser conluida")
    
    # Processar argumentos
    
    args = parser.parse_args()
    gerenciador = GerenciadorDeTarefas()
    
    if args.comando == "adicionar":
        gerenciador.adicionar_tarefa(args.titulo, args.descricao, args.data_vencimento)
    elif args.comando == "listar":
        gerenciador.listar_tarefas(args.status)
    elif args.comando == "editar":
        gerenciador.editar_tarefa(args.indice -1, args.titulo, args.descricao, args.data_vencimento)
    elif args.comando == "remover":
        gerenciador.remover_tarefa_tarefa(args.indice -1)
    elif args.comando == "concluir":
        gerenciador.marcar_concluida(args.indice -1)
    else:
        parser.print_help()
    
    
if __name__ == "__main__":
    main()