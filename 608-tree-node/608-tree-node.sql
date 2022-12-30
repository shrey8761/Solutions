select 
    id as "id",
    case
    when t.p_id is null then "Root"
    when t.id in(select p_id from Tree)then "Inner"
    else "Leaf" 
    end as "type"
    
from   Tree t
    