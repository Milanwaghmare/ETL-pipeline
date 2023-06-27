import os
from datetime import datetime

from src.extract import extract_transactional_data
from src.transform import identify_and_remove_duplicated_data
from src.load_data_to_S3 import df_to_s3

#from dotenv import load_dotenv
#load_dotenv() #only for local testing

#import variables from .env file
dbname= os.getenv('dbname')
host=os.getenv('host')
port=os.getenv('port')
user=os.getenv('user')
password=os.getenv('password')
aws_access_key_id=os.getenv('aws_access_key_id')
aws_secret_access_key_id=os.getenv('aws_secret_access_key_id')

#this creates a variable that tracks the time we executed the script
start_time=datetime.now()


online_trans_cleaned =extract_transactional_data(dbname, host, port, user, password)
print("Extraction and transformation tasks in sql completed")

online_trans_dedupted=identify_and_remove_duplicated_data(online_trans_cleaned)
print("Remove duplicated data")

#connection to s3_bucket next step
print("loading data to s3")
s3_bucket='waia-data-dump'
key = "bootcamp2/etl/mk_online_trans_cleaned.csv"


df_to_s3(online_trans_dedupted,key,s3_bucket,aws_access_key_id,aws_secret_access_key_id)

#this creates a variable that caclulates how long it takes to run the script

 #this creates a variable that calculates how long it takes to run the script
execution_time = datetime.now() - start_time
print(f"\nTotal execution time (hh:mm:ss.ms) {execution_time}")

