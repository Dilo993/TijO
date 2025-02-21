from src.math_lib import my_max,is_perfect;

def test_my_max():
    assert my_max(None) == None,"Should be None"

    assert my_max([]) == None,"Should be None"

    assert my_max([5]) == 5,"Should be 5"

    assert my_max([1, 3, 2, 7, 4]) == 7,"Should be 7"

    assert my_max([-1, -3, -2, -7, -4]) == -1,"Should be -1"

    assert my_max([-1, 3, -2, 7, -4]) == 7,"Should be 7"

    assert my_max([3, 3, 3, 3, 3]) == 3,"Should be 3"
    print("Przeszedłeś testy my_max")

def test_is_per():
    assert is_perfect(8128) == True,"Should be True"

    assert is_perfect(6) == True,"Should be True"

    assert is_perfect(496) == True,"Should be True"

    assert is_perfect(3) == False,"Should be False"

    assert is_perfect(100) == False,"Should be False"

    print("Przeszedłeś testy is_perfect")

test_my_max()
test_is_per()