# Write your MySQL query statement below

# bought all products that a company has by using count
# doesnt work always tho
select customer_id
from   
    Customer, Product
group by
    customer_id
having count(distinct(Customer.product_key))>= count(distinct(Product.product_key));
