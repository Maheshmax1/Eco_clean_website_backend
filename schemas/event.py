from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .registration import RegistrationWithUser

class EventBase(BaseModel):
    title: str
    description: str
    location: str
    event_date: str
    start_time: str
    end_time: str
    image_url: str
    status: str = "upcoming"

class EventCreate(EventBase):
    pass

class EventResponse(EventBase):
    id: int
    created_at: datetime
    is_registered: bool = False
    
    class Config:
        from_attributes = True

class EventWithRegistrations(EventResponse):
    registrations: List['RegistrationWithUser'] = []

