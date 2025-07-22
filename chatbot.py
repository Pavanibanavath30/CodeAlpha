import pandas as pd
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords

class FAQChatBot:
    def __init__(self, faq_path):
        self.faq_data = pd.read_csv(faq_path)
        self.stop_words = set(stopwords.words('english'))
        self.vectorizer = TfidfVectorizer(tokenizer=self.tokenize, token_pattern=None, stop_words='english')

        self.faq_vectors = self.vectorizer.fit_transform(self.faq_data['Question'])

    def tokenize(self, text):
       tokens = text.lower().split()
       return [word for word in tokens if word.isalpha() and word not in self.stop_words]

    def get_response(self, user_input):
        user_vector = self.vectorizer.transform([user_input])
        similarity = cosine_similarity(user_vector, self.faq_vectors)
        index = similarity.argmax()
        score = similarity[0, index]

        if score < 0.2:
            return "I'm sorry, I don't have an answer for that."
        return self.faq_data.iloc[index]['Answer']

if __name__ == "__main__":
    bot = FAQChatBot('C:\\Users\\Banavath Pavani\\OneDrive\\Desktop\\FAQChatBot_Project\\data\\faqs.csv')   # ✅ Correct the path to your faqs.csv

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        print("Bot:", bot.get_response(user_input))
