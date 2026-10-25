
from app.job import Job
from app.comparison import compare_algorithms


def test_compare_algorithms():
    jobs = [
        Job("J1", "First", 5, priority=3),
        Job("J2", "Second", 2, priority=1),
        Job("J3", "Third", 3, priority=2),
    ]

    comparison = compare_algorithms(
        jobs, time_quantum=2
    )

    assert set(comparison.keys()) == {
        "FCFS",
        "SJF",
        "Priority",
        "Round Robin",
    }

    for metrics in comparison.values():
        assert "average_waiting_time" in metrics
        assert "average_turnaround_time" in metrics
