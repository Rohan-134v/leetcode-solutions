# 180. Consecutive Numbers

### Difficulty: Medium

## Description
Table: Logs


+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| num         | varchar |
+-------------+---------+
In SQL, id is the primary key for this table.
id is an autoincrement column starting from 1.


 

Find all numbers that appear at least three times consecutively.

Return the result table in any order.

The result format is in the following example.

 
Example 1:


Input: 
Logs table:
+----+-----+
| id | num |
+----+-----+
| 1  | 1   |
| 2  | 1   |
| 3  | 1   |
| 4  | 2   |
| 5  | 1   |
| 6  | 2   |
| 7  | 2   |
+----+-----+
Output: 
+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+
Explanation: 1 is the only number that appears consecutively for at least three times.

## Submission Details
- **Status**: Accepted
- **Runtime**: 551
- **Memory**: 0.0B
- **Language**: mysql

## Code
```mysql
# Write your MySQL query statement below
select distinct l1.num as ConsecutiveNums
from Logs l1
Join Logs l2 On l1.id = l2.id - 1
Join Logs l3 on l1.id = l3.id - 2
where l1.num = l2.num and l2.num = l3.num;
```
