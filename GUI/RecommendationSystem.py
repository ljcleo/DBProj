import numpy as np
import pyodbc

cnxn = pyodbc.connect('DRIVER={SQL Server}; SERVER=localhost; DATABASE=film_db; UID=; PWD=;')
cursor = cnxn.cursor()

sql = "SELECT * FROM Comment"
result = cursor.execute(sql).fetchall()

all_film = set()
all_user = set()

for comment in result:
    all_film.add(comment[0])
    all_user.add(comment[1])

all_film = list(all_film)
all_user = list(all_user)

filmid2index = dict()
userid2index = dict()
for k, v in enumerate(all_film):
    filmid2index[v] = k
for k, v in enumerate(all_user):
    userid2index[v] = k

rate = np.zeros((len(all_user), len(all_film)))
for comment in result:
    rate[userid2index[comment[1]], filmid2index[comment[0]]] = float(comment[2])

cursor.close()

rate /= np.sqrt(np.sum(rate ** 2, axis=1, keepdims=True))
similarity = rate.dot(rate.T)
prediction = similarity.dot(rate)
prediction[rate > 0] = 0
recommendation = np.argsort(-prediction, axis=1)[:, :3]

file_path = 'recommendation.txt'
c = open(file_path, 'w')
for i in range(recommendation.shape[0]):
    c.write('{:s},{:s},{:s},{:s}\n'.format(all_user[i],
                                           str(all_film[recommendation[i, 0]]),
                                           str(all_film[recommendation[i, 1]]),
                                           str(all_film[recommendation[i, 2]])))
c.close()