import scrapy

# settings.py
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

START_URL = os.environ.get("START_URL")

class NihongoSpider(scrapy.Spider):
    name = 'nihongospider'
    start_urls = [START_URL]
    
    def parse(self, response):
        for quiz_link in response.css('div.post > h2 > a'):
            yield response.follow(quiz_link, self.parse_quiz)

        for next_page in response.css('a.nextpostslink'):
            yield response.follow(next_page, self.parse)

    def parse_quiz(self, response):
        for paragraph in response.css('div.entry > form > p'):
            yield {'question': paragraph.extract()}
