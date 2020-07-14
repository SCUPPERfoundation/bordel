import requests

from readability import Document

from summarizer import Summarizer
from summarizer.coreference_handler import CoreferenceHandler


handler = CoreferenceHandler(greedyness=.4)

SAMPLE_URL='https://www.nytimes.com/2020/07/14/opinion/coronavirus-shutdown.html'

r = requests.get(SAMPLE_URL)

doc = Document(r.text)
print(doc.title())
body = doc.get_clean_html()
#print(body)

#model = Summarizer(sentence_handler=handler)
model = Summarizer()

print(model(body))
