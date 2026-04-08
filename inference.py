from src.environment import OfficeEnv
from src.models import Action

env = OfficeEnv()

obs = env.reset()
print("RESET SUCCESS:", obs)

action = Action(action_type="archive", email_id="1")

obs, reward, done, info = env.step(action)

print("STEP SUCCESS:", obs)
print("REWARD:", reward)