# mongo-engine packages
from mongoengine import Document, StringField, FloatField

class KgFr(Document):
    kg = StringField(required=True)
    fr = StringField(required=True)

    def encode_to_json(self):
        return {
            "kg": self.kg,
            "fr": self.fr
        }

