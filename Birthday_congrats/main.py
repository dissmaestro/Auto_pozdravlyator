import sqlite3
import vk_api

#  В этом блоке кода представлены функции реализующие получение информации от вк
# ----------------------------------------------------------------------------
vk_session = vk_api.VkApi('89257828987', 'Maks1302')  # 89257828987  Maks1302
vk_session.auth()
vk = vk_session.get_api()
my_id = 81028675


def get_friends_id(user_id: int):
    id_fr = vk_session.method("friends.get", {"user_id": user_id})
    return id_fr.get('items')


def get_friends_bdate(id_friend: list):  # return list of id frirnd
    birthday = list()
    for i in range(len(id_friend)):
        bdate_json = (vk_session.method("friends.get", {"fields": {"bdate": int(id_friend[i])}}))
        bdate_clear = bdate_json.get('items')[i].get('bdate')
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


list_of_id = get_friends_id(my_id)
print(get_friends_bdate(list_of_id))
print(get_friends_name(list_of_id))
print(get_friends_lname(list_of_id))

#  В этом блоке кода представлена реализация бд на  Sqlite3  а так де запись в бд данныз из вк
# ----------------------------------------------------------------------------

conn = sqlite3.connect(r'./congrats.db') # cozdaine DB
cur = conn.cursor() # объект для реализации запросов

# crate a table

#cur.execute('''CREATE TABLE IF NOT EXISTS users(
#    user_id INT PRIMARY KEY,
#    fname TEXT
#    lname TEXT
#    bdate TEXT);
 #   ''')
#conn.commit()
