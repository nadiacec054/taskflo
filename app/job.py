
from dataclasses import dataclass


@dataclass
class Job:
    job_id: str
    name: str
    burst_time: int
    arrival_time: int = 0
    priority: int = 0

    def __post_init__(self):
        if not self.job_id:
            raise ValueError("Job ID cannot be empty")

        if not self.name:
            raise ValueError("Job name cannot be empty")

        if self.burst_time <= 0:
            raise ValueError("Burst time must be positive")

        if self.arrival_time < 0:
            raise ValueError("Arrival time cannot be negative")
