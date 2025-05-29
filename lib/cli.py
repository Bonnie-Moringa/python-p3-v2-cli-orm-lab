
from helpers import (
    exit_program,
    list_departments,
    find_department_by_name,
    find_department_by_id,
    create_department,
    update_department,
    delete_department,
    list_employees,
    find_employee_by_name,
    find_employee_by_id,
    create_employee,
    update_employee,
    delete_employee,
    list_department_employees
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_departments()
        elif choice == "2":
            find_department_by_name()
        elif choice == "3":
            find_department_by_id()
        elif choice == "4":
            create_department()
        elif choice == "5":
            update_department()
        elif choice == "6":
            delete_department()
        elif choice == "7":
            list_employees()
        elif choice == "8":
            find_employee_by_name()
        elif choice == "9":
            find_employee_by_id()
        elif choice == "10":
            create_employee()
        elif choice == "11":
            update_employee()
        elif choice == "12":
            delete_employee()
        elif choice == "13":
            list_department_employees()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all departments")
    print("2. Find department by name")
    print("3. Find department by id")
    print("4: Create department")
    print("5: Update department")
    print("6: Delete department")
    print("7. List all employees")
    print("8. Find employee by name")
    print("9. Find employee by id")
    print("10: Create employee")
    print("11: Update employee")
    print("12: Delete employee")
    print("13: List all employees in a department")


from models.employee import Employee

def list_employees():
    employees = Employee.select()
    for emp in employees:
        print(emp)


def find_employee_by_name():
    name = input("Enter the employee's name: ")
    employee = Employee.get_or_none(Employee.name == name)
    if employee:
        print(employee)
    else:
        print(f"Employee {name} not found")


def find_employee_by_id():
    try:
        emp_id = int(input("Enter the employee's id: "))
        employee = Employee.get_or_none(Employee.id == emp_id)
        if employee:
            print(employee)
        else:
            print(f"Employee {emp_id} not found")
    except ValueError:
        print("Invalid input. Please enter a number.")


from models.department import Department
from models.employee import Employee

def create_employee():
    name = input("Enter the employee's name: ").strip()
    job_title = input("Enter the employee's job title: ").strip()
    try:
        department_id = int(input("Enter the employee's department id: "))
        if not Department.get_or_none(Department.id == department_id):
            raise ValueError("department_id must reference a department in the database")
        employee = Employee.create(name=name, job_title=job_title, department_id=department_id)
        print(f"Success: {employee}")
    except Exception as e:
        print(f"Error creating employee: {e}")



def update_employee():
    try:
        emp_id = int(input("Enter the employee's id: "))
        employee = Employee.get_or_none(Employee.id == emp_id)
        if not employee:
            print(f"Employee {emp_id} not found")
            return

        name = input("Enter the employees's new name: ").strip()
        job_title = input("Enter the employee's new job title: ").strip()
        department_id = int(input("Enter the employees's new department id: "))

        if not Department.get_or_none(Department.id == department_id):
            raise ValueError("department_id must reference a department in the database")

        employee.name = name
        employee.job_title = job_title
        employee.department_id = department_id
        employee.save()
        print(f"Success: {employee}")
    except Exception as e:
        print(f"Error updating employee: {e}")


def delete_employee():
    try:
        emp_id = int(input("Enter the employee's id: "))
        employee = Employee.get_or_none(Employee.id == emp_id)
        if employee:
            employee.delete_instance()
            print(f"Employee {emp_id} deleted")
        else:
            print(f"Employee {emp_id} not found")
    except ValueError:
        print("Invalid input. Please enter a number.")


def list_department_employees():
    try:
        dept_id = int(input("Enter the department's id: "))
        from models.department import Department
        department = Department.get_or_none(Department.id == dept_id)
        if department:
            employees = department.employees()
            for emp in employees:
                print(emp)
        else:
            print(f"Department {dept_id} not found")
    except ValueError:
        print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()
