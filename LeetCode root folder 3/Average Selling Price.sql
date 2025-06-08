-- woo~, not easy
select
    p.product_id,
    if(
        u.purchase_date is null,
        0,
        round(sum(p.price*u.units)/sum(u.units), 2)
     ) as average_price
from Prices as p
left join UnitsSold as u
using(product_id)
where
    u.purchase_date is null or
    u.purchase_date >= p.start_date and
    u.purchase_date <= p.end_date
group by p.product_id;




-- deprecated

select p.product_id, (
    select sum(p.price*u.units)
    from UnitsSold as u
    where
        u.product_id = p.product_id and
        u.purchase_date >= p.start_date and
        u.purchase_date <= p.end_date
) as totalPrice
from Prices as p;