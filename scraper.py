# Module Installation
import importlib.util
import subprocess
import sys
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=DeprecationWarning)

modules = ['bs4', 'selenium']
for module in modules:
    if module not in sys.modules and importlib.util.find_spec(module) is None:
        subprocess.call([sys.executable, "-m", "pip", "install", "-q", module, "--upgrade"])

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
import re # regular expression
from datetime import datetime

CHROME_DRIVER_PATH = '../chromedriver'
FIELDS = ['id', 'headline', 'summary', 'created', 'source']
FILE_DIR = 'Data/'

# Reuters
RTR = 'Reuters'
RTR_URL = 'https://www.reuters.com/news/archive/baseball-mlb?view=page&pageSize=10&page='
RTR_FILE_NAME = 'reuters.csv'
RTR_LINK_TEXT = 'Next Page'
RTR_PAGES = 1000
RTR_ID_PREFIX = '1'

# MLB
MLB = 'MLB'
MLB_URL = 'https://www.mlb.com/news'
MLB_FILE_NAME = 'mlb.csv'
MLB_LINK_TEXT = 'LATER'
MLB_BUTTON_CLASS = 'onetrust-close-btn-handler onetrust-close-btn-ui banner-close-button onetrust-lg ot-close-icon'
MLB_ID_PREFIX = '2'

# WSJ
WSJ = 'WSJ'
WSJ_URL = 'https://www.wsj.com/news/types/mlb?page='
#WSJ_URL = 'https://www.wsj.com/news/types/mlb' # clickable issue
WSJ_FILE_NAME = 'wsj.csv'
WSJ_LINK_TEXT = 'Next Page'
WSJ_PAGES = 62
WSJ_ID_PREFIX = '3'

# NY Times
NYT = 'NYTimes'
MONTHS_CONV = {'Jan.': 'January', 'Feb.': 'February', 'Aug.': 'August', 'Sept.': 'September', 'Oct.': 'October', 'Nov.': 'November', 'Dec.': 'December'}
MONTHS_CONV_KEYS = MONTHS_CONV.keys()
MONTHS_FINE = ['March', 'April', 'May', 'June', 'July']
MONTHS = list(MONTHS_CONV.values()) + MONTHS_FINE
NYT_URL = 'https://www.nytimes.com/search?query=BASEBALL'
NYT_FILE_NAME = 'nyt.csv'
NYT_START_END_YEARS = {'start': 2011, 'end': 2021}
NYT_BUTTON_NAME = 'Show More'
NYT_ID_PREFIX = '4'

# ESPN
ESPN = 'ESPN'
ESPN_URL = 'https://www.espn.com/mlb/story/_/id/32388189'
ESPN_FILE_NAME = 'espn.csv'
ESPN_ID_PREFIX = '5'

# Reuters
def scrape_rtr(url, driver, idx):
    
    # execute js on webpage to load contents on webpage and get ready to parse the loaded HTML 
    soup = get_js_soup(url, driver)
    soup = remove_script(soup)

    articles = []
    div = soup.find('div', class_='column1 col col-10')
    for story in div.find_all('article', class_='story'):
        article = {}
        div1 = story.find('div', class_='story-content')
        
        # headline
        a = div1.find('a')
        headline = a.find('h3', class_='story-title').get_text()

        # created
        #tm = div.find('time', class_='article-time')
        for child in div1.children:

            # headline
            if child.name == 'a':
                headline = child.find('h3', class_='story-title').get_text()
            
            # summary
            elif child.name == 'p':
                summary = child.get_text()
            
            # summary
            elif child.name == 'time':
                span = child.find('span', class_='timestamp').get_text()
                created = format_date(span)
                break

        if created == None:
            continue

        # id
        id = generate_id(created, RTR_ID_PREFIX, idx)

        article[FIELDS[0]] = id
        article[FIELDS[1]] = process_text(headline)
        article[FIELDS[2]] = process_text(summary)
        article[FIELDS[3]] = created
        article[FIELDS[4]] = RTR
        articles.append(article)
    return articles, idx

# MLB
def scrape_mlb(url, driver):
    
    # execute js on webpage to load contents on webpage and get ready to parse the loaded HTML 
    soup = get_js_soup(url, driver, MLB_ID_PREFIX)
    soup = remove_script(soup)

    idx = {}
    articles = []
    for story in soup.find_all('article', class_='l-grid__content--card article-item article-item--article article-item--search'):
        article = {}

        # headline
        div1 = story.find('div', class_='article-item__top')
        headline = div1.find('h1', class_='article-item__headline').get_text()

        # created
        div2 = story.find('div', class_='article-item__meta-container')
        div3 = div2.find('div', class_='article-item__contributor-container')
        div4 = div3.find('div', class_='article-item__contributor-inner')
        div5 = div4.find('div', class_='article-item__contributor-date')['data-date']
        created = div5[:div5.find('T')]

        # summary
        div6 = story.find('div', class_='article-item__bottom')
        div7 = div6.find('div', class_='article-item__preview')
        summary = div7.find('p').get_text()

        # id
        id = generate_id(created, MLB_ID_PREFIX, idx)

        article[FIELDS[0]] = id
        article[FIELDS[1]] = process_text(headline)
        article[FIELDS[2]] = process_text(summary)
        article[FIELDS[3]] = created
        article[FIELDS[4]] = MLB
        articles.append(article)
    return articles

# WSJ
def scrape_wsj(url, driver):
    
    # execute js on webpage to load contents on webpage and get ready to parse the loaded HTML 
    soup = get_js_soup(url, driver)
    soup = remove_script(soup)

    idx = {}
    articles = []
    for story in soup.find_all('article', class_='WSJTheme--story--XB4V2mLz WSJTheme--design-refresh--2eDQsiEp'):
        article = {}
        div = story.find('div', class_='WSJTheme--content-float-right--1NZyrHNk')

        # headline
        div1 = div.find('div', class_='WSJTheme--headline--7VCzo7Ay')
        h2 = div1.find('h2', class_='WSJTheme--headline--unZqjb45 undefined')
        a = h2.find('a')
        headline = a.find('span', class_='WSJTheme--headlineText--He1ANr9C').get_text()

        # summary
        p = div.find('p', class_='WSJTheme--summary--lmOXEsbN typography--serif--1CqEfjrc')
        summary = p.find('span', class_='WSJTheme--summaryText--2LRaCWgJ').get_text()

        # created
        div2 = div.find('div', class_='')
        div3 = div2.find('div', class_='WSJTheme--timestamp--2zjbypGD')
        p = div3.find('p', class_='WSJTheme--timestamp--22sfkNDv').get_text()
        created = format_date(p)

        if created == None:
            continue

        # id
        id = generate_id(created, WSJ_ID_PREFIX, idx)

        article[FIELDS[0]] = id
        article[FIELDS[1]] = process_text(headline)
        article[FIELDS[2]] = process_text(summary)
        article[FIELDS[3]] = created
        article[FIELDS[4]] = WSJ
        articles.append(article)
    return articles

# NY Times
def scrape_nyt(url, driver):
    
    # execute js on webpage to load contents on webpage and get ready to parse the loaded HTML
    soup = get_js_soup(url, driver, NYT_ID_PREFIX)
    soup = remove_script(soup)

    idx = {}
    articles = []
    div = soup.find('div', class_='css-46b038')
    ol = div.find('ol')
    for li in ol.find_all('li', class_='css-1l4w6pd'):
        article = {}
        div1 = li.find('div', class_='css-1bdu3ax')
        if div1 == None:
            div1 = li.find('div', class_='css-1kl114x')

        # created
        span = div1.find('span', class_='css-17ubb9w').get_text()
        created = format_date(span)

        if created == None:
            continue
        
        # headline
        div2 = div1.find('div', class_='css-1i8vfl5')
        div3 = div2.find('div', class_='css-e1lvw9')
        a = div3.find('a')
        headline = a.find('h4', class_='css-2fgx4k').get_text()

        # summary
        summary = a.find('p', class_='css-16nhkrn').get_text()

        # id
        id = generate_id(created, NYT_ID_PREFIX, idx)

        article[FIELDS[0]] = id
        article[FIELDS[1]] = process_text(headline)
        article[FIELDS[2]] = process_text(summary) if summary != None else ''
        article[FIELDS[3]] = created
        article[FIELDS[4]] = NYT
        articles.append(article)
    return articles

# ESPN
def scrape_espn(url, driver):
    
    # execute js on webpage to load contents on webpage and get ready to parse the loaded HTML
    soup = get_js_soup(url, driver)
    soup = remove_script(soup)

    idx = {}
    articles = []
    section = soup.find('section', class_='col-b')
    for art in section.find_all('article', class_='article'):
        article = {}
        div = art.find('div', class_='container')

        # headline
        header = div.find('header', class_='article-header')
        headline = header.find('h1').get_text()

        # created
        div1 = div.find('div', class_='article-body')
        div2 = div1.find('div', class_='article-meta')
        span = div2.find('span', class_='timestamp')['data-date']
        created = span[:span.find('T')]

        # summary
        for child in div1.children:
            if child.name == 'p':
                summary = child.get_text()
                break
        # id
        id = generate_id(created, ESPN_ID_PREFIX, idx)

        article[FIELDS[0]] = id
        article[FIELDS[1]] = process_text(headline)
        article[FIELDS[2]] = process_text(summary)
        article[FIELDS[3]] = created
        article[FIELDS[4]] = ESPN
        articles.append(article)
    return articles

def generate_id(date, prefix, idx):
    id = date.replace('-', '') # e.g. 2021-09-01 -> 20210901
    suffix = idx.get(id, 0) + 1
    idx[id] = suffix
    suffix_ = '0' if suffix < 10 else ''
    id += prefix + suffix_ + str(suffix)
    return id
    
def format_date(date):
    date = date.strip()

    # NY Times
    for key in MONTHS_CONV_KEYS:
        date = date.replace(key, MONTHS_CONV[key]) # e.g. Sept. -> September

    # ignore data without Month (e.g. 8m ago)
    pos_start = date.find(" ")
    if date[:pos_start] not in MONTHS:
        return None
    
    pos_start += 1
    pos_stop = date.find(',')
    if pos_stop < 0:
        ws_cnt = date.count(" ")
        # Router
        if ws_cnt > 1:
            pos = len(date) - 4
            date = date[:pos - 1] + ', ' + date[pos:]
        # NY Times
        else:
            date = date + ', ' + str(NYT_START_END_YEARS['end']) # e.g. September 1 -> September 1, 2021
        pos_stop = date.find(',')

    # 2011 <= year
    year = date[pos_stop + 2:]
    if int(year) < NYT_START_END_YEARS['start']:
        return None

    if len(date[pos_start:pos_stop]) == 1:
        date = date[0:pos_start] + '0' + date[pos_start:]
    dt = datetime.strptime(date, '%B %d, %Y') # e.g. September 1, 2021 -> 2021-09-01 00:00:00
    date = dt.strftime('%Y-%m-%d')
    return date

# use webdriver object to execute javascript code and get dynamically loaded webcontent
def get_js_soup(url, driver, site=None):
    print(url)
    driver.maximize_window()
    driver.get(url)
    time_sleep = 1

    if site == MLB_ID_PREFIX:
        time_sleep = 5
        click_close(MLB_BUTTON_CLASS)
        time.sleep(30)
        click_link(MLB_LINK_TEXT)
    
    # scroll the page till the bottom
    last_height = driver.execute_script('return document.body.scrollHeight')
    while True:
        driver.execute_script("window.scrollTo({left: 0, top: " + str(last_height) + ", behavior: 'auto'})")
        time.sleep(time_sleep)

        if site == NYT_ID_PREFIX:
            click_button(NYT_BUTTON_NAME)
        elif site == WSJ_ID_PREFIX:
            driver.implicitly_wait(10)
            click_link(WSJ_LINK_TEXT)

        new_height = driver.execute_script('return document.body.scrollHeight')
        if new_height == last_height:
            break
        last_height = new_height
    res_html = driver.execute_script('return document.body.innerHTML')

    # beautiful soup object to be used for parsing html content
    soup = BeautifulSoup(res_html, 'html.parser')
    return soup

def click_close(class_name):
    button = driver.find_element_by_xpath("//button[@class='" + class_name + "']")
    if button != None:
        button.click()
        time.sleep(1)

def click_link(text):
    span = driver.find_element_by_xpath("//*[contains(text(), '" + text + "')]")
    if span != None:
        link = span.find_element_by_xpath(".//ancestor::a")
        if link != None:
            link.click()
            time.sleep(1)

def click_button(button_name):
    button = driver.find_element_by_xpath("//button[text()='" + button_name + "']")
    if button != None:
        button.click()
        time.sleep(1)

def remove_script(soup):
    for script in soup(["script", "style"]):
        script.decompose()
    return soup

# tidie extracted text
def process_text(text):
    text = text.strip()

    # removes non-ascii characters
    text = text.encode('ascii', errors='ignore').decode('utf-8')
    
    # repalces tab return and repeated whitespace characters with single space
    for c in ['"', "'", '\t', '\n']:
        text = text.replace(c, " ")
    cleaned = re.sub('\s+', " ", text)
    return cleaned

# write a csv
def write_csv(pages, file_name):
    with open(FILE_DIR + file_name, encoding='utf-8', mode='w') as f:
        f.write(','.join(f'"{v}"' for v in FIELDS) + '\n')
        for page in pages:
            for article in page:
                f.write(','.join(f'"{v}"' for v in article.values()) + '\n')

if __name__ == '__main__':

    if len(sys.argv) < 2 or sys.argv[1] is None or sys.argv[1].strip() == '':
        print('Please specify site_name: Reuters, MLB, WSJ, NYTimes or ESPN')
        exit()
    
    site_name = sys.argv[1]
    print('site_name: ' + site_name)

    if site_name not in ['Reuters', 'MLB', 'WSJ', 'NYTimes', 'ESPN']:
        print('Please specify site_name: Reuters, MLB, WSJ, NYTimes or ESPN')
        exit()

    # create a webdriver object and set options for headless browsing
    options = Options()
    options.headless = True # True: the page will not popup
    service = Service(CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)
    
    # Reuters
    if site_name == 'Reuters':
        pages = []
        idx = {}
        for i in range(RTR_PAGES):
            articles, idx = scrape_rtr(RTR_URL + str(i+1), driver, idx)
            pages.append(articles)
        write_csv(pages, RTR_FILE_NAME)
    
    # MLB
    elif site_name == 'MLB':
        pages = []
        articles = scrape_mlb(MLB_URL, driver)
        pages.append(articles)
        write_csv(pages, MLB_FILE_NAME)
    
    # WSJ
    elif site_name == 'WSJ':
        pages = []
        for i in range(WSJ_PAGES):
            articles = scrape_wsj(WSJ_URL + str(i+1), driver)
            pages.append(articles)
        write_csv(pages, WSJ_FILE_NAME)
    
    # NY Times
    elif site_name == 'NYTimes':
        pages = []
        articles = scrape_nyt(NYT_URL, driver)
        pages.append(articles)
        write_csv(pages, NYT_FILE_NAME)
    
    # ESPN
    elif site_name == 'ESPN':
        pages = []
        articles = scrape_espn(ESPN_URL, driver)
        pages.append(articles)
        write_csv(pages, ESPN_FILE_NAME)

    driver.close()
    exit()
