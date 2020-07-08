CREATE FUNCTION getNthHighestSalary(@N INT) RETURNS INT AS
BEGIN
    RETURN (
        /* Write your T-SQL query statement below. */
        SELECT MAX(SALARY) FROM EMPLOYEE E1
        WHERE (@N-1) == (SELECT COUNT(DISTINCT E2.SALARY)
        FROM EMPLOYEE E2 
        WHERE E2.SALARY > E1.SALARY)
    );
END