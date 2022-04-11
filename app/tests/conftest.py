import os
import pytest
import datetime
from app.main import create_app
from app.models import UserModel, PostModel
from config import TestingConfig

TEST_USERNAME = "TestUser"
TEST_PASSWORD = "test1234"
ADMIN_TEST_USERNAME = "TestAdmin"
ADMIN_TEST_PASSWORD = "admin123"

@pytest.fixture
def app():
    app = create_app(TestingConfig)

    return app


@pytest.fixture
def client(app):
    app.testing = True
    return app.test_client()


@pytest.fixture
def authentication_headers(client):
    def wrapper(is_admin: bool):
        username = ADMIN_TEST_USERNAME if is_admin else TEST_USERNAME
        password = ADMIN_TEST_PASSWORD if is_admin else TEST_PASSWORD

        response = client.post(
            '/auth/login',
            json={
                "username": username,
                "password": password
            }
        )

        if response.json['message'] == f"User {username} doesn't exist":
            response = client.post(
                '/auth/registration',
                json={
                    "name": username,
                    "age": 22,
                    "username": username,
                    "password": password,
                    "is_admin": is_admin
                }
            )
        auth_token = response.json['access_token']
        refresh_token = response.json['refresh_token']
        headers = {'Authorization': f'Bearer {auth_token}', 'refresh_token': refresh_token}

        return headers

    return wrapper

@pytest.fixture
def new_user_factory():
    def wrapper(name, username, age, email, hashed_password, is_admin=True, is_writer=True):
        new_user = UserModel(
            name=name,
            username=username,
            age=age,
            email=email,
            hashed_password=hashed_password,
            is_admin=is_admin,
            is_writer=is_writer,
        )
        return new_user

    return wrapper


@pytest.fixture
def new_post_factory():
    def wrapper(title, text, author_id):
        new_post = PostModel(
            title=title,
            text=text,
            author_id=author_id,
        )
        return new_post

    return wrapper


@pytest.fixture
def create_users(new_user_factory):
    user1 = new_user_factory(
        name='Jone',
        age=22,
        username='Jone22',
        hashed_password=UserModel.generate_hash('123'),
        email='Jone@gmail.com',
        is_admin=False,
        is_writer=False
    )
    user2 = new_user_factory(
        name='Jack',
        age=29,
        username='Jack228',
        hashed_password=UserModel.generate_hash('123'),
        email='Jack@gmail.com'
    )
    user3 = new_user_factory(
        name='Ann',
        age=18,
        username='Ann18',
        hashed_password=UserModel.generate_hash('123'),
        email='Ann@gmail.com'
    )
    return [user1, user2,user3]

@pytest.fixture
def create_posts(new_post_factory):
    post1 = new_post_factory(
        title='Post1',
        text='Test post text 1',
        author_id='1',
    )
    post2 = new_post_factory(
        title='Post2',
        text='Test post text 2',
        author_id='2',
    )
    post3 = new_post_factory(
        title='Post3',
        text='Test post text 3',
        author_id='3',
    )
    return [post1, post3,post3]