from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    data = txt_importer(path_file)

    list_data = [
        instance.search(i)["nome_do_arquivo"] for i in range(len(instance))
    ]

    if path_file not in list_data:
        processed_data = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(data),
            "linhas_do_arquivo": data,
        }

        instance.enqueue(processed_data)
        sys.stdout.write(str(processed_data))


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
