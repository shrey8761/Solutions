select Customers.name as 'Customers'
from Customers
left join Orders on Customers.id = orders.customerID
where Orders.customerID is  null
