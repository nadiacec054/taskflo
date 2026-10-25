
from app.comparison import find_best_algorithms


def test_find_best_algorithms():
    comparison = {
        "FCFS": {
            "average_waiting_time": 4.0,
            "average_turnaround_time": 7.0,
        },
        "SJF": {
            "average_waiting_time": 2.0,
            "average_turnaround_time": 5.0,
        },
        "Round Robin": {
            "average_waiting_time": 3.0,
            "average_turnaround_time": 6.0,
        },
    }

    result = find_best_algorithms(comparison)

    assert result["best_average_waiting_time"] == "SJF"
    assert result["best_average_turnaround_time"] == "SJF"


def test_empty_comparison():
    try:
        find_best_algorithms({})
        assert False, "Expected ValueError"
    except ValueError:
        pass
