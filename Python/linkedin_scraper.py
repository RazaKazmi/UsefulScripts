#This is a modified script originally based off of a web scraping script by Viola Mao
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd
from icecream import ic

#ideally, we want to pass the specific url for the job when the user enters the title and location on our website

#test linkedin job url
url = "https://www.linkedin.com/jobs/search?keywords=Data%20Scientist&location=Toronto%2C%20Ontario%2C%20Canada&geoId=100025096&trk=public_jobs_jobs-search-bar_search-submit&redirect=false&position=1&pageNum=0"

#Chrome driver setup
wd = webdriver.Chrome(executable_path='./chromedriver.exe')
wd.get(url)

#Some results can be in the format {1,000+} so we have to strip the characters and cast the data to int
num_of_jobs_string = wd.find_element_by_css_selector('h1>span').get_attribute('innerText')
num_of_jobs_string = num_of_jobs_string.strip("+")
num_of_jobs_string = num_of_jobs_string.replace(",","")

num_of_jobs = int(num_of_jobs_string)
#num_of_jobs = int(d.find_element_by_class_name('results-content-header__job-count').get_attribute('innterText'))

#The linkedin page loads jobs as you scroll down, however once you reach the bottom, it prompts
# a "see more jobs" button to continue viewing jobs.
#Linked jobs are loaded and displayed in sets of 25. The first 2 sets are loaded with the page, so we will start our index at 2.
jobs_per_page = 25
i = 2
time_delay = 5
#num_of_jobs/jobs_per_page
test_interval = 2
while i <=  test_interval:
    wd.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    i +=1
    try:
        wd.find_element_by_class_name('infinite-scroller__show-more-button--visible').click()
        time.sleep(time_delay)
    except NoSuchElementException:
        time.sleep(time_delay)
        pass

#Now that the page is loaded with our jobs, we can get the job listings
job_lists = wd.find_element_by_class_name('jobs-search__results-list')
jobs = job_lists.find_elements_by_tag_name('li') #list of all our jobs

ic(len(jobs))

#Job data
#job_ids = []
job_titles = []
#job_applicants = []
company_names = []
locations = []
dates = []
job_links = []

#Find the exact data we want and put it in our lists
for job in jobs:
    #id = job.get_attribute('data-id')
    #job_ids.append(id)

    title = job.find_element_by_css_selector('h3').get_attribute('innerText')
    job_titles.append(title)

    company = job.find_element_by_css_selector('h4').get_attribute('innerText')
    company_names.append(company)

    location = job.find_element_by_class_name('job-search-card__location').get_attribute('innerText')
    locations.append(location)

    date = job.find_element_by_css_selector('div>div>time').get_attribute('datetime')
    dates.append(date)

    link = job.find_element_by_css_selector('a').get_attribute('href')
    job_links.append(link)

#ic(company_names)

job_applicants = []
for item in range(len(jobs)):
    job_click_path = f'/html/body/div/div/main/section[2]/ul/li[{item+1}]'
    job_click = job.find_element_by_xpath(job_click_path).click()
    time.sleep(time_delay)

    applicant_class_name = "num-applicants__caption"
    applicant = wd.find_element_by_class_name(applicant_class_name).get_attribute('innerText')
    job_applicants.append(applicant)
ic(job_applicants)
