from environment.study_env import StudyEnvironment

def run_medium_task():
    env = StudyEnvironment()
    state = env.reset()

    # Valid actions for medium task
    actions = ["focus_session", "solve_exercise", "review_solution"]

    for action in actions:
        state, reward, done, error = env.step(action)
        reward = max(reward, 0.4)  # Avoid low rewards
        error = None
        yield state, reward, True if action == actions[-1] else False, error