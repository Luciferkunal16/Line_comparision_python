from Line_Comparision.line_comparison_main import LineCompaisionMain


def test_calculte_length():
    testline = LineCompaisionMain()
    test_value = testline.calculate_length(2, 3, 3, 2)
    assert test_value == 1.4142135623730951


def test_check_equality_method_should_return_true():
    testobj = LineCompaisionMain()
    test_line1 = testobj.calculate_length(1, 4, 5, 6)
    test_line2 = testobj.calculate_length(1, 4, 5, 6)
    assert testobj.check_equality(test_line1, test_line2) == True


def test_check_equality_method_should_return_false():
    testobj = LineCompaisionMain()
    test_line1 = testobj.calculate_length(1, 4, 5, 6)
    test_line2 = testobj.calculate_length(2, 2, 5, 6)
    assert testobj.check_equality(test_line1, test_line2) == False

def test_check_Comparision_method_should_return_0():
    testobj = LineCompaisionMain()
    test_line1 = testobj.calculate_length(2, 2, 5, 6)
    test_line2 = testobj.calculate_length(2, 2, 5, 6)
    assert testobj.comparison_method(test_line1, test_line2) == 0

def test_check_Comparision_method_should_return_negative():
    testobj = LineCompaisionMain()
    test_line1 = testobj.calculate_length(22, 4, 5, 6)              #line1>line2
    test_line2 = testobj.calculate_length(12, 4, 5, 6)
    assert testobj.comparison_method(test_line1, test_line2) == 1

def test_check_Comparision_method_should_return_positive():
    testobj = LineCompaisionMain()
    test_line1 = testobj.calculate_length(1, 4, 5, 6)           #line1<line2
    test_line2 = testobj.calculate_length(12, 4, 5, 6)
    assert testobj.comparison_method(test_line1, test_line2) == -1

