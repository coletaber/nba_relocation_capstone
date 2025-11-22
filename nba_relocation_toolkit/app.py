import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Dashboard",
    page_icon="🏀",
    layout="wide"
)

# custom CSS for theming
st.markdown("""
    <style>
    .main {
        background-color: #000000;
        color: #ffffff;
    }
    .css-1d391kg {  /* Sidebar background */
        background-color: #111111 !important;
    }
    .css-1v3fvcr {  /* Header title */
        color: #FFD700 !important;  /* gold */
    }
    .stButton>button {
        background-color: #FFD700;
        color: black;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>NBA Relocation Toolkit Dashboard!</h1>", unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center;'>Upload your survey CSV and explore key insights from fans</h3>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("### Raw Data Preview", df.head())

    # Allow user to select important columns dynamically
    st.sidebar.header("Column mappings (select columns for each section)")

    interest_col = st.sidebar.selectbox("Fan Interest Column", df.columns)
    ticket_col   = st.sidebar.selectbox("Ticket Price Column", df.columns)
    legacy_col   = st.sidebar.selectbox("Historical identity preference column", df.columns)
    concerns_col = st.sidebar.selectbox("Concerns column", df.columns)
    engagement_col = st.sidebar.selectbox("Fan engagement channel column", df.columns)
    community_col  = st.sidebar.selectbox("Community outreach importance column", df.columns)

    # 1. Fan Interest Chart
    st.write("## Fan Interest Levels")
    interest_counts = df[interest_col].value_counts().reset_index()
    interest_counts.columns = ["Interest", "Count"]
    fig1 = px.bar(interest_counts, x="Interest", y="Count", color="Interest",
                  title="How interested are fans in the new team?")
    st.plotly_chart(fig1)

    # 2. Ticket Price Sensitivity
    st.write("## Ticket Price Willingness")
    price_counts = df[ticket_col].value_counts().reset_index()
    price_counts.columns = ["Ticket Price Tier", "Count"]
    fig2 = px.bar(price_counts, x="Ticket Price Tier", y="Count",
                  title="Willingness to Pay for Lower‑Bowl Tickets")
    st.plotly_chart(fig2)

    # 3. Historical Identity Preference
    st.write("## Legacy vs. Fresh Start")
    legacy_counts = df[legacy_col].value_counts().reset_index()
    legacy_counts.columns = ["Preference", "Count"]
    fig4 = px.pie(legacy_counts, names="Preference", values="Count",
                  title="Would fans prefer honoring relocated franchise history?")
    st.plotly_chart(fig4)

    # 4. Fan Engagement Channels
    st.write("## Preferred Fan Engagement Channels")
    engagement_counts = df[engagement_col].value_counts().reset_index()
    engagement_counts.columns = ["Engagement Channel", "Count"]
    fig5 = px.bar(engagement_counts, x="Engagement Channel", y="Count",
                  title="Which digital/physical channels engage fans most?")
    st.plotly_chart(fig5)

    # 5. Community Outreach Importance
    st.write("## Importance of Community Outreach")
    community_counts = df[community_col].value_counts().reset_index()
    community_counts.columns = ["Importance Level", "Count"]
    fig6 = px.bar(community_counts, x="Importance Level", y="Count",
                  title="How important is community involvement to fans?")
    st.plotly_chart(fig6)

    # 6. Word Cloud: Fan Concerns
    st.write("## Word Cloud of Fan Concerns")
    all_concerns = " ".join(df[concerns_col].astype(str).tolist())
    stopwords = set(STOPWORDS)
    wordcloud = WordCloud(width=800, height=400,
                          background_color="orange",
                          stopwords=stopwords).generate(all_concerns)
    fig_wc, ax_wc = plt.subplots(figsize=(10, 5))
    ax_wc.imshow(wordcloud, interpolation="bilinear")
    ax_wc.axis("off")
    st.pyplot(fig_wc)

    st.write("### Data Summary")
    st.write(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
    st.write("Uploaded successfully! Use sidebar to map fields and explore.")

else:
    st.info("Upload a CSV file to begin.")
