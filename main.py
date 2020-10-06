import streamlit as st
import pandas as pd
import json
import requests
import nltk
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import main_functions
from pprint import pprint

from wordcloud import WordCloud
import matplotlib.pyplot as plt
import plotly.express as px

# nltk.download("punkt")
# nltk.download("stopwords")

api_key_dict = main_functions.read_from_file("JSON_Files/api_key.json")

api_key = api_key_dict["my_key"]

partial_url = "https://api.nytimes.com/svc/topstories/v2/"

# uncomment later
# url = "https://api.nytimes.com/svc/topstories/v2/world.json?api-key=" + api_key

# response = requests.get(url).json()

# main_functions.save_to_file(response, "JSON_Files/response.json")
# uncomment later

my_articles = main_functions.read_from_file("JSON_Files/response.json")

# print(type(my_articles))

# pprint(my_articles)

str1 = ""

for i in my_articles["results"]:
    str1 = str1 + i["abstract"]

# print(str1)

sentences = sent_tokenize(str1)

# print(len(sentences))

# print(sentences)

words = word_tokenize(str1)

# print(len(words))

# print(words)

fdist = FreqDist(words)

# pprint(fdist.most_common(10))

words_no_punc = []

for w in words:
    if w.isalpha():
        words_no_punc.append(w.lower())

# print(words_no_punc)

fdist2 = FreqDist(words_no_punc)

# pprint(fdist2.most_common(10))

stopwords = stopwords.words("english")

# print(stopwords)

clean_words = []

for w in words_no_punc:
    if w not in stopwords:
        clean_words.append(w)

# print(len(clean_words))

fdist3 = FreqDist(clean_words)

# pprint(fdist3.most_common(10))

wordcloud = WordCloud().generate(str1)

# testing code
wordcloud_two = WordCloud().generate(str1)

most_common = pd.DataFrame(fdist3.most_common(10))
df = pd.DataFrame({"words": most_common[0], "count": most_common[1]})
fig = px.line(df, x="words", y="count", title='')
# testing code stops here

plt.figure(figsize=(12, 12))
# plt.imshow(wordcloud) # uncomment later

plt.axis("off")
plt.show()

st.title("COP 4813 - Web Application Programming")

st.header("Project 1")

st.subheader("Part A - The Stories API")

st.write("This app uses the Top Stories API to display the most common words used in the top current articles "
         "based on a specified topic selected by the user. The data is displayed as a line chart and as a line "
         "and as a wordcloud image.")

st.write("I - Topic Selection")

user_name = st.text_input("Please enter your name")

options = st.selectbox("Select a topic of your interest",
                       ["", "Arts", "Automobiles", "Books", "Business", "Fashion", "Food",
                        "Health", "Home", "Insider", "Magazine", "Movies", "NY Region",
                        "Obituaries", "Opinion", "Politics", "Real Estate", "Science", "Sports",
                        "Sunday Review", "Technology", "Theater", "T-Magazine", "Travel", "Upshot", "US", "World"])

if user_name and options:
    st.write("Hi " + user_name + ", you selected {} as your topic of interest.".format(options))


def partA():
    response2 = requests.get(new_url).json()
    main_functions.save_to_file(response2, "JSON_Files/response.json")
    if user_name and options:
        st.subheader("II - Frequency Distribution")
        agree = st.checkbox("Click here to generate the frequency distribution")
        if agree:
            st.plotly_chart(fig)
        st.subheader("III - Wordcloud")
        agree = st.checkbox("Click here to generate wordcloud")
        if agree:
            st.image(wordcloud.to_array())
            st.write("Wordcloud generated for " + options + " topic")


if options == "Arts":
    new_url = partial_url + "arts.json?api-key=" + api_key
    partA()
elif options == "Automobiles":
    new_url = partial_url + "automobiles.json?api-key=" + api_key
    partA()
elif options == "Books":
    new_url = partial_url + "books.json?api-key=" + api_key
    partA()
elif options == "Business":
    new_url = partial_url + "business.json?api-key=" + api_key
    partA()
elif options == "Fashion":
    new_url = partial_url + "fashion.json?api-key=" + api_key
    partA()
elif options == "Food":
    new_url = partial_url + "food.json?api-key=" + api_key
    partA()
elif options == "Health":
    new_url = partial_url + "health.json?api-key=" + api_key
    partA()
elif options == "Home":
    new_url = partial_url + "home.json?api-key=" + api_key
    partA()
elif options == "Insider":
    new_url = partial_url + "insider.json?api-key=" + api_key
    partA()
elif options == "Magazine":
    new_url = partial_url + "magazine.json?api-key=" + api_key
    partA()
elif options == "Movies":
    new_url = partial_url + "movies.json?api-key=" + api_key
    partA()
elif options == "National":
    new_url = partial_url + "national.json?api-key=" + api_key
    partA()
elif options == "NY Region":
    new_url = partial_url + "nyregion.json?api-key=" + api_key
    partA()
elif options == "Obituaries":
    new_url = partial_url + "obituaries.json?api-key=" + api_key
    partA()
elif options == "Opinion":
    new_url = partial_url + "opinion.json?api-key=" + api_key
    partA()
elif options == "Politics":
    new_url = partial_url + "politics.json?api-key=" + api_key
    partA()
elif options == "Real Estate":
    new_url = partial_url + "realestate.json?api-key=" + api_key
    partA()
elif options == "Science":
    new_url = partial_url + "science.json?api-key=" + api_key
    partA()
elif options == "Sports":
    new_url = partial_url + "sports.json?api-key=" + api_key
    partA()
elif options == "Sunday Review":
    new_url = partial_url + "sundayreview.json?api-key=" + api_key
    partA()
elif options == "Technology":
    new_url = partial_url + "technology.json?api-key=" + api_key
    partA()
elif options == "Theater":
    new_url = partial_url + "theater.json?api-key=" + api_key
    partA()
elif options == "T-Magazine":
    new_url = partial_url + "tmagazine.json?api-key=" + api_key
    partA()
elif options == "Travel":
    new_url = partial_url + "travel.json?api-key=" + api_key
    partA()
elif options == "Upshot":
    new_url = partial_url + "upshot.json?api-key=" + api_key
    partA()
elif options == "US":
    new_url = partial_url + "us.json?api-key=" + api_key
    partA()
elif options == "World":
    new_url = partial_url + "world.json?api-key=" + api_key
    partA()

st.subheader("Part B - Most Popular Articles")

st.write("Select if you want to see the most shared, emailed or viewed articles.")
options2 = st.selectbox("Select your preferred set of articles",
                        ["", "Shared", "Emailed", "Viewed"])

options3 = st.selectbox("Select the period of time (last days)",
                        ["", "1", "7", "30"])

base_url = "https://api.nytimes.com/svc/mostpopular/v2/"


def partB():
    response = requests.get(com_shared_url).json()
    main_functions.save_to_file(response, "JSON_Files/response_two.json")
    st.image(wordcloud_two.to_array())


if options2 == "Shared" and options3 == "1":
    com_shared_url = base_url + "shared/" + "1.json?api-key=" + api_key
    partB()
elif options2 == "Shared" and options3 == "7":
    com_shared_url = base_url + "shared/" + "7.json?api-key=" + api_key
    partB()
elif options2 == "Shared" and options3 == "30":
    com_shared_url = base_url + "shared/" + "30.json?api-key=" + api_key
    partB()

if options2 == "Emailed" and options3 == "1":
    com_shared_url = base_url + "emailed/" + "1.json?api-key=" + api_key
    partB()
elif options2 == "Emailed" and options3 == "7":
    com_shared_url = base_url + "emailed/" + "7.json?api-key=" + api_key
    partB()
elif options2 == "Emailed" and options3 == "30":
    com_shared_url = base_url + "emailed/" + "30.json?api-key=" + api_key
    partB()

if options2 == "Viewed" and options3 == "1":
    com_shared_url = base_url + "viewed/" + "1.json?api-key=" + api_key
    partB()
elif options2 == "Viewed" and options3 == "7":
    com_shared_url = base_url + "viewed/" + "7.json?api-key=" + api_key
    partB()
elif options2 == "Viewed" and options3 == "30":
    com_shared_url = base_url + "viewed/" + "30.json?api-key=" + api_key
    partB()
