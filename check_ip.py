import socket

# كود بسيط لمعرفة اسم الجهاز وعنوان الـ IP الداخلي
def get_device_info():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    
    print("اسم جهازك البرمجي: " + hostname)
    print("عنوان الـ IP الداخلي هو: " + ip_address)

get_device_info()

