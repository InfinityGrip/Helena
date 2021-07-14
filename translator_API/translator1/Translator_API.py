import requests, uuid, json
import ipywidgets as widgets
from IPython.core.display import display

#this is a translation script that I was wrote with the help of Naser Tamimi.
#with knowledge in using google API, I wanted to see how Azure API work
# in comparison. here is the website for the orininal tutorial:
# https://towardsdatascience.com/a-quick-way-to-build-applications-in-python-51d5ef477d88#


def azure_translate(text):
    API_KEY = 'ca8f62306f7d4bd7afd3b0c0fe22c043'# mock api key to demonstrate functionality
    location = 'eastus'# my region, might change depending on what you specify in your own azure account


    endpoint = 'https://alibaba.cognitiveservices.azure.com/'

    header = {'Ocp-Apim-Subscription-key': API_KEY,
              'Ocp-Apim-Suscription-Region': location,
               'Content-type': 'application/json',
              'X-ClientTraceId': str(uuid.uuid4())
    }

    params = {'api-version': '3.0',
              'from': 'en',
              'to': ['fr', 'it']}
    api_url = endpoint + 'translate'
    body = [{'text': text}]
    response = requests.post(api_url, data = params, headers = header, json=body)
    return response.json()

def on_button_clicked(b):
    response = azure_translate(w_text.value)
    w_output.clear_output()
    with w_output:
        print(response[0]['translations'][0]['text'])
w_header = widgets.HTML('<h2><i>SIMPLE</i> <b>Translator</b></h2>')
w_text = widgets.Textarea(placeholder = 'Write someting!', layout=widgets.Layout(width = '80%'))
w_button = widgets.Button(description = 'Translate To French')
w_button.on_click(on_button_clicked)
w_output = widgets.Output()
w_ui = widgets.VBox([w_header, w_text, w_button, w_output], layout=widgets.Layout(align_items='center'))
display(w_ui)


if __name__ == '__main__':
    print(azure_translate('Hello Wolrd'))