from flask import render_template, request, redirect

from flask_app import app
from flask_app.models.user import User


@app.route('/')
def index():
   users = User.get_all()
   print(users)
   return render_template('index.html', users = users)

@app.route('/user/add')
def add_user():
   return render_template('add_users.html')

@app.route('/process', methods=['POST'])
def create_user():
   print(request.form)
   User.save(request.form)
   return redirect('/')

@app.route('/user/edit/<int:id>')
def edit(id):
   data = {
   'id': id
   }
   return render_template('edit_users.html', user = User.get_one(data))

@app.route('/user/show/<int:id>')
def show(id):
   data = {
      'id': id
   }
   return render_template('show_users.html', user = User.get_one(data))

@app.route('/update', methods=['POST'])
def update():
   print(request.form)
   User.update(request.form)
   return redirect('/')

@app.route('/user/delete/<int:id>')
def delete(id):
   data = {
      'id': id
   }
   User.delete(data)
   return redirect('/')
