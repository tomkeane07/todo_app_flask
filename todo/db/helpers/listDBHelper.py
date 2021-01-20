from ..schemas import db


class List(db.Model):
    __tablename__ = 'lists'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    title = db.Column(db.String(100), nullable=False)

def seed_list(user_id, title):
    list = List(user_id=user_id, title=title)
    db.session.add(list)
    db.session.commit()

def remove_list(list_id):
    db.session.delete(List).where(list_id==list_id)