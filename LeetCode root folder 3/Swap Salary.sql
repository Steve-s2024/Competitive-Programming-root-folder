-- another if (case) statement question: 80%
update Salary
set sex =
    case
        when sex = 'f' then 'm'
        else 'f'
    end;

