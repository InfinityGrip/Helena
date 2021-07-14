import requests, uuid, json
# eassy manipulations of different microsoft translation libraries in one single file

#this function will take in five imputs, the sentence to translate, the language it is in, the language you want to translate to,
#wherether or not you want to translate the sentence or simply want to know which language it is in,
# and the length of the sentence if no imput is inserted, it will default to translate hello world in french and swahili.
def translate(text, fraum = None, to = ['fr', 'sw'], transl = True, sentlength = True):
    subscription_key = "ca8f62306f7d4bd7afd3b0c0fe22c043" # use own api key
    endpoint = "https://api.cognitive.microsofttranslator.com/"#use personalized endpoint

    location = "eastus"
    if fraum != None  and transl:

        constructed_url = endpoint + "translate"

        params = {
            'api-version': '3.0',
            'from': fraum,
            'to': to,  # running conversion in French and swahili
            'includeSentenceLength': sentlength
        }
    #elif fraum != None and transl != True:


    elif fraum != None and transl == True:
        constructed_url = endpoint + "translate"
        params = {
            'api-version': '3.0',
            'to': to,  # running conversion in French and swahili
            'includeSentenceLength': sentlength
        }

    elif fraum != None and transl != True:
        print("helor")
        constructed_url = endpoint + "detect"
        params = {
            'api-version': '3.0'
            #'includeSentenceLength': sentlength

        }
        print("I am done")



    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
        }

    body = [{
        'text': text
    }]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()
    return json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': '))


## we can make this fun by adding imputs commands for user interface
translate_TXT = str(input("Enter word/sentence to translate:\n"))
language_TXT_from = str(input("What language is it? *use code of language(e.g: 'en' is english, 'fr' is french)\n"))
language_TXT_to = input("What language to translate to?\n") # use a list if you want to translate to more than one language: ['fr', 'sw']
translate_ToF = bool(input("Do you want to translate? True or False:\n"))
sentence_len = bool(input("Sentence length? True or False\n"))
print(translate(translate_TXT, language_TXT_from, language_TXT_to, translate_ToF, sentence_len))
#print(translate('mambo', 'sw', 'en', True, True))