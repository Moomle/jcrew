CSRF_ENABLE = True
SECRET_KEY = 'jcrew-check-in-app'

import os
app_path = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(app_path, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(app_path, 'db_repository')