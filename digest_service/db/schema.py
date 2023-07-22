import uuid
from typing import List
from uuid import UUID

from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

from digest_service.db.base import Base

digest_post = Table(
    "digest_post",
    Base.metadata,
    Column("digest_id", ForeignKey("digest.digest_id"), primary_key=True),
    Column("post_id", ForeignKey("post.post_id"), primary_key=True),
)


class User(Base):
    __tablename__ = "user"

    user_id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(nullable=False)
    subscription_id: Mapped[UUID] = mapped_column(ForeignKey("subscription.subscription_id"))
    digest_id: Mapped[UUID] = mapped_column(ForeignKey("digest.digest_id"))


class Subscription(Base):
    __tablename__ = "subscription"

    subscription_id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(nullable=False)
    user: Mapped[List["User"]] = relationship()
    post_id: Mapped[UUID] = mapped_column(ForeignKey("post.post_id"))


class Post(Base):
    __tablename__ = "post"

    post_id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    subscription: Mapped[List["Subscription"]] = relationship()
    text: Mapped[str] = mapped_column(nullable=False)
    popularity: Mapped[float] = mapped_column()


class Digest(Base):
    __tablename__ = "digest"

    digest_id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    posts: Mapped[List["Post"]] = relationship(secondary=digest_post)
    user: Mapped[List["User"]] = relationship()
