# Author: Madhur Gupta
# Github: github.com/guptamadhur
# Project: Hacker Rank Practice SQL

select n,CASE
    WHEN P IS NULL THEN "Root"
    WHEN N IN (select P from BST) THEN "Inner"
    ELSE "Leaf"
    END from BST ORDER BY N