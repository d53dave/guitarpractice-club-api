import logging
import pendulum

from fastapi import APIRouter, Request
from starlette.config import Config
from authlib.integrations.starlette_client import OAuth

from config import Settings

log = logging.getLogger(__name__)

router = APIRouter()

settings = Settings()
conf = Config(environ=settings.dict())
oauth = OAuth(conf)

oauth.register(name='google',
               server_metadata_url=settings.GOOGLE_CONF_URL,
               client_kwargs={'scope': 'openid email profile'})


@router.get('/signin')
async def login(request: Request):
    if request.session.get('user') is not None:
        return
    redirect_uri = settings.GOOGLE_REDIRECT_URL
    log.info('Preparing oauth with redirect_uri', redirect_uri)
    return await oauth.google.authorize_redirect(request, redirect_uri)


@router.get('/token')
async def auth(request: Request):
    token = await oauth.google.authorize_access_token(request)
    user = await oauth.google.parse_id_token(request, token)
    request.session['user'] = dict(user)


@router.post('/signout')
async def logout(request: Request):
    request.session.pop('user', None)


def _is_expired(unix_timestamp: str) -> bool:
    return pendulum.now('utc').subtract(
        hours=settings.TOKEN_TIMEOUT_HOURS) > pendulum.from_timestamp(
            int(unix_timestamp))


def expire_session(request: Request):
    if (user := request.session.get('user')) is not None:
        if (iat := user.get('iat')) is not None and _is_expired(iat):
            request.session.pop('user', None)
