import re

with open("raw.txt", "r", encoding="utf-8") as f:
    data = f.read()

print(data)

prices = re.findall(r"\d+\s?\d*,\d+", data)
print(prices)

products = re.findall(r"\d+\.\n(.+)", data)
print(products)

total_match = re.search(r"ИТОГО:\n([\d\s,]+)", data)
total = total_match.group(1).strip() if total_match else "Not found"
print(total)

payment_match = re.search(r"Банковская карта", data)
payment = payment_match.group() if payment_match else "Not found"
print(payment)

date_match = re.search(r"\d{2}\.\d{2}\.\d{4}", data)
date = date_match.group() if date_match else "Not found"
print(date)

time_match = re.search(r"\d{2}:\d{2}:\d{2}", data)
time = time_match.group() if time_match else "Not found"
print(time)

words = re.split(r"\s+", data)
print(words[:20])

clean_text = re.sub(r"\s+", " ", data)
print(clean_text[:200])

result = {
    "products": products,
    "prices": prices,
    "total": total,
    "date": date,
    "time": time,
    "payment": payment
}

print(result)