from summarizer import Summarizer
from summarizer.coreference_handler import CoreferenceHandler


handler = CoreferenceHandler(greedyness=.4)

#SAMPLE_URL='https://www.nytimes.com/2020/07/14/opinion/coronavirus-shutdown.html'
# static text dump:
with open('test.txt') as f:
    body = f.read()

#model = Summarizer(sentence_handler=handler)
model = Summarizer()

print(model(body))
