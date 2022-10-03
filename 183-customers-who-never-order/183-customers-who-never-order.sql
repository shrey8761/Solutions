# Write your MySQL query statement below
SELECT C.name as Customers from Customers C Where id NOT IN (SELECT customerId from Orders);

