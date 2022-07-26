--Cau 1
SELECT *
FROM Full_Mark_2020

--Cau 2
--SO luong bai thi
SELECT STT
FROM Full_Mark_2020
WHERE Toan IS NOT NULL

--Pho diem toan
SELECT Toan, COUNT(STT) 'SoLuong'
FROM Full_Mark_2020
WHERE Toan IS NOT NULL
GROUP BY Toan
ORDER BY TOAN

--Trung binh
SELECT AVG(Toan)
FROM Full_Mark_2020

--Mode
SELECT TOP 1 Toan, COUNT(STT) 'SoLuong'
FROM Full_Mark_2020
WHERE Toan IS NOT NULL
GROUP BY Toan
ORDER BY COUNT(STT) DESC

--Phuong sai
DECLARE @DiemTB float
SELECT @DiemTB=AVG(Toan)  
FROM Full_Mark_2020
CREATE TABLE #Temp(Diem float)
INSERT INTO #Temp
SELECT POWER(Toan-@DiemTB, 2)
FROM Full_Mark_2020
GROUP BY Toan

SELECT SUM(Diem)/(COUNT (Diem)-1) 
FROM #Temp

--Do lech chuan
SELECT SQRT(SUM(Diem)/(COUNT (Diem)-1)) 
FROM #Temp