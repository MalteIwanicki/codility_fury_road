import main

A = "A"
S = "S"


def test_by_foot():
    assert main.Times.by_foot({A: 2, S: 1}) == 20 + 30 + 20


def test_with_scooter():
    assert main.Times.with_scooter({A: 2, S: 1}) == 5 + 40 + 5


def test_solution():
    R = "ASAASS"
    assert main.solution(R) == 115
    R = "SSA"
    assert main.solution(R) == 80
    R = "SSSSAAA"
    assert main.solution(R) == 175
