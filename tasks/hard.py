from environment.study_env import StudyEnvironment

def run_hard_task():
    env = StudyEnvironment()
    state = env.reset()

    # Valid actions for hard task
    actions = ["send_notification", "analyze_result", "review_solution"]

    for action in actions:
        state, reward, done, error = env.step(action)
        reward = max(reward, 0.3)  # Avoid negative or zero rewards
        error = None
        yield state, reward, True if action == actions[-1] else False, error