import day14.main as d14

def test_part_one():
    assert d14.part_one("day14/test/sample.txt", 11, 7) == 12
    
def test_part_two():
    assert d14.part_one("day14/test/sample.txt") == 480