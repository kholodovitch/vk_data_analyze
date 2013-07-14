import vk_api
import json
import time
import datetime

def getDefinedAge(api):
    users = api.users_get(api.user_id, "bdate")
    # print ''.join(str(e) for e in users).replace("\\r\\n'", "'").decode('unicode-escape')
    now = datetime.datetime.now()

    if "bdate" in users[0]:
        bdate_str = users[0]["bdate"]
        date_parts = bdate_str.split('.')
        if len(date_parts) == 3:
            bdate_time = time.strptime(bdate_str, "%d.%m.%Y")
            bdate_date = datetime.datetime.fromtimestamp(time.mktime(bdate_time))
            delta = datetime.timedelta(days=(now - bdate_date).days)
            return delta.days / 365
    return None

email = "darkangel_xxi@mail.ru" # raw_input("Email: ")
password = "mamamia!16"         # getpass.getpass()
client_id = "2951857"           # Vk application ID

api = vk_api.vk_api()
api.auth(email, password, client_id)

definedAge = getDefinedAge(api)
if definedAge is not None:
    print definedAge

raw_input("Press Enter to continue...")