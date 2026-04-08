from .models import Action, Observation, Reward

class OfficeEnv:
    def __init__(self):
        self.done = False

    def reset(self) -> Observation:
        self.done = False
        return Observation(
            emails=[{"id": "1", "subject": "Spam Offer"}],
            message="Environment reset"
        )

    def state(self) -> Observation:
        return Observation(
            emails=[{"id": "1", "subject": "Spam Offer"}],
            message="Running"
        )

    def step(self, action: Action):
        self.done = True

        return (
            self.state(),
            Reward(value=1.0, reason="Task completed"),
            self.done,
            {}
        )