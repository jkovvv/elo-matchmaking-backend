from app import db

class Match(db.Model):
    __tablename__ = 'match'

    id = db.Column(db.Integer, primary_key=True)
    team1_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    team2_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    winning_team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=True)
    duration = db.Column(db.Integer, nullable=False)

    team_1 = db.relationship('Team', foreign_keys=[team1_id])
    team_2 = db.relationship('Team', foreign_keys=[team2_id])
    winning_team = db.relationship('Team', foreign_keys=[winning_team_id])

    def __init__(self, team_1_id, team_2_id, winning_team_id, duration):
        self.team1_id = team_1_id
        self.team2_id = team_2_id
        self.winning_team_id = winning_team_id
        self.duration = duration