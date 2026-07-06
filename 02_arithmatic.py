courseFees = 5000
students = 100
expenses = 350000

# Revenue
revenue = courseFees * students

# profit
profit = revenue - expenses

# average per student revenue
average = revenue / students

batchSize = 30
batches = students // batchSize
remaining = students % batchSize

print("Revenue : ",revenue)
print("Expenses : ",expenses)
print("Profit : ",profit)
print("Average revenue:",average)
print("Total Batches:",batches)
print("Remaining students:",remaining)




