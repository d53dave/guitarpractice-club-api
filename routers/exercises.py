import logging
from models.exercise import Difficulty, Exercise

from fastapi import APIRouter

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get('/')
async def test() -> Exercise:
    return Exercise(name='Minor Pentatonic',
                    description='5-8,5-7,5-7,5-7,5-8,5-8',
                    difficulty=Difficulty.absolute_beginner)
