from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings


# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"] # everything is allowed
#origins = ["https://www.google.com"]

app.add_middleware(
    CORSMiddleware,             #function that runs before every request
    allow_origins=origins,      #what domains should be abel to talk to our API
    allow_credentials=True,     #
    allow_methods=["*"],        #allow specifik http methods vb only allow GET request, not POST, DELETE ...
    allow_headers=["*"],        #specific headers
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return {"message": "from the dark side"}