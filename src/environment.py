import pydantic
from .models import Action, Observation, Reward

class OfficeEnv:
    def __init__(self):
        self.tasks = {
            "easy": {"id": "t1", "desc": "Archive 1 spam email"},
            "medium": {"id": "t2", "desc": "Reply to manager's request"},
            "hard": {"id": "t3", "desc": "Resolve schedule conflict"}
        }
        self.reset()

    def reset(self) -> Observation:
        self.step_count = 0
        return self.state()

    def state(self) -> Observation:
        return Observation(
            emails=[{"id": "e1", "from": "SpamBot", "subject": "Win Cash"}],
            calendar_slots=["10AM-11AM"],
            last_status="System Ready"
        )

    def step(self, action: Action) -> tuple[Observation, Reward, bool, dict]:
        self.step_count += 1
        
        # Meaningful Reward: Incremental Progress
        if action.action_type == "archive" and action.action_id == "e1":
            reward = Reward(value=1.0, reason="Successfully archived spam.")
            done = True
        else:
            reward = Reward(value=-0.1, reason="Inefficient action.")
            done = self.step_count >= 5 # Penalize infinite loops
            
        return self.state(), reward, done, {}
