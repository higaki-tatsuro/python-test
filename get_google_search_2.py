import json
from googleapiclient.discovery import build

api_key = 'AIzaSyBBZWF97QmFq-s1IFM4v4UzhNkdxJmbiCE'
# Custom Search で作成した検索エンジンのID
engine_id = '859da62cdfb296406'

# 検索ワード
keyword = '早稲田'

service = build('customsearch', 'v1', developerKey=api_key)

response = service.cse().list(q=keyword, cx=engine_id,
                              lr='lang_ja', num=10, start=1).execute()

with open('search_2.json', 'w', encoding='utf-8') as f:
    json.dump(response, f, indent=2, ensure_ascii=False)
