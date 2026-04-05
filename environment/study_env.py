# environment/study_env.py
import random

class StudyEnvironment:
    def __init__(self):
        self.focus_level = 50       # 0-100 scale
        self.energy_level = 50      # 0-100 scale
        self.blocked_apps = set()
        self.notifications_sent = 0
        self.steps_taken = 0
        self.max_steps_easy = 10
        self.max_steps_medium = 200
        self.max_steps_hard = 300

    def reset(self):
        self.focus_level = 50
        self.energy_level = 50
        self.blocked_apps.clear()
        self.notifications_sent = 0
        self.steps_taken = 0
        return self._get_state()

    def _get_state(self):
        return {
            "focus_level": self.focus_level,
            "energy_level": self.energy_level,
            "blocked_apps": list(self.blocked_apps),
            "notifications_sent": self.notifications_sent
        }

    def step(self, action):
        self.steps_taken += 1
        reward = 0.0
        done = False
        error = None

        try:
            if action == "motivational_message":
                reward = random.choice([0.2, 0.4, 0.7])
                self.focus_level += int(reward * 10)
            elif action == "suggest_break":
                reward = random.choice([0.1, 0.3, 0.4])
                self.energy_level += int(reward * 10)
            elif action == "send_notification":
                if self.notifications_sent < 5 and self.energy_level >= 30:
                    reward = random.choice([0.5, 0.7, -0.6])
                    self.notifications_sent += 1
                    self.focus_level += int(reward * 5)
                else:
                    reward = -0.6
            elif action == "block_app":
                if "Instagram" not in self.blocked_apps:
                    self.blocked_apps.add("Instagram")
                    reward = random.choice([0.8, 1.0, -0.3])
                    self.focus_level += int(reward * 5)
                else:
                    reward = -0.3
            else:
                reward = -0.2
                error = f"Unknown action '{action}'"
        except Exception as e:
            reward = -0.5
            error = str(e)

        # Clamp values
        self.focus_level = min(max(self.focus_level, 0), 100)
        self.energy_level = min(max(self.energy_level, 0), 100)

        # Determine done based on task type
        if self.steps_taken <= self.max_steps_easy:
            done = self.steps_taken >= self.max_steps_easy
        elif self.steps_taken <= self.max_steps_medium:
            done = self.focus_level >= 70 or self.steps_taken >= self.max_steps_medium
        else:
            done = self.focus_level >= 70 or self.steps_taken >= self.max_steps_hard

        return self._get_state(), reward, done, error