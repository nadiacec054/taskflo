
from app.scheduler import (
    fcfs,
    sjf,
    priority_scheduling,
    round_robin,
    calculate_metrics,
)


def compare_algorithms(jobs, time_quantum=2):
    algorithms = {
        "FCFS": lambda: fcfs(jobs),
        "SJF": lambda: sjf(jobs),
        "Priority": lambda: priority_scheduling(jobs),
        "Round Robin": lambda: round_robin(
            jobs, time_quantum
        ),
    }

    comparison = {}

    for name, run_algorithm in algorithms.items():
        results = run_algorithm()
        metrics = calculate_metrics(results)
        comparison[name] = metrics

    return comparison


def find_best_algorithms(comparison):
    if not comparison:
        raise ValueError("Comparison results cannot be empty")

    best_waiting = min(
        comparison,
        key=lambda name: comparison[name]["average_waiting_time"]
    )

    best_turnaround = min(
        comparison,
        key=lambda name: comparison[name]["average_turnaround_time"]
    )

    return {
        "best_average_waiting_time": best_waiting,
        "best_average_turnaround_time": best_turnaround,
    }

