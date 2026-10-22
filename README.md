# jobsdb

A Scrapy crawler for **jobsdb.pk**, the Pakistani job board. It walks the listing pages and
extracts each job's title, company and location.

## Stack

- Python, Scrapy
- Item pipelines and middlewares under `jobsdb/`

## Layout

```
scrapy.cfg
jobsdb/
  items.py         the item definitions the spider yields
  middlewares.py   request/response middlewares
  pipelines.py     item pipelines (validation, storage)
  settings.py
  spiders/
    jobs.py        the spider
```

## Running it

```bash
pip install scrapy
scrapy crawl jobs
```

Output format and destination are configured in `jobsdb/settings.py`.

## Note on selectors

The site's markup changes often and this spider parses CSS classes directly. Expect the
selectors in `spiders/jobs.py` to need updating when the board restructures its listing markup —
that is the usual failure mode for a scraper of this kind.
