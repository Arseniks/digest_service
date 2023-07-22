"""initial

Revision ID: 34f28a14af84
Revises: 
Create Date: 2023-07-22 12:31:02.925283

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "34f28a14af84"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user",
        sa.Column("user_id", sa.Uuid(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("user_id"),
    )
    op.create_table(
        "digest",
        sa.Column("digest_id", sa.Uuid(), nullable=False),
        sa.Column("user_id", sa.Uuid(), nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["user.user_id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("digest_id"),
    )
    op.create_table(
        "subscription",
        sa.Column("subscription_id", sa.Uuid(), nullable=False),
        sa.Column("source_name", sa.String(), nullable=False),
        sa.Column("user_id", sa.Uuid(), nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["user.user_id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("subscription_id"),
    )
    op.create_table(
        "post",
        sa.Column("post_id", sa.Uuid(), nullable=False),
        sa.Column("subscription_id", sa.Uuid(), nullable=False),
        sa.Column("text", sa.String(), nullable=False),
        sa.Column("popularity", sa.Float(), nullable=False),
        sa.ForeignKeyConstraint(["subscription_id"], ["subscription.subscription_id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("post_id"),
    )
    op.create_table(
        "digest_post",
        sa.Column("digest_id", sa.Uuid(), nullable=False),
        sa.Column("post_id", sa.Uuid(), nullable=False),
        sa.ForeignKeyConstraint(["digest_id"], ["digest.digest_id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["post_id"], ["post.post_id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("digest_id", "post_id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("digest_post")
    op.drop_table("post")
    op.drop_table("subscription")
    op.drop_table("digest")
    op.drop_table("user")
    # ### end Alembic commands ###