from flask import request, jsonify
from sqlalchemy.orm import joinedload
from app import db
from app.models.team import Team
from app.models.player import Player

def create_team():
    data = request.get_json()

    if 'teamName' not in data:
        return jsonify({'message': 'Team name is required'}), 400
    
    name = data['teamName']
    players = data['players']

    if Team.query.filter_by(name=name).first():
        return jsonify({'error': 'Name already exists'}), 400
    
    team = Team(name = name)
    
    player_data = []
    player_objs = []

    for player_id in players:

        player = Player.query.get(int(player_id))

        if not player:
            return jsonify({"message": "Player not found"}), 404

        if player.team_id:
            return jsonify({'error': 'Player already assigned to a team.'}), 400

        player_objs.append(player)
        if player:
            player.team_id = team.id
            db.session.add(player)
            player_data.append({
                'id': player.id,
                'nickname': player.nickname,
                'wins': player.wins,
                'losses': player.losses,
                'elo': player.elo,
                'hoursPlayed': player.hours_played,
                'team': player.team_id,
                'ratingAdjustment': player.ratingAdjustment
            })
    
    team.players = player_objs
    db.session.add(team)
    db.session.commit()


    return jsonify({'id': team.id, 'teamName': team.name, 'players': player_data }), 200

def get_team_by_id(team_id):
    team = Team.query.options(joinedload(Team.players)).get(team_id)

    if not team:
        return jsonify({'message': 'Team not found'}), 404

    players = [{
                'id': player.id,
                'nickname': player.nickname,
                'wins': player.wins,
                'losses': player.losses,
                'elo': player.elo,
                'hoursPlayed': player.hours_played,
                'team': player.team_id,
                'ratingAdjustment': player.ratingAdjustment } for player in team.players]
    
    return jsonify({'id': team.id, 'teamName': team.name, 'players': players}), 200
