from database.db import SessionLocal
from database.models import User
import random


def create_user(data):

    db = SessionLocal()

    ref = f"DNE-{random.randint(1000,9999)}"

    user = User(
        reference_id=ref,
        name=data["name"],
        role=data["role"],
        city=data["city"],
        status="PENDING"
    )

    db.add(user)
    db.commit()

    return user

from database.db import SessionLocal
from database.models import User


def get_pending_users():

    db = SessionLocal()

    users = db.query(User).filter(User.status == "PENDING").all()

    result = []

    for u in users:
        result.append({
            "id": u.id,
            "name": u.name,
            "reference_id": u.reference_id
        })

    db.close()

    return result

def get_status(reference_id):

    # Dummy response for testing

    return {
        "reference_id": reference_id,
        "status": "PENDING_ADMIN_APPROVAL"
    }