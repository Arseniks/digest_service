from __future__ import annotations

import uuid
from typing import List
from uuid import UUID

from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

from digest_service.db.base import Base

digest_post = Table(
    "digest_post",
    Base.metadata,
    Column("digest_id", ForeignKey("digest.digest_id", ondelete="CASCADE"), primary_key=True),
    Column("post_id", ForeignKey("post.post_id", ondelete="CASCADE"), primary_key=True),
)


class User(Base):
    __tablename__ = "user"

    user_id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(nullable=False)
    subscription: Mapped[List[Subscription]] = relationship()
    digest: Mapped[List[Digest]] = relationship()


class Subscription(Base):
    __tablename__ = "subscription"

    subscription_id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    source_name: Mapped[str] = mapped_column(nullable=False)
    user_id: Mapped[UUID] = mapped_column(ForeignKey("user.user_id", ondelete="CASCADE"))
    post: Mapped[List[Post]] = relationship()


class Post(Base):
    __tablename__ = "post"

    post_id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    subscription_id: Mapped[UUID] = mapped_column(ForeignKey("subscription.subscription_id", ondelete="CASCADE"))
    text: Mapped[str] = mapped_column(nullable=False)
    popularity: Mapped[float] = mapped_column()


class Digest(Base):
    __tablename__ = "digest"

    digest_id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    posts: Mapped[List[Post]] = relationship(secondary=digest_post)
    user_id: Mapped[UUID] = mapped_column(ForeignKey("user.user_id", ondelete="CASCADE"))
