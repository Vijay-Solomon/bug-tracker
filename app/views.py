from flask import current_app as app
from flask import render_template, redirect, url_for, request, flash, send_file
from .models import User, Ticket
from .forms import LoginForm, RegisterForm, TicketForm
from . import db
from .utils import login_user, logout_user, current_user
import csv
import io


@app.route("/")
def index():
    user = current_user()
    return render_template("index.html", user=user)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if User.query.filter_by(username=form.username.data).first():
            flash("Username already exists", "danger")
        else:
            u = User(username=form.username.data, role=form.role.data)
            u.set_password(form.password.data)
            db.session.add(u)
            db.session.commit()
            flash("Registered successfully. Please login.", "success")
            return redirect(url_for("login"))
    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        u = User.query.filter_by(username=form.username.data).first()
        if u and u.check_password(form.password.data):
            login_user(u)
            flash("Logged in", "success")
            return redirect(url_for("index"))
        flash("Invalid credentials", "danger")
    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/tickets")
def tickets():
    q = request.args.get("q", "")
    status = request.args.get("status", "")
    priority = request.args.get("priority", "")

    query = Ticket.query

    if q:
        query = query.filter(Ticket.title.contains(q) | Ticket.description.contains(q))
    if status:
        query = query.filter_by(status=status)
    if priority:
        query = query.filter_by(priority=priority)

    all_tickets = query.order_by(Ticket.created_at.desc()).all()
    users = User.query.all()

    return render_template("tickets.html", tickets=all_tickets, users=users, q=q, status=status, priority=priority)


@app.route("/ticket/new", methods=["GET", "POST"])
def new_ticket():
    form = TicketForm()
    users = User.query.all()
    form.assignee.choices = [(0, "Unassigned")] + [(u.id, u.username) for u in users]

    if form.validate_on_submit():
        t = Ticket(
            title=form.title.data,
            description=form.description.data,
            priority=form.priority.data,
            assignee_id=form.assignee.data if form.assignee.data != 0 else None,
            reporter_id=current_user().id if current_user() else None,
        )
        db.session.add(t)
        db.session.commit()
        flash("Ticket created", "success")
        return redirect(url_for("tickets"))

    return render_template("new_ticket.html", form=form)


@app.route("/ticket/<int:ticket_id>", methods=["GET", "POST"])
def ticket_detail(ticket_id):
    t = Ticket.query.get_or_404(ticket_id)

    if request.method == "POST":
        action = request.form.get("action")

        if action == "status":
            t.status = request.form.get("status")

        elif action == "assign":
            aid = int(request.form.get("assignee", 0))
            t.assignee_id = aid if aid != 0 else None

        db.session.commit()
        flash("Updated", "success")

    users = User.query.all()
    return render_template("ticket_detail.html", ticket=t, users=users)


@app.route("/ticket/delete/<int:ticket_id>", methods=["POST"])
def ticket_delete(ticket_id):
    t = Ticket.query.get_or_404(ticket_id)
    db.session.delete(t)
    db.session.commit()
    flash("Ticket deleted", "info")
    return redirect(url_for("tickets"))


@app.route("/export")
def export_tickets():
    tickets = Ticket.query.all()
    si = io.StringIO()
    cw = csv.writer(si)
    cw.writerow(["id", "title", "status", "priority", "reporter", "assignee", "created_at"])

    for t in tickets:
        cw.writerow([
            t.id,
            t.title,
            t.status,
            t.priority,
            t.reporter.username if t.reporter else "",
            t.assignee.username if t.assignee else "",
            t.created_at.isoformat(),
        ])

    output = io.BytesIO()
    output.write(si.getvalue().encode("utf-8"))
    output.seek(0)
    return send_file(output, as_attachment=True, download_name="tickets.csv", mimetype="text/csv")
