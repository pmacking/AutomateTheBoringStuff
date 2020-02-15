def isValidChessBoard(board):
    while True:
        blackPieces = 0
        whitePieces = 0
        wpawn = 0
        bpawn = 0
        letterAxis = ('a','b','c','d','e','f','g','h')
        pieceColour = ('b','w')
        pieceType = ('pawn','knight','bishop','rook','queen','king')

        #one black king and one white king
        if 'bking' not in board.values() or 'wking' not in board.values():
            print('KingError')
            return False

        #each player has <= 16 pieces
        for i in board.values():
            if i:
                if i[0] == 'b':
                    blackPieces+=1
                if i[0] == 'w':
                    whitePieces+=1
                if whitePieces >= 17 or blackPieces >= 17:
                    print('TotalPieceError')
                    return False

        #each player has <= 8 pawns
        for i in board.values():
            if i == 'wpawn':
                wpawn+=1
            elif i == 'bpawn':
                bpawn+=1
            if wpawn >9 or bpawn >= 9:
                print('PawnError')
                return False

        #all pieces must be on valid space from '1a' to '8h'
        for i in board.keys():
            if int(i[0]) >= 9:
                print('SpacesError')
                return False
            if i[1] not in letterAxis:
                print('yAxisError')
                return False

        #piece names begin with 'w' or 'b'
        for i in board.values():
            if i:
                if i[0] not in pieceColour:
                    print('WhiteOrBlackColourError')
                    return False

        #piece names must follow with 'pawn', 'knight', 'bishop', 'rook', 'queen', 'king'
        for i in board.values():
            if i:
                if i[1:] not in pieceType:
                    print('PieceTypeError')
                    return False
        return 'This board checks out'

board = {
'1a': 'bking','2a': 'bqueen','3a': 'brook','4a': 'brook','5a': 'bknight','6a': 'bknight','7a': 'bbishop','8a': 'bbishop',
'1b': 'bpawn','2b': 'bpawn','3b': 'bpawn','4b': 'bpawn','5b': 'bpawn','6b': 'bpawn','7b': 'bpawn','8b': 'bpawn',
'1c': 'wking','2c': 'wqueen','3c': 'wrook','4c': 'wrook','5c': 'wbishop','6c': 'wbishop','7c': 'wknight','8c': 'wknight',
'1e': 'wpawn','2e': 'wpawn','3e': 'wpawn','4e': 'wpawn','5e': 'wpawn','6e': 'wpawn','7e': 'wpawn','8e': 'wpawn',
'1f': '','2f': '','3f': '','4f': '','5f': '','6f': '','7f': '','8f': '',
'1g': '','2g': '','3g': '','4g': '','5g': '','6g': '','7g': '','8g': '',
'1h': '','2h': '','3h': '','4h': '','5h': '','6h': '','7h': '','8h': '',
}

print(isValidChessBoard(board))