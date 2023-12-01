import streamlit as st
import pandas as pd
from subprocess import call

def start_scrapping(course, page):
    #run scrapping spyder using subprocess
    
    call(["scrapy", "crawl", "coursera_data", "-a", f"course='{course}'", "-a" f"page={page}"])
    
    return "success"

def download_file(dataframe):
    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')

    csv = convert_df(dataframe)

    return csv

def clear_data(df):
    #columns = ['course_title','course_by','course_link','skills_you_gain','course_ratings','course_reviews','course_level']
    empty_df = df.iloc[0:0]
    empty_df.to_csv("output.csv", index=False)
    
    return empty_df

st.title('Coursera Data Scraping')
st.caption('This app will scraping courses data from coursera')

with st.form(key = 'user_info'):
    course = st.text_input('What course you want to scrap ? (i.e. data engineer)')
    page = st.number_input('How many page you want to scrap ?', 1, 100)
    
    submit_form = st.form_submit_button(label="Submit", help="Click to start scraping")
    if submit_form:
        start_scrapping(course, page)

df = pd.read_csv("output.csv")

colmn1, colmn2 = st.columns([1,1])
with colmn1:
    clear_button = st.button('Clear Data', type="primary")
        
with colmn2:    
    csv = download_file(df)
    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='output.csv',
        mime='text/csv',
        type="secondary"
    )

if clear_button:
    df = clear_data(df)
    # st.experimental_rerun() # will refresh the
    st.dataframe(df)
else:
    st.dataframe(df)



# if st.button('Clear Data'):
#     df = clear_data(df)

