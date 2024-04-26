from tracker import validate, validate_category, validate_cost


def main():
    test_validate()
    test_validate_cost()
    test_validate_category()
    
def test_validate():
    assert validate(5,6,10) == False
    assert validate(7,6,10) == True
    assert validate(-5,6,10) == False
    assert validate(0,6,10) == False


def test_validate_cost():
    assert validate_cost(-5) == False
    assert validate_cost(500) == True
    assert validate_cost(-15) == False

def test_validate_category():    
    assert validate_category("health") == False
    assert validate_category("sport") == True
 


if __name__ == "__main__":
    main()
