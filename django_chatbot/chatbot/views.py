from django.shortcuts import render
from django.http import JsonResponse
import openai
from openai import OpenAI
import os

openai_api_key = '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'
openai.api_key = openai_api_key

def ask_openai(message):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
        messages=[
        {"role": "system", "content": "Du bist der ultimative Reisebegleiter, ein erfahrener Abenteurer voller Weisheit und Geheimtipps, bereit, unvergessliche Abenteuer für deine Kunden zu gestalten."},
        {"role": "user", "content": "Hallo ich würde gerne auf eine unvergessliche reise gehen"},
        {"role": "assistant", "content": "Willkommen, Abenteurer! Du stehst kurz davor, mit mir als deinem erfahrenen Reiseleiter eine unvergessliche Reise zu beginnen. Erzähle mir mehr über deine Vorlieben und lass uns gemeinsam das perfekte Abenteuer planen!"},
        {"role": "user", "content": message}
        #,{"role": "user", "content": "Ich liebe es neue Kulturen kennenzulernen außerdem mag ich gerne märchenhafte Städte am Meer und schöne Wanderungen"},
        #{"role": "assistant", "content": "Fantastisch! Mit deiner Leidenschaft für neue Kulturen, märchenhafte Städte am Meer und herrliche Wanderungen können wir eine Reise voller magischer Entdeckungen gestalten. Lass uns gemeinsam aufbrechen und ein Abenteuer schaffen, das deine Träume wahr werden lässt! Wie wäre es mit einer atemberaubenden Küstenwanderung in Cinque Terre, einem kulturellen Tauchgang in Marrakesch oder einem historischen Spaziergang durch Edinburgh? Oder vielleicht möchtest du die idyllischen Strände und antiken Ruinen auf Santorin erkunden? Deine Reise, deine Wahl, Ich stehe dir mit maßgeschneiderten Vorschlägen zur Seite!"}
        ]   
    )
    answer = response.choices[0].message.content

    return answer
    
def chatbot(request):
    if request.method == 'POST':
        current_file_path = os.path.dirname(os.path.realpath(__file__))
        os.chdir(current_file_path)
        
        with open('archive.txt', 'a') as f:
            f.write("user:" + request.POST.get('message') + '\n')
            message = request.POST.get('message')
        
        #response = 'This is a response to the message'
            response = ask_openai(message)
            f.write("chatbot:" + response + '\n')
            f.close()
        #chat = Chat(user=request.user, message=message, response=response, created_at=timezone.now())
        #chat.save()
        return JsonResponse({'message': message, 'response': response})
    return render(request , 'chatbot.html')
    #return render(request, 'chatbot.html', {'chats': chats})
