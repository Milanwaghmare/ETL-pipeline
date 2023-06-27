## ETL-Pipeline Project
## Project Overview
The goal of the project is to build an ETL pipeline.ETL(Extract, Transform, Load) is a data pipeline used to collect data from various sources, transforms the data according to business requirements, and load the data into a destination data storage.

This repository contains my first attempt  of building an ETL pipeline 

- Extract, transform, and load (ETL) is the process of combining data from multiple sources into a large, central repository called a data warehouse. ETL uses a set of business rules to clean and organize raw data and prepare it for storage, data analytics, and machine learning (ML).

- In the given example I've extracted data from Redshift, explored it and made some cleaning of data i.e. transformation and then loaded it to an AWS S3 bucket.

This repository contains below python files on online transactions cleaned data
- src/extract.py - a python script that contains instructions to connect to Amazon Redshift data warehouse and to extract online transactions data with transformation tasks performed using SQL
- src/load_data_to_s3.py- a python script that contains instructions to connect to Amazon S3 cloud object storage and to write the cleaned data as a CSV file into an S3 bucket
-src/transform.py - a python script that contains instructions to identify and remove duplicated records
- .env file-a text document that contains list of enviornment variables used
-main.py - a python script that contains all instructions to execute all the steps to extract, transform and load the transformed data using the functions from extract.py,load-data-to-S3,and transform.py
- requirements.txt - a text document that contains all the libraries required to execute the code
- Dockerfile - a text document that contains all the instructions a user could call on the command line to assemble an image
- .dockerignore- a text document that contains files or directories to be excluded when docker CLI sends the context to docker daemon.This helps to avoid unnecessarily sending large or sensitive files and directories to the daemon and potentially adding them to images using ADD or copy
- .gitignore - a text document that specifies intentionally untracked files that Git should ignore

## How to Run the ETL Pipeline project
A. To run the ETL pipeline on local terminal:

## Requirements
 Python 3+
* Python IDE or a text editor to edit files

## Steps to follow 

1. Copy the .env.example file to .env and fill out the environment vars.
2. Install all the libraries needed to execute main.py
3. Run the main.py script

- Windows:
```bash
 pip3 install -requirements.txt
```
```bash
 python main .py
```


B. To run ETL pipeline using Docker :

## Requirements
-Docker for  Mac :
Installation: Install Docker Desktop on Mac 
- Docker for Windows:
- Installation: install Docker Desktop on Windows


## Instructions
- Ensure Docker is running locally
- Comment out the code from dotenv import load_dotenv and load_dotenv() in the main.py script before executing the following codes
- Copy the .env.example file to .env and fill out the environment vars.
- Make sure you are executing the code from the etl_pipeline folder, and you have Docker Desktop running.


#### Build an Image

* To run it locally first build the image.

```bash
  docker image build -t etl-pipeline:0.1 .
```

- Then run the etl job using docker:
```bash
  docker run --env-file .env etl-pipeline:0.1
```
