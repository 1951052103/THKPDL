USE Test

--Pho diem Toan
SELECT Toan, COUNT(STT) 'SoLuong'
FROM DSHN
WHERE Toan IS NOT NULL
GROUP BY Toan
Order by Toan 

--Trung Binh 7
SELECT AVG(Toan)  
FROM DSHN

--Trung vi 5.3

--Phuong sai 10.17
DECLARE @DiemTB float
SELECT @DiemTB=AVG(Toan)  
FROM DSHN
CREATE TABLE #Temp(Diem float)
INSERT INTO #Temp
SELECT POWER(Toan-@DiemTB, 2)
FROM DSHN
GROUP BY Toan

SELECT SUM(Diem)/(COUNT (Diem)-1) 
FROM #Temp

--Do lech chuan 3.18
SELECT SQRT(SUM(Diem)/(COUNT (Diem)-1)) 
FROM #Temp

--Mode 8.4
SELECT TOP 1 Toan
FROM DSHN
WHERE Toan IS NOT NULL
GROUP BY Toan
Order by COUNT(STT) DESC

DROP TABLE #Temp

----------------------------------------
CREATE TABLE #TempKHTN(Diem float, SoLuong int)
INSERT INTO #TempKHTN
SELECT Toan, COUNT(STT) --Toan
FROM DSHN
WHERE Toan IS NOT NULL
GROUP BY Toan
UNION ALL
SELECT Nguvan, COUNT(STT) --Ngu van
FROM DSHN
WHERE Nguvan IS NOT NULL
GROUP BY Nguvan
UNION ALL
SELECT Ngoaingu, COUNT(STT) --Ngoai ngu
FROM DSHN
WHERE Ngoaingu IS NOT NULL 
GROUP BY Ngoaingu
UNION ALL
SELECT KHTN, COUNT(STT) --KHTN
FROM DSHN
WHERE KHTN IS NOT NULL
GROUP BY KHTN

--Pho diem tong cong KHTN
SELECT Diem, SUM(SoLuong) 'SoLuong'
FROM #TempKHTN
GROUP BY Diem
ORDER BY Diem

--Trung Binh 5.61
SELECT AVG(Diem)
FROM #TempKHTN

--Trung vi 5.9

--Phuong sai 5.47
DECLARE @DiemTB float
SELECT @DiemTB=AVG(Diem)
FROM #TempKHTN
CREATE TABLE #Temp(Diem float)
INSERT INTO #Temp
SELECT POWER(Diem-@DiemTB, 2)
FROM #TempKHTN
GROUP BY Diem

SELECT SUM(Diem)/(COUNT (Diem)-1) 
FROM #Temp

--Do lech chuan 2.33
SELECT SQRT(SUM(Diem)/(COUNT (Diem)-1)) 
FROM #Temp

--Mode 8
SELECT TOP 1 Diem
FROM #TempKHTN
WHERE Diem IS NOT NULL
GROUP BY Diem
Order by Sum(SoLuong) DESC

DROP TABLE #Temp
DROP TABLE #TempKHTN
----------------------------------------


----------------------------------------
CREATE TABLE #TempKHXH(Diem float, SoLuong int)
INSERT INTO #TempKHXH
SELECT Toan, COUNT(STT) --Toan
FROM DSHN
WHERE Toan IS NOT NULL
GROUP BY Toan
UNION ALL
SELECT Nguvan, COUNT(STT) --Ngu van
FROM DSHN
WHERE Nguvan IS NOT NULL
GROUP BY Nguvan
UNION ALL
SELECT Ngoaingu, COUNT(STT) --Ngoai ngu
FROM DSHN
WHERE Ngoaingu IS NOT NULL
GROUP BY Ngoaingu
UNION ALL
SELECT KHXH, COUNT(STT) --KHXH
FROM DSHN
WHERE KHXH IS NOT NULL
GROUP BY KHXH

--Pho diem tong cong KHXH
SELECT Diem, SUM(SoLuong) 'SoLuong'
FROM #TempKHXH
GROUP BY Diem
ORDER BY Diem

--Trung Binh 5.66
SELECT AVG(Diem)
FROM #TempKHXH

--Trung vi 5.92

--Phuong sai 5.99
DECLARE @DiemTB float
SELECT @DiemTB=AVG(Diem)
FROM #TempKHXH
CREATE TABLE #Temp(Diem float)
INSERT INTO #Temp
SELECT POWER(Diem-@DiemTB, 2)
FROM #TempKHXH
GROUP BY Diem

SELECT SUM(Diem)/(COUNT (Diem)-1) 
FROM #Temp

--Do lech chuan 2.44
SELECT SQRT(SUM(Diem)/(COUNT (Diem)-1)) 
FROM #Temp

--Mode 8
SELECT TOP 1 Diem
FROM #TempKHXH
WHERE Diem IS NOT NULL
GROUP BY Diem
Order by Sum(SoLuong) DESC

DROP TABLE #Temp
DROP TABLE #TempKHXH