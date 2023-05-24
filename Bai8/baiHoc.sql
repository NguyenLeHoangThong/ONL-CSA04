-- Link tải cơ sở dữ liệu HR: https://drive.google.com/file/d/1LCY8nEvp4yAHzVbGHVCcul2Pz9Ic3U_y/view?usp=sharing
-- hoặc có thể lấy file HR.sqlite của Bai7 luôn nhé, vì trên link và file đấy giống nhau


-- Đề bài, lấy ra thông tin tất cả nhân viên, bao gồm TÊN PHÒNG BAN nhân viên đó làm việc
select employees.*, departments.DEPARTMENT_NAME
from employees
inner join departments on employees.DEPARTMENT_ID = departments.DEPARTMENT_ID;

--Đề bài, lấy ra thông tin tất cả nhân viên, bao gồm TÊN CÔNG VIỆC nhân viên đó đang làm
select employees.*, jobs.JOB_TITLE
from employees
inner join jobs on employees.JOB_ID = jobs.JOB_ID;

--Đề bài, lấy ra thông tin tất cả nhân viên, bao gồm TÊN CÔNG VIỆC, TÊN PHÒNG BAN nhân viên đó đang làm
select employees.*, jobs.JOB_TITLE, departments.DEPARTMENT_NAME
from employees
inner join departments on employees.DEPARTMENT_ID = departments.DEPARTMENT_ID
inner join jobs on employees.JOB_ID = jobs.JOB_ID;

--Đề, lấy toàn bộ thông tin bảng locations và tên quốc gia của locations đó, lấy thông tin châu lục của quốc gia đó 
SELECT locations.*, countries.COUNTRY_NAME, regions.REGON_NAME
FROM locations
LEFT JOIN countries ON locations.COUNTRY_ID = countries.COUNTRY_ID
LEFT JOIN regions ON countries.REGION_ID = regions.REGION_ID
