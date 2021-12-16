# from wxpusher import WxPusher
#
# apptoken = "AT_RoGjc93ix2Osz7ikWm0Q8Msma9Wo6PuS"
#
#
# uids = ['UID_SL6GTxhgnQommPYJMC9FqBeVxmSK']
#
# content = "hello, this is new message"
# WxPusher.send_message(content,
#                       uids=uids,
#                       # topic_ids='<topic_ids>',
#                       token=apptoken)
# # WxPusher.query_message('<messageId>')
# # WxPusher.create_qrcode('<extra>', '<validTime>', '<appToken>')
# # WxPusher.query_user('<page>', '<page_size>', '<appToken>')


import requests
u = 'https://tianqi.2345.com/'
r = requests.get(u)
print(r.text)
# r.encoding = 'utf-8'
# print(a.text)
# url='http://music.baidu.com'
# r = requests.get(url)
# html=r.content
# html_doc=str(html,'utf-8') #html_doc=html.decode("utf-8","ignore")
# print(html_doc)
# #
# bytes=r.content
#
# print(bytes.decode(encoding="utf-8"))