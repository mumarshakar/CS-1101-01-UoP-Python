# Step 1: Split the list into two sub-lists
employee_list = ["Ali", "Ahmad", "Hamza", "Azeem", "Shoukat", "Faheem", "Zohaib", "Touseef", "Danial", "Ghaffar"]
print("=======Printing Whole List===============")
print(employee_list)
print("=======Spliting SubLists===============")
subList1 = employee_list[:5]
subList2 = employee_list[5:]
# Printing Sublists
print(subList1)
print(subList2)
# Step 2: Add a new employee to subList2
subList2.append("Kriti Brown")
print("=====Printing Sublists After Adding New Employee in Sublist 2===")
print(subList1)
print(subList2)

# Step 3: Remove the second employee's name from subList1
del subList1[1]
print(subList1)
print(subList2)
# Step 4: Merge both lists
merged_list = subList1 + subList2
print(merged_list)


# Salary List
salary_list = [5000, 6000, 7000, 8000, 9000, 10000, 10000, 12000, 13000, 14000]
print(f"Salaries: {salary_list}")
# Step 5: Update the salary list with a 4% raise for each employee
updated_salary_list = [salary * 1.04 for salary in salary_list]
print(updated_salary_list)

# Step 6: Sort the salary list and show the top 3 salaries
sorted_salaries = sorted(updated_salary_list, reverse=True)
top_3_salaries = sorted_salaries[:3]

print(top_3_salaries)
