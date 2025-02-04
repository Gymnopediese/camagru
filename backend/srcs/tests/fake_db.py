
from faker import Faker

from imports.all import *

from hashlib import sha256
import random

def fake_users():
    users = []

    for _ in range(100):
        user = User(
            username=Faker().name(),
            mail=Faker().email(),
            password=Faker().password(),
            recieve_notifications=Faker().boolean())
        users.append(user)
    me = User(
        username="me",
        mail="kalityoflife@gmail.com",
        password=sha256("1234".encode()).hexdigest(),
        recieve_notifications=True
    )
    moi = User(
        username="moi",
        mail="camagru00@gmail.com",
        password=sha256("1234".encode()).hexdigest(),
        recieve_notifications=True
    )

    db.session.add_all(users + [me, moi])
    db.session.commit()
    return users

def fake_db():

    print("whs")

    users = fake_users()
    publications = []

    for i in range(100, random.randint(100, 200)):
        publication = Publication(
            title=Faker().sentence(),
            description=Faker().text(),
            user_id=Faker().random_element(users).id,
            url=f"https://picsum.photos/seed/{i}/500/500"
        )

        publications.append(publication)
        comments = []
        for i in range(5, random.randint(10, 50)):
            comment = Comment(
                publication=publication,
                user_id=Faker().random_element(users).id,
                content=Faker().text()
            )
            comments.append(comment)

        likes = []

        for i in range(3, random.randint(5, 70)):
            like = Like(
                publication=publication,
                user_id=Faker().random_element(users).id,
                dislike=Faker().boolean()
            )
            likes.append(like)

        db.session.add_all(likes)
        publication.likes = likes

        db.session.add_all(comments)
        publication.comments = comments



    db.session.add_all(publications)
    db.session.commit()
