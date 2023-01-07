SELECT P.email as Email
from Person P
group by email
having count(P.email) > 1
