import csv
from jobspy import scrape_jobs
from app.fetchers.base import BaseFetcher

class JobSpyFetcher(BaseFetcher):
    def __init__(self, source):
        self.source = source

    async def fetch(self):
        # simulate external API / scraping
        return self.get_scraped_jobs()

    def parse(self, data):
        return data
    

    def get_scraped_jobs(self):
        jobs = scrape_jobs(
            site_name=["indeed", "linkedin", "zip_recruiter", "google"], # "glassdoor", "bayt", "naukri", "bdjobs"
            search_term="software engineer",
            google_search_term="software engineer jobs near San Francisco, CA since yesterday",
            location="San Francisco, CA",
            results_wanted=20,
            hours_old=72,
            country_indeed='USA',
            
            # linkedin_fetch_description=True # gets more info such as description, direct job url (slower)
            # proxies=["208.195.175.46:65095", "208.195.175.45:65095", "localhost"],
        )
        jobs = jobs.to_dict(orient="records")
        data = []
        for job in jobs[:3]:
            data.append({
                "title": job.get("title"),
                "company": job.get("company"),
                "location": job.get("location"),
                "description": job.get("description", "")[:200], # truncate description for testing
                "salary": job.get("max_amount", 0),
                "url": job.get("job_url")
            })
        return data