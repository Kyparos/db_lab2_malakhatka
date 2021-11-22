SELECT
       dist_name
      ,COUNT(ath_id)
FROM
     disipline LEFT JOIN athletes a on disipline.dist_id = a.discipline_id
GROUP BY  dist_id;


SELECT
     noc_name
    ,g_medal
    ,s_medal
    ,b_medal
FROM noc
WHERE noc_id = 1;

SELECT
    noc_name
     ,g_medal + s_medal + b_medal AS total_medals
FROM noc;

