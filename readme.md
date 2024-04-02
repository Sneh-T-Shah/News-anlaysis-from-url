# Online Article Analysis

The Online Article Analysis project aims to analyze online articles retrieved from URLs. It performs various analyses on the article content to extract valuable insights such as readability metrics and sentiment analysis.

## Project Overview

### Components
1. **Web Scraping Module (`web_scrap.py`):**
   - This module contains the `WebScrap` class responsible for web scraping functionality. It utilizes the `goose3` library to extract text content from online articles by parsing the HTML of the article pages.
   - If the article is not in English, it uses the `googletrans` library to translate the article content to English before analysis.

2. **Text Analysis Module (`text_analysis.py`):**
   - The `TextAnalysis` class in this module performs various text analysis tasks on the extracted article content.
   - It calculates readability metrics such as average sentence length, percentage of complex words, and fog index to assess the readability of the article.
   - It conducts sentiment analysis by determining the polarity and subjectivity scores of the article content based on the presence of positive and negative words.

3. **Streamlit UI (`app.py`):**
   - The Streamlit application provides a user-friendly interface for users to input the URL of the article they want to analyze.
   - Upon entering the URL and clicking the "Analyze" button, the application retrieves the article content, performs text analysis using the `TextAnalysis` class, and displays the analysis results on the UI.
   - Analysis results include the title and text of the article, along with various metrics such as word count, average sentence length, percentage of complex words, sentiment scores, etc.

### Outputs
The project provides the following outputs from the analyzed article:
- **Title:** Title of the article.
- **Text:** Full text content of the article.
- **Analysis Results:** Various metrics and insights derived from the text analysis, including:
  - Word Count
  - Average Sentence Length
  - Percentage of Complex Words
  - Fog Index (Readability Metric)
  - Positive Score (Sentiment Analysis)
  - Negative Score (Sentiment Analysis)
  - Polarity Score (Sentiment Analysis)
  - Subjectivity Score (Sentiment Analysis)
  - Average Syllable Count Per Word
  - Complex Word Count
  - Personal Pronoun Count
  - Average Word Length

## Usage
Users can simply run the Streamlit application, input the URL of the article they want to analyze, and click the "Analyze" button to obtain detailed insights into the article's content and readability.

## Contribution
Contributions to the project are welcome! Users can submit issues or pull requests for any suggestions, improvements, or additional features they may have.