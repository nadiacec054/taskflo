
from app.job import Job
from app.scheduler import fcfs, calculate_metrics


def test_calculate_metrics():
    jobs = [
        Job("J1", "First job", 5, 0),
        Job("J2", "Second job", 3, 1),
        Job("J3", "Third job", 2, 2),
    ]

    results = fcfs(jobs)
    metrics = calculate_metrics(results)

    assert round(metrics["average_waiting_time"], 2) == 3.33
    assert round(metrics["average_turnaround_time"], 2) == 6.67


def test_metrics_for_empty_results():
    metrics = calculate_metrics([])

    assert metrics["average_waiting_time"] == 0
    assert metrics["average_turnaround_time"] == 0
