from temp_conversion_script_2 import convert_c_to_f, fever_detection


def test1():
    answer = convert_c_to_f(20.0)
    expected = 68.0
    assert answer == expected


def test2():
    answer = convert_c_to_f(-40)
    expected = -40
    assert answer == expected


def test3():
    answer = convert_c_to_f(50)
    expected = 122
    assert answer == expected


def test_fever_detection():
    temp_list = [93.0, 98.0, 100.0, 105.5, 101.0]
    max_temp, is_fever = fever_detection(temp_list)
    expected_max = 105.5
    expected_is_fever = True
    assert max_temp == expected_max
    assert is_fever == expected_is_fever


def test_fever_detection_bad():
    temp_list = [93.0, "98.0", 100.0, 105.5, 101.0]
    max_temp, is_fever = fever_detection(temp_list)
    expected_max = 105.5
    expected_is_fever = True
    assert max_temp == expected_max
