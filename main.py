from tasks.easy import run_easy_task
from tasks.medium import run_medium_task
from tasks.hard import run_hard_task

def calculate_total_score(task_results):
    """
    task_results: list of tuples like (state_dict, score, completed, extra)
    Returns total score as float
    """
    return sum(item[1] for item in task_results)

def main():
    print("🚀 Running Tasks...\n")

    # Run Easy Tasks
    easy_results = run_easy_task()
    easy_total = calculate_total_score(easy_results)
    print("💡 Easy Task Results:")
    for i, (state, score, completed, extra) in enumerate(easy_results, 1):
        print(f"  Task {i}: Score={score}, Completed={completed}")
    print(f"➡️ Easy Task Total Score: {easy_total}\n")

    # Run Medium Tasks
    medium_results = run_medium_task()
    medium_total = calculate_total_score(medium_results)
    print("⚡ Medium Task Results:")
    for i, (state, score, completed, extra) in enumerate(medium_results, 1):
        print(f"  Task {i}: Score={score}, Completed={completed}")
    print(f"➡️ Medium Task Total Score: {medium_total}\n")

    # Run Hard Tasks
    hard_results = run_hard_task()
    hard_total = calculate_total_score(hard_results)
    print("🔥 Hard Task Results:")
    for i, (state, score, completed, extra) in enumerate(hard_results, 1):
        print(f"  Task {i}: Score={score}, Completed={completed}")
    print(f"➡️ Hard Task Total Score: {hard_total}\n")

    # Overall Score
    overall_score = easy_total + medium_total + hard_total
    print(f"🏆 Overall Score: {overall_score}")

if __name__ == "__main__":
    main()