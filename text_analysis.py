# importing necessary libraries
import re
import syllapy
from nltk.corpus import stopwords

# nltk.download('stopwords')

# Class to perform text analysis
class TextAnalysis:


    def __init__(self):
        with open('positive-words.txt', 'r') as file:
            self.positive_words = [word.strip() for word in file.readlines()]
        with open('negative-words.txt', 'r') as file:
            self.negative_words = [word.strip() for word in file.readlines()]

    def get_preprocess(self, text):
        self.text = text
        self.remove_meta_tags()
        self.readability_report = self.calculate_readability()
        self.average_sentence_length = self.readability_report["Average Sentence Length"]
        self.percentage_complex_words = self.readability_report["Percentage of Complex Words"]
        self.complex_word_count = self.readability_report["Complex Word Count"]
        self.fog_index = self.readability_report["Fog Index"]
        self.syllable_count_per_word = self.calculate_syllable_count_per_word()
        self.personal_pronoun_count = self.calculate_personal_pronouns()
        self.average_word_length = self.calucluate_average_word_length()
        self.text = self.remove_stopwords()
        self.sentiment_report = self.sentiment_score()
        self.positive_score = self.sentiment_report["positive_score"]
        self.negative_score = self.sentiment_report["negative_score"]
        self.polarity_score = self.sentiment_report["polarity_score"]
        self.subjectivity_score = self.sentiment_report["subjectivity_score"]
        self.word_count = len(self.text.split())

    # Function to remove meta tags
    def remove_meta_tags(self):
        meta_tags_pattern = r'[\n\t\r]'
        self.text = re.sub(meta_tags_pattern, ' ', self.text)

    # Function to remove stopwords
    def remove_stopwords(self):
        pattern = r'[^a-zA-Z0-9\s]'
        self.text = re.sub(pattern, ' ', self.text)
        stop_words = set(stopwords.words('english'))
        words = self.text.split()
        words = [word for word in words if word.lower() not in stop_words]
        return ' '.join(words)


    # Function to calculate sentiment score
    def sentiment_score(self):
        words = self.text.split()
        total_words = len(words)
        positive_count = sum([1 for word in words if word in self.positive_words])
        negative_count = sum([1 for word in words if word in self.negative_words])
        polarity_score = (positive_count - negative_count) / (positive_count + negative_count + 0.000001)
        subjectivity_score = (positive_count + negative_count) / (total_words + 0.000001)
        return {
            'positive_score': positive_count,
            'negative_score': negative_count,
            'polarity_score': polarity_score,
            'subjectivity_score': subjectivity_score
        }
    
    
    # Function to count syllables
    def count_syllables(self,word):
            return syllapy.count(word)


    # Function to check if a word is complex
    def is_complex(self,word):
        return self.count_syllables(word) > 2


    # Function to calculate readability
    def calculate_readability(self):
        sentences = re.split(r'[.!?]', self.text)
        num_sentences = len(sentences)

        words = [word for sentence in sentences for word in sentence.split()]
        num_words = len(words)

        average_sentence_length = num_words / num_sentences
        num_complex_words = sum(1 for word in words if self.is_complex(word))
        percentage_complex_words = (num_complex_words / num_words) * 100
        fog_index = 0.4 * (average_sentence_length + percentage_complex_words)

        return {
            "Average Sentence Length": average_sentence_length,
            "Percentage of Complex Words": percentage_complex_words,
            "Complex Word Count": num_complex_words,
            "Fog Index": fog_index
        }


    # Function to calculate personal pronouns
    def calculate_syllable_count_per_word(self):
        words = self.text.split()
        syllable_counts = []
        for word in words:
            if word.endswith(("es", "ed")):
                syllable_counts.append(self.count_syllables(word[:-2]))
            else:
                syllable_counts.append(self.count_syllables(word))
        return syllable_counts


    # Function to calculate personal pronouns
    def calculate_personal_pronouns(self):
        pattern = r'\b(i|me|my|mine|myself|you|your|yours|yourself|he|him|his|himself|she|her|hers|herself|it|its|itself|we|us|our|ours|ourselves|you|your|yours|yourself|yourselves|they|them|their|theirs|themselves)\b'
        pronouns = re.findall(pattern, self.text)
        return len(pronouns)


    # Function to calculate average word length
    def calculate_syllable_count_per_word(self):
        words = self.text.split()
        syllable_counts = []
        for word in words:
            if word.endswith(("es", "ed")):
                syllable_counts.append(self.count_syllables(word[:-2]))
            else:
                syllable_counts.append(self.count_syllables(word))
        return sum(syllable_counts) / len(syllable_counts)
    

    # Function to calculate average word length
    def calucluate_average_word_length(self):
        words = ''.join(char if char.isalnum() or char.isspace() else ' ' for char in self.text)
        words = words.split()
        return sum(len(word) for word in words) / len(words)