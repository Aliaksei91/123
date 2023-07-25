from flask import Flask, request, jsonify
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, this is my first api'

@app.route('/user')
def usermain_page():
    return 'users main page'

@app.route('/user/<username>')
def show_user_page(username):
    return 'Hello ' + username.upper()

#можно создать влож пути
@app.route('/path/<path:subpath>')
def print_subpath(subpath):
    return 'Subpath is:  ' + subpath

# калькулятор квадрат
@app.route('/kvadrat/<int:x>')
def calc_kvadrat(x):
    return 'kvadrat ot ' + str(x) + '=' + str(x*x)


# калькулятор квадрат
@app.route('/htmlpage')
def show_html_page():
    myfile = open('week_2.html', mode='r')
    page = myfile.read()
    myfile.close()
    return page


@app.route('/help')
def helppage():
    return '<b>this is a help page</b>'


#---------------------------------------------------------------------
#в постмане добавить урл, и можно изменять вход. параметры
#args,form - места куда вводить данные в постамане, форм в бади
@app.route('/python_req_1', methods= ['GET'])
def python_req_1():
    name = request.args.get('name')
    age = request.args.get('age')
    salary = int(request.form.get('salary')) + 1000
    cat = request.form.get('cat')

    result = {
        'user_name': name,
        'user_age': age,
        'user_salary': salary,
        'user_cat': cat
    }
    return jsonify(result) # тут можно указать число, таким и будет статус код


@app.route('/python_req_2', methods= ['GET','POST'])
def python_req_2():

    if request.method == 'GET':
        model = request.args.get('model')
        title = request.args.get('title')

        price = int(request.form.get('price')) + 5000
        open_air = request.form.get('open_air')

        result = {
            'model': model,
            'title': title,
            'price': price,
            'open_air': open_air
        }
    elif request.method == 'POST':
        model = request.form.get('model')
        title = request.form.get('title')

        price = int(request.form.get('price')) + 11000
        open_air = request.form.get('open_air')

        result = {
            'model': model,
            'title': title,
            'price': price,
            'open_air': open_air
        }
    return jsonify(result)






#---------------------------------gift-------------------------------
gift_list ={'junior':['mac','coffe','fruits'],
            'middle':['junior+','gym','medical_ensurance_500'],
            'senior':['middle+','medical_ensurance-500','taxi', 'parking']}


@app.route('/get_pack', methods=['POST'])
def r_employee_pack():
     employee_level = request.json['employee_level']
     if employee_level in gift_list:
        pack_title = employee_level + ' _pack'
        employee_gift_pack = {pack_title: gift_list[employee_level]}




     return jsonify(employee_gift_pack)

#----------------------------------gift------------------------------------------------


if __name__ == '__main__':
    app.debug = True #не нужно перезапускать сервер после каждого изменения
    app.run()