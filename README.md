# Streaming Finance Data with AWS Lambda
**Name**: Hojin Lee<br>
**Course**: CIS9760<br>
**Date**: 5/24/2022<br>

For this project, I used a Lambda function to generate near real time finance data records for interactive querying. I generated a real time data pipeline for finance data records for interactive querying.

### Infrastructure
The project consists of four major infrastructure elements that work in tandem:
1. Data Trnasformer: A lambda function that gathers the data
2. Data Collector: A Kinesis stream that holds the data
3. Data Analyzer: A serverless process that allows us to query the S3 data
4. Data Visualization: Visualizations of the query results

### Technology leveraged
- Languages: SQL, Python
- Tools: AWS (S3, Kinesis, Lambda, Athena, Glue), Jupyter 

### Dataset
In the collector lambda, using the yfinance module, I gained pricing information for each of the following stocks:
-	Facebook (FB)
-	Shopify (SHOP)
-	Beyond Meat (BYND)
-	Netflix (NFLX)
-	Pinterest (PINS)
-	Square (SQ)
-	The Trade Desk (TTD)
-	Okta (OKTA)
-	Snap (SNAP)
-	Datadog (DDOG)
