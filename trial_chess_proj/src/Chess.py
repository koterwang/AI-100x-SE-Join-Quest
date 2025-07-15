class ChessPieces:
    def __init__(self, color='Red'):
        self.color = color
    def in_palace(self, pos, color):
        row, col = pos
        if color == 'Red':
            return 1 <= row <= 3 and 4 <= col <= 6
        else:
            return 8 <= row <= 10 and 4 <= col <= 6
    def is_same_color(self, to_pos, context):
        if context and hasattr(context, 'board') and to_pos in context.board:
            return context.board[to_pos]['color'] == self.color
        return False

class General(ChessPieces):
    def __init__(self, color='Red'):
        super().__init__(color)

    def move(self, from_pos, to_pos, context=None):
        if self.is_same_color(to_pos, context):
            return False
        if not self.in_palace(from_pos, self.color) or not self.in_palace(to_pos, self.color):
            return False
        dr = abs(to_pos[0] - from_pos[0])
        dc = abs(to_pos[1] - from_pos[1])
        return (dr == 1 and dc == 0) or (dr == 0 and dc == 1)

class Guard(ChessPieces):
    def __init__(self, color='Red'):
        super().__init__(color)

    def move(self, from_pos, to_pos, context=None):
        if self.is_same_color(to_pos, context):
            return False
        if not self.in_palace(from_pos, self.color) or not self.in_palace(to_pos, self.color):
            return False
        dr = abs(to_pos[0] - from_pos[0])
        dc = abs(to_pos[1] - from_pos[1])
        return dr == 1 and dc == 1

class Rook(ChessPieces):
    def __init__(self, color='Red'):
        super().__init__(color)

    def move(self, from_pos, to_pos, context=None):
        if self.is_same_color(to_pos, context):
            return False
        if from_pos == to_pos:
            return False
        fr, fc = from_pos
        tr, tc = to_pos
        # 只能直線
        if fr != tr and fc != tc:
            return False
        # 取得路徑上的格子（不含起點與終點）
        path = []
        if fr == tr:
            rng = range(fc+1, tc) if fc < tc else range(tc+1, fc)
            path = [(fr, c) for c in rng]
        else:
            rng = range(fr+1, tr) if fr < tr else range(tr+1, fr)
            path = [(r, fc) for r in rng]
        # 路徑上不能有任何棋子
        for pos in path:
            if context and hasattr(context, 'board') and pos in context.board:
                return False
        # 終點
        if context and hasattr(context, 'board') and to_pos in context.board:
            # 有敵方棋子可吃
            return context.board[to_pos]['color'] != self.color
        return True

class Horse(ChessPieces):
    def __init__(self, color='Red'):
        super().__init__(color)

    def move(self, from_pos, to_pos, context=None):
        if self.is_same_color(to_pos, context):
            return False
        fr, fc = from_pos
        tr, tc = to_pos
        dr = tr - fr
        dc = tc - fc
        # 只能走L形
        if not ((abs(dr) == 2 and abs(dc) == 1) or (abs(dr) == 1 and abs(dc) == 2)):
            return False
        # 馬腳判斷
        if abs(dr) == 2:
            leg = (fr + dr // 2, fc)
        else:
            leg = (fr, fc + dc // 2)
        if context and hasattr(context, 'board') and leg in context.board:
            return False
        # 終點出界
        if not (1 <= tr <= 10 and 1 <= tc <= 9):
            return False
        # 終點不能是己方棋子
        if context and hasattr(context, 'board') and to_pos in context.board:
            if context.board[to_pos]['color'] == self.color:
                return False
        return True

class Cannon(ChessPieces):
    def __init__(self, color='Red'):
        super().__init__(color)

    def move(self, from_pos, to_pos, context=None):
        if self.is_same_color(to_pos, context):
            return False
        if from_pos == to_pos:
            return False
        fr, fc = from_pos
        tr, tc = to_pos
        # 只能直線
        if fr != tr and fc != tc:
            return False
        # 取得路徑上的格子（不含起點與終點）
        path = []
        if fr == tr:
            rng = range(fc+1, tc) if fc < tc else range(tc+1, fc)
            path = [(fr, c) for c in rng]
        else:
            rng = range(fr+1, tr) if fr < tr else range(tr+1, fr)
            path = [(r, fc) for r in rng]
        # 計算障礙物數量
        screens = 0
        for pos in path:
            if context and hasattr(context, 'board') and pos in context.board:
                screens += 1
        # 終點
        has_target = context and hasattr(context, 'board') and to_pos in context.board
        if not has_target:
            # 不吃子時，不能跳過任何棋子
            return screens == 0
        else:
            # 吃子時，必須剛好跳過一個障礙物，且終點是敵方
            return screens == 1 and context.board[to_pos]['color'] != self.color

class Elephant(ChessPieces):
    def __init__(self, color='Red'):
        super().__init__(color)

    def move(self, from_pos, to_pos, context=None):
        if self.is_same_color(to_pos, context):
            return False
        fr, fc = from_pos
        tr, tc = to_pos
        dr = tr - fr
        dc = tc - fc
        # 只能走對角兩格
        if not (abs(dr) == 2 and abs(dc) == 2):
            return False
        # 不能過河
        if self.color == 'Red' and tr >= 6:
            return False
        if self.color == 'Black' and tr <= 5:
            return False
        # 象腳判斷
        leg = (fr + dr // 2, fc + dc // 2)
        if context is not None and hasattr(context, 'board') and leg in context.board:
            return False
        # 終點出界
        if not (1 <= tr <= 10 and 1 <= tc <= 9):
            return False
        return True

class Soldier(ChessPieces):
    def __init__(self, color='Red'):
        super().__init__(color)

    def move(self, from_pos, to_pos, context=None):
        if self.is_same_color(to_pos, context):
            return False
        fr, fc = from_pos
        tr, tc = to_pos
        dr = tr - fr
        dc = tc - fc
        if self.color == 'Red':
            if fr <= 5:
                return dr == 1 and dc == 0
            else:
                return (dr == 1 and dc == 0) or (dr == 0 and abs(dc) == 1)
        else:
            if fr >= 6:
                return dr == -1 and dc == 0
            else:
                return (dr == -1 and dc == 0) or (dr == 0 and abs(dc) == 1)

class ChessGame:
    def __init__(self, board):
        self.board = board  # board: dict, key: (row, col), value: {'type':..., 'color':...}
    def find_general(self, color):
        for pos, info in self.board.items():
            if info['type'] == 'General' and info['color'] == color:
                return pos
        return None
    def has_valid_move(self, general_pos, color):
        # General 所有可能移動
        candidate = [(general_pos[0]+1, general_pos[1]), (general_pos[0]-1, general_pos[1]),
                     (general_pos[0], general_pos[1]+1), (general_pos[0], general_pos[1]-1)]
        g = General(color)
        for to_pos in candidate:
            if not (1 <= to_pos[0] <= 10 and 1 <= to_pos[1] <= 9):
                continue
            if g.move(general_pos, to_pos, self):
                # 終點不能有己方棋子
                if to_pos not in self.board or self.board[to_pos]['color'] != color:
                    return True
        return False
    def move(self, color, piece_type, from_pos, to_pos, context=None):
        # 取得棋子物件
        piece_class = globals()[piece_type]
        piece = piece_class(color)
        # 檢查移動是否合法
        if not piece.move(from_pos, to_pos, self):
            return 'Invalid move'
        # 模擬移動
        new_board = self.board.copy()
        if to_pos in new_board:
            del new_board[to_pos]
        new_board[to_pos] = new_board.pop(from_pos)
        # 檢查敵方 General 是否被吃掉
        enemy_color = 'Black' if color == 'Red' else 'Red'
        # 只有當原本棋盤有敵方 General 才檢查勝負
        orig_enemy_general = any(info['type'] == 'General' and info['color'] == enemy_color for info in self.board.values())
        if orig_enemy_general:
            enemy_general_pos = None
            for pos, info in new_board.items():
                if info['type'] == 'General' and info['color'] == enemy_color:
                    enemy_general_pos = pos
                    break
            if not enemy_general_pos:
                return f'{color} wins'  # 擊殺敵方 General
            # 檢查敵方 General 是否無法移動
            temp_game = ChessGame(new_board)
            if not temp_game.has_valid_move(enemy_general_pos, enemy_color):
                return f'{color} wins'  # 對方 General 無法移動
        return 'Continue' 