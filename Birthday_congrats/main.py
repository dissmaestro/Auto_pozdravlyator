
import sqlite3 as sq
import vk_api
import datetime
#  В этом блоке кода представлены функции реализующие получение информации от вк
# ----------------------------------------------------------------------------



try:
    vk_session = vk_api.VkApi('89257828987', 'Maks1302')  # 89257828987  Maks1302
    vk_session.auth()
    vk = vk_session.get_api()

except vk_api.exceptions.Captcha as captcha:
    sid = captcha.sid # Получение sid
    url = captcha.get_url() # Получить ссылку на изображение капчи
    img = captcha.get_image() # Получить изображение капчи (jpg)
    print(f"Беда с каптчей вот sid {sid} url на картинку {url} img в jpg {img}")

my_id = 781028675 #781028675


def get_friends_id(user_id: int):
    id_fr = vk_session.method("friends.get", {"user_id": user_id})
    return id_fr.get('items')


def get_friends_bdate(id_friend: list):  # return list of id frirnd
    birthday = list()
    for i in range(len(id_friend)):
        bdate_json = (vk_session.method("friends.get", {"fields": {"bdate": int(id_friend[i])}}))
        bdate_list = bdate_json.get('items')[i].get('bdate').split('.', 2)
        bdate_clear = str(bdate_list[0]) + '.' + str(bdate_list[1])
        birthday.append(bdate_clear)

    return birthday


def get_friends_name(id_friend: list):   # return list of first name
    Name = list()
    for i in range(len(id_friend)):
        Name_json = (vk_session.method("friends.get",{"fields": {"first_name": int(id_friend[i])}}))
        Name_clear = Name_json.get('items')[i].get('first_name')
        Name.append(Name_clear)
    return Name


def get_friends_lname(id_friend: list): # return list of last name
    Lname = list()
    for i in range(len(id_friend)):
        lname_json = (vk_session.method("friends.get", {"fields": {"last_name": int(id_friend[i])}}))
        lname_clear = lname_json.get('items')[i].get('last_name')
        Lname.append(lname_clear)
    return Lname

def list_of_tuple(list_id: list, bdate: list, name: list, lname: list):
    list_of_all = list()   # преобразование кортежей в список кортежей

    for i in range(len(list_id)):
        list_of_one = list()
        list_of_one.append(list_id[i])
        list_of_one.append(name[i])
        list_of_one.append(lname[i])
        list_of_one.append(bdate[i])
        list_of_all.append(tuple(list_of_one))
    return list_of_all

def dm():
    today = datetime.datetime.today()
    sr_d = str(today.day)
    sr_m = str(today.month)
    sr_dm = sr_d + '.' + sr_m
    return sr_dm

list_of_id = get_friends_id(my_id)

list_of_bdate = get_friends_bdate(list_of_id)
list_of_name = get_friends_name(list_of_id)
list_of_lname = get_friends_lname(list_of_id)

list_tuple = list_of_tuple(list_of_id, list_of_bdate, list_of_name, list_of_lname)
            #  В этом блоке кода представлена реализация бд на  Sqlite3  а так де запись в бд данныз из вк
# ----------------------------------------------------------------------------
print(list_tuple)


try:
    conn = sq.connect(r'./congrats.db')  # cozdaine DB
    cur = conn.cursor()  # объект для реализации запросов
    print("Подключен к SQLite")

    cur.execute('''CREATE TABLE IF NOT EXISTS MyFriends(
        user_id INT PRIMARY KEY,
        fname VCHAR,
        lname VCHAR,
        bdate VCHAR);
        ''')

    cur.executemany('''INSERT INTO MyFriends 
    (user_id, fname, lname, bdate)
    VALUES(?, ?, ?, ?);''', list_tuple)
    conn.commit()
    print("Запись успешно вставлена в таблицу MyFriends  ", cur.rowcount)

    cur.execute('''SELECT user_id FROM MyFriends WHERE bdate = '4.1' ''')
    rec = cur.fetchone()

    cur.close()

except sq.Error as error:
    print("Ошибка при работе с SQLite", error)
finally:
    if conn:
        conn.close()
        print("Соединение с SQLite закрыто")



