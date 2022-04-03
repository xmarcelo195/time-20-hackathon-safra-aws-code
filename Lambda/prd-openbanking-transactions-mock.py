import json

def lambda_handler(event, context):
    return_json ='''{
      "data": [
        {
          "transactionId": "TXpRMU9UQTROMWhZV2xSU1FUazJSMDl",
          "completedAuthorisedPaymentType": "TRANSACAO_EFETIVADA",
          "creditDebitType": "DEBITO",
          "transactionName": "TRANSFCWAR5TXHCX5I9IDBHML8082N8NEO30M6LNNG7ANAYIJYRM00ZBZPU8",
          "type": "PIX",
          "amount": 500.54,
          "transactionCurrency": "BRL",
          "transactionDate": "2021-01-07",
          "partieCnpjCpf": "43908445778",
          "partiePersonType": "PESSOA_NATURAL",
          "partieCompeCode": "001",
          "partieBranchCode": "6272",
          "partieNumber": "67890854360",
          "partieCheckDigit": "4"
        }
      ],
      "links": {
        "self": "https://api.itau.com.br/open-banking/api/v1/resource",
        "first": "https://api.itau.com.br/open-banking/api/v1/resource",
        "prev": "https://api.itau.com.br/open-banking/api/v1/resource",
        "next": "https://api.itau.com.br/open-banking/api/v1/resource",
        "last": "https://api.itau.com.br/open-banking/api/v1/resource"
      },
      "meta": {
        "totalRecords": 1,
        "totalPages": 1,
        "requestDateTime": "2021-05-21T08:30:00Z"
      }
    }'''
    j=json.loads(return_json)
    return {
        'statusCode': 200,
        'body': j
    }
