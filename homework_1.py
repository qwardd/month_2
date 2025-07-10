class Person:
    def __init__(self,name,birth_date,occupation,higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = True if higher_education\
            else False
    def introduce(self):
        print(f'Имя: {self.name}, Дата рождения: {self.birth_date}, Профессия: {self.occupation}, Высшее образование(если имеется): {self.higher_education}' )

amir = Person('Amir',2006, "студент", False )
egor = Person('Egor', 2008, "ученик", False )
masha = Person('Masha', 2002, "интерн скрой помоши", 'ВГМУ' )

amir.introduce()
egor.introduce()
masha.introduce()