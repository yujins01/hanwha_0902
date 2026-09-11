# from dotenv import load_dotenv
# import os

# #.env 파일에 있는 key_url을 환경변수로 불러오는 역할
# load_dotenv()

# api_key = os.getenv("OPENAI_API_KEY")

# if api_key:
#     print("✅ API 키가 정상적으로 설정되었습니다.")
# else:
#     print("❌ API 키를 찾을 수 없습니다.")

#=============================#
# from openai import OpenAI

# #OpenAI가 자동으로 OPENAI_API_KEY라는 환경변수를 찾아서 키를 가져옴
# client = OpenAI()

# response = client.responses.create(
#     model="gpt-5-mini",
#     input="안녕하세요. API 연결 테스트입니다. '연결됨'이라고만 말해주세요"
# )

# print(response.output_text)

#LangSmith 추적을 설정 https://smith.langchain.com
#.env 파일에 LANGCHAIN_API_KEY를 입력
#pip install langchain-teddynote <- 실습용 패키지

from langchain_teddynote import logging

#프로젝트 이름을 입력
logging.langsmith("CH01-Basic")
