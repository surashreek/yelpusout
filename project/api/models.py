import datetime

from project import db


# class User(db.Model):
#     __tablename__ = "users"
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     username = db.Column(db.String(128), nullable=False)
#     email = db.Column(db.String(128), nullable=False)
#     active = db.Column(db.Boolean(), default=False, nullable=False)
#     created_at = db.Column(db.DateTime, nullable=False)

#     def __init__(self, username, email):
#         self.username = username
#         self.email = email
#         self.created_at = datetime.datetime.utcnow()

class Group(db.Model):
    __tablename__ = "group"
    group_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    group_name = db.Column(db.String(50), nullable=False)
    member_count = db.Column(db.Integer, default=0)
    create_date = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    update_date = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, group_name):
        self.group_name = group_name