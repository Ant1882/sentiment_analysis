import glob
import streamlit as st
import plotly.express as px

from nltk.sentiment import SentimentIntensityAnalyzer

# Get a list of filepaths
filepaths = sorted(glob.glob("diary/*.txt"))

# Instatiate sentiment intensity analyzer class
analyzer = SentimentIntensityAnalyzer()

# Get positivity & negativity coefficients for each entry
negativity = []
positivity = []
for filepath in filepaths:
    with open(filepath) as file:
        content = file.read()
    scores = analyzer.polarity_scores(content)
    positivity.append(scores["pos"])
    negativity.append(scores["neg"])

# Get dates from file names
dates = [name.strip(".txt").strip("diary/") for name in filepaths]

# Streamlit app
st.title("Diary tone")
# Chart positivity
st.subheader("Positivity")
pos_figure = px.line(x=dates, y=positivity,
                     labels={"x": "Date", "y": "Positivity"})
st.plotly_chart(pos_figure)
# Chart negativity
st.subheader("Positivity")
neg_figure = px.line(x=dates, y=negativity,
                     labels={"x": "Date", "y": "Negativity"})
st.plotly_chart(neg_figure)

