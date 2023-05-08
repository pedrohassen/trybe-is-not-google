from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    data = txt_importer(path_file)

    list_data = [
        instance.search(i)["nome_do_arquivo"] for i in range(len(instance))
    ]

    if path_file not in list_data:
        list_data = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(data),
            "linhas_do_arquivo": data,
        }

        instance.enqueue(list_data)
        sys.stdout.write(str(list_data))


def remove(instance):
    if len(instance) == 0:
        sys.stdout.write("Não há elementos\n")
    else:
        file_path = instance.dequeue()["nome_do_arquivo"]
        sys.stdout.write(
            f'Arquivo {file_path} removido com sucesso\n'
        )


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
