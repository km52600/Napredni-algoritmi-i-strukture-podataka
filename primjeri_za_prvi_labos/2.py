person_data : dict = {"Ana":1995,"Zoran":1979,"Lucija":2001,"Anja":1997}
print(person_data)

for person,year in person_data.items():
    person_data[person] = int(year) - 1

print(person_data)

year_age : list = []

for year in person_data.values():
    tup : tuple = (year, 2022-year)
    year_age.append(tup)
print(year_age)