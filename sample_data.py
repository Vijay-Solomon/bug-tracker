from app import create_app, db
from app.models import User, Ticket

app = create_app()

with app.app_context():
    # sample users
    if not User.query.filter_by(username='tester1').first():
        tester = User(username='tester1', role='Tester')
        tester.set_password('test123')
        db.session.add(tester)

    if not User.query.filter_by(username='dev1').first():
        dev = User(username='dev1', role='Developer')
        dev.set_password('dev123')
        db.session.add(dev)

    db.session.commit()

    # sample ticket
    if not Ticket.query.first():
        sample_ticket = Ticket(
            title="Sample bug: App crashes on login",
            description="If username empty, app crashes",
            priority="High",
            reporter_id=User.query.filter_by(username='tester1').first().id,
            assignee_id=User.query.filter_by(username='dev1').first().id
        )
        db.session.add(sample_ticket)
        db.session.commit()

    print("Sample users & ticket created!")
