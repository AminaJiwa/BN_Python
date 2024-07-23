import pandas as pd
import matplotlib.pyplot as plt

#Task 1 
cars = pd.read_csv('vw.csv')
fuel_type_count = cars.groupby("fuelType")[["model"]].count().sort_values('model', ascending=False).reset_index()
plt.pie(fuel_type_count.model, labels=fuel_type_count.fuelType, autopct='%1.1f%%')
plt.show()

#Task 2
average_mileage = cars.groupby("model")[['mileage']].mean().sort_values('mileage', ascending=False).reset_index()
plt.bar(average_mileage.model,
  average_mileage.mileage, 
  color ='blue',
  width = 0.4)
plt.xlabel("Model")
plt.ylabel("Average mileage")
plt.title("Average mileage for VW models")
plt.show()