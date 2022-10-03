# Write your MySQL query statement below
select name from SalesPerson where SalesPerson.sales_id NOT IN (select SalesPerson.sales_id from SalesPerson, Orders where SalesPerson.sales_id=Orders.sales_id AND Orders.com_id=(select com_id from Company where name="RED"));
