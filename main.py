import matplotlib.pyplot as plt
import psycopg2

username = 'sashamalakhatka'
password = '111'
database = 'sashamalakhatka'
host = 'localhost'
port = '5432'

query_1 = '''
SELECT
       dist_name
      ,COUNT(ath_id)
FROM
     disipline LEFT JOIN athletes a on disipline.dist_id = a.discipline_id
GROUP BY  dist_id;

'''
query_2 = '''

SELECT
     noc_name
    ,g_medal
    ,s_medal
    ,b_medal
FROM noc
WHERE noc_id = 1;
'''

query_3 = '''
SELECT
    noc_name
     ,g_medal + s_medal + b_medal AS total_medals
FROM noc;'''

con = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with con:
    print("Database opened successfully")

    cur = con.cursor()

    print('1.  \n')

    cur.execute(query_1)
    for row in cur:
        print(row)

    print('\n2.  \n')
    cur.execute(query_2)
    for row in cur:
        print(row)

    print('\n3.  \n')
    cur.execute(query_3)
    for row in cur:
        print(row)

plt.show()
