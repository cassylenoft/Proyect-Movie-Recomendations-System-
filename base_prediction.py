import pickle, joblib, random
import numpy as np

base_model = joblib.load(open('chat/english_version/models/base_model.joblib','rb'))
base_encoder = pickle.load(open('chat/english_version/objects/base_encoder','rb'))
cv = pickle.load(open('chat/english_version/objects/base_vectorizer','rb'))

chatbot_responses = {
    'hello':
    [
    "Hello",
    "Hi",
    "Hey",
    "Hi there",
    "Hey there",
    "Greetings",
    "Howdy",
    "Yo",
    "Hiya",
    "Hello there",
    "Well hello",
    "Hiya",
    "Hey buddy",
    "Hi folk",
    "Hi everyone",
    "Hi friend",
    "What's up",
    "Hey ya",
    "Good to see you",
    "Nice to see you"
],
    'responses_to_thanks':
    [
    "You're welcome",
    "No problem",
    "No worries",
    "Don't mention it",
    "It was nothing",
    "My pleasure",
    "Anytime",
    "Sure thing",
    "You got it",
    "Glad to help",
    "Happy to help",
    "That's okay",
    "Not at all",
    "It's my pleasure",
    "I'm happy to assist",
    "It's no trouble at all",
    "I'm glad you liked it",
    "You're very welcome",
    "It's the least I could do",
    "Of course"
],
    'enjoy_messagges':
    [
    "Enjoy!",
    "Have fun!",
    "Have a great time!",
    "Enjoy yourself!",
    "Have a blast!",
    "Make the most of it!",
    "Hope you have a good one!",
    "Wishing you a great time!",
    "Hope it's a good one!",
    "Have a good one!",
    "Hope you enjoy it!",
    "Make it a great one!",
    "Hope you have a fantastic time!",
    "Enjoy every moment!",
    "Make the most of your day!",
    "Wishing you lots of fun!",
    "Have an awesome time!",
    "Hope you have a wonderful time!"
],
    'info_messages':
    ['mys functiosn are','here my funcs'],
    'recomendation_trigger':
    ['sure here you go button','clicl the botton below!']
}


def chatbot_response(user_text):
    show_button=False
    matrix = cv.transform([user_text]).toarray()
    pred = base_model.predict(matrix)
    
    pred_label = base_encoder.inverse_transform(pred)
    if pred_label == 'hello_trigger':
        message= random.choice(chatbot_responses['hello'])
        return message, show_button

    elif pred_label == 'info_trigger':
        message = random.choice(chatbot_responses['info_messages'])
        return message, show_button

    elif pred_label == 'recomm_trigger':
        show_button=True
        message = random.choice(chatbot_responses['recomendation_trigger']) + ' ' + random.choice(chatbot_responses['enjoy_messagges'])
        return message, show_button

    elif pred_label == 'thanks_trigger':
        message = random.choice(chatbot_responses['responses_to_thanks'])
        return message, show_button
    else:
        message = 'i did not undestand thtat'
        return message, show_button
    
# text = input('entrea tu mensaje')
# a = chatbot_response(text)
# print(a)

# if __name__ == " __main__":
#     text = input('entrea tu mensaje')
#     a = chatbot_response(text)
#     print(a)