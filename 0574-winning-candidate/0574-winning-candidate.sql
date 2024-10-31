# Write your MySQL query statement below
SELECT name FROM Candidate
JOIN Vote
ON Candidate.id = Vote.candidateId
GROUP BY 1
ORDER BY COUNT(*) DESC
LIMIT 1