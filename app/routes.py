from flask import Blueprint
from app.controllers.player_controller import create_player, get_all, get_player
from app.controllers.team_controller import create_team, get_team_by_id
from app.controllers.match_controller import create_match

bp = Blueprint('routes', __name__)

# Player related routes

@bp.route('/players/create', methods=['POST'])
def create_player_route():
    return create_player()

@bp.route('/players', methods=['GET'])
def get_all_players():
    return get_all()

@bp.route('/players/<int:player_id>', methods=['GET'])
def get_player_by_id(player_id):
    return get_player(player_id)

# Team related routes

@bp.route('/teams', methods=['POST'])
def create_team_route():
    return create_team()


@bp.route('/teams/<int:team_id>', methods=['GET'])
def get_team_route(team_id):
    return get_team_by_id(team_id)

# Match related routes

@bp.route('/matches', methods=['POST'])
def create_match_route():
    return create_match()