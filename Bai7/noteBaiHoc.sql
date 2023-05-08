-- hàm có sẵn trong SQL
-- SELECT SUM(ten_cot) ... 

-- tính tổng lương của các nhân viên thuộc phòng ban IT
SELECT SUM(SALARY)
FROM EMPLOYEES
WHERE DEPARTMENT_ID = "60";


-- tính tổng lương cao nhất của 2 job: Stock Manager và Accountant
SELECT SUM(MAX_SALARY)
FROM JOBS
WHERE JOB_TITLE = "Stock Manager" OR JOB_TITLE = "Accountant";


-- tính trung bình lương tất cả nhân viên
SELECT AVG(SALARY)
FROM EMPLOYEES;

-- tìm nhân viên có lương lớn nhất
select *, MAX(SALARY)
from employees;

-- đếm số lượng nhân viên phòng ban IT
SELECT COUNT(*) 
FROM EMPLOYEES
WHERE DEPARTMENT_ID = '60';


--NORTHWIND

SELECT CustomerID, COUNT(OrderID)
FROM ORDERS
GROUP BY CustomerID
ORDER BY COUNT(OrderID) DESC
LIMIT 1;