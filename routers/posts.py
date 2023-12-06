from typing import List

from httpx import post
from schemas import Post
from sqlalchemy.orm import Session
from fastapi import Query, Response, status, APIRouter, Depends, HTTPException
from database import get_db
import models
from oauth2 import get_current_user

router = APIRouter(prefix="/post", tags=["Posts"])


@router.get("/", response_model=List[Post])
async def get_posts(
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user),
    limit=Query(default=30, ge=10, le=100, alias="page_size"),
):
    posts = db.query(models.Post).where(models.Post.owner_id == user_id).all()
    return posts


@router.post(path="/", status_code=status.HTTP_201_CREATED)
def create_post(
    payload: Post,
    db: Session = Depends(get_db),
    get_current_user: int = Depends(get_current_user),
):
    new_post = models.Post(owner_id=get_current_user, **payload.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.get(
    "/{id}",
    response_model=Post,
)
async def get_post(
    id: int,
    db: Session = Depends(get_db),
    get_current_user: int = Depends(get_current_user),
):
    post = db.query(models.Post).where(models.Post.id == id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} was not found",
        )

    return post


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(
    id: int,
    db: Session = Depends(get_db),
    current_user_id: int = Depends(get_current_user),
):
    post = db.query(models.Post).where(models.Post.id == id)
    if not post.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} was not found",
        )
    if post.first().owner_id != current_user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to perform requested action",
        )
    post.delete(synchronize_session=False)
    db.commit()
    return Response(
        status_code=status.HTTP_204_NO_CONTENT,
    )
