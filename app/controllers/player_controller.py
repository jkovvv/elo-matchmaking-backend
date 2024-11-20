from flask import jsonify, request
from app.models.player import Player
from app import db

def create_player():
    data = request.json
    nickname = data.get('nickname')
    
    if not nickname:
        return jsonify({'error': 'Nickname is required'}), 400

    if Player.query.filter_by(nickname=nickname).first():
        return jsonify({'error': 'Nickname already exists'}), 400

    player = Player(nickname=nickname)
    db.session.add(player)
    db.session.commit()
    
    return jsonify({
        'id': player.id,
        'nickname': player.nickname,
        'wins': player.wins,
        'losses': player.losses,
        'elo': player.elo,
        'hoursPlayed': player.hours_played,
        'team': player.team_id,
        'ratingAdjustment': player.ratingAdjustment
    }), 200

def get_all():
    try:
        players = Player.query.all()
        players_list = [{
            'id': player.id,
            'nickname': player.nickname,
            'wins': player.wins,
            'losses': player.losses,
            'elo': player.elo,
            'hoursPlayed': player.hours_played,
            'team': player.team_id,
            'ratingAdjustment': player.ratingAdjustment
        } for player in players]
        return jsonify(players_list), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

def get_player(player_id):
    player = Player.query.get(player_id)
    
    if not player:
        return jsonify({"message": "Player not found"}), 404

    return jsonify({
        'id': player.id,
        'nickname': player.nickname,
        'wins': player.wins,
        'losses': player.losses,
        'elo': player.elo,
        'hoursPlayed': player.hours_played,
        'team': player.team_id,
        'ratingAdjustment': player.ratingAdjustment
    })
