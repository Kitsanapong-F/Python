def calculate_biochar_ratio(total_weight, ph_level):
# T000: สัปดาห์ที 5 - กิจกรรม Pair Prograoaing
# 1. ตรวจสอบความถูกต้องของ Input ก่อน (Validation)

    if ph_level < 0 or ph_level > 14:
        raise ValueError("ค่า pH ของดินต้องอยู่ระหว่าง 0 ถึง 14 เท่านั้น")

    if total_weight <= 0:
        raise ValueError("น้ำหนักรวมของปุ๋ยต้องมากกว่า 0 กิโลกรัม")

    # 2. คู่นักศึกษาเขียนตรรกะคำนวณตามเงื่อนไข pH ดินกรด/ต่าง/กลาง ต่อตรงนี้ ...
    if ph_level < 5.5:
        biochar_weight  =  total_weight * 0.30

    elif ph_level <= 7.5:
        biochar_weight  =  total_weight * 0.15

    else:
        biochar_weight  =  total_weight * 0.05

    return biochar_weight
