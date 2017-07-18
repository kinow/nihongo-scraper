# Nihongo Scraper

Scraper to download Japanese news, quizzes, and other resources for use offline.
Data is used for personal study only, and NLP is applied to isolate Kanji for
reading cards, for example.

* nihongo-spider simply scrapes a known site with quizzes and saves the response as JSON/CSV

URL's used are hidden, to prevent a mass of requests to all the sites, or bots following
links from GitHub.

## Build

```
git clone https://github.com/kinow/nihongo-scraper.git
cd nihongo-scraper
pip install -r requirements
```

## Execute nihongo-spider

```
cat > .env <<EOF
START_URL=http://<url>/context/path/
EOF
scrapy runspider nihongo-spider.py -o questions.json
```
