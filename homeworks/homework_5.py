from distance import Distance

city_1 = Distance(120, 'km')
city_2 = Distance(130, 'km')
city_3 = Distance(140, 'm')


print(city_1)
print(city_1 + city_2)
#print(city_1 + city_3)   # сложение разных ед изм
print(city_2 - city_1)
#print(city_1 - city_3)    #разные ед изм
#print(city_1 - city_2)   # отр расстояние