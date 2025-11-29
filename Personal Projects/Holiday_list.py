

while True:
    print("\n--- Add a New Holiday ---")
    name = input("Holiday name: ")
    start = input("Date it started (DD/MM/YYYY): ")
    end = input("Date it ended (DD/MM/YYYY): ")
    memories = []
    
    print("Enter three core memories from this holiday:")
    for i in range(1, 4):
        memory = input(f"Memory {i}: ")
        memories.append(memory)

    holiday = {
        "name": name,
        "start": start,
        "end": end,
        "memories": memories
    }
    holidays.append(holiday)

    print("\n=== Holidays Collected So Far ===")
    for h in holidays:
        print(f"\n🏖 {h['name']} ({h['start']} → {h['end']})")
        for m in h["memories"]:
            print(f"  - {m}")

    cont = input("\nAdd another holiday? (yes/no): ").lower()
    if cont != "yes":
        print("\nThanks for using the Holiday Collector!")
        break
