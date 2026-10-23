from app.job import Job
from app.scheduler import priority_scheduling


def test_priority_order():
    jobs = [
        Job("J1", "First", 5, priority=3),
        Job("J2", "Second", 2, priority=1),
        Job("J3", "Third", 3, priority=2),
    ]

    results = priority_scheduling(jobs)

    assert [job["job_id"] for job in results] == [
        "J2", "J3", "J1"
    ]


def test_priority_with_arrival_times():
    jobs = [
        Job("J1", "First", 4, arrival_time=0, priority=2),
        Job("J2", "Second", 2, arrival_time=3, priority=1),
    ]

    results = priority_scheduling(jobs)

    assert [job["job_id"] for job in results] == [
        "J1", "J2"
    ]

    assert results[1]["start_time"] == 4
    assert results[1]["completion_time"] == 6