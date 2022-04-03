import logging
import pymysql
import json
import urllib3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

db_host = "open-finance-safra.cfkpvcmypu2t.sa-east-1.rds.amazonaws.com"
db_username = ""
db_password = ""
db_name = "safra"


try:
    conn = pymysql.connect(host=db_host,port = 3306, user=db_username, passwd=db_password, db=db_name, connect_timeout=10)
    logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")
except pymysql.MySQLError as e:
    logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
    logger.error(e)

query = f"SELECT * FROM safra.open_banking_participants;"

with conn.cursor() as cur:
    cur.execute(query)
    rows = cur.fetchall()

html = ''

rows_sorted = []
for row in rows:
    rows_sorted.append(row[1])
    
rows_sorted.sort()

for row in rows_sorted:
    html += f'''<option value="{row}">{row}</option>\n'''

print(html)