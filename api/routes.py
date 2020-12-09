from flask_restful import Api
# from models.kg_fr import KgFr


def app_routes(api: Api):
    api.add_resource(_, '/api/kg_fr/')