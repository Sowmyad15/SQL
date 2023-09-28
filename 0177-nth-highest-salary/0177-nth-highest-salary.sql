CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
        Select salary as Nthgreatestsalary from 
        (Select salary, dense_rank() over(order by salary desc) as salary_rank
        from Employee) t
        where t.salary_rank=N
        limit 1
  );
END