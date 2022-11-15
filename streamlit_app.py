import snowflake.connector
import streamlit
#import pandas
import requests
from urllib.error import URLError

streamlit.stop()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("fruit_load_list")
streamlit.dataframe(my_data_rows)

my_cur.execute("insert into fruit_load_list values ('from streamlit')")
