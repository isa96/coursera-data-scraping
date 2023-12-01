# Scraping Coursera Courses

## APP OVERVIEW

![image](https://github.com/lixx21/coursera-data-scarping/assets/91602612/bf83e562-4193-460c-b821-6824825952ad)

## TECH STACK

1. [Scrapy](https://docs.scrapy.org/en/latest/topics/exporters.html)
2. [Streamlit](https://docs.streamlit.io/)
3. [Pandas](https://pandas.pydata.org/docs/)

## RUN CRAWLING

1. Clone this repository ```https://github.com/lixx21/coursera-data-scarping.git```
2. Go to spiders directory path with ```cd coursera_data_scraping/coursera_data_scraping/spiders```
3. Start running streamlit app with following command ```streamlit run streamlit_app.py```

## NOTES

1. In this case, we need to install all libraries in ```requirements.txt```
2. Start Scrapy project with this command ```scrapy startproject {folder name}``` in this case, I used folder name = coursera_data_scraping so the comman will be like this ```scrapy startproject coursera_data_scraping``` 
3. Because Scraping in Coursera will return this error ```DEBUG: Forbidden by robots.txt:``` Therefore, in ```settings.py``` we set ```ROBOTSTXT_OBEY = False```
4. We also need to define our ```USER_AGENT``` in ```settings.py```
5. Because we want to store (append) data in csv, we need to create a csv first named ```output.csv``` in ```coursera_data_scraping/coursera_data_scraping/spiders``` directory and filled the header and keep the rest empty. **Just filled the header**
