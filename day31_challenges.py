# Study Tracker System
tasks = []
for i in range(3):
    study_task = input("Enter your task: ")
    tasks.append(study_task)
print("Your Tasks:", tasks)
print("Last Task:", tasks[-1])
print("Total Tasks:", len(tasks))
if tasks[1] == "revision":
    tasks[1] = "practice question"
    print("Updated Tasks:", tasks)