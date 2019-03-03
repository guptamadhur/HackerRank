# Author: Madhur Gupta
# Github: github.com/guptamadhur
# Project: Hacker Rank Practice SQL

select
    CASE
        WHEN g.Grade >=8 THEN s.Name ELSE NULL
    END,
    g.Grade,
    s.Marks
    from Students as s
    INNER JOIN Grades as g ON s.Marks BETWEEN g.Min_Mark AND g.Max_Mark
    ORDER BY g.Grade DESC, s.NAME