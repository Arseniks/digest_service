import uuid

from sqlalchemy import Column, Float, ForeignKey, String, Table, UUID
from sqlalchemy.orm import backref, relationship

from digest_service.db.base import Base

digest_post = Table(
    "digest_post",
    Base.metadata,
    Column("digest_id", ForeignKey("digest.digest_id")),
    Column("post_id", ForeignKey("post.post_id")),
)


class User(Base):
    __tablename__ = "user"

    user_id = Column("user_id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column("name", String, nullable=False)


class Subscription(Base):
    __tablename__ = "subscription"

    subscription_id = Column("subscription_id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column("name", String, nullable=False)
    user = Column("user", UUID(as_uuid=True), ForeignKey("user.user_id"), nullable=False)


class Post(Base):
    __tablename__ = "post"

    post_id = Column("post_id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    subscription = Column("subscription", UUID(as_uuid=True), ForeignKey("subscription.subscription_id"), nullable=False)
    text = Column("text", String, nullable=False)
    popularity = Column("popularity", Float, default=False)


class Digest(Base):
    __tablename__ = "digest"

    digest_id = Column("digest_id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    posts = relationship("Post", secondary=digest_post, backref=backref("post_digest", lazy="dynamic"), lazy="subquery")
    user = Column("user", UUID(as_uuid=True), ForeignKey("user.user_id"), nullable=False)
