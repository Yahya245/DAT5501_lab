PASSWORD = "1234"   # you can change this to anything you want

print("🔒 Device Locked")

while True:
    entered = input("Enter passcode to unlock: ")

    if entered == PASSWORD:
        print("✅ Device Unlocked")
        break
    else:
        print("❌ Incorrect passcode — try again")
