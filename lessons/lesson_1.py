class Car: #методы
    #инициализатор
    def __init__(self, model, year):
        #свойства, атрибуты, поля
        self.model = model
        self.year = year
        self.fined = False


subaru_model = 'Subaru Forester'
car_subaru = Car('Forester',2020)
car_honda = Car('Honda Fit',2018)
print('Model',car_subaru.model, ' Year',car_subaru.year, 'fined',car_subaru.fined)
#print(car_honda)
print(type(car_subaru))
