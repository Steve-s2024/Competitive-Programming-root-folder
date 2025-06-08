-- learn the case statement! yeah: 55%
select x, y, z,
    case
        when (x+y>z) and (x+z>y) and (y+z>x) then 'Yes'
        else 'No'
    end as triangle
from Triangle;




-- dont know why it didn't work, maybe I have to do query only
alter table Triangle
add column triangle varchar(3) not null;

update Triangle
set t.triangle = 'Yes'
where x + y + z > 2 * greatest(x, y, z);

update Triangle t
set t.triangle = 'No'
where x + y + z <= 2 * greatest(x, y, z);

select *
from Triangle;