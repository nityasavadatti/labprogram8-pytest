def employee_details(name,emp_id,department,salary):
    result = (
        f"Employee Name:{name}\n"
        f"Employee ID:{emp_id}\n"
        f"department:{department}\n"
        f"salary:{salary}\n"
    )
    return result
    
if __name__ == "__main__":
    name="alice"
    emp_id="e1001"
    department="IT"
    salary=55000
    print(employee_details(name,emp_id,department,salary))
