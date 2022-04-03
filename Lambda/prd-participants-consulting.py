import logging
import pymysql
import json

from datetime import datetime


import collections
from itertools import zip_longest as zip

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


def lambda_handler(event, context):
    logger.info(event)
    # TODO implement
    with conn.cursor() as cur:
        expression = f"SELECT * FROM safra.open_banking_participants where tx_status='Active';"
        cur.execute(expression)
        #cur.execute(f"select * from fiix.adalo_workorder_fiix_view LIMIT 5")
        rows = cur.fetchall()
        objects_list = []
        
    for row in rows:
        d = collections.OrderedDict()
        d["id_organization"] = row[0]
        d["tx_name"] = row[1]
        d["tx_status"] = row[2]
        d["dt_modified"] = row[3] if row[1] is None else row[3].strftime("%Y-%m-%dT%H:%M:%SZ")
        
        objects_list.append(d)

    j = json.dumps(objects_list)
    j = json.loads(j)


#chamar json load
    return  {
        "statusCode": 200,
        "body": j,
        "isBase64Encoded": False
    }