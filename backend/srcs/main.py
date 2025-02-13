from imports.all import *
from tests.fake_db import fake_db
os.environ['PYTHONUNBUFFERED'] = "1"

if __name__ == '__main__':
    
    # if os.getenv("TEST") == "True":
    with app.app_context():
        db.drop_all()
        # db.session.execute("DROP SCHEMA public CASCADE;")
        # db.session.execute("CREATE SCHEMA public;")
        # db.session.commit()
        db.create_all()
        fake_db()

    app.run(debug=True, host="0.0.0.0")
    