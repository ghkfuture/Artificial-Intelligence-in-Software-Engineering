"""
SQLAlchemy ORM Refactored Implementation
Replaces procedural mysql.connector code with an object-oriented SQLAlchemy model.
"""

from datetime import datetime
from typing import Optional, List
from sqlalchemy import create_engine, String, DateTime, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from sqlalchemy.exc import SQLAlchemyError

# 1. Base Class Definition
class Base(DeclarativeBase):
    pass

# 2. Declarative User Model
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False, index=True)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}')>"

# 3. Engine & Session Setup
DATABASE_URL = "mysql+pymysql://root:yourpassword@localhost/example_db"
engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)

def init_db():
    """Create tables if they do not exist."""
    Base.metadata.create_all(engine)

# 4. Refactored CRUD Functions Using ORM
def create_user(username: str, email: str) -> Optional[User]:
    """Create a new user safely using ORM session."""
    if not username or not email:
        print("Username and email are required.")
        return None

    with SessionLocal() as session:
        try:
            new_user = User(username=username, email=email)
            session.add(new_user)
            session.commit()
            session.refresh(new_user)
            print(f"User '{username}' created successfully with ID {new_user.id}.")
            return new_user
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error creating user: {e}")
            return None

def get_user_by_username(username: str) -> Optional[User]:
    """Retrieve a user by username."""
    with SessionLocal() as session:
        stmt = select(User).where(User.username == username)
        return session.scalar(stmt)

def update_user_email(username: str, new_email: str) -> bool:
    """Update a user's email address."""
    with SessionLocal() as session:
        try:
            stmt = select(User).where(User.username == username)
            user = session.scalar(stmt)
            if user:
                user.email = new_email
                session.commit()
                print(f"Updated email for '{username}'.")
                return True
            print(f"User '{username}' not found.")
            return False
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error updating email: {e}")
            return False

def delete_user(username: str) -> bool:
    """Delete a user by username."""
    with SessionLocal() as session:
        try:
            stmt = select(User).where(User.username == username)
            user = session.scalar(stmt)
            if user:
                session.delete(user)
                session.commit()
                print(f"User '{username}' deleted successfully.")
                return True
            print(f"User '{username}' not found.")
            return False
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error deleting user: {e}")
            return False

def list_users() -> List[User]:
    """Retrieve all users."""
    with SessionLocal() as session:
        stmt = select(User)
        return list(session.scalars(stmt).all())

if __name__ == "__main__":
    init_db()
