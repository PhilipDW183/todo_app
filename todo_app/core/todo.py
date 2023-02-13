from core import app
from flask import render_template, url_for, redirect, request
from data.session_items import get_items, add_item, remove_item, update_item

base_route = "/todo"

@app.route(base_route)
def todo():
    items = get_items()
    return render_template("todo.html", items=items)


@app.route(f'{base_route}/create_new_task', methods=["POST"])
def create_new_task():
    new_item = request.form.get('todo')
    add_item(new_item)
    return redirect(url_for("todo"))

@app.route(f'{base_route}/doing_item/<id>')
def doing_item(id):
    update_item(id, "Doing")
    return redirect(url_for("todo"))

@app.route(f'{base_route}/to_do_item/<id>')
def to_do_item(id):
    update_item(id, "Not Started")
    return redirect(url_for("todo"))

@app.route(f'{base_route}/complete_item/<id>')
def complete_item(id):
    update_item(id, "Completed")
    return redirect(url_for("todo"))


@app.route(f'{base_route}/delete_item/<id>')
def delete_item(id):
    remove_item(id)
    return redirect(url_for("todo"))