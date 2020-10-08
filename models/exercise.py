from enum import Enum
from pydantic import BaseModel


class Difficulty(str, Enum):
    absolute_beginner = 'absolute_beginner'
    beginner = 'beginner'
    intermediate = 'intermediate'
    advanced = 'advanced'


class Exercise(BaseModel):
    name: str
    description: str
    difficulty: Difficulty
