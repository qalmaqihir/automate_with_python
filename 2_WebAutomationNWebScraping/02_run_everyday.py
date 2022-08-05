"""
We have to install chrome driver for our version of chrome,
then install seleninum
----------------------
a driver will help us to interact with the website using the selenium
"""

"""
To run everday, we need to make the .py file to an executable

"""
# creating_the_driver

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# for headless mode
from selenium.webdriver.Chrome.Options import Options
# To run everyday
from datatime import datetime
import os
import sys

#Get the path to the executable
application_path=os.path.dirname(sys.executable)
# Using the datetime to format/customize our file name
now = datetime.now()
#Format MMDDYY goto strftime.org to find a format you want
moth_day_year=now.strftime("%m%d%y")

# Lets define the website and the path that we are using
website = ""  # paste the link you want to scrap
path = ""  # the path to our chrome driver, we install above

#Headless mode
options=Options()

options.headless=True

## To define the driver
# driver = webdriver.Chrome()
# lets define the driver, for selenium 4 we need smth more, thats creating a service
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service,options=options) # For headless mode we added options defiened above
driver.get(website)
# The browser will be opend


"""
Inspect the website you want...
select the element and creat a xpath to go to that element
=> Check out the basics of finding the xpath
=> you can just right click and copyt the element path
"""

# only one element
# driver.find_element(By="xpath",value='') # Mostly we used By=xpath, but other can also be used like id, class etc
# for getting all the elements
contaniners = driver.find_elements(by="xpath", value='')
# containers will be a list as we used .find_elements()

titles = []
subtitles = []
links = []

for container in contaniners:
    title = contaniners.find_element(by='xpath', value='./a/h2').text  # . is used to refere to the parent xpath
    sub_title = contaniners.find_element(by='xpath', value='./a/p').text
    # after having the container we can get to it using xpath, be it a list, image, link or anything
    link = contaniners.find_element(by='xpath', value='./a').get_attribute('href')
    titles.append(title)
    subtitles.append(sub_title)
    links.append(link)

# Check if we got the staff we wented
print(titles)
print(links)
print(links)
my_dic = {'titles': titles, 'subtitles': subtitles, 'links': links}

# to create the dataframe
import pandas as pd

df_scrape = pd.DataFrame(data=my_dic)
file_name=""
final_path=os.path.join(application_path,file_name)
df_scrape.to_csv(final_path)
#df_scrape.to_csv(f'{application_path}name_{moth_day_year}.csv',) # to avoid the confict of / btw os we use join method

# End the session
driver.quit()

# TODO:
"""

To make it executable, install 
pip install pyinstaller

then go to the terminal at the same location as this file
pyinstaller --onefile nameoffile.py 
"""

#TODO:
"""
Schedule python script with crontab

"""




























