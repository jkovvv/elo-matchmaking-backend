from app import db
from app.models.player import Player 

class Team(db.Model):
    __tablename__ = 'team'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    players = db.relationship('Player', backref='team', lazy=True)

    def __init__(self, name):
        self.name = name
