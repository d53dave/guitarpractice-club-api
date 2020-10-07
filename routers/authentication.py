import logging

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


@router.post('/signin')
async def login(request: Request):
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