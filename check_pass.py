import re
import hashlib
import requests

def analyze_password():
    print("\n--- محلل كلمات السر الذكي (للأمن الأخلاقي) ---")
    password = input("أدخل كلمة السر التي تريد فحصها: ")
    
    # 1. تحليل القوة البرمجية
    score = 0
    if len(password) >= 8: score += 1
    if re.search("[a-z]", password) and re.search("[A-Z]", password): score += 1
    if re.search("[0-9]", password): score += 1
    if re.search("[!@#$%^&*(),.?\":{}|<>]", password): score += 1
    
    # 2. حساب وقت التخمين (بناءً على مليار محاولة في الثانية)
    pool_size = 0
    if re.search("[a-z]", password): pool_size += 26
    if re.search("[A-Z]", password): pool_size += 26
    if re.search("[0-9]", password): pool_size += 10
    if re.search("[!@#$%^&*(),.?\":{}|<>]", password): pool_size += 32
    
    # تجنب الخطأ إذا كانت الكلمة فارغة
    if pool_size == 0 or len(password) == 0:
        combinations = 0
    else:
        combinations = pool_size ** len(password)
        
    seconds = combinations / 1_000_000_000
    
    # 3. الفحص في قاعدة بيانات التسريبات (API)
    is_leaked = False
    try:
        # تشفير الكلمة بطريقة SHA-1
        sha1_pwd = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
        prefix, suffix = sha1_pwd[:5], sha1_pwd[5:]
        
        # استدعاء قاعدة البيانات العالمية للتسريبات
        response = requests.get(f"https://api.pwnedpasswords.com/range/{prefix}")
        if suffix in response.text:
            is_leaked = True
    except:
        print("خطأ: تعذر الاتصال بقاعدة بيانات التسريبات (تأكد من الإنترنت).")

    # --- عرض النتائج النهائية ---
    print("\n" + "="*40)
    print(f"النتيجة الأمنية: {score}/4")
    
    if is_leaked:
        print("⚠️ تنبيه أمني: هذه الكلمة 'مسربة' في اختراقات سابقة! لا تستخدمها.")
    else:
        print("✅ كلمة السر هذه لم تظهر في التسريبات العالمية المعروفة.")

    if seconds < 1:
        print("الوقت المتوقع للكسر: فوري (أقل من ثانية).")
    elif seconds < 3600:
        print(f"الوقت المتوقع للكسر: {seconds/60:.1f} دقيقة.")
    elif seconds < 86400:
        print(f"الوقت المتوقع للكسر: {seconds/3600:.1f} ساعة.")
    elif seconds < 31536000:
        print(f"الوقت المتوقع للكسر: {int(seconds/86400)} يوم تقريباً.")
    else:
        print(f"الوقت المتوقع للكسر: {int(seconds/31536000)} سنة تقريباً!")
    print("="*40)

# تشغيل الأداة

if __name__ == "__main__":
    analyze_password()
