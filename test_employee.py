

from employee import employee_details
def test_employee_details():
    expected_output = (
        "Employee_Name:alice\n"
        "Employee_Id:e1001\n"
        "Department:IT\n"
        "Salary:55000"
    )
    assert employee_details("alice","e1001","IT",55000)== expected_output
