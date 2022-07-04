USE Test

--Pho diem Toan
SELECT Toan, COUNT(STT) 'SoLuong'
FROM DSHCM
WHERE Toan IS NOT NULL
GROUP BY Toan
Order by Toan 

--Trung Binh 7.36
SELECT AVG(Toan)  
FROM DSHCM

--Trung vi 5.3

--Phuong sai 6.26
DECLARE @DiemTB float
SELECT @DiemTB=AVG(Toan)  
FROM DSHCM
CREATE TABLE #Temp(Diem float)
INSERT INTO #Temp
SELECT POWER(Toan-@DiemTB, 2)
FROM DSHCM
GROUP BY Toan

SELECT SUM(Diem)/(COUNT (Diem)-1) 
FROM #Temp

--Do lech chuan 3.53
SELECT SQRT(SUM(Diem)/(COUNT (Diem)-1)) 
FROM #Temp

--Mode 7.8
SELECT TOP 1 Toan
FROM DSHCM
WHERE Toan IS NOT NULL
GROUP BY Toan
Order by COUNT(STT) DESC

DROP TABLE #Temp

----------------------------------------
CREATE TABLE #TempKHTN(Diem float, SoLuong int)
INSERT INTO #TempKHTN
SELECT Toan, COUNT(STT) --Toan
FROM DSHCM
WHERE Toan IS NOT NULL
GROUP BY Toan
UNION ALL
SELECT Nguvan, COUNT(STT) --Ngu van
FROM DSHCM
WHERE Nguvan IS NOT NULL
GROUP BY Nguvan
UNION ALL
SELECT Ngoaingu, COUNT(STT) --Ngoai ngu
FROM DSHCM
WHERE Ngoaingu IS NOT NULL 
GROUP BY Ngoaingu
UNION ALL
SELECT KHTN, COUNT(STT) --KHTN
FROM DSHCM
WHERE KHTN IS NOT NULL
GROUP BY KHTN

--Pho diem tong cong KHTN
SELECT Diem, SUM(SoLuong) 'SoLuong'
FROM #TempKHTN
GROUP BY Diem
ORDER BY Diem

--Trung binh 5.59
SELECT AVG(Diem)
FROM #TempKHTN

--Trung vi 5.81

--Phuong sai 5.3
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

--Do lech chuan 2.3
SELECT SQRT(SUM(Diem)/(COUNT (Diem)-1)) 
FROM #Temp

--Mode 7
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
FROM DSHCM
WHERE Toan IS NOT NULL
GROUP BY Toan
UNION ALL
SELECT Nguvan, COUNT(STT) --Ngu van
FROM DSHCM
WHERE Nguvan IS NOT NULL
GROUP BY Nguvan
UNION ALL
SELECT Ngoaingu, COUNT(STT) --Ngoai ngu
FROM DSHCM
WHERE Ngoaingu IS NOT NULL
GROUP BY Ngoaingu
UNION ALL
SELECT KHXH, COUNT(STT) --KHXH
FROM DSHCM
WHERE KHXH IS NOT NULL
GROUP BY KHXH

--Pho diem tong cong KHXH
SELECT Diem, SUM(SoLuong) 'SoLuong'
FROM #TempKHXH
GROUP BY Diem
ORDER BY Diem

--Trung Binh 5.71
SELECT AVG(Diem)
FROM #TempKHXH

--Trung vi 5.97

--Phuong sai 5.47
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

--Do lech chuan 2.33
SELECT SQRT(SUM(Diem)/(COUNT (Diem)-1)) 
FROM #Temp

--Mode 7
SELECT TOP 1 Diem
FROM #TempKHXH
WHERE Diem IS NOT NULL
GROUP BY Diem
Order by Sum(SoLuong) DESC

DROP TABLE #Temp
DROP TABLE #TempKHXH
----------------------------------------


----------------------------------------
CREATE TABLE #Temp1
(
	[STT] [int],
	[Code] [int],
	[Diali] [float],
	[GDCD] [float],
	[Hoahoc] [float],
	[KHTN] [float],
	[KHXH] [float],
	[LichSu] [float],
	[Ngoaingu] [float],
	[Nguvan] [float],
	[Sinhhoc] [float],
	[Toan] [float],
	[Vatli] [float],
	[City] [smallint],
	DiemTB float,
	DiemMin float
)

INSERT INTO #Temp1
SELECT *, ROUND((
				SELECT AVG(c)
				FROM (VALUES(Diali),(GDCD),(Hoahoc),(LichSu),(Ngoaingu),(Nguvan),(Sinhhoc),(Toan),(Vatli)) T (c)
			), 2),
		ROUND((
			SELECT Min(c)
			FROM (VALUES(Diali),(GDCD),(Hoahoc),(LichSu),(Ngoaingu),(Nguvan),(Sinhhoc),(Toan),(Vatli)) T (c)
		), 2)
FROM DSHCM

CREATE TABLE #Temp2
(
	STT int,
	DiemTB float,
	DiemMin float,
	XepLoai NVARCHAR(50)
)

INSERT INTO #Temp2
SELECT STT, DiemTB, DiemMin, (CASE
				WHEN DiemTB >= 8 AND DiemMin >= 7 THEN 'Gioi'
				WHEN DiemTB >= 6.5 AND DiemMin >= 6 THEN 'Kha'
				WHEN DiemTB >= 4 AND DiemMin >= 1 THEN 'Trung binh'
				ELSE 'Khong tot nghiep'
			END) AS 'XepLoai'
FROM #Temp1

SELECT XepLoai, COUNT(STT) 'SoLuong'
FROM #Temp2
GROUP BY XepLoai

DROP TABLE #Temp1
DROP TABLE #Temp2