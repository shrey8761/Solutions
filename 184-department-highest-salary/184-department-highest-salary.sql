SELECT 

d.name AS Department, 
e.name AS Employee, 
e.salary AS Salary

FROM Employee e
LEFT JOIN Department d ON e.departmentId = d.id




WHERE 
(e.departmentId, e.salary) 
in 
(
    SELECT 
    e2.departmentId, 
    MAX(e2.salary) 
    FROM Employee e2 
    GROUP BY e2.departmentId
)