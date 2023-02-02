import vk
import requests
import vk_api
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

vk_session = vk_api.VkApi('89257828987', 'Maks1302')
vk_session.auth()
vk = vk_session.get_api()
my_id = 781028675


def get_friends_id(user_id: int):
    id_fr = vk_session.method("friends.get", {"user_id": user_id})
    return id_fr.get('items')


def get_friends_bdate(id_friend: list):
    birthday = list()
    for i in range(len(id_friend)):
        bdat_json = (vk_session.method("friends.get", {"fields": {"bdate": int(id_friend[i])}}))
        bdate_clear = bdat_json.get('items')[i].get('bdate')
        birthday.append(bdate_clear)

    return birthday



h = get_friends_id(my_id)
print(get_friends_bdate(h))

# print(vk.wall.post(message = 'Kuki muki'))

'''
driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
------------------------------------------------------
my_id = 781028675  # moi id v vk
token = "0b4f6e210b4f6e210b4f6e2131085d00af00b4f0b4f6e21689672b7ead64a1ebf3b706f"  # Сервисный ключ доступа
my_id, login, password = '781028675', '89257828987', '13022002m'
session = vk.AuthSession(my_id, login, password,)
vk_api = vk.API(session)
session = vk.session(access_token='0b4f6e210b4f6e210b4f6e2131085d00af00b4f0b4f6e21689672b7ead64a1ebf3b706f')
api = vk.API(session)

param = {'access_token': token, 'user_id': my_id, 'v': 5.131}
method = 'friends.get'
rec = requests.get(url=f'https://api.vk.com/method{method}', params=param)
print(rec.json())
def get_friends_id(user_id):
    friends = session.method("friends.get", {"user_id": user_id})
    '''
