CREATE PROCEDURE getUserIDs(startDate DATE, endDate DATE, minAmount INT)
BEGIN
	SELECT distinct user_id FROM Purchases
    WHERE amount >= minAmount 
    AND date(time_stamp) >= startDate and date(time_stamp) < endDate
    ORDER BY 1;
END