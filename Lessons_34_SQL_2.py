from SQL_CON_QUERY import create_connection, execute_query, select_query
from pprint import pprint

connection = create_connection('hr.db')

select_fullname = 'select first_name || " " || last_name from employees'
for item in select_query(connection, select_fullname):
    print(item)
print('*'*80)
select_department_id = 'select distinct department_id from employees'
for item in select_query(connection, select_department_id):
    print(item)
print('*'*80)
select_first_name = 'select * from employees ORDER BY first_name'
for item in select_query(connection, select_first_name):
    print(item)
print('*'*80)
select_fullname_salaryPF = \
    'select first_name || " " || last_name, salary * 0.12 from employees'
for item in select_query(connection, select_fullname_salaryPF):
    print(item)
print('*'*80)
select_max_min_salary = 'select min(salary), max(salary) from employees'
pprint(select_query(connection,select_max_min_salary))
print('*'*80)
select_month_salary = '' \
                      'select first_name || " " || last_name,' \
                      ' round(salary, 2) from employees'
for item in select_query(connection, select_month_salary):
    print(item)
