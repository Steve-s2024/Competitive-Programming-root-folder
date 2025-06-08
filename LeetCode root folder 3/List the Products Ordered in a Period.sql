-- 900th question solved! hoorah: 49%
select p.product_name, sum(o.unit) as unit
from Products as p
join Orders as o using(product_id)
where o.order_date between '2020-02-01' and '2020-02-29'
group by p.product_id
having unit >= 100;