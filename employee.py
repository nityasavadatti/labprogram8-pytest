def  employee_details(name,emp_id,department,salary):
    result= (
        f" Employee Name: {name}\n"
        f" Employee ID: {Emp_id}\n"
        f" Employee department: {department}\n"
        f" Employee salary: {salary}\n"
    )
    return result
if__name__="__main__":
#sample input(you can change)
Name="alice"
Emp_id="e1001"
department="IT"
salary=55000
print(employee_details(name,emp_id,department,salary))
