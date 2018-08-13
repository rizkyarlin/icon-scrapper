import atexit
import re
import pymysql.cursors
from bs4 import BeautifulSoup
from urllib.request import urlopen

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='chainkiller',
                             db='lora',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


html = urlopen("https://themify.me/themify-icons")
# print(html.read())

soup = BeautifulSoup(html, features="html.parser")

icon_names = soup.find_all('span', {'class': 'icon-name'})
for icon_name in icon_names:
    print(icon_name.text)

# for icon_name in soup.find_all('span'):
#     print(icon_name.get('href'))

# with connection.cursor() as cursor:
#     # Create a new record
#     sql = "INSERT INTO `preparing` (`node_id`, `packet_num`, `SF`, `CR`, `BW`, `RSSI`, `SNR`, " \
#           "`experiment`, `interval`, `frame_size`, `n_node`) " \
#           "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
#     cursor.execute(sql, (node_id[1], packet_num[1], SF[1], CR[1], BW[1], RSSI[1], SNR[1],
#                          experiment[1], interval[1], frame_size[1], n_node))
#
# # connection is not autocommit by default. So you must commit to save
# # your changes.
# connection.commit()