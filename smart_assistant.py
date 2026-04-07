import random

# احتمالات اللعبة
teams = {
    "Barcelona (x40)": 1, 
    "Real Madrid (x40)": 1,
    "Man City (x4)": 44,
    "Bayern (x4)": 44
}

def analyze_and_save():
    print("--- مساعد التوقع الذكي ---")
    last_winner = input("ما هو آخر فريق فاز في اللعبة؟ ")
    
    # محاكاة بسيطة
    prediction = "احتمالية فوز x40 هي 1% فقط. ننصح بالحذر."
    
    # الجزء الخاص بتخزين البيانات في ملف
    with open("history.txt", "a", encoding="utf-8") as file:
        file.write(f"الفريق الفائز: {last_winner} | التوقع: {prediction}\n")
    
    print(f"✅ تم حفظ النتيجة في ملف history.txt")
    print(prediction)

analyze_and_save()
