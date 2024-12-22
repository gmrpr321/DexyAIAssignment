from flask import Flask, jsonify, request
from flask_cors import CORS
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

app = Flask(__name__)
CORS(app)


@app.route('/api/sendMessage', methods=['POST'])
def send_message():
    data = request.json
    app_id = data.get("appId")
    recipient_name = data.get("recName")
    message = data.get("message")

    if not app_id or not recipient_name or not message:
        return jsonify({"error": "Missing appId, recName, or message in the payload"}), 400

    try:
        if app_id == 1:
            result = send_message_wellfound(recipient_name, message)
        elif app_id == 2:
            result = send_message_linkedin(recipient_name, message)
        else:
            return jsonify({"error": f"Unsupported appId: {app_id}"}), 400

        return jsonify({"success": True, "result": result})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
def send_message_wellfound(recipient_name, message):
    options = Options()
    userdatadir = 'C:/Users/Pradeep/AppData/Local/Google/Chrome/User Data'
    options.add_argument(f"--user-data-dir={userdatadir}")
    options.add_argument(f"--profile-directory={"Pradeep"}")
    options.add_experimental_option("detach", True)
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    service = Service(executable_path="C:/Users/Pradeep/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")    # w = webdriver.Chrome(executable_path="C:\\Users\\chromedriver.exe", chrome_options=options)   
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://wellfound.com/jobs")
    time.sleep(5)  
    search_box = driver.find_element(By.ID, "search-box")  
    search_box.send_keys(recipient_name)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)  
    message_box = driver.find_element(By.ID, "message-input") 
    message_box.send_keys(message)
    send_button = driver.find_element(By.ID, "send-button")  
    send_button.click()

    time.sleep(2)
    driver.quit()

    return f"Message sent to {recipient_name} on Wellfound."


def send_message_linkedin(recipient_name, message):
    options = Options()
    userdatadir = 'C:/Users/Pradeep/AppData/Local/Google/Chrome/User Data'
    options.add_argument(f"--user-data-dir={userdatadir}")
    options.add_argument(f"--profile-directory={"Pradeep SN"}")
    options.add_experimental_option("detach", True)
    service=Service(executable_path="C:/Users/Pradeep/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=service,options=options)


    time.sleep(5) 
    driver.get("https://www.linkedin.com/messaging")


    search_box = driver.find_element(By.CLASS_NAME, "search-global-typeahead__input")
    search_box.send_keys(recipient_name)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)  

    recipient = driver.find_element(By.PARTIAL_LINK_TEXT, recipient_name) 
    recipient.click()
    time.sleep(2)

    message_box = driver.find_element(By.CLASS_NAME, "msg-form__contenteditable") 
    message_box.send_keys(message)
    send_button = driver.find_element(By.CLASS_NAME, "msg-form__send-button") 
    send_button.click()

    time.sleep(2)
    driver.quit()

    return f"Message sent to {recipient_name} on LinkedIn."


if __name__ == '__main__':
    app.run(debug=True)
