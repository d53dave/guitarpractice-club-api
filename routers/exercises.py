import logging
from models.exercise import Difficulty, Exercise

from fastapi import APIRouter, Request

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get('/')
async def test(request: Request) -> Exercise:
    return Exercise(
        name=f'Minor Pentatonic user=[{request.session.get("user")}]',
        description='5-8,5-7,5-7,5-7,5-8,5-8',
        difficulty=Difficulty.absolute_beginner)
