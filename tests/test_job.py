
import pytest

from app.job import Job


def test_create_job():
    job = Job("J1", "Data processing", 5)

    assert job.job_id == "J1"
    assert job.name == "Data processing"
    assert job.burst_time == 5
    assert job.arrival_time == 0
    assert job.priority == 0


def test_create_job_with_custom_values():
    job = Job("J2", "File backup", 3, 2, 1)

    assert job.arrival_time == 2
    assert job.priority == 1


def test_burst_time_must_be_positive():
    with pytest.raises(ValueError):
        Job("J3", "Invalid job", 0)


def test_arrival_time_cannot_be_negative():
    with pytest.raises(ValueError):
        Job("J4", "Invalid job", 5, -1)


def test_job_id_cannot_be_empty():
    with pytest.raises(ValueError):
        Job("", "Invalid job", 5)
