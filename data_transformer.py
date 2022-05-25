import os
import json
import boto3
import yfinance as yf

REGION = os.environ['REGION']
StreamName = os.environ['StreamName']

def lambda_handler(event, context):

    kinesis = boto3.client('kinesis', region_name = REGION)
    tickers = ['FB', 'SHOP', 'BYND', 'NFLX', 'PINS', 'SQ', 'TTD', 'OKTA', 'SNAP', 'DDOG']
    start_date = "2022-05-02"
    end_date = "2022-05-03"
    interval_time = "5m"
    
    for ticker in tickers:
        data = yf.download(ticker, start=start_date, 
                           end=end_date,
                          interval = interval_time)
        for datetime, stock in data.iterrows():
            datetime = str(datetime)
            main_data = {"high": stock["High"],
                        "low": stock["Low"],
                         "ts": datetime,
                         "name": ticker}
            data = json.dumps(main_data) + "\n"
            output = kinesis.put_record(StreamName = StreamName,
                                       Data=data,
                                       PartitionKey = "partitionkey"
                                       )
    print(output)
    
    return {
        "statusCode":200,
        "body": json.dumps("Finally Done!")
    }
            
            
