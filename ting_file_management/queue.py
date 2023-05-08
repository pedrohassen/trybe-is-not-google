from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def enqueue(self, value):
        return self.data.append(value)

    def dequeue(self):
        if len(self.data) == 0:
            raise IndexError("Não há elementos")
        return self.data.pop(0)

    def search(self, index):
        if index < 0 or index > len(self.data) - 1:
            raise IndexError('Índice Inválido ou Inexistente')
        return self.data[index]
