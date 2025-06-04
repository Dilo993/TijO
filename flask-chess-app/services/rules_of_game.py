class RulesOfGame:

    """
        Metoda zwraca true, tylko gdy przejscie z polozenia source na destination w jednym ruchu jest zgodne
        z zasadami gry w szachy.
    """
    def is_correct_move(self, source, destination):
        raise NotImplementedError("Subclasses must implement this method")

class Bishop(RulesOfGame):
    def is_correct_move(self, source, destination):
        if not source or not destination:
            return False
        dx = abs(destination[0] - source[0])
        dy = abs(destination[1] - source[1])
        return dx == dy and dx != 0

class Rook(RulesOfGame):
    def is_correct_move(self, source, destination):
        if not source or not destination:
            return False
        dx = abs(destination[0] - source[0])
        dy = abs(destination[1] - source[1])
        return (dx == 0 and dy != 0) or (dy == 0 and dx != 0)
    

class King(RulesOfGame):
    def is_correct_move(self, source, destination):
        if not source or not destination:
            return False
        dx = abs(destination[0] - source[0])
        dy = abs(destination[1] - source[1])
        return max(dx, dy) == 1 and (dx != 0 or dy != 0)

class Queen(RulesOfGame):
    def is_correct_move(self, source, destination):
        if not source or not destination:
            return False
        dx = abs(destination[0] - source[0])
        dy = abs(destination[1] - source[1])
        return (dx == dy and dx != 0) or (dx == 0 and dy != 0) or (dy == 0 and dx != 0)

class Knight(RulesOfGame):
    def is_correct_move(self, source, destination):
        if not source or not destination:
            return False
        dx = abs(destination[0] - source[0])
        dy = abs(destination[1] - source[1])
        return (dx, dy) in [(1, 2), (2, 1)]

class Pawn(RulesOfGame):
    def is_correct_move(self, source, destination):
        if not source or not destination:
            return False
        dx = destination[0] - source[0]
        dy = destination[1] - source[1]
        # Zakładamy, że pionek porusza się "w górę" (białe), czyli y rośnie
        # Ruch o jedno pole do przodu
        if dx == 0 and dy == 1:
            return True
        # Ruch o dwa pola do przodu z pozycji początkowej
        if dx == 0 and dy == 2 and source[1] == 2:
            return True
        # Bicie po skosie
        if abs(dx) == 1 and dy == 1:
            return True
        return False
