trip_dist = 420 #total miles in the trip
bike_per_day = 50 #miles you can bicycle in a day
trip_days = trip_dist / bike_per_day
print("To bike", trip_dist, "miles, ", bike_per_day, "miles per day,")
print(" takes", trip_days, "days.")

for i in range(1, 5):
  for j in range(i):
    print(i, end=" ")
  print()