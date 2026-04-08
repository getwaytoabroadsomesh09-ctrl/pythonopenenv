from pydantic import BaseModel
from typing import List, Dict, Optional

class Action(BaseModel):
    action_type: str
    email_id: Optional[str] = None

class Observation(BaseModel):
    emails: List[Dict]
    message: str

class Reward(BaseModel):
    value: float
    reason: str