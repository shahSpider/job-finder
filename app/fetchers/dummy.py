from app.fetchers.base import BaseFetcher

class DummyFetcher(BaseFetcher):
    def __init__(self, source):
        self.source = source

    async def fetch(self):
        # simulate external API / scraping
        return [
            {
                "title": "Backend Engineer",
                "company": "ABC Corp",
                "location": "Remote",
                "description": "FastAPI developer working on scalable APIs",
                "salary": 100000,
                "url": "https://example.com/job1"
            },
            {
                "title": "Frontend Developer",
                "company": "TechNova",
                "location": "Karachi",
                "description": "React developer for UI/UX applications",
                "salary": 80000,
                "url": "https://example.com/job2"
            },
            {
                "title": "Full Stack Engineer",
                "company": "CodeBase Ltd",
                "location": "Lahore",
                "description": "Work on both frontend and backend systems",
                "salary": 120000,
                "url": "https://example.com/job3"
            },
            {
                "title": "DevOps Engineer",
                "company": "CloudNet",
                "location": "Remote",
                "description": "CI/CD pipelines and cloud infrastructure",
                "salary": 130000,
                "url": "https://example.com/job4"
            },
            {
                "title": "Data Scientist",
                "company": "DataWorks",
                "location": "Islamabad",
                "description": "Machine learning and analytics",
                "salary": 140000,
                "url": "https://example.com/job5"
            },
            {
                "title": "Backend Developer",
                "company": "InnovateX",
                "location": "Remote",
                "description": "Django and FastAPI backend systems",
                "salary": 110000,
                "url": "https://example.com/job6"
            },
            {
                "title": "Mobile App Developer",
                "company": "Appify",
                "location": "Karachi",
                "description": "Flutter and Android development",
                "salary": 90000,
                "url": "https://example.com/job7"
            },
            {
                "title": "QA Engineer",
                "company": "SoftTest",
                "location": "Lahore",
                "description": "Automation and manual testing",
                "salary": 70000,
                "url": "https://example.com/job8"
            },
            {
                "title": "AI Engineer",
                "company": "DeepVision",
                "location": "Remote",
                "description": "AI models and deep learning systems",
                "salary": 150000,
                "url": "https://example.com/job9"
            },
            {
                "title": "System Administrator",
                "company": "NetSecure",
                "location": "Islamabad",
                "description": "Server management and security",
                "salary": 85000,
                "url": "https://example.com/job10"
            },
            {
                "title": "Cloud Engineer",
                "company": "SkyHigh",
                "location": "Remote",
                "description": "AWS and cloud architecture",
                "salary": 125000,
                "url": "https://example.com/job11"
            },
            {
                "title": "Product Manager",
                "company": "BuildIt",
                "location": "Karachi",
                "description": "Manage product lifecycle and teams",
                "salary": 135000,
                "url": "https://example.com/job12"
            },
            {
                "title": "Cybersecurity Analyst",
                "company": "SecureOps",
                "location": "Lahore",
                "description": "Security monitoring and threat analysis",
                "salary": 115000,
                "url": "https://example.com/job13"
            },
            {
                "title": "Database Administrator",
                "company": "DataCore",
                "location": "Islamabad",
                "description": "Manage and optimize databases",
                "salary": 105000,
                "url": "https://example.com/job14"
            },
            {
                "title": "Software Engineer",
                "company": "NextGen Tech",
                "location": "Remote",
                "description": "General software development tasks",
                "salary": 95000,
                "url": "https://example.com/job15"
            }
        ]

    def parse(self, data):
        return data