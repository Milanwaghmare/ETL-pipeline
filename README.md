## ETL-pipeline
This repository contains my first try of building an ETL pipeline.

- Extract, transform, and load (ETL) is the process of combining data from multiple sources into a large, central repository called a data warehouse. ETL uses a set of business rules to clean and organize raw data and prepare it for storage, data analytics, and machine learning (ML).

- In the given example I've extracted data from Redshift, explored it and made some cleaning of data i.e. transformation and then loaded it to an AWS S3 bucket.

This repository contains below python files on online transactions cleaned data
- extract.py
- load_data_to_s3.py
- transform.py
- .env file
- main.py
## Instructions
- Copy the .env.example file to .env and fill out the environment vars.

- Make sure you are executing the code from the etl_pipeline folder and you have Docker Desktop running.

- To run it locally first build the image.

```bash
  docker image build -t etl-pipeline:0.1 .
```

- Then run the etl job using docker:
```bash
  docker run --env-file .env etl-pipeline:0.1
```