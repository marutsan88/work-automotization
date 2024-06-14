from smartphone import Smartphone

catalog = []
catalog.append(Smartphone("Samsung", "Galaxy S21", "+790145689"))
catalog.append(Smartphone("Xiaomi", "Mi 5", "+7931543490"))
catalog.append(Smartphone("Google", "TECHNO SPARK 9 pro", "+7954267890"))
catalog.append(Smartphone("OnePlus", "8 Pro", "+7911456525"))
catalog.append(Smartphone("Apple", "iPhone 13pro", "+7934567890"))

for phone in catalog:
    print(f"{phone.brand}, {phone.model}, {phone.phone_number}")


