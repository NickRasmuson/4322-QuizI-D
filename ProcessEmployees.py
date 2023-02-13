'''
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
'''

import csv

# open the file
infile = open('employee_data.csv', 'r')
reader = csv.reader(infile)
header = next(reader)

# create an empty dictionary

salary_dict = {}
salary_dict_new = {}

# use a loop to iterate through the csv file
employee_data = []
for i in reader:
    employee_data.append(i)


for i in employee_data:
    if i[3] == 'Marketing':
        full_name = i[1] + ' ' + i[2]
        current_salary = float(i[5])
        salary_dict[full_name] = [current_salary]

# check if the employee fits the search criteria

print()
print('=========================================')
print()

for i in employee_data:
    if i[3] == 'Marketing':
        full_name = i[1] + ' ' + i[2]
        new_salary = float(i[5])*1.1
        new_salary1 = round(new_salary, 2)
        salary_dict_new[full_name] = [new_salary1]

# iternate through the dictionary and print out the key and value as per printout
print(salary_dict)
print(salary_dict_new)
