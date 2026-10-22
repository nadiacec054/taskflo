
from app.job import Job
from app.scheduler import fcfs


def test_fcfs_schedule():
    jobs = [
        Job("J1", "First job", 5, 0),
        Job("J2", "Second job", 3, 1),
        Job("J3", "Third job", 2, 2),
    ]

    results = fcfs(jobs)

    assert results[0]["completion_time"] == 5
    assert results[1]["completion_time"] == 8
    assert results[2]["completion_time"] == 10

    assert results[0]["waiting_time"] == 0
    assert results[1]["waiting_time"] == 4
    assert results[2]["waiting_time"] == 6


def test_fcfs_handles_idle_cpu():
    jobs = [
        Job("J1", "First job", 2, 0),
        Job("J2", "Second job", 3, 5),
    ]

    results = fcfs(jobs)

    assert results[1]["start_time"] == 5
    assert results[1]["completion_time"] == 8
    assert results[1]["waiting_time"] == 0


def test_fcfs_does_not_modify_input_order():
    jobs = [
        Job("J2", "Second job", 3, 2),
        Job("J1", "First job", 2, 0),
    ]

    fcfs(jobs)

    assert jobs[0].job_id == "J2"
