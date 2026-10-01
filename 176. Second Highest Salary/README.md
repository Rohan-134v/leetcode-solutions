# 176. Second Highest Salary

### Difficulty: Medium

## Description
Table: Employee


+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.


 

Write a solution to find the second highest distinct salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).

The result format is in the following example.

 
Example 1:


Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
Output: 
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+


Example 2:


Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
Output: 
+---------------------+
| SecondHighestSalary |
+---------------------+
| null                |
+---------------------+

## Submission Details
- **Status**: Accepted
- **Runtime**: 258
- **Memory**: 0.0B
- **Language**: mysql

## Code
```mysql
# Write your MySQL query statement below
select MAX(salary) AS SecondHighestSalary From
Employee
where
salary < (select Max(salary) from employee) ;

```
