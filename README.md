# Scrapy and MongoDB project.

This is a ETL project. 

For extraction and transformation, Scrapy is used. Scrapy scrapes "s01.json" and "s02.json" files based on the structure provided in "job_spider.py".
For loading process, created data will be send to the Mongo database with MongoPipeline exists in "pipelines.py".

Necessary dependencies are in requirements.txt.

This project uses "s01.json" and "s02.json" files in directory "jobs_project/data" where 
"jobs_project/jobs_project" directory and "jobs_project/scrapy.cfg" exists.
Before using the project, I highly suggest you the create "jobs_project/data" directory, 
put your files that needs to be scraped and change the file names inside "jobs_project/jobs_project/spiders/job_spider.py".

"s01.json" and "s02.json" won't be shared.

Docker is used in this project. 

Build the project:
```
docker compose build
```

Run the project:
```
docker compose up
```

Multicontainer is created and there will be 3 images and 1 volume.
Mongo is the database will be the first one up and will stay on.
Scrapy is the Scrapy project that will scrape data, send it to Mongo with pipeline and close up.
Query is a simple query for testing if scraped data send to the database.

If you want to test it with external connection these lines can be used:

After, 
```
docker compose up
```
Open another terminal to externally connect the database:
```
docker exec -it jobs_project-mongo-1 sh
```
Open mongosh:
```
mongosh
```
To see existing databases:
```
show dbs
```
Enter the database:
```
use jobs_db
```
To see existing collections:
```
show collections
```
To see all data:
```
db.jobs.find()
```
To see the number of documents:
```
db.jobs.countDocuments()
```

