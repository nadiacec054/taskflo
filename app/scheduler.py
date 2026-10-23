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
