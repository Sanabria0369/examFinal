
import random
SPAM_WORDS = ["offer","win","free","money","click"]
PHISHING_WORDS = ["password","bank","verify","account","urgent"]
def analyze_email(text):
    t = text.lower()
    spam = [w for w in SPAM_WORDS if w in t]
    phish = [w for w in PHISHING_WORDS if w in t]
    if phish:
        return {"classification":"Phishing","confidence":round(random.uniform(80,95),2),"keywords":phish}
    elif spam:
        return {"classification":"Spam","confidence":round(random.uniform(70,90),2),"keywords":spam}
    else:
        return {"classification":"Ham (Legítimo)","confidence":round(random.uniform(85,98),2),"keywords":[]}
