from dotenv import load_dotenv
import os
import requests

load_dotenv()

api_key = os.getenv('API_KEY')

url = f'http://openapi.seoul.go.kr:8088/{api_key}/json/CardSubwayStatsNew/1/5/20240830'

response = requests.get(url)
response_content = response.content
