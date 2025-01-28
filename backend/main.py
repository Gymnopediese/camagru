from app import app, db, socketio
# from routes.__imports__ import *
# from tests.database import fake_db
import os

os.environ['PYTHONUNBUFFERED'] = "1"

if __name__ == '__main__':
    
    if os.getenv("TEST") == "True":
        with app.app_context():
            db.drop_all()
            # db.session.execute("DROP SCHEMA public CASCADE;")
            # db.session.execute("CREATE SCHEMA public;")
            # db.session.commit()
            db.create_all()
            # fake_db()
    
    app.run(debug=True, host="0.0.0.0", allow_unsafe_werkzeug=True)
    