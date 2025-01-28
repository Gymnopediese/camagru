
from faker import Faker

from __import__ import *


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
    db.session.add_all(users)
    db.session.commit()
    return users

def fake_db():
    
    print("whs")

    users = fake_users()
    posts = []
    
    for i in range(100, random.randint(100, 200)):
        post = Post(
            title=Faker().sentence(),
            description=Faker().text(),
            user_id=Faker().random_element(users).id,
            url=f"https://picsum.photos/seed/{i}/500/500"
        )
        
        posts.append(post)
        comments = []
        for i in range(5, random.randint(10, 50)):
            comment = Comment(
                post=post,
                user_id=Faker().random_element(users).id,
                content=Faker().text()
            )
            comments.append(comment)
            
        likes = []
        
        for i in range(3, random.randint(5, 70)):
            like = Like(
                post=post,
                user_id=Faker().random_element(users).id,
                dislike=Faker().boolean()
            )
            likes.append(like)
        
        db.session.add_all(likes)
        post.likes = likes
        
        db.session.add_all(comments)
        post.comments = comments
        

    
    db.session.add_all(posts)
    db.session.commit()
    
    
    
    
    