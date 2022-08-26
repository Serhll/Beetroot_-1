class Notebook:
    min_diagonal = 13
    max_diagonal = 19

    def __init__(self,
                 brand,
                 type_of_work,
                 processor,
                 RAM,
                 memory,
                 weight,
                 material,
                 diagonal):
        self.brand = brand
        self.type_of_work = type_of_work
        self.processor = processor
        self.RAM = RAM
        self.memory = memory
        self.material = material
        self.weight = weight
        self.diagonal = diagonal

    def brand(self):
        return f'{self.brand}'

    def type_of_word(self):
        return self.type_of_work

    def processor(self):
        return self.processor

    def RAM(self):
        return self.RAM

    def memory(self):
        return self.memory

    def weight(self):
        return self.weight

    def diagonal(self):
        print(self.diagonal)


class SteelCase(Notebook):
    material = 'steel'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.steel = self.material


class PlasticCase(Notebook):
    material = 'plastic'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.plastic = self.material


def main():
    laptop = Notebook('Asus', 'work', 'Intel', '16GB', 'SSD-512', 'over 2kg',
                      'steel', '17')
    laptop.brand()


if __name__ == '__main__':
    main()
