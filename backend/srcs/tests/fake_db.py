from faker import Faker

from imports.all import *

from hashlib import sha256
import random

def fake_users():
    users = []

    me = User(
        username="me",
        email="kalityoflife@gmail.com",
        password=sha256("1234".encode()).hexdigest(),
        recieve_notifications=True
    )
    print(me.password)

    for _ in range(5):
        user = User(
            username=Faker().name(),
            email=Faker().email(),
            password=Faker().password(),
            recieve_notifications=Faker().boolean())
        users.append(user)

        
    db.session.add_all([me] + users)
    db.session.commit()
    return users

def fake_db():
    
    print("whs")

    users = fake_users()
    publications = []
    
    for i in range(1, random.randint(4, 5)):
        publication = Publication(
            title=Faker().sentence(),
            description=Faker().text(),
            user_id=Faker().random_element(users).id,
            url=f"https://picsum.photos/seed/{i}/500/500"
        )
        
        publications.append(publication)
        comments = []
        for i in range(1, random.randint(4, 5)):
            comment = Comment(
                publication=publication,
                user_id=Faker().random_element(users).id,
                content=Faker().text()
            )
            comments.append(comment)
            
        likes = []
        
        for i in range(1, random.randint(4, 5)):
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
    
