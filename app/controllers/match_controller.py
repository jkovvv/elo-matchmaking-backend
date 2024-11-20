from flask import request, jsonify
from app.models.match import Match
from app.models.team import Team
from app.models.player import Player
from app import db
from sqlalchemy.orm import joinedload

def get_rating_adjustment(hours_played):
    if hours_played < 500:
        return 50
    elif 500 <= hours_played <= 999:
        return 40
    elif 1000 <= hours_played <= 2999:
        return 30
    elif 3000 <= hours_played <= 4999:
        return 20
    else:  
        return 10

def create_match():
    data = request.get_json()

    team_1_id = data.get('team1Id')
    team_2_id = data.get('team2Id')
    winning_team_id = data.get('winningTeamId')
    duration = data.get('duration')

    if duration < 1:
        return jsonify({'message': 'Invalid value of match duration'}), 400

    team1 = Team.query.get(int(team_1_id))
    team2 = Team.query.get(int(team_2_id))

    if winning_team_id is not None:
        winningteam = Team.query.options(joinedload(Team.players)).get(int(winning_team_id))

    if not team1 or not team2:
        return jsonify({'message': 'Teams not found'}), 404

    match = Match(
        team_1_id=team1.id,
        team_2_id=team2.id, 
        winning_team_id=winning_team_id, 
        duration=duration
    )

    db.session.add(match)

    #Updating player data

    if winning_team_id is not None:
        if winningteam.id == team1.id:
            losingteam_id = team2.id
        else:
            losingteam_id = team1.id

        losingteam = Team.query.options(joinedload(Team.players)).get(losingteam_id)
    else:
        winningteam = team1
        losingteam = team2

    winners_elo = 0
    losers_elo = 0

    for player in winningteam.players:
        player.hours_played+=duration
        if winning_team_id is not None:
            player.wins +=1
        winners_elo += player.elo

    winners_elo = winners_elo/5

    for player in losingteam.players:
        player.hours_played+=duration
        if winning_team_id is not None:
            player.losses +=1
        losers_elo += player.elo
    
    losers_elo = losers_elo/5

    for player in winningteam.players:
        e = 1 / (1 + 10 ** ((losers_elo - player.elo)/400))
        k = get_rating_adjustment(player.hours_played)
        player.ratingAdjustment = k

        if winning_team_id is None:
            s = 0.5
        else:
            s = 1

        player.elo += k * (s-e) 
        
    for player in losingteam.players:
        e = 1 / (1 + 10 ** ((winners_elo - player.elo)/400))
        k = get_rating_adjustment(player.hours_played)
        player.ratingAdjustment = k

        if winning_team_id is None:
            s = 0.5
        else:
            s = 0

        player.elo += k * (s-e) 
        
    db.session.commit()

    return jsonify(), 200

