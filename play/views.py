from django.shortcuts import render
from django.http import JsonResponse
from .utils import get_possible_moves,is_under_attack
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def chess_moves(request,chesspiece):
    chess_piece_names = [   'king',
                            'queen',
                            'rook',
                            'bishop',
                            'knight',
                            'pawn'
                        ]
    data = {}
    if chesspiece not in chess_piece_names:
        data["error"] = "Invalid chess piece"
        data ["msg"] = "please select from king, queen, rook, bishop, knight, pawn"
        return JsonResponse(data, status=404)
    
    # Extract request data
    request_data = json.loads(request.body)
    positions = request_data.get("postions")

    if not positions:
        data["error"] = "positions not provided"
        return JsonResponse(data, status=404)
    if not isinstance(positions, dict):
        data["error"] = "positions must be a dictionary"
        return JsonResponse(data, status=404)
    valid_moves = get_possible_moves(positions, chesspiece,positions.get(chesspiece.title(), '') )

    removed_moves = []
    for move in valid_moves:
        if is_under_attack(request_data,move,chesspiece):
            removed_moves.append(move)

    moves = [x for x in valid_moves if x not in removed_moves]

    data["valid_moves"] = moves
    return JsonResponse(data, status=200)
