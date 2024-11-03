from app import app, db, socketio
from flask_migrate import Migrate

migrate = Migrate(app, db)

if __name__ == '__main__':
    socketio.run(app, debug=True)
