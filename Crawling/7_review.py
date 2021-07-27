from selenium import webdriver
import logging, time

# 로거생성
logger = logging.getLogger('movie_logger')
logger.setLevel(logging.INFO)

# 로그 포멧 설정
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# 가상 브라우저 실행
browser = webdriver.Chrome('./chromedriver.exe')

page = 1
rank = 0

while True:
    # 현재 브라우저를 전환
    browser.switch_to.default_content()

    # 페이지 이동
    if page > 40:
        break

    browser.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&page=%d' % page)

    if rank == 49:
        rank = 0
        page += 1

    # 순위별 영화 클릭
    titles = browser.find_elements_by_css_selector('#old_content > table > tbody > tr > td.title > div > a')
    titles[rank].click()
    rank += 1

    # 영화 제목
    movie_title = browser.find_element_by_css_selector('#content > div.article > div.mv_info_area > div.mv_info > h3 > a').text

    # 영화 평점 클릭
    menu_score = browser.find_element_by_css_selector('#movieEndTabMenu > li > a.tab05')
    menu_score.click()

    # 현재 가상 브라우저를 영화리뷰가 있는 iframe으로 전환
    browser.switch_to.frame('pointAfterListIframe')

    while True:
        # 영화 리뷰 출력
        lis = browser.find_elements_by_css_selector('body > div > div > div.score_result > ul > li')

        for li in lis:
            score = li.find_element_by_css_selector('div.star_score > em').text
            reple = li.find_element_by_css_selector('div.score_reple > p > span:last-child').text

            print('{},{}'.format(score, reple))

        # 다음 페이지 클릭
        try:
            btn_next = browser.find_element_by_css_selector('body > div > div > div.paging > div > a:last-child > em')
            btn_next.click()
        except:
            break

print('영화 리뷰 수집 완료')

browser.close()
