import requests
from bs4 import BeautifulSoup
from textblob import TextBlob

import openai 
openai.api_key='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'

def generate_ideas(title):
    prompt = f"""I have a topic related to startups: '{title}'. What could be potential problems to solve related 
        to this topic?"""
    
    # Assuming you have set up OpenAI's GPT-4 as per their instructions and have it available as gpt4
    response = openai.Completion.create(engine="text-davinci-001", prompt=prompt, max_tokens=50)

    return response.choices[0].text.strip()

def get_titles(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/top/?t=week'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = soup.find_all('h3', {'class': '_eYtD2XCVieq6emjKBH3m'})
    return [title.text for title in titles]

def analyze_sentiment(title):
    blob = TextBlob(title)
    return blob.sentiment.polarity

subreddits = [
    'AskReddit', 'startups', 'Entrepreneur', 'business', 'venturecapital', 'smallbusiness', 'SideProject', 
    'technology', 'programming', 'webdev', 'javascript', 'python', 'EntrepreneurRideAlong', 
    'growmybusiness', 'startup_ideas', 'Lightbulb', 'InvestmentClub', 'stocks', 'investing', 
    'financialindependence', 'personalfinance', 'CryptoCurrency', 'Bitcoin', 'ethereum', 'ProductManagement', 
    'marketing', 'socialmedia', 'SEO', 'bigdata', 'machinelearning', 'datascience', 'artificial', 'Futurology', 
    'siliconvalley', 'hwstartups', 'indiebiz', 'roastmystartup', 'alphaandbetausers', 'codetogether', 'learnprogramming', 
    'AskProgramming', 'dotcom', 'CoFounder', 'Business_Ideas', 'AppBusiness', 'saas', 'artificial', 
    'MachineLearning', 'learnmachinelearning', 'deeplearning', 'LearnDeepLearning', 'datascience', 'learnpython', 'learnprogramming', 
    'LearnDataScience', 'OpenAI', 'chatbots', 'NLP', 'languagelearning', 'computervision', 'neuralnetworks', 'AI_Startups', 
    'ArtificialInteligence', 'AInews', 'ArtificialIntell', 'DeepIntoYouTube'
]

for subreddit in subreddits:
    print(f'Scraping r/{subreddit}...')
    titles = get_titles(subreddit)
    for title in titles:
        sentiment = analyze_sentiment(title)
        if sentiment < 0:
            print(f'Potential problem detected: "{title}" (sentiment: {sentiment})')
            print(f"Generating ideas for '{title}'...")
            ideas = generate_ideas(title)
            print(f"Ideas: {ideas}")
        else:
            print(f"Just a title {title}")