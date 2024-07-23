import csv 
from collections import namedtuple

class analysis:

    Car = namedtuple("Car", "model year price transmission mileage fueltype tax mpg enginesize")
    cars = []
    with open("vw.csv", "r") as csvfile:
      reader = csv.reader(csvfile, skipinitialspace=True)
      next(reader)
      for row in reader:
        cars.append(Car(*row))

    #Task 1
    mostExpensive = cars[0]
    for c in cars:
       if mostExpensive.price < c.price:
          mostExpensive = c
    print(mostExpensive)

    #Task 2
    totalPrice = 0
    count = 0
    for c in cars:
       if c.model == "Golf":
          totalPrice += int(c.price)
          count += 1
    print(totalPrice / count)

    #Task 3
    totalMile = 0
    countMile = 0
    for c in cars:
       if c.model == "Polo" and c.year == "2020":
          totalMile += int(c.mileage)
          countMile += 1
    print(totalMile/ countMile)
          






