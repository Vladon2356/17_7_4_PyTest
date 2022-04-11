import pytest
from app.models import UserModel

# Methods
def test_find_by_id(app):
    user = UserModel.find_by_id(id=1,to_dict=False)
    assert user.name == user1.name
    assert user.age == user1.age
    assert user.email == user1.email
    assert user.username == user1.username
    assert user.hashed_password == user1.hashed_password

def test_find_by_not_exist_id(app):
    user = UserModel.find_by_id(id=999)
    assert user == {}

def test_find_by_username(app):
    user = UserModel.find_by_username(username='Ann18',to_dict=False)
    assert user.name == user3.name
    assert user.age == user3.age
    assert user.email == user3.email
    assert user.username == user3.username
    assert user.hashed_password == user3.hashed_password


def test_find_by_not_exist_username(app):
    user = UserModel.find_by_username(username='something',to_dict=False)
    assert user == {}


def test_find_by_email(app):
    user = UserModel.find_by_username(email='Jack@gmail.com',to_dict=False)
    assert user.name == user2.name
    assert user.age == user2.age
    assert user.email == user2.email
    assert user.username == user2.username
    assert user.hashed_password == user2.hashed_password


def test_find_by_not_exist_email(app):
    user = UserModel.find_by_username(email='XXX@xxx.com',to_dict=False)
    assert user == {}

def test_return_all(app):
    users = UserModel.return_all(to_dict=False)
    assert len(user) >= 1


def test_delete_by_id(app):
    deleted_user = UserModel.find_by_id(4, to_dict=False)
    code = UserModel.delete_by_id(4)
    users = UserModel.return_all(to_dict=False)
    assert code == 200
    assert deleted_user not in users

def test_delete_by_not_exist_id(app):
    code = UserModel.delete_by_id(999)
    assert code == 404


def test_to_dict(app):
    res = UserModel.to_dict(user1)
    assert res['id'] == 1
    assert res['name'] == 'Jone'
    assert res['hashed_password'] == user1.hashed_password
    assert res['username'] == 'Jone22'
    assert res['email'] == 'Jone@gmail.com'
    assert res['is_admin'] == False
    assert res['is_writer'] == False
