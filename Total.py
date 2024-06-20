class Buildings:
    def __init__(self, total):
        self.total = total

    def __len__(self):
        return self.total + 1

    def new_object(self):
        for self.total in range(self.total):
            print(f'Объект номер {self.total}')


buildings = Buildings(40)
buildings.new_object()
print('Итого объектов:', (len(buildings)))
