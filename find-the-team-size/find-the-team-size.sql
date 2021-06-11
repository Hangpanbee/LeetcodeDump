# Write your MySQL query statement below

SELECT
    employee_id, team_size
FROM (
    SELECT 
        Count(employee_id) as team_size, team_id
    FROM
        Employee
    GROUP BY 
        team_id
    ) as teamSize 
    JOIN 
        Employee 
    ON Employee.team_id = teamSize.team_id;