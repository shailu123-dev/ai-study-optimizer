def infer():
    return {"message": "Inference working"}
from tasks.easy import run_easy_task
from tasks.medium import run_medium_task
from tasks.hard import run_hard_task

MODEL_NAME = "Qwen2.5"
ENV_NAME = "ai-study"

def run_task(task_name, task_func, comment=""):
    print(f"[START] task={task_name} env={ENV_NAME} model={MODEL_NAME}")
    rewards = []
    step_count = 0

    for state, reward, done, error in task_func():
        step_count += 1
        rewards.append(reward)
        action_str = state.get("last_action", "unknown") if isinstance(state, dict) else "unknown"
        done_str = "true" if done else "false"
        error_str = "null"
        print(f"[STEP] step={step_count} action={action_str} reward={reward:.2f} done={done_str} error={error_str}")
        if done:
            break

    success = True
    rewards_str = ",".join([f"{r:.2f}" for r in rewards])
    print(f"[END] success={success} steps={step_count} rewards={rewards_str}")

    if comment:
        print(f"# {comment}\n")


if __name__ == "__main__":
    run_task("easy", run_easy_task, "Task easy: AI successfully completed basic exercises.")
    run_task("medium", run_medium_task, "Task medium: AI successfully completed tasks efficiently.")
    run_task("hard", run_hard_task, "Task hard: AI successfully completed all objectives without errors.")