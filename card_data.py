import requests
from bs4 import BeautifulSoup
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_card.settings')
import django
django.setup()

from card.models import Card

# KB 국민카드 전체 링크 목록 (132 cards)
urlList = ['https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01790&categoryCode=L0086&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01772&categoryCode=L0087&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01788&categoryCode=L0086&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01946&categoryCode=L0087&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01664&categoryCode=L0086&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01990&categoryCode=L0087&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01988&categoryCode=L0086&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01560&categoryCode=L0087&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=04120&categoryCode=L0086&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01781&categoryCode=L0088&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01911&categoryCode=L0089&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01932&categoryCode=L0088&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01945&categoryCode=L0088&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01988&categoryCode=L0090&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=04906&categoryCode=L0091&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01928&categoryCode=L0090&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01736&categoryCode=L0091&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01996&categoryCode=L0091&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01690&categoryCode=L0092&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01776&categoryCode=L0093&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01560&categoryCode=L0092&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01974&categoryCode=L0093&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01552&categoryCode=L0092&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01754&categoryCode=L0093&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=09156&categoryCode=L0093&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01998&categoryCode=L0093&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01976&categoryCode=L0093&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01946&categoryCode=L0093&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01556&categoryCode=L0093&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01770&categoryCode=L0094&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01945&categoryCode=L0095&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01930&categoryCode=L0094&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01699&categoryCode=L0095&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01680&categoryCode=L0095&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01794&categoryCode=L0096&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01798&categoryCode=L0097&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01792&categoryCode=L0096&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01796&categoryCode=L0097&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01728&categoryCode=L0096&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01730&categoryCode=L0097&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01784&categoryCode=L0096&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01786&categoryCode=L0097&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01564&categoryCode=L0096&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01568&categoryCode=L0097&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01720&categoryCode=L0096&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01722&categoryCode=L0097&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01724&categoryCode=L0096&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01726&categoryCode=L0097&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01756&categoryCode=L0096&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01758&categoryCode=L0097&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01704&categoryCode=L0096&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01708&categoryCode=L0097&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01732&categoryCode=L0096&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01734&categoryCode=L0097&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01992&categoryCode=L0096&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01994&categoryCode=L0097&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01706&categoryCode=L0096&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01710&categoryCode=L0097&sGroupCode=2', #여기까지 체크카드
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=09194&categoryCode=L0049&sGroupCode=1', #여기부터 신용카드
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=09243&categoryCode=L0048&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=09251&categoryCode=L0048&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=04350&categoryCode=L0048&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=04581&categoryCode=L0049&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=04420&categoryCode=L0049&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=04415&categoryCode=L0048&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=04422&categoryCode=L0049&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=09175&categoryCode=L0048&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01234&categoryCode=L0049&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=09173&categoryCode=L0048&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=09157&categoryCode=L0048&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=09167&categoryCode=L0048&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=09176&categoryCode=L0048&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=09040&categoryCode=L0048&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=04413&categoryCode=L0048&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=04433&categoryCode=L0048&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=09245&categoryCode=L0050&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=09252&categoryCode=L0051&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=09244&categoryCode=L0050&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=09169&categoryCode=L0051&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=04434&categoryCode=L0050&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=04451&categoryCode=L0051&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=09231&categoryCode=L0050&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=09230&categoryCode=L0050&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=04404&categoryCode=L0050&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=04411&categoryCode=L0050&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=04451&categoryCode=L0053&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=09249&categoryCode=L0052&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=09228&categoryCode=L0053&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01111&categoryCode=L0052&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=04432&categoryCode=L0052&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=04260&categoryCode=L0053&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=04333&categoryCode=L0052&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=02222&categoryCode=L0054&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=04240&categoryCode=L0055&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=09180&categoryCode=L0054&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=04249&categoryCode=L0055&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=04322&categoryCode=L0055&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=04484&categoryCode=L0055&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=04482&categoryCode=L0055&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=04444&categoryCode=L0056&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=09184&categoryCode=L0057&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=09183&categoryCode=L0057&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=09214&categoryCode=L0057&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=04409&categoryCode=L0057&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=09233&categoryCode=L0057&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=09232&categoryCode=L0057&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=09063&categoryCode=L0058&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=04419&categoryCode=L0059&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=02233&categoryCode=L0058&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=04440&categoryCode=L0059&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01142&categoryCode=L0059&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=04583&categoryCode=L0059&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=09246&categoryCode=L0060&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=04418&categoryCode=L0061&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=09218&categoryCode=L0060&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=04328&categoryCode=L0061&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=09217&categoryCode=L0060&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=04417&categoryCode=L0061&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=09237&categoryCode=L0060&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=04416&categoryCode=L0061&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=04459&categoryCode=L0060&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=04423&categoryCode=L0061&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=02245&categoryCode=L0060&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=04426&categoryCode=L0061&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=04863&categoryCode=L0060&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=04481&categoryCode=L0061&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=04478&categoryCode=L0061&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=04485&categoryCode=L0061&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=04487&categoryCode=L0061&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=04486&categoryCode=L0061&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=04489&categoryCode=L0061&sGroupCode=1',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=04425&categoryCode=L0061&sGroupCode=1']



# 카드 혜택 분류 기준
# 1 : 외식/eatout, 2 : 생활/living, 3 : 쇼핑/shopping, 4 : 주유/refuel, 5 : 통신/communicate, 6 : 해외/overseas, 7 : 문화/culture
eatout = ['외식', '커피', '패스트푸드', '패밀리레스토랑', '제과', '아이스크림', '커피빈', '아웃백',
          'VIPS', 'TGIF', '세븐스프링스', '스타벅스', '파리바게뜨', '뚜레쥬르', '해피포인트', '리테일']
living = ['골프', '사우나', '병원', '약국', '학원', '보험료', '버스', '지하철', '택시', '대중교통', '야놀자', '동물', '학습비','CU', 'GS25', '편의점']
shopping = ['마트', '홈쇼핑', '다이소', '헤어', '올리브영', '소셜커머스', '백화점', '롯데', '현대', '신세계', 'G마켓', '옥션', '화장품',
            '미용', 'AK', '아모레퍼시픽', '티몬', '쿠팡', '위메프', '홈플러스', '11번가', '쇼핑', '배달', '캐릭터샵', '식품', '면세점' ]
refuel = ['주유소', 'GS칼텍스', '스피드메이트', 'SK에너지', '충전소', '주유']
communicate = ['통신']
overseas = ['해외', '항공', '라이프샵', '여행', '공항', '라운지', 'RefreshPoint', '투어', '마일리지']
culture = ['놀이공원', '문고', 'CGV', '메가박스', '에버랜드', '서울랜드', '롯데월드', '서점', '게임', '미술관', '영화']



# benefitCheck : 혜택을 string으로 받아 카드 혜택별로 번호를 부여해주는 함수
def benefitCheck(str):
    code = ""

    for word in eatout:
        if word in str:
            code = "1"
            return code

    for word in living:
        if word in str:
            code = "2"
            return code

    for word in shopping:
        if word in str:
            code = "3"
            return code

    for word in refuel:
        if word in str:
            code = "4"
            return code

    for word in communicate:
        if word in str:
            code = "5"
            return code

    for word in overseas:
        if word in str:
            code = "6"
            return code

    for word in culture:
        if word in str:
            code = "7"
            return code

    return code


for url in urlList:
    req = requests.get(url)
    raw = req.text
    html = BeautifulSoup(raw, 'html.parser')

    cardname = html.select('h1.tit')
    benefits = html.select('span.txt')


    benefitList = ""  # benefitList : 혜택을 문자열로 저장
    benefitCode = []  # benefitCode : 혜택 코드를 문자열로 저장
    codeNum = "" #혜택 코드를 문자열로 변환해서 저장할 변수
    num = 0  # num : 혜택을 나열할 때 쉼표를 표시하기 위해 해당 혜택이 첫번째인지 아닌지를 확인하는 수

    for benefit in benefits:
        # 해당 혜택 앞에 쉼표를 붙일지말지 확인
        if num == 0:
            benefitList = benefit.text
            num += 1
        else:
            benefitList += ', ' + benefit.text

        # 혜택이 해당되는 분야를 찾아 특정 코드 받아오기기
        benefitCode += benefitCheck(benefit.text)
        benefitCode = list(set(benefitCode))
        benefitCode.sort()
        codeNum = ",".join(benefitCode)

    if __name__ == '__main__':
        Card(name=cardname[0].text, bank='국민카드', benefit=benefitList, bn=codeNum, af='').save()