# Write your MySQL query statement below
SELECT
    Ranking.score, row_num as `Rank`
FROM (
    SELECT 
        score, ROW_NUMBER() OVER(order by score desc) row_num
    FROM
        Scores
    GROUP BY
        Score
    ) as Ranking join Scores on Scores.score = Ranking.score
ORDER BY
    Ranking.row_num asc
;
