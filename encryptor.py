# أداة تشفير بسيطة - خطوتي الأولى في الأمن السيبراني
def simple_encrypt(text, key):
    result = ""
    for char in text:
        # تحويل الحرف إلى رمز مشفر باستخدام المفتاح
        result += chr(ord(char) + key)
    return result

# تجربة الأداة على رسالة سرية
message = "Security is Priority"
key = 7
print("الرسالة الأصلية: " + message)
print("الرسالة المشفرة: " + simple_encrypt(message, key))

