import cx_Oracle
my_dsn = cx_Oracle.makedsn("host_or_ip",1521,sid="sid_")
con = cx_Oracle.connect(user="user_oracle", password="pass_oracle", dsn=my_dsn)

cur = con.cursor()
cur.execute("SELECT * FROM TRADING.TFO_USERCUST WHERE USERID='GAVIL'")
               
res = cur.fetchall()
print res
            
cur.close()
con.close()