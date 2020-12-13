# mongo-engine packages
from mongoengine import Document, StringField, FloatField

class KgFr(Document):
    kg = StringField(required=True, unique=True)
    fr = StringField(required=True, unique=True)

    def encode_to_json(self):
        return {
            "kg": self.kg,
            "fr": self.fr
        }

