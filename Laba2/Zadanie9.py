class Stude:
    name = 'John'
    surname = 'Libert'

    def show(self):
        return self.name, self.surname

stude = Stude()

print(stude.name, stude.surname)