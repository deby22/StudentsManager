from students_manager import db


class Repo:
    @staticmethod
    def all(model):
        return db.session.query(model).all()

    @staticmethod
    def get(model: object, id: str):
        return db.session.query(model).get(id)

    @staticmethod
    def save(model):
        db.session.add(model)
        db.session.commit()

    @staticmethod
    def delete(model: object, id):
        db.session.query(model).filter_by(id=id).delete()
        db.session.commit()
