import cx_Oracle

dsn_tns = cx_Oracle.makedsn('192.168.1.z', '1521', service_name='test')
conn = cx_Oracle.connect(user='x', password='y', dsn=dsn_tns)
i = 0
c = conn.cursor()
c.execute("select * from fnd_full_user order by identity")
res = c.fetchall()
for row in res:
    i = i + 1
    print(i,row[0])
conn.close()

