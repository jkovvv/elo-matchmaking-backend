from app import db

class Player(db.Model):
    __tablename__ = 'player'

    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(50), unique=True, nullable=False)
    wins = db.Column(db.Integer, default=0)
    losses = db.Column(db.Integer, default=0)
    elo = db.Column(db.Float, default=0)
    hours_played = db.Column(db.Float, default=0)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=True)
    ratingAdjustment = db.Column(db.Integer, nullable=True)