from fastapi import FastAPI
from routers import users, posts, auth
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="HieuBui",
    description="Learning FastApi",
    version="0.0.1",
)


origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=[],
    allow_methods=["*"],
    allow_headers=["*"],
)
# models.Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(posts.router)
app.include_router(auth.router)
