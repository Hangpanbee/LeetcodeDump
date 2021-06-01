# Write your MySQL query statement below


#Solution 1: find people who have bought AB
#           if they are not the same people who bought ABC


#SELECT 
#    o1.customer_id, Customers.customer_name
#FROM 
#    Orders o1 
#    join Orders o2 on (o1.customer_id = o2.customer_id) 
#    join Customers on (o1.customer_id = Customers.customer_id)
#WHERE 
#    o1.product_name = "A" and o2.product_name = "B" and 
#    o1.customer_id not in (
#        SELECT 
#            o1.customer_id
#        FROM Orders o1 
#            join Orders o2 on (o1.customer_id = o2.customer_id)  
#            join Orders o3 on (o3.customer_id = o1.customer_id)
#        WHERE o1.product_name = "A" and o2.product_name = "B" and o3.product_name = "C"
#    );


#Solution2:
SELECT 
    o1.customer_id, Customers.customer_name
FROM
    Orders o1 natural join Customers
GROUP BY 
    customer_id
HAVING
    sum(product_name = 'A') > 0
    and sum(product_name = 'B') > 0
    and sum(product_name = 'C') = 0;
    

