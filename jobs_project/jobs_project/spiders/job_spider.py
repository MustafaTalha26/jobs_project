import scrapy
import json
import os
from urllib.request import pathname2url

class JobSpider(scrapy.Spider):
    name = 'job_spider'

    def start_requests(self):
        # This used for reaching data file due to the scrapy runspider command. 
        project_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the spider file
        data_dir = os.path.join(project_dir, "..","..", "data")  # Go up two directories to reach "data"

        file_paths = [
            os.path.join(data_dir, "s01.json"),
            os.path.join(data_dir, "s02.json"),
        ]

        # pathname2url used for changing local directory to a link.
        # scrapy didn't accepted normal directories.
        for file_path in file_paths:
            if os.path.exists(file_path): 
                print(f"File exists: {file_path}")
                file_url = "file:" + pathname2url(file_path) 
                yield scrapy.Request(url=file_url, callback=self.parse_page)
            else:
                print(f"File NOT found: {file_path}")

    # Necessary function to parse links.
    # Structured based on s01.json and s02.json. 
    def parse_page(self, response):
        print(f"Parsing URL: {response.url}")
        try:
            jobs = json.loads(response.text)
            for job in jobs.get('jobs', []):
                data = job.get('data', {})
                item = {}
                item['req_id'] = data.get('req_id')
                item['languages'] = data.get('languages')
                item['title'] = data.get('title')
                item['description'] = data.get('description')
                item['street_address'] = data.get('street_address')
                item['city'] = data.get('city')
                item['state'] = data.get('state')
                item['country_code'] = data.get('country_code')
                item['postal_code'] = data.get('postal_code')
                item['category'] = data.get('category')
                item['benefits'] = data.get('benefits')
                item['employment_type'] = data.get('employment_type')
                item['hiring_organization'] = data.get('hiring_organization')
                item['apply_url'] = data.get('apply_url')
                item['update_date'] = data.get('update_date')
                item['create_date'] = data.get('create_date')
                yield item

        except json.JSONDecodeError as e:
            self.logger.error(f"JSONDecodeError: {e} - URL: {response.url}") 
        except Exception as e:
            self.logger.error(f"Other Error: {e} - URL: {response.url}")