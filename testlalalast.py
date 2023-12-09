from io import BytesIO
import matplotlib.pyplot as plt
import asyncio
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import discord
import schedule
import time
from datetime import datetime

# 디스코드 봇 토큰 및 채널 아이디
TOKEN = 'MTE3MTk4MzM4MTgxOTU2NDA0Mg.G8cC7X.7UDG5PlQMboUhgUsGq0_wuvjzUnx73qQMzHQgc'
CHANNEL_ID = '1181488218919682058'
count = 0
h9, h91, h92, h93, h94, h95 = 0, 0, 0, 0, 0, 0
h10, h101, h102, h103, h104, h105 = 0, 0, 0, 0, 0, 0
h11, h111, h112, h113, h114, h115 = 0, 0, 0, 0, 0, 0
h12, h121, h122, h123, h124, h125 = 0, 0, 0, 0, 0, 0
h13, h131, h132, h133, h134, h135 = 0, 0, 0, 0, 0, 0
h14, h141, h142, h143, h144, h145 = 0, 0, 0, 0, 0, 0
h15, h151, h152, h153 = 0, 0, 0, 0,
url1 = "https://www.paxnet.co.kr/stock/analysis/main?abbrSymbol=005930"
url2 = "https://www.paxnet.co.kr/news/005930/stock?stockCode=005930&objId=S005930"
url3 = "https://kr.investing.com/equities/samsung-electronics-co-ltd-earnings"
user_input_value = None

# 봇 초기화
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

def scrape_page(url):
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(url)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    driver.quit()
    return soup

async def send_discord_message():
    global count, h9, h91, h92, h93, h94, h95, h10, h101, h102, h103, h104, h105, h11, h111, h112, h113, h114, h115, h12, h121, h122, h123, h124, h125, h13, h131, h132, h133, h134, h135, h14, h141, h142, h143, h144, h145, h15, h151, h152, h153
    current_time = time.strftime("%H:%M:%S")
    channel = client.get_channel(int(CHANNEL_ID))
    
     # 첫 번째 페이지 크롤링
    soup1 = scrape_page(url1)
    af_element = soup1.find('span', class_=['color-blue', 'color-red', 'color-'])
    be_element = soup1.find('span', string='전일').find_next('span')

    # 두 번째 페이지 크롤링
    soup2 = scrape_page(url2)
    first_li = soup2.select_one('.thumb-list li')

    # 세 번째 페이지 크롤링
    soup3 = scrape_page(url3)
    info_row = soup3.find('tr', {'name': 'instrumentEarningsHistory'})
    date_td = info_row.find('td', {'class': 'bold left'})

    if first_li:
        date_element = first_li.find('dd', class_='date')
        spans = date_element.find_all('span')

        if len(spans) == 2:
            span2_value = spans[1].text.strip()
        else:
            print("최근 데이터가 없습니다.")

     # 제목과 링크를 출력합니다.
    title_a = first_li.select_one('dt a')
    if title_a:
     title_text = title_a.text.strip()
     link_url = "https://www.paxnet.co.kr" + title_a['href'] 
     print("기사 제목 구함")
     print("링크 구함")
    else:
       print("날짜 정보를 찾을 수 없습니다.")

    if af_element and be_element:
     After = af_element.text
     Before = be_element.text
     noaf = af_element.text.replace(',', '')
     nobf = be_element.text.replace(',', '')

     percentage_difference = ((int(noaf) - int(nobf)) / int(nobf)) * 100
     percentage_difference = round(percentage_difference, 2)  # 소수점 둘째 자리까지 반올림

     if int(noaf) > int(nobf):
      comparison_message = f'어제 대비 {percentage_difference}% 상승'
     elif int(noaf) < int(nobf):
      comparison_message = f'어제 대비 {abs(percentage_difference)}% 하락'
     else:
      comparison_message = '어제와 동일' 

    if user_input_value is not None:
        percentage_difference2 = ((int(noaf) - int(user_input_value)) / int(user_input_value)) * 100
        percentage_difference2 = round(percentage_difference2, 2)
        
        if int(noaf) > int(user_input_value):
         comparison_message = f'사용자값 비교 {percentage_difference2}% 상승'
        elif int(noaf) < int(user_input_value):
         comparison_message = f'사용자값 비교 {abs(percentage_difference2)}% 하락'
        else:
         comparison_message = f'사용자값 비교 {percentage_difference2}% 변함없음'  
    else:
         comparison_message = '입력값이 없음'

    pday = nobf
    
    if count == 0:
     h9, h91, h92, h93, h94, h95 = noaf, noaf, noaf, noaf, noaf, noaf
     h10, h101, h102, h103, h104, h105 = noaf, noaf, noaf, noaf, noaf, noaf
     h11, h111, h112, h113, h114, h115 = noaf, noaf, noaf, noaf, noaf, noaf
     h12, h121, h122, h123, h124, h125 = noaf, noaf, noaf, noaf, noaf, noaf
     h13, h131, h132, h133, h134, h135 = noaf, noaf, noaf, noaf, noaf, noaf
     h14, h141, h142, h143, h144, h145 = noaf, noaf, noaf, noaf, noaf, noaf
     h15, h151, h152, h153 = noaf, noaf, noaf, noaf
    elif count == 1:
     h91, h92, h93, h94, h95 = noaf, noaf, noaf, noaf, noaf
     h10, h101, h102, h103, h104, h105 = noaf, noaf, noaf, noaf, noaf, noaf
     h11, h111, h112, h113, h114, h115 = noaf, noaf, noaf, noaf, noaf, noaf
     h12, h121, h122, h123, h124, h125 = noaf, noaf, noaf, noaf, noaf, noaf
     h13, h131, h132, h133, h134, h135 = noaf, noaf, noaf, noaf, noaf, noaf
     h14, h141, h142, h143, h144, h145 = noaf, noaf, noaf, noaf, noaf, noaf
     h15, h151, h152, h153 = noaf, noaf, noaf, noaf
    elif count == 2:
     h92, h93, h94, h95 = noaf, noaf, noaf, noaf
     h10, h101, h102, h103, h104, h105 = noaf, noaf, noaf, noaf, noaf, noaf
     h11, h111, h112, h113, h114, h115 = noaf, noaf, noaf, noaf, noaf, noaf
     h12, h121, h122, h123, h124, h125 = noaf, noaf, noaf, noaf, noaf, noaf
     h13, h131, h132, h133, h134, h135 = noaf, noaf, noaf, noaf, noaf, noaf
     h14, h141, h142, h143, h144, h145 = noaf, noaf, noaf, noaf, noaf, noaf
     h15, h151, h152, h153 = noaf, noaf, noaf, noaf             
    elif count == 3:
     h93, h94, h95 = noaf, noaf, noaf
     h10, h101, h102, h103, h104, h105 = noaf, noaf, noaf, noaf, noaf, noaf
     h11, h111, h112, h113, h114, h115 = noaf, noaf, noaf, noaf, noaf, noaf
     h12, h121, h122, h123, h124, h125 = noaf, noaf, noaf, noaf, noaf, noaf
     h13, h131, h132, h133, h134, h135 = noaf, noaf, noaf, noaf, noaf, noaf
     h14, h141, h142, h143, h144, h145 = noaf, noaf, noaf, noaf, noaf, noaf
     h15, h151, h152, h153  = noaf, noaf, noaf, noaf                
    elif count == 4:
     h94, h95 = noaf, noaf
     h10, h101, h102, h103, h104, h105 = noaf, noaf, noaf, noaf, noaf, noaf
     h11, h111, h112, h113, h114, h115 = noaf, noaf, noaf, noaf, noaf, noaf
     h12, h121, h122, h123, h124, h125 = noaf, noaf, noaf, noaf, noaf, noaf
     h13, h131, h132, h133, h134, h135 = noaf, noaf, noaf, noaf, noaf, noaf
     h14, h141, h142, h143, h144, h145 = noaf, noaf, noaf, noaf, noaf, noaf
     h15, h151, h152, h153  = noaf, noaf, noaf, noaf    
    elif count == 5:
     h95 = noaf
     h10, h101, h102, h103, h104, h105 = noaf, noaf, noaf, noaf, noaf, noaf
     h11, h111, h112, h113, h114, h115 = noaf, noaf, noaf, noaf, noaf, noaf
     h12, h121, h122, h123, h124, h125 = noaf, noaf, noaf, noaf, noaf, noaf
     h13, h131, h132, h133, h134, h135 = noaf, noaf, noaf, noaf, noaf, noaf
     h14, h141, h142, h143, h144, h145 = noaf, noaf, noaf, noaf, noaf, noaf
     h15, h151, h152, h153  = noaf, noaf, noaf, noaf              
    elif count == 6:
     h10, h101, h102, h103, h104, h105 = noaf, noaf, noaf, noaf, noaf, noaf
     h11, h111, h112, h113, h114, h115 = noaf, noaf, noaf, noaf, noaf, noaf
     h12, h121, h122, h123, h124, h125 = noaf, noaf, noaf, noaf, noaf, noaf
     h13, h131, h132, h133, h134, h135 = noaf, noaf, noaf, noaf, noaf, noaf
     h14, h141, h142, h143, h144, h145 = noaf, noaf, noaf, noaf, noaf, noaf
     h15, h151, h152, h153  = noaf, noaf, noaf, noaf
    elif count == 7:
     h101, h102, h103, h104, h105 = noaf, noaf, noaf, noaf, noaf
     h11, h111, h112, h113, h114, h115 = noaf, noaf, noaf, noaf, noaf, noaf
     h12, h121, h122, h123, h124, h125 = noaf, noaf, noaf, noaf, noaf, noaf
     h13, h131, h132, h133, h134, h135 = noaf, noaf, noaf, noaf, noaf, noaf
     h14, h141, h142, h143, h144, h145 = noaf, noaf, noaf, noaf, noaf, noaf
     h15, h151, h152, h153  = noaf, noaf, noaf, noaf, noaf, noaf 
    elif count == 8:
     h102, h103, h104, h105 = noaf, noaf, noaf, noaf
     h11, h111, h112, h113, h114, h115 = noaf, noaf, noaf, noaf, noaf, noaf
     h12, h121, h122, h123, h124, h125 = noaf, noaf, noaf, noaf, noaf, noaf
     h13, h131, h132, h133, h134, h135 = noaf, noaf, noaf, noaf, noaf, noaf
     h14, h141, h142, h143, h144, h145 = noaf, noaf, noaf, noaf, noaf, noaf
     h15, h151, h152, h153  = noaf, noaf, noaf, noaf
    elif count == 9:
     h103, h104, h105 = noaf, noaf, noaf
     h11, h111, h112, h113, h114, h115 = noaf, noaf, noaf, noaf, noaf, noaf
     h12, h121, h122, h123, h124, h125 = noaf, noaf, noaf, noaf, noaf, noaf
     h13, h131, h132, h133, h134, h135 = noaf, noaf, noaf, noaf, noaf, noaf
     h14, h141, h142, h143, h144, h145 = noaf, noaf, noaf, noaf, noaf, noaf
     h15, h151, h152, h153  = noaf, noaf, noaf, noaf, noaf, noaf
    elif count == 10:
     h104, h105 = noaf, noaf
     h11, h111, h112, h113, h114, h115 = noaf, noaf, noaf, noaf, noaf, noaf
     h12, h121, h122, h123, h124, h125 = noaf, noaf, noaf, noaf, noaf, noaf
     h13, h131, h132, h133, h134, h135 = noaf, noaf, noaf, noaf, noaf, noaf
     h14, h141, h142, h143, h144, h145 = noaf, noaf, noaf, noaf, noaf, noaf
     h15, h151, h152, h153  = noaf, noaf, noaf, noaf
    elif count == 11:
     h105 = noaf
     h11, h111, h112, h113, h114, h115 = noaf, noaf, noaf, noaf, noaf, noaf
     h12, h121, h122, h123, h124, h125 = noaf, noaf, noaf, noaf, noaf, noaf
     h13, h131, h132, h133, h134, h135 = noaf, noaf, noaf, noaf, noaf, noaf
     h14, h141, h142, h143, h144, h145 = noaf, noaf, noaf, noaf, noaf, noaf
     h15, h151, h152, h153  = noaf, noaf, noaf, noaf
    elif count == 12:
     h11, h111, h112, h113, h114, h115 = noaf, noaf, noaf, noaf, noaf, noaf
     h12, h121, h122, h123, h124, h125 = noaf, noaf, noaf, noaf, noaf, noaf
     h13, h131, h132, h133, h134, h135 = noaf, noaf, noaf, noaf, noaf, noaf
     h14, h141, h142, h143, h144, h145 = noaf, noaf, noaf, noaf, noaf, noaf
     h15, h151, h152, h153  = noaf, noaf, noaf, noaf 
    elif count == 13:
     h111, h112, h113, h114, h115 = noaf, noaf, noaf, noaf, noaf
     h12, h121, h122, h123, h124, h125 = noaf, noaf, noaf, noaf, noaf, noaf
     h13, h131, h132, h133, h134, h135 = noaf, noaf, noaf, noaf, noaf, noaf
     h14, h141, h142, h143, h144, h145 = noaf, noaf, noaf, noaf, noaf, noaf
     h15, h151, h152, h153  = noaf, noaf, noaf, noaf
    elif count == 14:
     h112, h113, h114, h115 = noaf, noaf, noaf, noaf
     h12, h121, h122, h123, h124, h125 = noaf, noaf, noaf, noaf, noaf, noaf
     h13, h131, h132, h133, h134, h135 = noaf, noaf, noaf, noaf, noaf, noaf
     h14, h141, h142, h143, h144, h145 = noaf, noaf, noaf, noaf, noaf, noaf
     h15, h151, h152, h153  = noaf, noaf, noaf, noaf
    elif count == 15:
     h113, h114, h115 = noaf, noaf, noaf
     h12, h121, h122, h123, h124, h125 = noaf, noaf, noaf, noaf, noaf, noaf
     h13, h131, h132, h133, h134, h135 = noaf, noaf, noaf, noaf, noaf, noaf
     h14, h141, h142, h143, h144, h145 = noaf, noaf, noaf, noaf, noaf, noaf
     h15, h151, h152, h153  = noaf, noaf, noaf, noaf
    elif count == 16:
     h114, h115 = noaf, noaf
     h12, h121, h122, h123, h124, h125 = noaf, noaf, noaf, noaf, noaf, noaf
     h13, h131, h132, h133, h134, h135 = noaf, noaf, noaf, noaf, noaf, noaf
     h14, h141, h142, h143, h144, h145 = noaf, noaf, noaf, noaf, noaf, noaf
     h15, h151, h152, h153  = noaf, noaf, noaf, noaf
    elif count == 17:
     h115 = noaf
     h12, h121, h122, h123, h124, h125 = noaf, noaf, noaf, noaf, noaf, noaf
     h13, h131, h132, h133, h134, h135 = noaf, noaf, noaf, noaf, noaf, noaf
     h14, h141, h142, h143, h144, h145 = noaf, noaf, noaf, noaf, noaf, noaf
     h15, h151, h152, h153  = noaf, noaf, noaf, noaf
    elif count == 18:
     h12, h121, h122, h123, h124, h125 = noaf, noaf, noaf, noaf, noaf, noaf
     h13, h131, h132, h133, h134, h135 = noaf, noaf, noaf, noaf, noaf, noaf
     h14, h141, h142, h143, h144, h145 = noaf, noaf, noaf, noaf, noaf, noaf
     h15, h151, h152, h153  = noaf, noaf, noaf, noaf
    elif count == 19:
     h121, h122, h123, h124, h125 = noaf, noaf, noaf, noaf, noaf
     h13, h131, h132, h133, h134, h135 = noaf, noaf, noaf, noaf, noaf, noaf
     h14, h141, h142, h143, h144, h145 = noaf, noaf, noaf, noaf, noaf, noaf
     h15, h151, h152, h153  = noaf, noaf, noaf, noaf
    elif count == 20:
     h122, h123, h124, h125 = noaf, noaf, noaf, noaf
     h13, h131, h132, h133, h134, h135 = noaf, noaf, noaf, noaf, noaf, noaf
     h14, h141, h142, h143, h144, h145 = noaf, noaf, noaf, noaf, noaf, noaf
     h15, h151, h152, h153  = noaf, noaf, noaf, noaf
    elif count == 21:
     h123, h124, h125 = noaf, noaf, noaf
     h13, h131, h132, h133, h134, h135 = noaf, noaf, noaf, noaf, noaf, noaf
     h14, h141, h142, h143, h144, h145 = noaf, noaf, noaf, noaf, noaf, noaf
     h15, h151, h152, h153  = noaf, noaf, noaf, noaf
    elif count == 22:
     h124, h125 = noaf, noaf
     h13, h131, h132, h133, h134, h135 = noaf, noaf, noaf, noaf, noaf, noaf
     h14, h141, h142, h143, h144, h145 = noaf, noaf, noaf, noaf, noaf, noaf
     h15, h151, h152, h153  = noaf, noaf, noaf, noaf
    elif count == 23:
     h125 = noaf
     h13, h131, h132, h133, h134, h135 = noaf, noaf, noaf, noaf, noaf, noaf
     h14, h141, h142, h143, h144, h145 = noaf, noaf, noaf, noaf, noaf, noaf
     h15, h151, h152, h153  = noaf, noaf, noaf, noaf
    elif count == 24:
     h13, h131, h132, h133, h134, h135 = noaf, noaf, noaf, noaf, noaf, noaf
     h14, h141, h142, h143, h144, h145 = noaf, noaf, noaf, noaf, noaf, noaf
     h15, h151, h152, h153  = noaf, noaf, noaf, noaf
    elif count == 25:
     h131, h132, h133, h134, h135 = noaf, noaf, noaf, noaf, noaf
     h14, h141, h142, h143, h144, h145 = noaf, noaf, noaf, noaf, noaf, noaf
     h15, h151, h152, h153  = noaf, noaf, noaf, noaf
    elif count == 26:
     h132, h133, h134, h135 = noaf, noaf, noaf, noaf
     h14, h141, h142, h143, h144, h145 = noaf, noaf, noaf, noaf, noaf, noaf
     h15, h151, h152, h153  = noaf, noaf, noaf, noaf
    elif count == 27:
     h133, h134, h135 = noaf, noaf, noaf
     h14, h141, h142, h143, h144, h145 = noaf, noaf, noaf, noaf, noaf, noaf
     h15, h151, h152, h153  = noaf, noaf, noaf, noaf
    elif count == 28:
     h134, h135 = noaf, noaf, noaf, noaf
     h14, h141, h142, h143, h144, h145 = noaf, noaf, noaf, noaf, noaf, noaf
     h15, h151, h152, h153  = noaf, noaf, noaf, noaf
    elif count == 29:
     h135 = noaf
     h14, h141, h142, h143, h144, h145 = noaf, noaf, noaf, noaf, noaf, noaf
     h15, h151, h152, h153  = noaf, noaf, noaf, noaf
    elif count == 30:
     h14, h141, h142, h143, h144, h145 = noaf, noaf, noaf, noaf, noaf, noaf
     h15, h151, h152, h153  = noaf, noaf, noaf, noaf
    elif count == 31:
     h141, h142, h143, h144, h145 = noaf, noaf, noaf, noaf, noaf
     h15, h151, h152, h153  = noaf, noaf, noaf, noaf
    elif count == 32:
     h142, h143, h144, h145 = noaf, noaf, noaf, noaf
     h15, h151, h152, h153  = noaf, noaf, noaf, noaf
    elif count == 33:
     h143, h144, h145 = noaf, noaf, noaf
     h15, h151, h152, h153  = noaf, noaf, noaf, noaf 
    elif count == 34:
     h144, h145 = noaf, noaf
     h15, h151, h152, h153  = noaf, noaf, noaf, noaf
    elif count == 35:
     h145 = noaf
     h15, h151, h152, h153  = noaf, noaf, noaf, noaf
    elif count == 36:
     h15, h151, h152, h153  = noaf, noaf, noaf, noaf
    elif count == 37:
     h151, h152, h153 = noaf, noaf, noaf
    elif count == 38:
     h152, h153 = noaf, noaf 
    elif count == 39:
     h153 = noaf      

    # 차트 생성
    fig, ax = plt.subplots()

    # 전일 값 점선
    ax.plot([0, 39], [int(nobf), int(nobf)], linestyle='dashed', color='gray', label='Previous day value')

    if int(pday) > int(h9):  # 전날값과 9시의 값을 비교
        ax.plot([0, 1], [int(pday), int(h9)], color='blue')
    elif int(pday) < int(h9):
        ax.plot([0, 1], [int(pday), int(h9)], color='red')
    else:
        ax.plot([0, 1], [int(pday), int(h9)], color='gray')

    if int(h9) > int(h91):   # 9 10
        ax.plot([1, 2], [int(h9), int(h91)], color='blue')
    elif int(h9) < int(h91):
        ax.plot([1, 2], [int(h9), int(h91)], color='red')
    else:
        ax.plot([1, 2], [int(h9), int(h91)], color='gray')

    if int(h91) > int(h92):   # 9 20
        ax.plot([2, 3], [int(h91), int(h92)], color='blue')
    elif int(h91) < int(h92):
        ax.plot([2, 3], [int(h91), int(h92)], color='red')
    else:
        ax.plot([2, 3], [int(h91), int(h92)], color='gray')

    if int(h92) > int(h93):   # 9 30
        ax.plot([3, 4], [int(h92), int(h93)], color='blue')
    elif int(h92) < int(h93):
        ax.plot([3, 4], [int(h92), int(h93)], color='red')
    else:
        ax.plot([3, 4], [int(h92), int(h93)], color='gray')

    if int(h93) > int(h94):   # 9 40
        ax.plot([4, 5], [int(h93), int(h94)], color='blue')
    elif int(h93) < int(h94):
        ax.plot([4, 5], [int(h93), int(h94)], color='red')
    else:
        ax.plot([4, 5], [int(h93), int(h94)], color='gray')

    if int(h94) > int(h95):   # 9 50
        ax.plot([5, 6], [int(h94), int(h95)], color='blue')
    elif int(h94) < int(h95):
        ax.plot([5, 6], [int(h94), int(h95)], color='red')
    else:
        ax.plot([5, 6], [int(h94), int(h95)], color='gray')

    if int(h95) > int(h10):   # 10
        ax.plot([6, 7], [int(h95), int(h10)], color='blue')
    elif int(h95) < int(h10):
        ax.plot([6, 7], [int(h95), int(h10)], color='red')
    else:
        ax.plot([6, 7], [int(h95), int(h10)], color='gray')     

    if int(h10) > int(h101):   # 10 10
        ax.plot([7, 8], [int(h10), int(h101)], color='blue')
    elif int(h10) < int(h101):
        ax.plot([7, 8], [int(h10), int(h101)], color='red')
    else:
        ax.plot([7, 8], [int(h10), int(h101)], color='gray')   

    if int(h101) > int(h102):   # 10 20
        ax.plot([8, 9], [int(h101), int(h102)], color='blue')
    elif int(h101) < int(h102):
        ax.plot([8, 9], [int(h101), int(h102)], color='red')
    else:
        ax.plot([8, 9], [int(h101), int(h102)], color='gray')  

    if int(h102) > int(h103):   # 10 30
        ax.plot([9, 10], [int(h102), int(h103)], color='blue')
    elif int(h102) < int(h103):
        ax.plot([9, 10], [int(h102), int(h103)], color='red')
    else:
        ax.plot([9, 10], [int(h102), int(h103)], color='gray')  

    if int(h103) > int(h104):   # 10 40
        ax.plot([10, 11], [int(h103), int(h104)], color='blue')
    elif int(h103) < int(h104):
        ax.plot([10, 11], [int(h103), int(h104)], color='red')
    else:
        ax.plot([10, 11], [int(h103), int(h104)], color='gray')   

    if int(h104) > int(h105):   # 10 50
        ax.plot([11, 12], [int(h104), int(h105)], color='blue')
    elif int(h104) < int(h105):
        ax.plot([11, 12], [int(h104), int(h105)], color='red')
    else:
        ax.plot([11, 12], [int(h104), int(h105)], color='gray')   

    if int(h105) > int(h11):   # 11
        ax.plot([12, 13], [int(h105), int(h11)], color='blue')
    elif int(h105) < int(h11):
        ax.plot([12, 13], [int(h105), int(h11)], color='red')
    else:
        ax.plot([12, 13], [int(h105), int(h11)], color='gray')

    if int(h11) > int(h111):   # 11 10
        ax.plot([13, 14], [int(h11), int(h111)], color='blue')
    elif int(h11) < int(h111):
        ax.plot([13, 14], [int(h11), int(h111)], color='red')
    else:
        ax.plot([13, 14], [int(h11), int(h111)], color='gray')

    if int(h111) > int(h112):   # 11 20
        ax.plot([14, 15], [int(h111), int(h112)], color='blue')
    elif int(h111) < int(h112):
        ax.plot([14, 15], [int(h111), int(h112)], color='red')
    else:
        ax.plot([14, 15], [int(h111), int(h112)], color='gray')

    if int(h112) > int(h113):   # 11 30
        ax.plot([15, 16], [int(h112), int(h113)], color='blue')
    elif int(h112) < int(h113):
        ax.plot([15, 16], [int(h112), int(h113)], color='red')
    else:
        ax.plot([15, 16], [int(h112), int(h113)], color='gray') 

    if int(h113) > int(h114):   # 11 40
        ax.plot([16, 17], [int(h113), int(h114)], color='blue')
    elif int(h113) < int(h114):
        ax.plot([16, 17], [int(h113), int(h114)], color='red')
    else:
        ax.plot([16, 17], [int(h113), int(h114)], color='gray')

    if int(h114) > int(h115):   # 11 50
        ax.plot([17, 18], [int(h114), int(h115)], color='blue')
    elif int(h114) < int(h115):
        ax.plot([17, 18], [int(h114), int(h115)], color='red')
    else:
        ax.plot([17, 18], [int(h114), int(h115)], color='gray')  

    if int(h115) > int(h12):   # 12
        ax.plot([18, 19], [int(h115), int(h12)], color='blue')
    elif int(h115) < int(h12):
        ax.plot([18, 19], [int(h115), int(h12)], color='red')
    else:
        ax.plot([18, 19], [int(h115), int(h12)], color='gray')      

    if int(h12) > int(h121):   # 12 10
        ax.plot([19, 20], [int(h12), int(h121)], color='blue')
    elif int(h12) < int(h121):
        ax.plot([19, 20], [int(h12), int(h121)], color='red')
    else:
        ax.plot([19, 20], [int(h12), int(h121)], color='gray')    

    if int(h121) > int(h122):   # 12 20
        ax.plot([20, 21], [int(h121), int(h122)], color='blue')
    elif int(h121) < int(h122):
        ax.plot([20, 21], [int(h121), int(h122)], color='red')
    else:
        ax.plot([20, 21], [int(h121), int(h122)], color='gray')     

    if int(h122) > int(h123):   # 12 30
        ax.plot([21, 22], [int(h122), int(h123)], color='blue')
    elif int(h122) < int(h123):
        ax.plot([21, 22], [int(h122), int(h123)], color='red')
    else:
        ax.plot([21, 22], [int(h122), int(h123)], color='gray') 

    if int(h123) > int(h124):   # 12 40
        ax.plot([22, 23], [int(h123), int(h124)], color='blue')
    elif int(h123) < int(h124):
        ax.plot([22, 23], [int(h123), int(h124)], color='red')
    else:
        ax.plot([22, 23], [int(h123), int(h124)], color='gray')  

    if int(h124) > int(h125):   # 12 50
        ax.plot([23, 24], [int(h124), int(h125)], color='blue')
    elif int(h124) < int(h125):
        ax.plot([23, 24], [int(h124), int(h125)], color='red')
    else:
        ax.plot([23, 24], [int(h124), int(h125)], color='gray')    

    if int(h125) > int(h13):   # 13
        ax.plot([24, 25], [int(h125), int(h13)], color='blue')
    elif int(h125) < int(h13):
        ax.plot([24, 25], [int(h125), int(h13)], color='red')
    else:
        ax.plot([24, 25], [int(h125), int(h13)], color='gray')

    if int(h13) > int(h131):   # 13 10
        ax.plot([25, 26], [int(h13), int(h131)], color='blue')
    elif int(h13) < int(h131):
        ax.plot([25, 26], [int(h13), int(h131)], color='red')
    else:
        ax.plot([25, 26], [int(h13), int(h131)], color='gray')   

    if int(h131) > int(h132):   # 13 20
        ax.plot([26, 27], [int(h131), int(h132)], color='blue')
    elif int(h131) < int(h132):
        ax.plot([26, 27], [int(h131), int(h132)], color='red')
    else:
        ax.plot([26, 27], [int(h131), int(h132)], color='gray')  

    if int(h132) > int(h133):   # 13 30
        ax.plot([27, 28], [int(h132), int(h133)], color='blue')
    elif int(h132) < int(h133):
        ax.plot([27, 28], [int(h132), int(h133)], color='red')
    else:
        ax.plot([27, 28], [int(h132), int(h133)], color='gray')  

    if int(h133) > int(h134):   # 13 40
        ax.plot([28, 29], [int(h133), int(h134)], color='blue')
    elif int(h133) < int(h134):
        ax.plot([28, 29], [int(h133), int(h134)], color='red')
    else:
        ax.plot([28, 29], [int(h133), int(h134)], color='gray')  

    if int(h134) > int(h135):   # 13 50
        ax.plot([29, 30], [int(h134), int(h135)], color='blue')
    elif int(h134) < int(h135):
        ax.plot([29, 30], [int(h134), int(h135)], color='red')
    else:
        ax.plot([29, 30], [int(h134), int(h135)], color='gray')   

    if int(h135) > int(h14):   # 14
        ax.plot([30, 31], [int(h135), int(h14)], color='blue')
    elif int(h135) < int(h14):
        ax.plot([30, 31], [int(h135), int(h14)], color='red')
    else:
        ax.plot([30, 31], [int(h135), int(h14)], color='gray')      

    if int(h14) > int(h141):   # 14 10
        ax.plot([31, 32], [int(h14), int(h141)], color='blue')
    elif int(h14) < int(h141):
        ax.plot([31, 32], [int(h14), int(h141)], color='red')
    else:
        ax.plot([31, 32], [int(h14), int(h141)], color='gray')  

    if int(h141) > int(h142):   # 14 20
        ax.plot([32, 33], [int(h141), int(h142)], color='blue')
    elif int(h141) < int(h142):
        ax.plot([32, 33], [int(h141), int(h142)], color='red')
    else:
        ax.plot([32, 33], [int(h141), int(h142)], color='gray')     

    if int(h142) > int(h143):   # 14 30
        ax.plot([33, 34], [int(h142), int(h143)], color='blue')
    elif int(h142) < int(h143):
        ax.plot([33, 34], [int(h142), int(h143)], color='red')
    else:
        ax.plot([33, 34], [int(h142), int(h143)], color='gray')

    if int(h143) > int(h144):   # 14 40
        ax.plot([34, 35], [int(h143), int(h144)], color='blue')
    elif int(h143) < int(h144):
        ax.plot([34, 35], [int(h143), int(h144)], color='red')
    else:
        ax.plot([34, 35], [int(h143), int(h144)], color='gray')  

    if int(h144) > int(h145):   # 14 50
        ax.plot([35, 36], [int(h144), int(h145)], color='blue')
    elif int(h144) < int(h145):
        ax.plot([35, 36], [int(h144), int(h145)], color='red')
    else:
        ax.plot([35, 36], [int(h144), int(h145)], color='gray')   

    if int(h145) > int(h15):   # 15
        ax.plot([36, 37], [int(h145), int(h15)], color='blue')
    elif int(h145) < int(h15):
        ax.plot([36, 37], [int(h145), int(h15)], color='red')
    else:
        ax.plot([36, 37], [int(h145), int(h15)], color='gray')       

    if int(h15) > int(h151):   # 15 10
        ax.plot([37, 38], [int(h15), int(h151)], color='blue')
    elif int(h15) < int(h151):
        ax.plot([37, 38], [int(h15), int(h151)], color='red')
    else:
        ax.plot([37, 38], [int(h15), int(h151)], color='gray')  

    if int(h151) > int(h152):   # 15 20
        ax.plot([38, 39], [int(h151), int(h152)], color='blue')
    elif int(h151) < int(h152):
        ax.plot([38, 39], [int(h151), int(h152)], color='red')
    else:
        ax.plot([38, 39], [int(h151), int(h152)], color='gray')    

    if int(h152) > int(h153):   # 15 30
        ax.plot([39, 40], [int(h152), int(h153)], color='blue')
    elif int(h152) < int(h153):
        ax.plot([39, 40], [int(h152), int(h153)], color='red')
    else:
        ax.plot([39, 40], [int(h152), int(h153)], color='gray')                                                                                                          

        ax.set_xlabel('Time')
        ax.set_ylabel('Samsung')
        ax.legend()

        # x축 눈금 설정
        ax.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40])  
        xticklabels = ['', '9h', '10', '20', '30', '40', '50', '10h', '10', '20', '30', '40', '50', '11h', '10', '20', '30', '40', '50', '12h', '10', '20', '30', '40', '50', '13h', '10', '20', '30', '40', '50', '14h', '10', '20', '30', '40', '50', '15h', '10', '20', '30'] 
       
        # 눈금 레이블에 대한 스타일 설정
        for i, label in enumerate(ax.get_xticklabels()):
          label.set_fontsize(5)  # 글자 크기 5로 조절
          label.set_verticalalignment('top')  # 세로 정렬 조절      

        ax.set_xticklabels(xticklabels)

        # 차트를 이미지로 저장
        img_buffer = BytesIO()
        plt.savefig(img_buffer, format='png')
        img_buffer.seek(0)

    if channel:
        await channel.send(file=discord.File(img_buffer, filename='chart.png'))
        await channel.send(f'현재 시간: {current_time}\n삼성 주가: {After}원\n삼성 전일 주가{Before}원\n사용자 입력 값 : {user_input_value}\n{comparison_message}\n기사 제목: {title_text}\n기사 날짜: {span2_value}\n기사 링크: {link_url}')
        if date_td:
         date_info = date_td.text.strip()
         # 크롤링한 날짜 문자열을 datetime 객체로 변환
         crawled_date = datetime.strptime(date_info, "%Y년 %m월 %d일")
         today = datetime.today()
         d_day = (crawled_date - today).days + 1

         print(f'크롤링한 날짜: {crawled_date.strftime("%Y-%m-%d")}')
         print(f'현재 날짜: {today.strftime("%Y-%m-%d")}')

         if today == crawled_date:
          print('D-day')
          await channel.send('D-day')
         else:
          print(f'D-day: {d_day}')
          await channel.send(f'실적발표 까지 : D-{d_day}')

        else:
         print('날짜 정보를 찾을 수 없습니다.')
        
        print('메시지 보냄')

        count += 1
        if count == 40:
           count = 0
           print(f'카운트{count} 초기화')
        else: 
           print(f'카운트{count}')  
    else:
        print("채널을 찾을 수 없습니다.")

# 비동기 함수로 스케줄러를 시작합니다.
async def start_scheduler():
    # 스케줄링을 시작합니다.
    schedule.every().day.at("09:00").do(lambda: asyncio.create_task(send_discord_message()))
    schedule.every().day.at("09:10").do(lambda: asyncio.create_task(send_discord_message()))
    schedule.every().day.at("09:20").do(lambda: asyncio.create_task(send_discord_message()))
    schedule.every().day.at("09:30").do(lambda: asyncio.create_task(send_discord_message()))
    schedule.every().day.at("09:40").do(lambda: asyncio.create_task(send_discord_message()))
    schedule.every().day.at("09:50").do(lambda: asyncio.create_task(send_discord_message()))
    schedule.every().day.at("10:00").do(lambda: asyncio.create_task(send_discord_message()))
    schedule.every().day.at("10:10").do(lambda: asyncio.create_task(send_discord_message()))
    schedule.every().day.at("10:20").do(lambda: asyncio.create_task(send_discord_message()))
    schedule.every().day.at("10:30").do(lambda: asyncio.create_task(send_discord_message()))
    schedule.every().day.at("10:40").do(lambda: asyncio.create_task(send_discord_message()))
    schedule.every().day.at("10:50").do(lambda: asyncio.create_task(send_discord_message()))
    schedule.every().day.at("11:00").do(lambda: asyncio.create_task(send_discord_message()))
    schedule.every().day.at("11:10").do(lambda: asyncio.create_task(send_discord_message()))
    schedule.every().day.at("11:20").do(lambda: asyncio.create_task(send_discord_message()))
    schedule.every().day.at("11:30").do(lambda: asyncio.create_task(send_discord_message()))
    schedule.every().day.at("11:40").do(lambda: asyncio.create_task(send_discord_message()))
    schedule.every().day.at("11:50").do(lambda: asyncio.create_task(send_discord_message()))
    schedule.every().day.at("12:00").do(lambda: asyncio.create_task(send_discord_message()))
    schedule.every().day.at("12:10").do(lambda: asyncio.create_task(send_discord_message()))
    schedule.every().day.at("12:20").do(lambda: asyncio.create_task(send_discord_message()))
    schedule.every().day.at("12:30").do(lambda: asyncio.create_task(send_discord_message()))
    schedule.every().day.at("12:40").do(lambda: asyncio.create_task(send_discord_message()))
    schedule.every().day.at("12:50").do(lambda: asyncio.create_task(send_discord_message()))
    schedule.every().day.at("13:00").do(lambda: asyncio.create_task(send_discord_message()))
    schedule.every().day.at("13:10").do(lambda: asyncio.create_task(send_discord_message()))
    schedule.every().day.at("13:20").do(lambda: asyncio.create_task(send_discord_message()))
    schedule.every().day.at("13:30").do(lambda: asyncio.create_task(send_discord_message()))
    schedule.every().day.at("13:40").do(lambda: asyncio.create_task(send_discord_message()))
    schedule.every().day.at("13:50").do(lambda: asyncio.create_task(send_discord_message()))
    schedule.every().day.at("14:00").do(lambda: asyncio.create_task(send_discord_message()))
    schedule.every().day.at("14:10").do(lambda: asyncio.create_task(send_discord_message()))
    schedule.every().day.at("14:20").do(lambda: asyncio.create_task(send_discord_message()))
    schedule.every().day.at("14:30").do(lambda: asyncio.create_task(send_discord_message()))
    schedule.every().day.at("14:40").do(lambda: asyncio.create_task(send_discord_message()))
    schedule.every().day.at("14:50").do(lambda: asyncio.create_task(send_discord_message()))
    schedule.every().day.at("15:00").do(lambda: asyncio.create_task(send_discord_message()))
    schedule.every().day.at("15:10").do(lambda: asyncio.create_task(send_discord_message()))
    schedule.every().day.at("15:20").do(lambda: asyncio.create_task(send_discord_message()))
    schedule.every().day.at("15:30").do(lambda: asyncio.create_task(send_discord_message()))
    
    while True:
        schedule.run_pending()
        await asyncio.sleep(1)

# 봇 실행 시 이벤트 루프에 스케줄러를 등록합니다.
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    client.loop.create_task(start_scheduler())

@client.event
async def on_message(message):
    global user_input_value

    if message.author == client.user:
        return

    if message.content.startswith('!입력'):
        user_input_value = message.content[4:].strip()
        await message.channel.send(f'입력값으로 {user_input_value} 을(를) 받았습니다.')
        return

# 봇을 실행합니다.
client.run(TOKEN)