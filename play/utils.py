def is_under_attack(chessboard, position,chesspiece):
    for piece, piece_position in chessboard["postions"].items():
        if piece != chesspiece.title():  # Exclude the piece itself
            moves = get_possible_moves(chessboard, piece, piece_position)
            if position in moves:
                return True
    return False

def get_possible_moves(chessboard, piece_name, current_position):
    piece_name = piece_name.capitalize()
    col = ord(current_position[0]) - ord("A")
    row = int(current_position[1]) -1

    # Define possible moves for each chess piece
    dispacher = {
        "Pawn": get_pawn_moves,
        "Rook": get_rook_moves,
        "Knight": get_knight_moves,
        "Bishop": get_bishop_moves,
        "Queen": get_possible_queen_moves,
        "King": get_king_moves,
    }

    possible_moves = []
    get_moves = dispacher.get(piece_name, lambda: None)
    moves = get_moves((col, row))
    for move in moves:
        new_col =  move[0]
        new_row =  move[1]
        # Check if the new position is within the chessboard bounds
        if 0 <= new_col <= 7 and 0 <= new_row <= 7:
            pos = f"{chr(new_col + ord('A'))}{new_row + 1}"
            possible_moves.append(pos)
        
    return possible_moves

def get_possible_queen_moves(position):
    column, row = position
    possible_moves = []

    # Horizontal and Vertical moves
    for i in range(8):
        if i != column:
            possible_moves.append((i, row))
        if i != row:
            possible_moves.append((column, i))

    # Diagonal moves
    for i in range(1, 8):
        if 0 <= column + i < 8 and 0 <= row + i < 8:
            possible_moves.append((column + i, row + i))
        if 0 <= column - i < 8 and 0 <= row + i < 8:
            possible_moves.append((column - i, row + i))
        if 0 <= column + i < 8 and 0 <= row - i < 8:
            possible_moves.append((column + i, row - i))
        if 0 <= column - i < 8 and 0 <= row - i < 8:
            possible_moves.append((column - i, row - i))

    return possible_moves

def get_rook_moves(position):
    column, row = position
    possible_moves = []

    # Horizontal moves
    for i in range(8):
        if i != column:
            possible_moves.append((i, row))

    # Vertical moves
    for i in range(8):
        if i != row:
            possible_moves.append((column, i))

    return possible_moves

def get_knight_moves(position):
    column, row = position
    possible_moves = []

    knight_moves = [
        (-2, -1), (-2, 1),   # Upward moves
        (-1, -2), (-1, 2),   # Left moves
        (1, -2), (1, 2),     # Right moves
        (2, -1), (2, 1)      # Downward moves
    ]

    for move in knight_moves:
        new_column = column + move[0]
        new_row = row + move[1]

        if 0 <= new_column < 8 and 0 <= new_row < 8:
            possible_moves.append((new_column, new_row))

    return possible_moves

def get_king_moves(position):
    column, row = position
    possible_moves = []

    king_moves = [
        (-1, -1), (-1, 0), (-1, 1),   # Left moves
        (0, -1), (0, 1),               # Up and down moves
        (1, -1), (1, 0), (1, 1)        # Right moves
    ]

    for move in king_moves:
        new_column = column + move[0]
        new_row = row + move[1]

        if 0 <= new_column < 8 and 0 <= new_row < 8:
            possible_moves.append((new_column, new_row))

    return possible_moves



def get_bishop_moves(position):
    column, row = position
    possible_moves = []

    # Diagonal moves
    for i in range(1, 8):
        if 0 <= column + i < 8 and 0 <= row + i < 8:
            possible_moves.append((column + i, row + i))
        if 0 <= column - i < 8 and 0 <= row + i < 8:
            possible_moves.append((column - i, row + i))
        if 0 <= column + i < 8 and 0 <= row - i < 8:
            possible_moves.append((column + i, row - i))
        if 0 <= column - i < 8 and 0 <= row - i < 8:
            possible_moves.append((column - i, row - i))

    return possible_moves

def get_pawn_moves(position, is_white=True):
    column, row = position
    possible_moves = []

    # Define direction based on pawn color
    direction = 1 if is_white else -1

    # Pawn's initial move (two squares forward)
    if (row == 1 and is_white) or (row == 6 and not is_white):
        if 0 <= row + 2 * direction < 8:
            possible_moves.append((column, row + 2 * direction))

    # Pawn's regular move (one square forward)
    if 0 <= row + direction < 8:
        possible_moves.append((column, row + direction))

    # Pawn captures diagonally
    if 0 <= row + direction < 8:
        if 0 <= column - 1 < 8:
            possible_moves.append((column - 1, row + direction))
        if 0 <= column + 1 < 8:
            possible_moves.append((column + 1, row + direction))

    return possible_moves