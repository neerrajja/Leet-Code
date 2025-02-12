/* Write your T-SQL query statement below */
select  euni.unique_id, e.name
from Employees e
left join employeeUNI euni
on e.id = euni.id