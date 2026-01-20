def robot_ai(temp, alarm, raining):
    # 1. เงื่อนไข: ฝนตกและอุณหภูมิต่ำ (< 20°C) -> เปิดฮีตเตอร์
    if raining == True and temp < 20:
        decision = "เปิดฮีตเตอร์ (Heater ON)"
    
    # 2. เงื่อนไข: อุณหภูมิเกิน 50°C และไม่มีสัญญาณเตือน -> หยุดเครื่อง
    elif temp > 50 and alarm == False:
        decision = "หยุดเครื่อง (STOP)"
    
    # 3. เงื่อนไข: มีสัญญาณเตือน หรือ อุณหภูมิปกติ -> ทำงานต่อ
    elif alarm == True or temp <= 50:
        decision = "ทำงานต่อ (Continue)"
    
    else:
        decision = "ตรวจสอบระบบ (Check System)"
        
    return decision

# --- ส่วนการแสดงผลแบบตารางง่ายๆ ---
print("-" * 65)
print(f"{'Temp':<10} | {'Alarm':<10} | {'Rain':<10} | {'AI Decision'}")
print("-" * 65)

# ทดสอบสถานการณ์ต่างๆ
test_cases = [
    (55, False, False),  # ร้อนเกิน + ไม่มีเตือน
    (55, True, False),   # ร้อนเกิน + มีเตือน
    (30, False, False),  # ปกติ
    (15, False, True),   # หนาว + ฝนตก
]

for t, a, r in test_cases:
    result = robot_ai(t, a, r)
    # แสดงผลจัดรูปแบบให้ตรงกัน
    print(f"{t:<10} | {str(a):<10} | {str(r):<10} | {result}")

print("-" * 65)