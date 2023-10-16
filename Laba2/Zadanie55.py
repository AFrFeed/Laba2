class Text:
    def __init__(self, text):
        self.text = text

    def simvol(self):
        return len(self.text)

    def bykvi(self):
        return sum(1 for char in self.text if char.isalpha())

    def space(self):
        return sum(1 for char in self.text if char.isspace())

    def simvol_bez_space(self):
        return len(self.text.replace(" ", ""))

    def mass_slov(self):
        return self.text.split()

    def mass_predloz(self):
        return self.text.split(".!?")

text = Text("Здесь могла быть ваша реклама!!")

print("Количество cимволов:",text.simvol())
print("Количество букв:",text.bykvi())
print("Количество пробелов:",text.space())
print("Количество символов без пробела:",text.simvol_bez_space())
print(text.mass_slov())
print(text.mass_predloz())