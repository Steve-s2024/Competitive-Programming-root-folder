-- this should be a medium: 67%
select
    stu.student_id,
    stu.student_name,
    sub.subject_name,
    if(exa.attended_exams is null, 0, exa.attended_exams) as attended_exams
from Students as stu
cross join Subjects as sub
left join (
    select student_id, subject_name, count(*) as attended_exams
    from Examinations
    group by student_id, subject_name
) as exa
on(stu.student_id = exa.student_id and exa.subject_name = sub.subject_name)
order by stu.student_id, sub.subject_name;