#function takes dictionary argument, and returns True or False if board is valid
#valid board has:
    #all pieces must be on valid space from '1a' to '8h'
    #piece names begin with 'w' or 'b'
    #piece names must follow with 'pawn', 'knight', 'bishop', 'rook', 'queen', 'king'
    #function should detect when a bug has resulted in improper chess board

def isValidChessBoard(board):
    while True:
        blackPieces = 0
        whitePieces = 0
        wpawn = 0
        bpawn = 0
        #one black king and one white king
        if 'bking' not in board.values():
            print('KingError')
            return False
            break
        if 'wking' not in board.values():
            print('KingError')
            return False
            break
        #each player has <= 16 pieces
        for i in list(board.values()):
            if i[0] == 'b':
                blackPieces+=1
            if i[0] == 'w':
                whitePieces+=1
            if blackPieces or whitePieces >= 17:
                print('TotalPieceError')
                return False
                break
        #each player has <= 8 pawns
        for i in board.values():
            if i == 'wpawn':
                wpawn+=1
            if i == 'bpawn':
                bpawn+=1
            if wpawn or bpawn >= 9:
                return False
                break
        #all pieces must be on valid space from '1a' to '8h'
        for i in board.keys():
            if i[0] >= 9:
                return False
                break
        #piece names begin with 'w' or 'b'
        #piece names must follow with 'pawn', 'knight', 'bishop', 'rook', 'queen', 'king'
        #function should detect when a bug has resulted in improper chess board

    return True

board = {'1a':'bking','2a':'wking'}
print(isValidChessBoard(board))