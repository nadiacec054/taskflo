
from app.job import Job
from app.scheduler import round_robin


def test_round_robin_order():
    jobs = [
        Job("J1", "First", 5),
        Job("J2", "Second", 3),
        Job("J3", "Third", 1),
    ]

    results = round_robin(jobs, time_quantum=2)

    assert [job["job_id"] for job in results] == [
        "J3", "J2", "J1"
    ]


def test_round_robin_completion_times():
    jobs = [
        Job("J1", "First", 5),
        Job("J2", "Second", 3),
        Job("J3", "Third", 1),
    ]

    results = round_robin(jobs, time_quantum=2)
    results_by_id = {
        job["job_id"]: job for job in results
    }

    assert results_by_id["J1"]["completion_time"] == 9
    assert results_by_id["J2"]["completion_time"] == 8
    assert results_by_id["J3"]["completion_time"] == 5


def test_round_robin_rejects_invalid_quantum():
    jobs = [Job("J1", "First", 5)]

    try:
        round_robin(jobs, time_quantum=0)
        assert False, "Expected ValueError"
    except ValueError:
        pass
