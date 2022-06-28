# Write your MySQL query statement below
Select max(Salary) AS SecondHighestSalary 
From Employee
Where Salary not in (select max(salary) from Employee);
