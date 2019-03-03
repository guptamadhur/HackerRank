# Author: Madhur Gupta
# Github: github.com/guptamadhur
# Project: Hacker Rank Practice SQL

select C.company_code, founder,
COUNT(distinct LM.lead_manager_code), COUNT(distinct SM.senior_manager_code), COUNT(distinct M.manager_code), COUNT(distinct E.employee_code)
from Company as C
JOIN Lead_Manager as LM ON C.company_code=LM.company_code
JOIN Senior_Manager as SM ON LM.lead_manager_code=SM.lead_manager_code
JOIN Manager as M ON SM.senior_manager_code=M.senior_manager_code
JOIN Employee as E on M.manager_code=E.manager_code
GROUP BY C.company_code,founder
ORDER BY C.company_code