from googleapiclient.discovery import build
import json

GOOGLE_CSE_ID='create your cx'
GOOGLE_API_KEY='enabled search API KEY'
API_SERVICE_NAME = 'searchconsole'

#def gsearch(keyword, num=10) -> dict:
def gsearch(keyword, num=10):
    search_service = build("customsearch","v1",developerKey=GOOGLE_API_KEY)
    response = search_service.cse().list(
                q=keyword,
                cx=GOOGLE_CSE_ID,
                lr='lang_en',
                num=num,
                start=1
            ).execute()
    res = json.dumps(response, ensure_ascii=False, indent=4)
    print(res)

if __name__ == '__main__':
    keyword = input("enter your question: ")
    gsearch(keyword)
