from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


chromedriver = "/Users/kashyap/Downloads/chromedriver"
browser = webdriver.Chrome(chromedriver)

userName = ""

def login(stremail, strpassword):
    browser.get('https://www.linkedin.com/')
    time.sleep(2)
    try:
        user = browser.find_element_by_css_selector('#login-email')
        user.send_keys(stremail)
    except NoSuchElementException as exception:
        print('login email Element not found and test failed')

    try:
        password = browser.find_element_by_css_selector('#login-password')
        password.send_keys(strpassword)
    except NoSuchElementException as exception:
        print('password textbox not found')

    try:
        login = browser.find_element_by_css_selector('#login-submit')
        login.click()
        time.sleep(4)
    except NoSuchElementException as exception:
        print('Login button not found')
    sep = ' '
    username = browser.find_element_by_class_name('profile-rail-card__actor-link').text
    first_letter = username.split(sep, 1)[0]
    if first_letter == "Welcome,":
        username = username.split(sep,1)[1]
        username = username.split('!',1)[0]
    else:
        username = first_letter
    browser.get('https://www.linkedin.com/sales?trk=d_flagship3_nav')
    print(username)
    return username


def exclude_saved_leads():
    time.sleep(1)
    try:
        button = browser.find_element_by_link_text('Exclude saved leads')
        button.click()
    except NoSuchElementException as exception:
        print("Not able to exclude saved leads")
    #exclude_contacted_leads()



def scroll_down(pixels):
    browser.execute_script("window.scrollTo(0, "+str(pixels)+")")

def exclude_contacted_leads():
    element = browser.find_element_by_link_text('Exclude contacted leads')
    element.click()

def select_finance():
    element = browser.find_element_by_link_text()

def send_requestion_and_save_lead(request_amount,username):
    send_count = 0
    c=1
    for y in range(1, 100):
        print('y value is : '+ str(y))
        if request_amount > 0 and y >2:
            time.sleep(1)
            data = 1

            for x in range(1, 25): #because there are 25 person per lead..
                if request_amount > 0:
                    scroll_down(100)
                    temp = 1
                    try:
                        scroll_down(30)
                        str_hover = '//*[@id="results-list"]/li[' + str(
                            x) + ']/div[2]/div/div[1]/div[2]/div[1]/div[1]/button/li-icon'
                        action_trigger = browser.find_element_by_xpath(str_hover)
                        hover = ActionChains(browser).move_to_element(action_trigger)
                        hover.perform()
                        time.sleep(1)
                    except NoSuchElementException as exception:
                        temp = 0
                    except StaleElementReferenceException as exception:
                        temp = 0
                    if temp == 1:
                        connect_Str = '//*[@id="results-list"]/li[' + str(
                            x) + ']/div[2]/div/div[1]/div[2]/div[1]/div[1]/div/ul/li[1]/button'
                        try:
                            scroll_down(120)
                            connect_btn = browser.find_element_by_xpath(connect_Str)
                            connect_btn.click()
                        except NoSuchElementException as exception:
                            print("failed to exceute connect button")
                            temp = 0
                        except ElementNotVisibleException as exception:
                            print("Failed to excecute connection button")
                            temp = 0
                        if temp == 1:
                            if temp == 1:
                                browser.switch_to_active_element()
                                time.sleep(1)
                                print(username)
                                send_message(username)
                                request_amount = request_amount-1
                                print("Request Left : " + str(request_amount))
                                time.sleep(2)
                                try:
                                    save_as_lead = browser.find_element_by_xpath('// *[ @ id = "results-list"] / li[' + str(
                                    x) + '] / div[2] / div / div[1] / div[2] / div[1] / div[2] / form / button')
                                    save_as_lead.click()
                                except NoSuchElementException as exception:
                                    print("Not able to save lead")
                                time.sleep(1)
                                try:
                                    browser.switch_to_active_element()
                                    try:
                                        browser_connect_btn = browser.find_element_by_xpath(
                                            '//*[@id="dialog"]/div/div[2]/ul/li[2]/form/button')
                                    except NoSuchElementException as exception:
                                        try:
                                            browser_connect_btn = browser.find_element_by_xpath('//*[@id="dialog"]/div/div[2]/ul/li[4]/form/button')
                                        except NoSuchElementException as exception:
                                            try:
                                                browser_connect_btn = browser.find_element_by_xpath('//*[@id="dialog"]/div/div[2]/ul/li[5]/form/button')
                                            except NoSuchElementException as exception:
                                                try:
                                                    browser_connect_btn = browser.find_element_by_xpath('//*[@id="dialog"]/div/div[2]/ul/li[6]/form/button')
                                                except NoSuchElementException as exception:
                                                    try:
                                                        browser_connect_btn=browser.find_element_by_xpath('//*[@id="dialog"]/div/div[2]/ul/li[7]/form/button')
                                                    except NoSuchElementException as exception:
                                                        browser_connect_btn=browser.find_element_by_xpath('//*[@id="dialog"]/div/div[2]/ul/li[8]/form/button')
                                    browser_connect_btn.click()
                                except NoSuchElementException as exception:
                                    print("no alert window")

            browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(3)

        else:
            if request_amount == 0:
                break;

        scroll_down(3000)
        time.sleep(3)
        c = c + 1

        if y == 5:
            c = c + 2
        if y == 6:
            c = 8
        if y > 6:
            c = 8

        print('value of y :'+str(y))
        try:
            next_page_btn = browser.find_element_by_xpath('//*[@id="pagination"]/div/ul/li[' + str(c) + ']')
            next_page_btn.click()
        except NoSuchElementException as exception:
            try:
                next_page_btn = browser.find_element_by_xpath('//*[@id="pagination"]/div/ul/li[' + str(c) + ']')
                next_page_btn.click()
            except NoSuchElementException as exception:
                print("Continue")



def send_message(username):
    try:
        time.sleep(1)
        try:
            name = browser.find_element_by_xpath('//*[@id="connect-dialog"]/div/div/div[2]/div/div').text
        except NoSuchElementException as exception:
            try:
                name = browser.find_element_by_xpath('//*[@id="connect-dialog"]/div/div/div[2]/div/div').text
            except NoSuchElementException as exception:
                print('not fatching names')
        try:
            text_area_value = browser.find_element_by_xpath('//*[@id="connect-message-content"]')
        except NoSuchElementException as exception:
            print('not able to find message text area')
        time.sleep(1)
        text_area_value.clear()
        text_area_value.click()
    except NoSuchElementException as exception:
        print('Not able to find element //*[@id="connect-message-content"]')
    skip_save_lead = 0
    sep = ' '
    name = name.split(sep, 1)[0]
    str_msg = "Hi " + name + ","
    if username == "Jihane":
        str_msg = "Bonjour " + name + ","
    text_area_value.send_keys(str_msg)
    text_area_value.send_keys('\n')
    if username == "Brandyn" or username == "Asad" or username == "Omer":
        text_area_value.send_keys("hope this note finds you doing well. I have some ideas around automating your prospecting efforts that I'd love to share. Would you have some time for a quick chat perhaps to see if there's any mutual synergy, schedule permitting of course? Hope to talk to you soon.\nThanks, "+ username)
    if username == "Ryan":
        text_area_value.send_keys("I’d like to introduce myself. My name is "+ username +" and I’m an investment advisor at Merrill Lynch. It seems like we know some of the same people. I am always looking to expand my network, and when I came across your profile, I was intrigued. Looking forward to connecting.\n –Thanks, "+username)
    if username == "Steven":
        text_area_value.send_keys("I’d like to introduce myself. My name is Steven and I’m an investment advisor at Morgan Stanley. It seems like we know some of the same people. I am always looking to expand my network, and when I came across your profile, I was intrigued. Looking forward to connecting.\n–Thanks, Steven")
    if username == "Janet":
        text_area_value.send_keys(" I live & work locally and am looking to grow my network. With my team, we assess financial risk for business owners and solutions to the 120% tax obligations recently introduced by the Federal government.  I'd like to learn more about you & your business. Can we connect?")
    if username == "Ron":
        text_area_value.send_keys("I’d like to introduce myself. My name is Ron, and I’m an Investment Advisor at Kassies Financial. It seems like we know some of the same people. I am always looking to expand my network, and when I came across your profile, I was intrigued. Looking forward to connecting. - Thanks, "+ username)
    if username == "Robert":
        text_area_value.send_keys("I hope you're having a great day. Have you ever wondered if you're ahead, behind or on target to afford the future lifestyle you really want? I'd love the opportunity to talk about how I can help you answer that question. Let me know if you'd be open to having a quick chat.\n- Rob Reid")
    if username == "Percy":
        text_area_value.send_keys("I’m Percy, a Financial Advisor at Bloom Wealth and I live & work locally. I help clients build wealth and assess financial risk, helping business owners and individuals make smart choices about money. I’d like to learn more about you and your business. Hope to connect with your soon.")
    if username == "Karim":
        text_area_value.send_keys(" I’d like to introduce myself. My name is Karim and I’m an investment advisor at Freedom 55. It seems like we know some of the same people. I am always looking to expand my network, and when I came across your profile, I was intrigued. Looking forward to connecting.\n– Thanks, Karim")
    if username == "Jihane":
        text_area_value.send_keys("J'aimerais avoir l'occasion de vous rencontrer pour vous montrer la manière dont nous protégeons et améliorons le bien-être financier de nos clients. Seriez-vous ouvert à une discussion pour voir comment je pourrais vous être utile. En espérant échanger avec vous bientôt. Jihane.")
    if username == "Jamie":
        text_area_value.send_keys("I hope you’re having a great day. I’d love the opportunity to show you how I improve and protect the overall well-being of individuals, families, and businesses. Would you be open to a quick chat to see how I might help you prosper? Hope to talk to you soon. Thanks, Jamie")
    if username == "Gleb":
        text_area_value.send_keys("I’d like to introduce myself. My name is Gleb and I’m a financial advisor at Holliswealth. It seems like we know some of the same people. I am always looking to expand my network, and when I came across your profile, I was intrigued. Looking forward to connecting.\n–Thanks, Gleb.")
    if username == "David":
        text_area_value.send_keys("I’d like to introduce myself. My name is David, and I’m a Financial Advisor at DFSIN. It seems like we know some of the same people. I am always looking to expand my network, and when I came across your profile, I was intrigued. Looking forward to connecting.\n– Thanks,\nDavid.")
    if username == "Cara":
        text_area_value.send_keys("I'm Cara a Financial Advisor at Bloom Wealth & Legacy planning. I live & work locally and I'm looking to grow my network. I assess financial risk helping business owners and individuals make smart choices about money. I'd like to learn more about you & your business. Can we connect?")
    if username == "Tom":
        text_area_value.send_keys("I’d like to introduce myself. My name is Tom and I’m an Investment Advisor at McLean & Partners. It seems like we know some of the same people. I am always looking to expand my network, and when I came across your profile, I was intrigued. Looking forward to connecting. Thanks, Tom")
    if username == "Sam":
        text_area_value.send_keys("I'm Sam, a Financial Advisor at Ridgewood Investments. I live & work locally, and I'm looking to grow my network. I assess financial risk helping business owners and individuals make smart choices about money. I'd like to learn more about you & your business. Can we connect?")
    if username == "Lynn":
        text_area_value.send_keys("I’d like to introduce myself. My name is Lynn Trevisan, a Private Wealth Advisor at Raintree Financial Solutions. I am always looking to expand my network and was intrigued by your profile. Look forward to connecting! Thanks, Lynn")
    if username=="Alexis":
        text_area_value.send_keys("I’d like to introduce myself. My name is Alexis, and I’m an Investment Advisor at WFG Group. It seems like we know some of the same people. I am always looking to expand my network, and when I came across your profile, I was intrigued. Looking forward to connecting.– Thanks, Alexis")
    time.sleep(1)
    try:
        send_invitation_btn = browser.find_element_by_xpath('//*[@id="connect-dialog"]/div/form/div[2]/button[2]')
        if send_invitation_btn.is_enabled():
                send_invitation_btn.click()
        else:
            send_invitation_btn = browser.find_element_by_xpath('//*[@id="connect-dialog"]/div/form/div[3]/button[1]')
            send_invitation_btn.click()
            try:
                browser.switch_to.alert.accept()
                print('Alarm! ALARM!')
            except NoAlertPresentException:
                print('*crickets*')
    except NoSuchElementException as exception:
        send_invitation_btn = browser.find_element_by_xpath('//*[@id="connect-dialog"]/div/form/div[3]/button[1]')
        send_invitation_btn.click()
        try:
            browser.switch_to.alert.accept()
            print('Alarm! ALARM!')
        except NoAlertPresentException:
            print('*crickets*')
        print("i was here")
    try:
        temp = 1
        time.sleep(0.1)
        check_for_cancle = browser.find_element_by_xpath('//*[@id="connect-dialog"]/div/form/div[2]/button[1]')
        check_for_cancle.click()
    except NoSuchElementException as exception:
        temp = 0

    if temp ==1:
        try:
            browser.switch_to.alert.accept()
        except NoSuchElementException:
            print("Can't switch to alert window")



def open_save_search(save_search_name,amount_of_requestion,username):
    time.sleep(3)
    try:
        save_search_btn = browser.find_element_by_link_text("Saved Searches")
        hover = ActionChains(browser).move_to_element(save_search_btn)
        hover.perform()
    except NoSuchElementException as exception:
        try:
            time.sleep(2)
            save_search_btn = browser.find_element_by_class_name("global-nav-saved-searches-button")
            hover = ActionChains(browser).move_to_element(save_search_btn)
            hover.perform()
        except NoSuchElementException as exception:
            print("Not able to find save Search button")

    try:
        save_search_name_btn = browser.find_element_by_xpath('//*[@title="'+save_search_name+'"]').click()
    except NoSuchElementException as exception:
        print("Not able to find saved search name from list")
        exit(0)
    time.sleep(4)
    exclude_saved_leads()
#    browser.find_element_by_xpath('//*[@id="stream-container"]/div[1]/div[2]/section/div[3]/ul/li[7]/div/ol[2]/li[2]/a').click()
#    browser.find_element_by_xpath('//*[@id="stream-container"]/div[1]/div[2]/section/div[3]/ul/li[7]/div/ol[2]/li[4]/a').click()
    send_requestion_and_save_lead(amount_of_requestion,username)

###########
open_save_search('Save_search name',login('username','password'))
