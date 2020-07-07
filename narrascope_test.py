from bordel import db
from bordel.models.alpha import ReviewDoc
import csv

reader = csv.DictReader(open('examples/articles.csv'))
for r in reader:
    db.session.add(ReviewDoc(blob=r))

#print(items[3]['Author'])
db.session.commit()
