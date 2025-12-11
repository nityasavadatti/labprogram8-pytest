

from employee import employee_details
def test_employee_details():
    expected_output = (
        "employee name:alice\n"
        "employee id:e1001\n"
        "department:IT\n"
        "salary:55000"
    )
    assert employee_details("alice","e1001","IT",55000)== expected_output
