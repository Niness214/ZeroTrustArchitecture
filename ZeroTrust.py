allowed_users = {
    "lando": {"device": "mobile134"},
    "norris": {"device": "laptop9800"},
}

def verify_access(user, device_id):
    # Step 1: Check if user exists
    if user not in allowed_users:
        return False, "Access Denied: Unknown user"

    # Step 2: Verify device ID matches user's registered device
    if allowed_users[user]["device"] != device:
        return False, "Access Denied: Unrecognized device"

    # Access granted if both checks pass
    return True, "Access Granted"

# Simulate access requests
requests = [
    ("lando", "mobile134"),
    ("lando", "device999"),
    ("leclerc", "raspberrypi"),
    ("norris", "laptop9800"),
]

for user, device in requests:
    result, message = verify_access(user, device)
    print(f"User: {user}, Device: {device} => {message}")
