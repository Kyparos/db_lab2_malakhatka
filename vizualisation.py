import matplotlib.pyplot as plt
import pandas as pd
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
    cur.execute(query_1)
    q_1 = cur.fetchall()
    cur.execute(query_2)
    q_2 = cur.fetchall()
    cur.execute(query_3)
    q_3 = cur.fetchall()

fig, ax = plt.subplots(3, 1, figsize=(10, 15))
q_1 = list(map(lambda x: [x[0].replace(' ', ''), x[1]], q_1))
q_1 = pd.DataFrame(q_1, columns=['disipline', 'count'])
q_2 = q_2[0]
q_3 = list(map(lambda x: [x[0].replace(' ', ''), x[1]], q_3))
q_3 = pd.DataFrame(q_3, columns=['NOC', 'total'])
ax[1].pie(q_2[1:], labels=['gold', 'silver', 'bronze'], autopct='%1.1f%%')
ax[0].bar(x='disipline', height='count', data=q_1)
ax[2].bar(x='NOC', height='total', data=q_3)
ax[2].tick_params(rotation=45)
# ax[]
#

plt.show()
