from app import create_app, db
from app.models import User

app = create_app()

with app.app_context():
    db.create_all()

    # create admin user if not exists
    if not User.query.filter_by(username='admin').first():
        admin = User(username='admin', role='Admin')
        admin.set_password('adminpass')
        db.session.add(admin)
        db.session.commit()

    print("Database initialized. Admin user created (admin/adminpass)")
