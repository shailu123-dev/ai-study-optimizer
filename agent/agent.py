# agent/agent.py

import random

class StudyAgent:
    def __init__(self, name="AI Student"):
        self.name = name
        self.actions_taken = []
        self.rewards = []

    def choose_action(self, state):
        """
        Decide which action to take based on the current state.
        Replace random choice with smarter logic if needed.
        """
        # Define possible actions
        actions = [
            "send_notification('Study now')",
            "suggest_break(5)",
            "block_app('Instagram')",
            "motivational_message('Keep going!')"
        ]
        action = random.choice(actions)
        return action

    def update(self, action, reward):
        """
        Update agent memory after taking an action.
        """
        self.actions_taken.append(action)
        self.rewards.append(reward)