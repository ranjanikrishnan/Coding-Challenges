SELECT DISTINCT EMAIL FROM PERSON
GROUP BY EMAIL
HAVING COUNT(EMAIL)>1