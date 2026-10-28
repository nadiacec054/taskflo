\
def fcfs(jobs):
    sorted_jobs = sorted(jobs, key=lambda job: job.arrival_time)

    current_time = 0
    results = []

    for job in sorted_jobs:
        start_time = max(current_time, job.arrival_time)
        completion_time = start_time + job.burst_time
        turnaround_time = completion_time - job.arrival_time
        waiting_time = turnaround_time - job.burst_time

        results.append({
            "job_id": job.job_id,
            "start_time": start_time,
            "completion_time": completion_time,
            "turnaround_time": turnaround_time,
            "waiting_time": waiting_time,
        })

        current_time = completion_time

    return results

def calculate_metrics(results):
    if not results:
        return {
            "average_waiting_time": 0,
            "average_turnaround_time": 0,
        }

    total_jobs = len(results)

    average_waiting_time = sum(
        job["waiting_time"] for job in results
    ) / total_jobs

    average_turnaround_time = sum(
        job["turnaround_time"] for job in results
    ) / total_jobs

    return {
        "average_waiting_time": average_waiting_time,
        "average_turnaround_time": average_turnaround_time,
    }


def sjf(jobs):
    pending_jobs = list(jobs)

    current_time = 0
    results = []

    while pending_jobs:
        available_jobs = [
            job for job in pending_jobs
            if job.arrival_time <= current_time
        ]

        if not available_jobs:
            current_time = min(
                job.arrival_time for job in pending_jobs
            )
            continue

        job = min(
            available_jobs,
            key=lambda job: (job.burst_time, job.arrival_time)
        )

        start_time = current_time
        completion_time = start_time + job.burst_time
        turnaround_time = completion_time - job.arrival_time
        waiting_time = turnaround_time - job.burst_time

        results.append({
            "job_id": job.job_id,
            "start_time": start_time,
            "completion_time": completion_time,
            "turnaround_time": turnaround_time,
            "waiting_time": waiting_time,
        })

        current_time = completion_time
        pending_jobs.remove(job)

    return results

def priority_scheduling(jobs):
    pending_jobs = list(jobs)

    current_time = 0
    results = []

    while pending_jobs:
        available_jobs = [
            job for job in pending_jobs
            if job.arrival_time <= current_time
        ]

        if not available_jobs:
            current_time = min(
                job.arrival_time for job in pending_jobs
            )
            continue

        job = min(
            available_jobs,
            key=lambda job: (job.priority, job.arrival_time)
        )

        start_time = current_time
        completion_time = start_time + job.burst_time
        turnaround_time = completion_time - job.arrival_time
        waiting_time = turnaround_time - job.burst_time

        results.append({
            "job_id": job.job_id,
            "start_time": start_time,
            "completion_time": completion_time,
            "turnaround_time": turnaround_time,
            "waiting_time": waiting_time,
        })

        current_time = completion_time
        pending_jobs.remove(job)

    return results

from collections import deque


def round_robin(jobs, time_quantum=2):
    if time_quantum <= 0:
        raise ValueError("Time quantum must be positive")

    pending_jobs = sorted(
        jobs, key=lambda job: job.arrival_time
    )

    ready_queue = deque()

    remaining_time = {
        job.job_id: job.burst_time
        for job in pending_jobs
    }

    current_time = 0
    next_job = 0

    results = []
    first_start_time = {}
    execution_history = []

    while ready_queue or next_job < len(pending_jobs):

        # Move time forward if no job is ready
        if (
            not ready_queue
            and current_time < pending_jobs[next_job].arrival_time
        ):
            current_time = pending_jobs[next_job].arrival_time

        # Add jobs that have arrived
        while (
            next_job < len(pending_jobs)
            and pending_jobs[next_job].arrival_time <= current_time
        ):
            ready_queue.append(pending_jobs[next_job])
            next_job += 1

        job = ready_queue.popleft()

        # Record the first time this job starts
        start_time = current_time
        first_start_time.setdefault(job.job_id, start_time)

        # Execute for one time quantum or until completion
        execution_time = min(
            time_quantum,
            remaining_time[job.job_id]
        )

        current_time += execution_time
        remaining_time[job.job_id] -= execution_time

        # Record this execution slice
        execution_history.append({
            "job_id": job.job_id,
            "start": start_time,
            "end": current_time,
        })

        # Add newly arrived jobs to the ready queue
        while (
            next_job < len(pending_jobs)
            and pending_jobs[next_job].arrival_time <= current_time
        ):
            ready_queue.append(pending_jobs[next_job])
            next_job += 1

        # Requeue unfinished jobs
        if remaining_time[job.job_id] > 0:
            ready_queue.append(job)

        # Record completed jobs
        else:
            completion_time = current_time
            turnaround_time = (
                completion_time - job.arrival_time
            )
            waiting_time = (
                turnaround_time - job.burst_time
            )

            results.append({
                "job_id": job.job_id,
                "start_time": first_start_time[job.job_id],
                "completion_time": completion_time,
                "turnaround_time": turnaround_time,
                "waiting_time": waiting_time,
            })

    return results