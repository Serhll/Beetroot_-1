from SQL_CON_QUERY import create_connection, execute_query, select_query
from pprint import pprint
#####################################################################
#Task_1
connection = create_connection('Les_34_task_1.sqlite')

job_title_table = '''
create table if not exists JobTitle(
    id integer primary key autoincrement, 
    name text not null,
    salary integer not null
);
'''
workers_table = '''create table if not exists Workers (
    id integer primary key autoincrement,
    name text not null,
    speciality text,
    age integer,
    gender text not null,
    id_JobTitle integer not null,
    foreign key (id_JobTitle) references JobTitle(id)   
);
'''
# execute_query(connection, job_title_table)
# execute_query(connection, workers_table)
# execute_query(connection, department_table)
list_job_title = '''
insert into
    JobTitle(name, salary)
values
    ('Director', 50000),
    ('Chief Engineer', 40000),
    ('Engineer', 30000),
    ('Accountant', 40000),
    ('Driver', 25000);
'''
list_workers = '''
insert into
    Workers (name, speciality, age, gender, id_JobTitle)
values
    ('Roman', 'builder', '30', 'male', 3),
    ('Oleg ', 'technologist', 29, 'male', 3),
    ('Oleksandra', 'economist', 31, 'female', 4),
    ('Taras', null, 37, 'male', 1),
    ('Maksym', 'power engineer', 35, 'male', 5),
    ('Serhii', 'technologist', 30, 'male', 2);
'''
# execute_query(connection, list_job_title)
# execute_query(connection, list_workers)
# execute_query(connection, create_department)
#
select_workers = '''
select
    workers.id,
    workers.name,
    workers.age,
    Workers.speciality,
    Jobtitle.name,
    Jobtitle.salary
from
    workers
    left outer join JobTitle on JobTitle.id = workers.id_JobTitle
'''
select_workers_speciality = '''
select
    workers.id,
    workers.name,
    Jobtitle.name   
from
    workers
    left outer join JobTitle on JobTitle.id = workers.id_JobTitle
'''
pprint(select_query(connection, select_workers))
pprint(select_query(connection, select_workers_speciality))

update_workers = 'UPDATE Workers SET name = "Olga" WHERE id = 3'
delete_workers = 'DELETE FROM Workers where name = "Roman"'

execute_query(connection, update_workers)
execute_query(connection, delete_workers)

pprint(select_query(connection, select_workers))

#####################################################################
#Task_2
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