from pydantic import BaseModel, Field
from typing import List, Optional, Dict
from enum import Enum

class ActionType(str, Enum):
    REPLY = "reply"
    ARCHIVE = "archive"
    DELETE = "delete"
    SCHEDULE = "schedule"

class Action(BaseModel):
    action_id: str
    action_type: ActionType
    payload: Optional[str] = None

class Observation(BaseModel):
    emails: List[Dict]
    calendar_slots: List[str]
    last_status: str

class Reward(BaseModel):
    value: float
    reason: str
