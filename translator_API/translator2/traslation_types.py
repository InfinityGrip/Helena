import requests, uuid, json
# eassy manipulations of different microsoft translation libraries in one single file

def translate(text):
    subscription_key = "" # use own api key
    endpoint = ""#use personalized endpoint

    location = "eastus"

    constructed_url = endpoint + "translate"

    params = {
        'api-version': '3.0',
        # 'from': 'en',
        'to': ['fr', 'sw']  # running conversion in French and swahili
    }
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

print(translate('hello world'))
