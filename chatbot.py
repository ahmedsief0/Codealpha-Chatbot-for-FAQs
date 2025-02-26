import nltk
import string
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Sample FAQ dataset (questions and answers)
faq_data = {
    "What is your return policy?": "Our return policy allows returns within 30 days of purchase.",
    "How can I contact customer support?": "You can reach customer support via email at support@example.com.",
    "Where are your products made?": "Our products are made in the USA with locally sourced materials.",
    "Do you offer international shipping?": "Yes, we offer international shipping to select countries.",
    "What payment methods do you accept?": "We accept Visa, MasterCard, PayPal, and other major payment methods.",
    "How long does shipping take?": "Shipping usually takes between 5-7 business days for domestic orders and 10-14 business days for international orders.",
    "Can I track my order?": "Yes, you will receive a tracking number via email once your order has been shipped.",
    "Do you offer gift cards?": "Yes, we offer digital gift cards in various denominations. You can purchase them on our website.",
    "Can I cancel my order?": "Orders can only be canceled within 1 hour of placing them. Please contact customer support immediately if you wish to cancel your order.",
    "Do you offer any discounts or promotions?": "Yes, we have seasonal sales and offer occasional promo codes. Please subscribe to our newsletter for updates on discounts.",
    "What should I do if I receive a damaged product?": "Please contact customer support immediately with photos of the damaged product, and we will assist you with a replacement or refund.",
    "Do you have a loyalty program?": "Yes, we offer a loyalty program where you can earn points on purchases and redeem them for discounts on future orders.",
    "What is your privacy policy?": "We take your privacy seriously. Your personal information will never be shared with third parties without your consent. Please read our full privacy policy on our website.",
    "How do I change my password?": "To change your password, log in to your account and go to the 'Account Settings' page. From there, you can update your password.",
    "How do I unsubscribe from the newsletter?": "To unsubscribe, please click the 'unsubscribe' link at the bottom of any of our newsletter emails.",
    "What do I do if I forgot my account password?": "If you've forgotten your password, click 'Forgot Password' on the login page, and you'll receive an email with instructions to reset your password.",
    "Do you offer any bulk purchasing options?": "Yes, we offer bulk purchasing for businesses. Please contact customer support for more information on pricing and orders.",
    "Can I modify my order after placing it?": "Once an order is placed, it cannot be modified. Please make sure all details are correct before submitting your order.",
    "What is the warranty on your products?": "All of our products come with a 1-year warranty against manufacturing defects. Please refer to our warranty policy for more details.",
    "Are your products environmentally friendly?": "Yes, we are committed to sustainability and use eco-friendly materials whenever possible. Our packaging is also recyclable.",
    "Do you accept returns on sale items?": "Sale items are eligible for return within 14 days of purchase. Please review our return policy for more information on returns.",
    "thank you":"No worries i am here to help"
}

# Preprocess function to clean and tokenize the input
def preprocess(text):
    text = text.lower()
    text = "".join([char for char in text if char not in string.punctuation])
    tokens = nltk.word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    return " ".join(tokens)

# Prepare the FAQ questions and answers for processing
faq_questions = list(faq_data.keys())
faq_answers = list(faq_data.values())

# Preprocess all FAQ questions
processed_faq_questions = [preprocess(question) for question in faq_questions]

# Vectorizer for converting text to vector format (TF-IDF)
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(processed_faq_questions)

# Function to get the best matching FAQ answer
def get_faq_answer(user_input):
    user_input_processed = preprocess(user_input)
    user_input_vector = vectorizer.transform([user_input_processed])
    cosine_similarities = cosine_similarity(user_input_vector, tfidf_matrix)
    best_match_index = cosine_similarities.argmax()
    return faq_answers[best_match_index]
