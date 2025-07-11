class Person:
    def __init__(self,name,birth_date,occupation,higher_education=False):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education
    def introduce(self):
        print(f'Привет меня зовут {self.name}, я родился {self.birth_date}, я {self.occupation}' )

class Classmate(Person):
    def __init__(self,name,birth_date,occupation,higher_education,group_name):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name
    def introduce(self):
        print(f'Привет меня зовут {self.name}, я одноклассник Егора , учились в {self.group_name},  я родился {self.birth_date}, я {self.occupation} , Высшее образование -  {self.higher_education}')


class Friend(Person):
    def __init__(self,name,birth_date,occupation,higher_education,hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        print(f'Привет меня зовут {self.name}, я друг Егора ,  родился {self.birth_date}, я {self.occupation} и я увлекаюсь {self.hobby} , Высшее образование -  {self.higher_education}')


amirkhan = Classmate(name='Амирхан', birth_date="07.01.2008", occupation='студент',higher_education=False,group_name= '11A' )
adelya = Classmate(name='Аделя', birth_date='28.05.2009', occupation='студентка',higher_education=False ,group_name= '11A' )
emir = Friend(name="Эмир", birth_date= '18.03.2000', occupation='Преподаватель', higher_education=True,hobby='Волейболом' )
chingiz = Friend(name="Чынгыз", birth_date='20.10.2001', occupation="Консультант", higher_education=True, hobby='Играми')

names = [amirkhan, adelya, emir, chingiz]
for person in names:
    person.introduce()


