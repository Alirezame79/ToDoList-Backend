from models import db

class TaskModel(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    creator = db.Column(db.String(25), unique=False)
    task = db.Column(db.String(100) , unique=False)
    status = db.Column(db.Integer, nullable=True, default=1)

    def __str__(self):
        return {
            "ID": self.id,
            "Creator": self.creator,
            "Body": self.task,
            "Status": self.status
        }