class Lesson:
    def __init__(self, name, age, heigh):
        self.name = name
        self.age = age
        self.heigh = heigh
    def info(self):
        return f'{self.name} info'

    def height(self):
        return f'Рост {self.name} состовляет {self.heigh}'

a = Lesson('bakbergen', 18, 1.75)
print(a.height())

