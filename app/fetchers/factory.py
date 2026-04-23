from app.fetchers.dummy import DummyFetcher
from app.fetchers.job_spy import JobSpyFetcher


FETCHER_MAP = {
    "job_spy": JobSpyFetcher,
    # "dummy": DummyFetcher,
    # "api": APIFetcher,
    # "scraping": ScraperFetcher,
}

def get_fetcher(source):
    fetcher_class = FETCHER_MAP.get("job_spy") # source.type

    if not fetcher_class:
        raise ValueError(f"No fetcher for type {source.type}")

    return fetcher_class(source)