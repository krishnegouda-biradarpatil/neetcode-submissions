-- Write your query below

select customer_id ,customer_name from customers
where customers.customer_id in 
(select customer_id from orders where product_name ='A')
and customers.customer_id in (select customer_id from orders where product_name ='B' )
and customers.customer_id not in (select customer_id from orders where product_name ='C')
order by customers.customer_name