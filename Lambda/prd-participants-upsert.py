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



def lambda_handler(event, context):
    url = 'https://data.directory.openbankingbrasil.org.br/participants'
    
    http = urllib3.PoolManager()
    r = http.request('GET', 'https://data.directory.openbankingbrasil.org.br/participants')
    response = json.loads(r.data.decode('utf-8'))
    
    for item in response:
        break
        id_organization = item['OrganisationId']
        tx_name = item['RegisteredName']
        tx_status = item['Status']
        query = f"call `safra`.`open_banking_participants_upsert`('{id_organization}','{tx_name}','{tx_status}',now())"
        logger.info(query)
        conn.cursor().execute(query)
        conn.commit()
    
    return {
        'statusCode': 200,
        'body': json.dumps(f'SUCCESS')
    }
