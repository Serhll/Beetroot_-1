from SQL_CON_QUERY import create_connection, execute_query, select_query
connection = create_connection('hr.db')
##################################################
FullnameDepidDepname = """
select
    employees.first_name || ' ' || employees.last_name,
    employees.department_id
from
    departments
inner join employees on departments.department_id = employees.department_id
"""
for item in select_query(connection, FullnameDepidDepname):
    print(item)
print('*'*80)
###################################################
FullnameDepCityState = """
select employees.first_name || ' ' || employees.last_name,
    departments.depart_name,
    locations.city,
    locations.state_province
from employees
    join departments using (department_id)
    join locations using (location_id)#
"""
for item in select_query(connection, FullnameDepCityState):
    print(item)
print('*'*80)
###################################################
FullnameDepCityState = """
select
    employees.first_name,
    employees.last_name,
    employees.department_id,
    departments.depart_name
from employees
    join departments using (department_id)
    where employees.department_id = 40
"""
for item in select_query(connection, FullnameDepCityState):
    print(item)
print('*' * 80)
###################################################
AllDepartment = """
select depart_name
from departments
"""
for item in select_query(connection, AllDepartment):
    print(item)
print('*' * 80)
###################################################
# Не знайшов таблицю з менеджерами
EmployeeAndManageName = """
select
    employees.first_name,
    employees.manager_id
from employees
"""
for item in select_query(connection, EmployeeAndManageName):
    print(item)
print('*' * 80)
###################################################
JobTitleFullNameDifSalary = """
select
employees.first_name || ' ' || employees.last_name,
jobs.job_title,
jobs.max_salary - employees.salary
from employees
    join jobs using (job_id)

"""
for item in select_query(connection, JobTitleFullNameDifSalary):
    print(item)
print('*' * 80)
###################################################
JobTitleAvgSalary = """
select
    jobs.job_title,
    (jobs.min_salary + jobs.max_salary)/2,
    employees.first_name || ' ' || employees.last_name
from jobs
    join employees using (job_id)
"""
for item in select_query(connection, JobTitleAvgSalary):
    print(item)
print('*' * 80)
##################################################
SalaryEmplLondon = """
select
    employees.first_name || ' ' || employees.last_name,
    employees.salary,
    locations.city
from employees
    join departments using (department_id)
    join locations using (location_id)
    where locations.city = 'London'
"""
for item in select_query(connection, SalaryEmplLondon):
    print(item)
print('*' * 80)
##################################################