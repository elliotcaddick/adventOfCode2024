import day12.main as d12

def test_part_one_1():
    assert d12.part_one("day12/test/sample.txt") == 140
    
def test_part_one_2():
    assert d12.part_one("day12/test/sample2.txt") == 1930
    
def test_part_two_1():
    assert d12.part_two("day12/test/sample.txt") == 80
    
def test_part_two_2():
    assert d12.part_two("day12/test/sample3.txt") == 236
    
def test_part_two_3():
    assert d12.part_two("day12/test/sample4.txt") == 368

def test_part_two_4():
    assert d12.part_two("day12/test/sample2.txt") == 1930