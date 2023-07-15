from flask import Flask, request
from models import db
from flask_cors import CORS, cross_origin
from requests import add_task, active_tasks_list

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config["PROPAGATION_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "My test app"
    app.config["API_VERISON"] = "v1"

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app

app = create_app()

##########################################################################

@app.get("/all")
@cross_origin()
def get_all_tasks_list():
    return active_tasks_list()


@app.post("/add")
@cross_origin()
def add_new_task():
    request_data = request.get_json()
    if (add_task(request_data)):
        return request_data, 200
    else:
        return "Something went wrong!", 400