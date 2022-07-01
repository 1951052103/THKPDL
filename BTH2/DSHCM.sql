USE Test

--Pho diem Toan
SELECT Toan, COUNT(STT)
FROM DSHCM
WHERE Toan IS NOT NULL
GROUP BY Toan
Order by Toan 

--Trung Binh 7.36
SELECT AVG(Toan)  
FROM DSHCM

--Trung vi 5.3

--Phuong sai 6.26
CREATE TABLE #Temp(Diem float)
INSERT INTO #Temp
SELECT POWER(Toan-AVG(Toan), 2)
FROM DSHCM
GROUP BY Toan

SELECT SUM(Diem)/(COUNT (Diem)-1) 
FROM #Temp

--Do lech chuan 2.5
SELECT SQRT(SUM(Diem)/(COUNT (Diem)-1)) 
FROM #Temp

--Mode 7.8
SELECT TOP 1 Toan
FROM DSHCM
WHERE Toan IS NOT NULL
GROUP BY Toan
Order by COUNT(STT) DESC

--Pho diem Van
SELECT Nguvan, COUNT(STT)
FROM DSHCM
WHERE Nguvan IS NOT NULL
GROUP BY Nguvan
Order by Nguvan

--Pho diem Ngoai ngu
SELECT Ngoaingu, COUNT(STT)
FROM DSHCM
WHERE Ngoaingu IS NOT NULL
GROUP BY Ngoaingu
Order by Ngoaingu

--Pho diem KHXH
SELECT KHXH, COUNT(STT)
FROM DSHCM
WHERE KHXH IS NOT NULL
GROUP BY KHXH
Order by KHXH

--Pho diem KHTN
SELECT KHTN, COUNT(STT)
FROM DSHCM
WHERE KHTN IS NOT NULL
GROUP BY KHTN
Order by KHTN