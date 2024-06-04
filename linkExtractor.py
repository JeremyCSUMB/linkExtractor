import re
import pandas as pd
from canvasapi import Canvas
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

load_dotenv()

API_URL = os.getenv("CANVAS_API_URL")
API_KEY = os.getenv("CANVAS_API_KEY")

canvas = Canvas(API_URL, API_KEY)

def get_discussion_entries(course_id, discussion_topic_id):
    course = canvas.get_course(course_id)
    discussion_topic = course.get_discussion_topic(discussion_topic_id)
    entries = discussion_topic.get_topic_entries()
    return entries

def extract_linkedin_urls(message):
    soup = BeautifulSoup(message, 'html.parser')
    clean_message = soup.get_text()
    urls = re.findall(r'(https?://[^\s]+|www\.linkedin\.com[^\s]*)', clean_message)
    linkedin_urls = ['https://' + url if not url.startswith('http') else url for url in urls if 'linkedin.com' in url]
    return linkedin_urls

def get_user_email(user_id):
    user = canvas.get_user(user_id)
    return user.email

def download_discussion_posts_and_extract_linkedin_urls(course_id, discussion_topic_id):
    entries = get_discussion_entries(course_id, discussion_topic_id)
    data = []
    for entry in entries:
        linkedin_urls = extract_linkedin_urls(entry.message)
        email = get_user_email(entry.user_id)
        if linkedin_urls:
            data.append({
                "user_name": entry.user_name,
                "email": email,
                "linkedin_url": linkedin_urls[0]
            })
        try:
            replies = entry.get_replies()
            for reply in replies:
                linkedin_urls = extract_linkedin_urls(reply.message)
                email = get_user_email(reply.user_id)
                if linkedin_urls:
                    data.append({
                        "user_name": reply.user_name,
                        "email": email,
                        "linkedin_url": linkedin_urls[0]
                    })
        except AttributeError:
            pass
    df = pd.DataFrame(data)
    return df

course_id = 21 # Change this to your course id
discussion_topic_id = 440 # Change this to your discussion topic id

df = download_discussion_posts_and_extract_linkedin_urls(course_id, discussion_topic_id)
df.to_csv("linkedin_urls.csv", index=False)
