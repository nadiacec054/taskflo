
from app.job import Job
from app.scheduler import sjf, fcfs, calculate_metrics


def test_sjf_selects_shortest_job():
    jobs = [
        Job("J1", "Long job", 6, 0),
        Job("J2", "Short job", 2, 0),
        Job("J3", "Medium job", 4, 0),
    ]

    results = sjf(jobs)

    assert [r["job_id"] for r in results] == ["J2", "J3", "J1"]
    assert results[0]["completion_time"] == 2
    assert results[1]["completion_time"] == 6
    assert results[2]["completion_time"] == 12


def test_sjf_does_not_run_job_before_arrival():
    jobs = [
        Job("J1", "First job", 3, 0),
        Job("J2", "Later job", 1, 5),
    ]

    results = sjf(jobs)

    assert results[0]["start_time"] == 0
    assert results[1]["start_time"] == 5
    assert results[1]["completion_time"] == 6


def test_sjf_reduces_waiting_time_for_same_workload():
    jobs = [
        Job("J1", "Long job", 6, 0),
        Job("J2", "Short job", 2, 0),
        Job("J3", "Medium job", 4, 0),
    ]

    sjf_metrics = calculate_metrics(sjf(jobs))
    fcfs_metrics = calculate_metrics(fcfs(jobs))

    assert (
        sjf_metrics["average_waiting_time"]
        < fcfs_metrics["average_waiting_time"]
    )


def test_sjf_does_not_modify_input_order():
    jobs = [
        Job("J2", "Short job", 2, 0),
        Job("J1", "Long job", 6, 0),
    ]

    sjf(jobs)

    assert jobs[0].job_id == "J2"
