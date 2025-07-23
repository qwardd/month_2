class Distance:
    def __init__(self,  value,  measure):    #value(значение) и measure(мера - см, метры, км и тд)
        self.value = value
        self.measure = measure


    def __str__(self):
        return f" Дистанция - {self.value} {self.measure}"


    def __add__(self, other):
        if self.measure == other.measure:
            return Distance(self.value + other.value, self.measure)
        else:
            raise ValueError ("Нельзя складывать разные единицы измериния !!!")


    def __sub__(self, other):
        if self.measure == other.measure:
            result = self.value - other.value
            if result < 0:
                raise ValueError ("Расстояние не может быть отрицательным !")
            return Distance(self.value - other.value, self.measure)
        else:
            print("Нельзя отнимать  разные единицы измериния !!!")




