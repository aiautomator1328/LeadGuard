
# 1. ДАНІ КЛІЄНТІВ

leads = [
    {
        "id": 1,
        "name": "alex",
        "email": "alex@gmail.com",
        "phone": "+3655644",
        "budget": 500
    },
    {
        "id": 2,
        "name": "bob",
        "email": "bob@gmail.com",
        "phone": "+6666549849",
        "budget": ""
    },
    {
        "id": 3,
        "name": "jery",
        "email": "hih@iuwehi",
        "phone": "+",
        "budget": 2600
    },
    {
        "id": 4,
        "name": "coil",
        "email": "",
        "phone": "+6666549849",
        "budget": 1000
    },
    {
        "id": 5,
        "name": "vasya",
        "email": "bek@gmail.com",
        "phone": "+3655644",
        "budget": 2550
    },
    {
        "id": 6,
        "name": "kate",
        "email": "kate@gmail.com",
        "phone": "+1234567890",
        "budget": 6000
    }
]

# 2. ФУНКЦІЇ


def validate_lead(lead):
    if lead["email"] == "" or lead["name"] == "":
        return False

    if lead["budget"] == "" or lead["budget"] <= 0:
        return False

    return True


def get_invalid_reason(lead):
    if lead["email"] == "":
        return "Missing email"

    elif lead["budget"] == "":
        return "Missing budget"

    elif lead["budget"] <= 0:
        return "Invalid budget"

    elif lead["name"] == "":
        return "Missing name"

    else:
        return "No errors"


def get_priority(budget):
    if budget >= 4000:
        return "High"

    elif budget >= 2000:
        return "Medium"

    else:
        return "Low"


# 3. ПІДГОТОВКА ДО ОБРОБКИ


seen_phones = set()

valid_count = 0
invalid_count = 0
duplicate_count = 0

results = []



# 4. ОСНОВНА ОБРОБКА ЗАЯВОК

for lead in leads:
    phone = lead["phone"]

    if not validate_lead(lead):
        reason = get_invalid_reason(lead)

        print(lead["name"], "- Invalid", reason)
        invalid_count += 1

        results.append({
            "name": lead["name"],
            "status": "Invalid",
            "reason": reason
        })

    elif phone in seen_phones:
        print(lead["name"], "- Duplicate")
        duplicate_count += 1

        results.append({
            "name": lead["name"],
            "status": "Duplicate"
        })

    else:
        priority = get_priority(lead["budget"])

        print(lead["name"], "- Valid", priority)
        seen_phones.add(phone)
        valid_count += 1

        results.append({
            "name": lead["name"],
            "status": "Valid",
            "priority": priority
        })


# 5. ФІНАЛЬНИЙ ЗВІТ


print("Valid:", valid_count)
print("Invalid:", invalid_count)
print("Duplicate:", duplicate_count)

print("=== HIGH PRIORITY LEADS ===")

for result in results:
    if result["status"] == "Valid" and result["priority"] == "High":
        print(result["name"])


high_leads = []
medium_leads = []
low_leads = []

for result in results:
    if result["status"] == "Valid":

        if result["priority"] == "High":
            high_leads.append(result["name"])

        elif result["priority"] == "Medium":
            medium_leads.append(result["name"])

        else:
            low_leads.append(result["name"])

print("High:", high_leads)
print("Medium:", medium_leads)
print("Low:", low_leads)


