import streamlit as st
import pandas as pd
from web_scrap import WebScrap
from text_analysis import TextAnalysis

# Initialize objects
web_scrapper = WebScrap()
analysis = TextAnalysis()

def perform_analysis(url):
    try:
        text, title = web_scrapper.get_text(url)
        text = title + "\n" + text
        
        # Perform text analysis
        analysis.get_preprocess(text)
        
        # Display analysis results
        st.write("**Title**:", title)
        st.write("**Text**:", text)
        st.write("**Analysis Results**:")
        st.write("Word Count:", analysis.word_count)
        st.write("Average Sentence Length:", analysis.average_sentence_length)
        st.write("Percentage of Complex Words:", analysis.percentage_complex_words)
        st.write("Complex Word Count:", analysis.complex_word_count)
        st.write("Fog Index:", analysis.fog_index)
        st.write("Positive Score:", analysis.positive_score)
        st.write("Negative Score:", analysis.negative_score)
        st.write("Polarity Score:", analysis.polarity_score)
        st.write("Subjectivity Score:", analysis.subjectivity_score)
        st.write("Average Syllable Count Per Word:", analysis.syllable_count_per_word)
        st.write("Personal Pronoun Count:", analysis.personal_pronoun_count)
        st.write("Average Word Length:", analysis.average_word_length)


    except Exception as e:
        st.error(f"Error processing URL: {url}")
        st.error(str(e))


def main():
    st.title("Online Article Analysis")

    url = st.text_input("Enter the URL of the article:")
    if st.button("Analyze"):
        if url:
            perform_analysis(url)
        else:
            st.warning("Please enter a valid URL.")

if __name__ == "__main__":
    main()
