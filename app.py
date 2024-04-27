from flask import Flask, render_template, url_for, request, redirect, json, jsonify
import sqlite3

# from sql_logic import check_sql, select_all_shops, create_clients, select_all_for_main, sql_check_phone, sql_all_from_clients, select_all_clients, sql_creat_shop



app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
# @app.route("/")
def index():
    # check_sql()
    # if request.is_json:
    #     seconds = time()
    #     return jsonify({'seconds': seconds})
    #
    # return render_template('index.html')
    # if request.method == 'POST':
    #     response_data = request.form['btn_check_phone']
    #     if response_data == 'Проверить':
    #         chars = "() -"
    #         phone = request.form['phone']# .translate(str.maketrans('', '', chars))
    #         checked_phone = sql_check_phone(phone)
    #         if checked_phone == []:
    #             print(f"Нет такого номера {checked_phone}")
    #             all_clients = select_all_for_main()
    #             return render_template("index.html", all_clients=all_clients, phone=phone)
    #         else:
    #             cache = checked_phone[0]
    #             id_client = cache[0]
    #             name = cache[1]
    #             number = cache[2]
    #             all_clients = sql_all_from_clients(id_client)
    #             print(f"Телефон {number} привязан за {name}")
    #             return render_template("index.html", all_clients=all_clients, phone=number, name=name)
    #         markers = request.form.getlist("check_phone")
    #         all_client = select_all_for_main()
    #         return render_template("index.html", all_clients=all_client)
    #     if response_data == 'Отправить':
    #
    #
    #         phone = request.form['phone']
    #         name = request.form['name']
    #         price_name = request.form['price_name']
    #         price = request.form['price']
    #         comment = request.form['comment']
    #
    #         cache_check = sql_check_phone(phone)
    #         if cache_check == []:
    #             id_client = create_clients(name, phone)
    #             sql_creat_shop(id_client, price_name, price, comment)
    #         else:
    #             id_client_cache = cache_check[0]
    #             id_client = id_client_cache[0]
    #             sql_creat_shop(id_client, price_name, price, comment)
    #         # print('send')
    #         all_clients = select_all_for_main()
    #         return render_template("index.html", all_clients=all_clients)
    # else:
        # all_clients = select_all_for_main()
    return render_template("index.html") #, all_clients=all_clients)


# @app.route('/get_len', methods=['GET', 'POST'])
# def get_len():
#     name = request.form['phone']
#     return json.dumps({'len': len(name)})


@app.route('/cart')
def cart():
    return render_template("cart.html")


@app.route('/fix')
def fix():
    return render_template("fix.html")


@app.route('/copy')
def copy():
    return render_template("copy.html")


@app.route('/actions')
def actions():
    return render_template("actions.html")


@app.route('/delivery')
def delivery():
    return render_template("delivery.html")


@app.route('/contacts')
def contacts():
    return render_template("contacts.html")


@app.route('/about')
def about():
    lst = []
    conn = sqlite3.connect('base.db')
    try:
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM shop")
        lst = cur.fetchall()
        print(lst)
    except sqlite3.Error as e:
        print("Ошибка получения статей из БД " + str(e))

    #return "About"
    return render_template("about.html", title='Список статей', lst=lst)


# @app.route('/create_client', methods=['POST', 'GET'])
# def create_client():
#     if request.method == 'POST':
#         print(request)
#         fio = request.form['name']
#         phone = request.form['phone']
#         all_phones = sql_check_phone(phone)
#         all_clients = select_all_clients()
#         if all_phones == []:
#             create_clients(fio, phone)
#             print(fio)
#             return render_template('create_client.html', clients=all_clients, fio=fio)
#         else:
#             all_phones = all_phones[0]
#             has_already = f"Клиент с номером {all_phones[2]} уже есть в базе под именем {all_phones[1]}"
#             return render_template('create_client.html', clients=all_clients, has_already=has_already)
#     else:
#         all_clients = select_all_clients()
#         return render_template('create_client.html', clients=all_clients)



# @app.route('/user/<string:name>/<int:id>') # для изминения урла
# def user(name, id):
#     #return f"User {name}, {str(id)}"
#     return render_template("user.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="8000")
