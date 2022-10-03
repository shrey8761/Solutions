SELECT DISTINCT t1.id,
    CASE 
        WHEN t1.p_id IS NULL THEN 'Root' ELSE
        CASE
            WHEN t1.id = t2.p_id THEN 'Inner' ELSE 'Leaf'
        END
    END AS 'Type'
    FROM Tree t1 LEFT JOIN Tree t2 ON t1.id = t2.p_id
    ORDER BY id