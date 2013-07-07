import vk_api

email = "darkangel_xxi@mail.ru" # raw_input("Email: ")
password = "mamamia!16"         # getpass.getpass()
client_id = "2951857"           # Vk application ID

api = vk_api.vk_api()
api.auth(email, password, client_id);
print api.get_albums()
print ""