from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    mock = [
        {
            "nome_do_arquivo": "mock1.txt",
            "qtd_linhas": 4,
            "linhas_do_arquivo": ["Eu sou um mock"],
        },
        {
            "nome_do_arquivo": "mock2.txt",
            "qtd_linhas": 17,
            "linhas_do_arquivo": ["Eu também sou um mock"],
        },
    ]

    instance = PriorityQueue()

    instance.enqueue(mock[1])
    assert len(instance.high_priority) == 0
    assert len(instance.regular_priority) == 1
    assert len(instance) == 1

    instance.enqueue(mock[0])
    assert len(instance.high_priority) == 1
    assert len(instance.regular_priority) == 1
    assert len(instance) == 2

    search1 = instance.search(0)
    search2 = instance.search(1)
    assert search1 == mock[0]
    assert search2 == mock[1]

    instance.dequeue()
    assert len(instance.high_priority) == 0
    assert len(instance.regular_priority) == 1
    assert len(instance) == 1

    instance.dequeue()
    assert len(instance.high_priority) == 0
    assert len(instance.regular_priority) == 0
    assert len(instance) == 0

    instance.enqueue(mock[1])

    with pytest.raises(IndexError):
        instance.search(1)
