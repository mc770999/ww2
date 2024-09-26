from sqlalchemy import Integer
from sqlalchemy.exc import SQLAlchemyError
from returns.maybe import Maybe
from config.base import session_factory
from models import Target
from typing import List
from returns.result import Success, Failure


def create_target(target: Target):
    try:
        with session_factory() as  session:
            session.add(target)
            session.commit()
            session.refresh(target)
    except SQLAlchemyError as e:
        print("create_target failed", str(e))

def update_target(t_id : int, new_target : Target):
    try:
        with session_factory() as session:
            target =  find_target_by_id(t_id).map(session.merge).value_or(0)
            if target:
                target.target_priority = new_target.target_priority
                target.target_type_id = new_target.target_type_id
                target.city_id = new_target.city_id
                target.target_industry = new_target.target_industry
            session.commit()
            session.refresh(new_target)
    except SQLAlchemyError as e:
        print("update_target failed", str(e))

def delete_target(t_id):
    try:
        with session_factory() as session:
            target = session.get(Target, t_id)
            if target:
                session.delete(target)
                session.commit()
                return Success(target)
            else:
                Failure(target)
    except SQLAlchemyError as e:
        print("delete_target failed", str(e))

def get_all_target():
    try:
        with session_factory() as session:
            return Maybe.from_optional(session.query(Target).all())
    except SQLAlchemyError as e:
        print("get_all_target failed", str(e))



def find_target_by_id(t_id: int) -> Maybe[Target]:
    with session_factory() as session:
        return Maybe.from_optional(session.get(Target, t_id))

