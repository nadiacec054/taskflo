# taskflo
reliable asynchronous job scheduling system


trying to create a software that can make use of different os scheduling algorithms to perform tasks and optimise the output produced by a system.

IDEA is to implement os scheduling algos such as 
* fcfc
* sjf
* round robin
* priority queues


try to understand the use of these algorithms and implement it using data structures to create a method of scheduling tasks that is optimal and aligns with the needs of the user, i.e. they can choose which type of scheduling they prefer for their tasks

workflow in simple terms---
allow the user to input "jobs" as a class in python, which gives insight of the task, resources required for it, approximate time needed to complete the task
a list of jobs can be entered by the user
a preferred scheduling algorithm can be entered based on preference
algorithm is run and scheduling of tasks is done to optimise the use of resources and efficiency is ensured as well.
the user can also mention if their tasks should follow preemptive or non preemptive scheduling

tech stack -
python- backend
html,css- frontend 
javascript- interactivity 
postGREsql- database management

extra implementation
* create a report on how all resources were used optimally and a comparison of normal scheduling vs scheduling performed by the software to provide insights to user.

Performance Analysis

The system will compare scheduling algorithms using metrics such as:
Average waiting time
Average turnaround time
Response time
CPU utilisation
Throughput
Resource usage

