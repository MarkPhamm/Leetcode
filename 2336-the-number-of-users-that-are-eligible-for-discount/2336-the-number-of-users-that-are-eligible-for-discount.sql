CREATE FUNCTION getUserIDs(startDate DATE, endDate DATE, minAmount INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      SELECT COUNT(distinct user_id) FROM Purchases
      WHERE date(time_stamp) >= startDate and date(time_stamp)< endDate
      AND amount >= minAmount
  );
END