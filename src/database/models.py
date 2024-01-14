import uuid
from sqlalchemy import String, Uuid, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class User(Base):
    def __init__(self, username: str, hash_password: bytes):
        self.username = username
        self.hash_password = hash_password

    __tablename__ = "users"
    id: Mapped[Uuid] = mapped_column(
        Uuid, name="id", primary_key=True, default=uuid.uuid4
    )
    username: Mapped[str] = mapped_column(String(50), name="username", unique=True)
    hash_password: Mapped[bytes] = mapped_column(
        String(255), name="hash_password", nullable=False
    )
    profile_id: Mapped[Uuid] = mapped_column(Uuid, name="profile_id", nullable=True)

    profile = relationship(
        "Profile",
        back_populates="user",
        primaryjoin="User.profile_id == Profile.id",
        foreign_keys=profile_id,
    )

    def __repr__(self) -> str:
        return f"user: {self.id} - {self.username}"


class Profile(Base):
    __tablename__ = "profiles"
    id: Mapped[Uuid] = mapped_column(
        Uuid, name="id", primary_key=True, default=uuid.uuid4
    )
    bio: Mapped[str] = mapped_column(Text, name="bio")
    address: Mapped[str] = mapped_column(String(250), name="address")
    gender: Mapped[str] = mapped_column(String(10), name="gender")

    user = relationship(
        "User",
        back_populates="profile",
        primaryjoin="Profile.id == User.profile_id",
        foreign_keys="User.profile_id",
    )

    def __repr__(self) -> str:
        return f"Profile: {self.id} - {self.bio}"
