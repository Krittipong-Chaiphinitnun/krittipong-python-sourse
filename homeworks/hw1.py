"""
Personal Finance Calculator
Student: Krittipong Chaiphinitnun
Date: 27-07-2025
Purpose: Calculate monthly budget and savings
"""

# ขอข้อมูลจากผู้ใช้เกี่ยวกับรายได้และค่าใช้จ่ายรายเดือน
monthly_income = float(input("Enter your monthly income (THB): "))
rent_cost = float(input("Enter your rent cost (THB): "))
food_budget = int(input("Enter your food budget (THB): "))
transportation_cost = float(input("Enter your transportation cost (THB): "))
entertainment_budget = int(input("Enter your entertainment budget (THB): "))
emergency_fund_percent = float(input("Enter emergency fund percentage (e.g., 10.5): "))
investment_percent = float(input("Enter investment percentage (e.g., 15.0): "))

# คำนวณค่าใช้จ่ายคงที่ = ค่าเช่า + ค่าเดินทาง
total_fixed_expenses = rent_cost + transportation_cost

# คำนวณค่าใช้จ่ายไม่คงที่ = ค่ากิน + ค่าที่พัก
total_variable_expenses = food_budget + entertainment_budget

# ค่าใช้จ่ายรวม
total_expenses = total_fixed_expenses + total_variable_expenses

# รายได้ที่เหลือหลังจากหักค่าใช้จ่าย
remaining_income = monthly_income - total_expenses

# เงินสำรองฉุกเฉินตามเปอร์เซ็นต์ที่กำหนด
emergency_fund = monthly_income * (emergency_fund_percent / 100)

# เงินลงทุนตามเปอร์เซ็นต์ที่กำหนด
investment_amount = monthly_income * (investment_percent / 100)

# เงินที่สามารถเก็บออมได้ เป็นเงินเก็บฉุกเฉิน
available_for_savings = remaining_income - emergency_fund

# คำนวณสัดส่วนค่าใช้จ่ายต่อรายได้
expense_ratio = (total_expenses / monthly_income) * 100

# แสดงผลลัพธ์ออกทางหน้าจอ
print("\n=== MONTHLY BUDGET REPORT ===")
print(f"Income: {monthly_income:.2f} THB")
print(f"Fixed Expenses: {total_fixed_expenses:.2f} THB")
print(f"Variable Expenses: {total_variable_expenses:.2f} THB")
print(f"Total Expenses: {total_expenses:.2f} THB")
print(f"Remaining: {remaining_income:.2f} THB")

print("\n=== SAVINGS BREAKDOWN ===")
print(f"Emergency Fund ({emergency_fund_percent}%): {emergency_fund:.2f} THB")
print(f"Investment ({investment_percent}%): {investment_amount:.2f} THB")
print(f"Available for Savings: {available_for_savings:.2f} THB")

print("\n=== ANALYSIS ===")
print(f"Expense Ratio: {expense_ratio:.2f}%")