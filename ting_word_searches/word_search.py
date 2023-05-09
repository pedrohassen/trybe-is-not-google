def word_search(word, lines, complete=False):
    return [
        {"linha": i + 1, "conteudo": line} if complete else {"linha": i + 1}
        for i, line in enumerate(lines)
        if word.lower() in line.lower()
    ]


def exists_word(word, instance):
    word_list = []
    for i in range(len(instance)):
        file = instance.search(i)
        data = {"palavra": word, "arquivo": file["nome_do_arquivo"]}
        incomplete_ocurrencies = word_search(word, file["linhas_do_arquivo"])

        if len(incomplete_ocurrencies):
            data["ocorrencias"] = incomplete_ocurrencies
            word_list.append(data)
    return word_list


def search_by_word(word, instance):
    word_list = []
    for i in range(len(instance)):
        file = instance.search(i)
        data = {"palavra": word, "arquivo": file["nome_do_arquivo"]}
        complete_ocurrencies = word_search(
            word, file["linhas_do_arquivo"], True
        )

        if len(complete_ocurrencies):
            data["ocorrencias"] = complete_ocurrencies
            word_list.append(data)
    return word_list
