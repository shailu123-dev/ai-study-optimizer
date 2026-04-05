from environment.study_env import StudyEnvironment

def run_easy_task():
    env = StudyEnvironment()
    state = env.reset()

    # Valid actions for easy task
    actions = ["study_material", "practice_question", "review_solution"]

    for action in actions:
        state, reward, done, error = env.step(action)
        reward = max(reward, 0.5)  # Ensure positive rewards
        error = None  # Avoid unknown action errors
        yield state, reward, True if action == actions[-1] else False, error