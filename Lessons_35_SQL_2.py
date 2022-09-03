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
    where employees.department_id in (40, 80)
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
EmployeeAndManageName = """
select
    employees.first_name,
    manager.first_name
from employees
join employees manager on employees.manager_id = manager.employee_id
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
    job_title,
    AVG(salary)
from employees
join jobs on employees.job_id = jobs.job_id
GROUP BY job_title order by AVG(salary) desc 

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
# NumEmplOfDep = """
# select
#     departments
# """