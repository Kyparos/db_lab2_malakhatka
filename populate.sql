INSERT INTO disipline (dist_id, dist_name)
VALUES (1, 'Basketball'),
       (2, 'Athletics'),
       (3, 'Swimming'),
       (4, 'Karate'),
       (5, 'Judo');

INSERT INTO noc(noc_id, noc_name, g_medal, s_medal, b_medal)
VALUES (1, 'United States of America',    39, 41, 33),
       (2, 'People''s Republic of China', 38, 32, 18),
       (3, 'Japan',                       27, 14, 17),
       (4, 'Great Britain',               22, 21, 22),
       (5, 'ROC',                         20, 28, 23);

INSERT INTO athletes (ath_id, ath_name, noc_id, discipline_id)
VALUES (1, 'HARIMOTO Tenketsu', 3, 1),
       (2, 'YANG Qian',         2, 3),
       (3, 'MOGUSHKOV Musa',    5, 5),
       (4, 'MIDDLETON Khris',   1, 1),
       (5, 'TAURASI Diana',     1, 1);

