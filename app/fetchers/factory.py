from app.fetchers.dummy import DummyFetcher

FETCHER_MAP = {
    "dummy": DummyFetcher,
    # "api": APIFetcher,
    # "scraping": ScraperFetcher,
}

def get_fetcher(source):
    fetcher_class = FETCHER_MAP.get("dummy") # source.type

    if not fetcher_class:
        raise ValueError(f"No fetcher for type {source.type}")

    return fetcher_class(source)