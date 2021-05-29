# Write your MySQL query statement below

#Your group by would not know whether you are referring to the underlying column, or the output of your function code (it would assume the underlying column)

# 1, 2 refers to column
select lower(trim(product_name)) as PRODUCT_NAME, substring(sale_date, 1 , 7) as SALE_DATE, count(*) as TOTAL
from Sales
group by 1, 2
order by 1, 2;