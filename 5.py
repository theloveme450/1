import subprocess
import os
import time

os.system('sudo apt update')
time.sleep(5)
apt_packages = [
    "python3-pip",
    "xsel"]

for package in apt_packages:
    subprocess.run(["sudo", "apt", "install", "-y", package], check=True)

# تثبيت الحزم باستخدام pip
pip_packages = [
    "selenium",
    "pytz",
    "qrcode",
    "telebot",
    "webdriver_manager"
]

for package in pip_packages:
    subprocess.run(["pip", "install", package], check=True)
import shutil

import telebot
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import qrcode
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from random import randint
import sys
from datetime import datetime, date
import pytz
import random
import string
import zipfile
import os
import subprocess

# الآن يمكنك استخدام الحزم المثبتة في الكود الخاص بك

bot = telebot.TeleBot("6091291751:AAF9vBQZbwWkj2vKWvRUThq1o24uJSQaQ_o", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN
to_time = '5'
form_time = '10'
number_send_massage ='1'
stop_total_number = '1'
time_back_start = '10'
stop_code_exit='0'
#phone_message_data='hi'
def stop_code_bot():
    global driver
    try:
        stop_code_exit_2 = '1'
        if int(stop_code_exit_2) == int(stop_code_exit):
            all_windows = driver.window_handles
            for window in all_windows:
                try:
                    driver.switch_to.window(window)
                    driver.close()
                except Exception as ssdff:
                    print(ssdff)
                    print('اغلاق جميع المتصفحات')
                    try:
                        driver.close()
                    except:
                        pass
    except:
        print('ssssssssssssssss')
    

def login_whatsappnew(message):
    
    
    
    try:
        
        bot.reply_to(message, 'qrcode من فصلك انتظر هيتم الان ارسال ')
        options = Options()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.implicitly_wait(60)
        driver.get("https://web.whatsapp.com/")
        qr_element = driver.find_element(By.XPATH, "//div[@data-testid='qrcode']")
        data_ref = qr_element.get_attribute("data-ref")
        print(data_ref)
        img = qrcode.make(data_ref)
        type(img)
        img.save("download.png")
        time.sleep(1)
        bot.reply_to(message, 'تسجل الدخول  امسح qrcode من فضلك')
        photo = open("download.png", 'rb')
        bot.send_photo(message.chat.id, photo)
        driver.find_element(By.CSS_SELECTOR, '[data-testid="menu"]')
        bot.send_message(message.chat.id, 'تم تسجل الدخول بنجاح')
        #input('s')


    except Exception as ssdf:
        print(ssdf)
        msg = bot.send_message(message.chat.id, "من فضلك حاول مره اخر")
        try:
            driver.close()
        except:
            pass
@bot.message_handler(commands=['start'])
def main_menu(message):
    print('yes')
    markup_main_menu = InlineKeyboardMarkup()
    markup_main_menu.row_width = 2
    markup_main_menu.add(InlineKeyboardButton("الي ( {} )".format(to_time), callback_data="update_to_time"),
                         InlineKeyboardButton(" الارسال من الثانية ( {} )".format(form_time), callback_data="update_form_time"))
    
    #markup_main_menu.add(InlineKeyboardButton(" الارسال من الثانية ( {} )".format(form_time), callback_data="update_form_time"))
    markup_main_menu.row_width = 1
    markup_main_menu.add(InlineKeyboardButton("ارسال رساله نص", callback_data="send_namuber_massage_new"),
        InlineKeyboardButton("ارسال رساله نص وصوره".format(form_time), callback_data="send_namuber_massage_photo_new"))
    markup_main_menu.add(InlineKeyboardButton("ايقاف البوت", callback_data="update_stop_bot"))
    markup_main_menu.add(InlineKeyboardButton("الحصول علي التقرير", callback_data="update_get_report"))
    bot.send_message(message.chat.id, "القائمة الرئيسية", reply_markup=markup_main_menu)
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "update_to_time":
        msg = bot.send_message(call.message.chat.id, "يرجى إدخال الوقت الجديد من الثانية:")
        bot.register_next_step_handler(msg, update_to_time)
    elif call.data == "update_form_time":
        msg = bot.send_message(call.message.chat.id, "يرجى إدخال الوقت الجديد إلى الثانية:")
        bot.register_next_step_handler(msg, update_form_time)
    elif call.data == "send_namuber_massage_new":
        #login_whatsappnew(call.message)
        msg = bot.send_message(call.message.chat.id, "اكتب الارقام المراد الارسال اليها")
        bot.register_next_step_handler(msg, send_namuber_massage_new)

    elif call.data == "send_namuber_massage_photo_new":
        phone_msg = bot.send_message(call.message.chat.id, "اكتب الارقام المراد الارسال اليها")
        bot.register_next_step_handler(phone_msg, send_namuber_massage_photo_new)

    elif call.data == "update_stop_bot":
        update_stop_bot(call.message)
        
    elif call.data == "update_get_report":
        
        msg_report = bot.send_message(call.message.chat.id, "من فضلك اكتب رقم الشهر")
        bot.register_next_step_handler(msg_report, update_get_report)

def update_get_report(message):
    update_get_report_month = message.text
    msg_report_2 = bot.send_message(message.from_user.id, 'من فضلك اكتب رقم اليوم')
    bot.register_next_step_handler(msg_report_2, update_get_report_2, update_get_report_month)

def update_get_report_2(message, update_get_report_month):
    update_get_report_day = message.text
    try:
        
        for report_month_day_1 in os.listdir(os.getcwd()):
            report_month_day = report_month_day_1.split('.z')[-1]
            if report_month_day == 'ip':
                #print(report_month_day_1)
                data_month = report_month_day_1.split('month ')[-1].split(' day')[0]
                data_day = report_month_day_1.split('day ')[-1].split(' hour')[0]
                if data_month + data_day == update_get_report_month + update_get_report_day:
                    print(report_month_day_1)
                    with open(report_month_day_1, "rb") as file_month_day:
                        bot.send_document(message.chat.id, file_month_day)
        try:
            
            with open('تقرير بسيط الان.txt', "rb") as file_report_day:
                bot.send_document(message.chat.id, file_report_day)
        except:
            pass
        try:
            
            with open('نجح الارسال الان.txt', "rb") as file_sussod_day:
                
                bot.send_document(message.chat.id, file_sussod_day)
        except:
            pass
        try:
            with open('فشل الارسال الان.txt', "rb") as file_fluse_day:
                bot.send_document(message.chat.id, file_fluse_day)
        except:
            pass
    except Exception as ssdfsd:
        print(ssdfsd)
    bot.send_message(message.chat.id, "تم الانتهاء من ارسال جميع تقرير بنجاح نتمني ليك وقت سعيد")

    
#############################################
def send_namuber_massage_photo_new(message):
    totel_the_send_to_whatsapp_photo = message.text
    phone_msg_2  = bot.send_message (message.from_user.id, 'من فضلك اكتب الرساله المراد ارسالها')
    bot.register_next_step_handler (phone_msg_2, send_namuber_massage_new_photo,totel_the_send_to_whatsapp_photo)
    
def send_namuber_massage_new_photo(message,totel_the_send_to_whatsapp_photo):
    send_to_whatsapp_photo_and_massge = message.text
    phone_msg_3  = bot.send_message (message.from_user.id, 'من فضلك ارسال الصوره  المراد ارسالهم')
    bot.register_next_step_handler (phone_msg_3, send_namuber_send_photo,totel_the_send_to_whatsapp_photo,send_to_whatsapp_photo_and_massge)




def send_namuber_send_photo(message,totel_the_send_to_whatsapp_photo,send_to_whatsapp_photo_and_massge):
    
    try:
        
        photo_id = message.photo[-1].file_id
        file_info = bot.get_file(photo_id)
        downloaded_file = bot.download_file(file_info.file_path)
        print('2')
        # قم بحفظ الملف المُحمّل
        file_path_photo_send_2 = os.getcwd() #+ r'/photo'

        with open('{}/downloaded_photo.jpg'.format(file_path_photo_send_2), 'wb') as new_file:
            new_file.write(downloaded_file)
        print('2')        
            #totel_the_send_to_whatsapp = message.text
            
        bot.send_message(message.chat.id, 'من فضلك لا تقوم بفعل اي شي الانتظار سيتم الان ارسال التقرير')

        send_to_whatsappnew_list_2 = []

        for new_list_add_number_whatsapp_to_list_2 in totel_the_send_to_whatsapp_photo.splitlines():
            
            send_to_whatsappnew_list_2.append(new_list_add_number_whatsapp_to_list_2)
            print(new_list_add_number_whatsapp_to_list_2)
            
        chat_id_masngget = message.chat.id
        bot.reply_to(message, 'qrcode من فصلك انتظر هيتم الان ارسال ')
        options = webdriver.ChromeOptions()
        #options.headless = True
        options.add_argument('--no-sandbox')
        
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)

        driver.maximize_window()
        driver.implicitly_wait(60)
        driver.get("https://web.whatsapp.com/")
        time.sleep(15)
        qr_element = driver.find_element(By.XPATH, "//div[@data-testid='qrcode']")
        data_ref = qr_element.get_attribute("data-ref")
        print(data_ref)
        img = qrcode.make(data_ref)
        type(img)
        img.save("download.png")
        time.sleep(1)
        bot.reply_to(message, 'تسجل الدخول  امسح qrcode من فضلك')
        photo = open("download.png", 'rb')
        bot.send_photo(message.chat.id, photo)
        driver.find_element(By.CSS_SELECTOR, '[data-testid="menu"]')
        bot.send_message(message.chat.id, 'تم تسجل الدخول بنجاح')
        #input('s')
        bot.send_message(message.chat.id, 'من فضلك لا تقوم بفعل اي شي الانتظار سيتم الان ارسال التقرير')
        stop_code_bot()

        ##########################report##########################
        totel_send = 0
        totel_success = 0
        totel_failed = 0
        original_message = "هيتم الان ارسال التقرير"
        sent_message_repot_whatsapp = bot.send_message(message.chat.id, original_message)
        edited_message = original_message + " - تم التعديل"
        ##################################### totel_success####################################
        original_message_phone_totel_success = "الارقام التي نجح الارسال اليها" 

        sent_message_phone_totel_success = bot.send_message(message.chat.id,original_message_phone_totel_success)
            
        ########################################################## totel_failed ################################################
        original_message_phone_totel_failed = "الارقام الي فشل الارسال اليها" 

        sent_message_phone_totel_failed = bot.send_message(message.chat.id,original_message_phone_totel_failed)
        ##########################################################################
        send_to_whatsappnew_phone_totel_success = ''
        send_to_whatsappnew_phone_totel_failed = ''

        for phone in send_to_whatsappnew_list_2:
            
            try:
                stop_code_bot()
                totel_send +=1 
                driver.get("https://web.whatsapp.com/send?phone={}&text&type=phone_number".format(phone))
                            
                input_box = driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]')
                time.sleep(2)
                subprocess.run(f'echo "{send_to_whatsapp_photo_and_massge}" | xsel -b', shell=True)
                input_box.send_keys(Keys.CONTROL, 'v')#.send_keys(message_line)
                input_box.send_keys(Keys.SHIFT +Keys.ENTER)  # This will simulate a line break
                            
                timezone = pytz.timezone("Africa/Cairo")
                now = datetime.now(timezone)
                current_time = now.strftime("%I:%M:%S %p")
                current_date = date.today().strftime("%Y-%m-%d")
                current_day = now.strftime("%A")
                def generate_random_string(length):
                    letters = string.ascii_letters + string.digits
                    random_string = ''.join(random.choice(letters) for _ in range(length))
                    return random_string
                random_string = generate_random_string(6)

                random_whatsatpp =  current_date + ' '+random_string+' ' +'  '+current_day + ' '+current_time
                subprocess.run(f'echo "{random_whatsatpp}" | xsel -b', shell=True)
                input_box.send_keys(Keys.CONTROL, 'v')
                time.sleep(2)
                driver.find_element(By.CSS_SELECTOR, '[data-testid="clip"]').click()
                number_send_add_new = '/downloaded_photo.jpg'
                file_path_photo_send = os.getcwd() + '{}'.format(number_send_add_new)
                time.sleep(2)
                driver.find_element(By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]').send_keys(file_path_photo_send)
                time.sleep(2)
                driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div').click()
                time_wait = random.randrange(int(to_time), int(form_time))
                print(time_wait)
                time.sleep(time_wait)
                #input_box.send_keys(Keys.ENTER)
                driver.save_screenshot('{}.png'.format(phone))
                photo_2 = open("{}.png".format(phone), 'rb')
                bot.send_photo(chat_id_masngget, photo_2)
                #############################
                totel_success +=1
                edited_message_totel_report = "احمالي الارقام ({})  نجح الارسال ({})   فشل الارسال  ({}) ".format(totel_send,totel_success,totel_failed)        
                bot.edit_message_text(chat_id=sent_message_repot_whatsapp.chat.id, message_id=sent_message_repot_whatsapp.message_id, text=edited_message_totel_report)
                
                ###################################################################
                send_to_whatsappnew_phone_totel_success += '\n' + str(phone)
                edited_message_phone_totel_success = "{}\n{}".format(original_message_phone_totel_success, send_to_whatsappnew_phone_totel_success)
                bot.edit_message_text(chat_id=sent_message_phone_totel_success.chat.id, message_id=sent_message_phone_totel_success.message_id, text=edited_message_phone_totel_success)

                ########################
                bot.pin_chat_message(message.chat.id, sent_message_repot_whatsapp.message_id)
                bot.pin_chat_message(message.chat.id, sent_message_phone_totel_success.message_id)
                with open('نجح الارسال الان.txt' , 'a',encoding='utf-8') as result:
                    result.write("\n")
                    result.write(phone)
                with open("تقرير بسيط الان.txt" , "w") as file_report_smple_4:
                    file_report_smple_4.write("احمالي الارقام ({})  نجح الارسال ({})   فشل الارسال  ({}) ".format(str (totel_send),str(totel_success),str(totel_failed)))

            except Exception as ssdf:
                print(ssdf)
                totel_failed +=1
                time.sleep(1)
                #bot.send_message(message.chat.id, phone)
                #################################report########
                edited_message_totel_report = "احمالي الارقام ({})  نجح الارسال ({})   فشل الارسال  ({}) ".format(totel_send,totel_success,totel_failed)      
                bot.edit_message_text(chat_id=sent_message_repot_whatsapp.chat.id, message_id=sent_message_repot_whatsapp.message_id, text=edited_message_totel_report)
                
                ###################################phone####################
                send_to_whatsappnew_phone_totel_failed += '\n' + str(phone)
                edited_message_phone_totel_failed = "{}\n{}".format(original_message_phone_totel_failed, send_to_whatsappnew_phone_totel_failed)
                bot.edit_message_text(chat_id=sent_message_phone_totel_failed.chat.id, message_id=sent_message_phone_totel_failed.message_id, text=edited_message_phone_totel_failed)


                #########################pin##############################################
                bot.pin_chat_message(message.chat.id, sent_message_repot_whatsapp.message_id)
                bot.pin_chat_message(message.chat.id, sent_message_phone_totel_failed.message_id)
                with open('فشل الارسال الان.txt' , 'a',encoding='utf-8') as result:
                    result.write("\n")
                    result.write(phone)
                with open("تقرير بسيط الان.txt" , "w") as file_report_smple_5:
                    file_report_smple_5.write("احمالي الارقام ({})  نجح الارسال ({})   فشل الارسال  ({}) ".format(str (totel_send),str(totel_success),str(totel_failed)))

    except Exception as ssdf:
        print(ssdf)
        msg = bot.send_message(message.chat.id, "من فضلك حاول مره اخر")
        try:
            driver.close()
        except:
            pass
    try:
        driver.close()
    except:
        pass
    
    try:
        Message_success = "نجح الارسال.txt"
        Message_failed = "فشل الارسال.txt"
        report_Message_failed_sussfe="تقرير بسيط.txt"
        #photo_paths = send_to_whatsappnew_phone_totel_success
        timezone = pytz.timezone("Africa/Cairo")
        now = datetime.now(timezone)
        current_time = now.strftime("%I_%M_%S_%p")
        month = date.today().strftime("%m").lstrip('0')
        day = date.today().strftime("%d").lstrip('0')
        current_day = now.strftime("%A")
        
        zip_filename = "month {} day {} hour {} .zip".format(month,day,current_time)
        print(zip_filename)
        # كتابة أسماء الملفات في ملف نصي
        send_to_whatsappnew_phone_totel_failed += '\n'
        send_to_whatsappnew_phone_totel_success = send_to_whatsappnew_phone_totel_success.strip()
        with open(Message_success, "w") as txt_file:
            for  send_to_whatsappnew_phone_totel_success in send_to_whatsappnew_phone_totel_success:
                txt_file.write(send_to_whatsappnew_phone_totel_success)
        with open(Message_failed, "w") as txt_file_2:
            
            for send_to_whatsappnew_Message_failed in send_to_whatsappnew_phone_totel_failed:
                
                txt_file_2.write(send_to_whatsappnew_Message_failed)
                
        with open(report_Message_failed_sussfe, "w") as txt_file_3:
            
            txt_file_3.write(edited_message_totel_report)
        print('s')
        # إنشاء ملف ZIP وإضافة الصور وملف النص
        with open('نجح الارسال.txt') as f:
            
            mylis_ttotel_success = f.read().splitlines()
        with zipfile.ZipFile(zip_filename, "w") as zip_file:
            for mylis_ttotel_success_firest in mylis_ttotel_success:                
                mylis_ttotel_success_firest_2 = mylis_ttotel_success_firest+ '.png'
                print(mylis_ttotel_success_firest_2)
                zip_file.write(mylis_ttotel_success_firest_2, os.path.basename(mylis_ttotel_success_firest_2))
                #os.remove(mylis_ttotel_success_firest_2)
                #print('1221')
            #print('2')
            zip_file.write(Message_success, os.path.basename(Message_success))
            #print('3')
            zip_file.write(Message_failed, os.path.basename(Message_failed))
            zip_file.write(report_Message_failed_sussfe, os.path.basename(report_Message_failed_sussfe))
        #print('4')
        # حذف الصور الأصلية
        time.sleep(2)
        with open(zip_filename, "rb") as file:
            print('6')
            bot.send_document(message.chat.id, file)
        for photo_path_remove in mylis_ttotel_success:
            
            try:
                
                #os.remove(photo_path_remove + '.png')
                file_path_photo = photo_path_remove + '.png'
                print(file_path_photo)
                os.remove(file_path_photo)
                #shutil.rmtree(file_path_photo)
                print('finsh')
            except Exception as sssddf2d:
                print(sssddf2d)
                print('eroofile')

    except Exception as sssdd:
        print(sssdd)
    try:
        
        os.remove('نجح الارسال الان.txt')
            
    except:
        
        pass
    try:
        
        os.remove('فشل الارسال الان.txt')
            
    except:
            
        pass
    try:
        os.remove('تقرير بسيط الان.txt')
            
    except:
        pass 
    bot.send_message(message.chat.id, 'تم الانتهاء من ارسال الحمله الرسال نتمني وقت سعيد')
    main_menu(message)

##########################################
############## send_masgge_text####################
###################################################
####################################################
###################################################
def send_namuber_massage_new(message):
    totel_the_send_to_whatsapp = message.text
    msg_send_message_2  = bot.send_message (message.from_user.id, 'من فضلك اكتب الرساله المراد ارسالها')
    bot.register_next_step_handler (msg_send_message_2, send_namuber_massage_new_2,totel_the_send_to_whatsapp)
def send_namuber_massage_new_2(message,totel_the_send_to_whatsapp):
    try:
        
        phone_message_data=message.text
        
        send_to_whatsappnew_list = []
        for new_list_add_number_whatsapp_to_list in totel_the_send_to_whatsapp.splitlines():
            send_to_whatsappnew_list.append(new_list_add_number_whatsapp_to_list)
            print(new_list_add_number_whatsapp_to_list)
        stop_totel_number_stop_number = 0
        con_number_send = 0
        chat_id_masngget = message.chat.id
            #options.headless = True
        bot.reply_to(message, 'qrcode من فصلك انتظر هيتم الان ارسال ')
        options = webdriver.ChromeOptions()
        #options.headless = True
        options.add_argument('--no-sandbox')
        
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)          
        driver.maximize_window()
        driver.implicitly_wait(50)
        driver.get("https://web.whatsapp.com/")
        time.sleep(15)
        #driver.save_screenshot('1.png')
        qr_element = driver.find_element(By.XPATH, "//div[@data-testid='qrcode']")
        data_ref = qr_element.get_attribute("data-ref")
        print(data_ref)
        img = qrcode.make(data_ref)
        type(img)
        img.save("download.png")
        time.sleep(1)
        bot.reply_to(message, 'تسجل الدخول  امسح qrcode من فضلك')
        photo = open("download.png", 'rb')
        bot.send_photo(message.chat.id, photo)
        time.sleep(10)
        #driver.save_screenshot('2.png')
        driver.find_element(By.CSS_SELECTOR, '[data-testid="menu"]')
        bot.send_message(message.chat.id, 'تم تسجل الدخول بنجاح')
        #input('s')
        bot.send_message(message.chat.id, 'من فضلك لا تقوم بفعل اي شي الانتظار سيتم الان ارسال التقرير')
        stop_code_bot()
        ##########################report##########################
        totel_send = 0
        totel_success = 0
        totel_failed = 0
        original_message = "هيتم الان ارسال التقرير"
        sent_message_repot_whatsapp = bot.send_message(message.chat.id, original_message)
        edited_message = original_message + " - تم التعديل"
        ##################################### totel_success####################################
        original_message_phone_totel_success = "الارقام التي نجح الارسال اليها" 

        sent_message_phone_totel_success = bot.send_message(message.chat.id,original_message_phone_totel_success)
            
        ########################################################## totel_failed ################################################
        original_message_phone_totel_failed = "الارقام الي فشل الارسال اليها" 

        sent_message_phone_totel_failed = bot.send_message(message.chat.id,original_message_phone_totel_failed)
        ##########################################################################
        send_to_whatsappnew_phone_totel_success = ''
        send_to_whatsappnew_phone_totel_failed = ''
      
        for phone in send_to_whatsappnew_list:
            
            try:
                print(phone)
                stop_code_bot()
                totel_send +=1 
                time.sleep(2)
                driver.get("https://web.whatsapp.com/send?phone={}&text&type=phone_number".format(phone))                        
                input_box = driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]')
                time.sleep(2)
                subprocess.run(f'echo "{phone_message_data}" | xsel -b', shell=True)
                input_box.send_keys(Keys.CONTROL, 'v')
                input_box.send_keys(Keys.SHIFT +Keys.ENTER)
                timezone = pytz.timezone("Africa/Cairo")
                now = datetime.now(timezone)
                current_time = now.strftime("%I:%M:%S %p")
                current_date = date.today().strftime("%Y-%m-%d")
                current_day = now.strftime("%A")
                def generate_random_string(length):
                    letters = string.ascii_letters + string.digits
                    random_string = ''.join(random.choice(letters) for _ in range(length))
                    return random_string
                random_string = generate_random_string(6)
                random_whatsatpp =  current_date + ' '+random_string+' ' +'  '+current_day + ' '+current_time
                subprocess.run(f'echo "{random_whatsatpp}" | xsel -b', shell=True)
                input_box.send_keys(Keys.CONTROL, 'v')
                input_box.send_keys(Keys.SHIFT +Keys.ENTER)
                input_box.send_keys(Keys.ENTER)

                time_wait = random.randrange(int(to_time), int(form_time))
                print(time_wait)
                time.sleep(time_wait)
                driver.save_screenshot('{}.png'.format(phone))
                photo_2 = open("{}.png".format(phone), 'rb')
                bot.send_photo(chat_id_masngget, photo_2)
                #############################
                totel_success +=1
                edited_message_totel_report = "احمالي الارقام ({})  نجح الارسال ({})   فشل الارسال  ({}) ".format(totel_send,totel_success,totel_failed)        
                bot.edit_message_text(chat_id=sent_message_repot_whatsapp.chat.id, message_id=sent_message_repot_whatsapp.message_id, text=edited_message_totel_report)
                
                ###################################################################
                send_to_whatsappnew_phone_totel_success += '\n' + str(phone)
                edited_message_phone_totel_success = "{}\n{}".format(original_message_phone_totel_success, send_to_whatsappnew_phone_totel_success)
                bot.edit_message_text(chat_id=sent_message_phone_totel_success.chat.id, message_id=sent_message_phone_totel_success.message_id, text=edited_message_phone_totel_success)

                ########################
                bot.pin_chat_message(message.chat.id, sent_message_repot_whatsapp.message_id)
                bot.pin_chat_message(message.chat.id, sent_message_phone_totel_success.message_id)

                with open('نجح الارسال الان.txt' , 'a',encoding='utf-8') as result:
                    result.write("\n")
                    result.write(phone)
                with open("تقرير بسيط الان.txt" , "w") as file_report_smple_3:
                    file_report_smple_3.write("احمالي الارقام ({})  نجح الارسال ({})   فشل الارسال  ({}) ".format(str (totel_send),str(totel_success),str(totel_failed)))

            except Exception as ssdf:
                print(ssdf)
                totel_failed +=1
                time.sleep(1)
                #bot.send_message(message.chat.id, phone)
                #################################report########
                edited_message_totel_report = "احمالي الارقام ({})  نجح الارسال ({})   فشل الارسال  ({}) ".format(totel_send,totel_success,totel_failed)      
                bot.edit_message_text(chat_id=sent_message_repot_whatsapp.chat.id, message_id=sent_message_repot_whatsapp.message_id, text=edited_message_totel_report)
                
                ###################################phone####################
                send_to_whatsappnew_phone_totel_failed += '\n' + str(phone)
                edited_message_phone_totel_failed = "{}\n{}".format(original_message_phone_totel_failed, send_to_whatsappnew_phone_totel_failed)
                bot.edit_message_text(chat_id=sent_message_phone_totel_failed.chat.id, message_id=sent_message_phone_totel_failed.message_id, text=edited_message_phone_totel_failed)


                #########################pin##############################################
                bot.pin_chat_message(message.chat.id, sent_message_repot_whatsapp.message_id)
                bot.pin_chat_message(message.chat.id, sent_message_phone_totel_failed.message_id)
                with open('فشل الارسال الان.txt' , 'a',encoding='utf-8') as result:
                    result.write("\n")
                    result.write(phone)
                with open("تقرير بسيط الان.txt" , "w") as file_report_smple_2:
                    file_report_smple_2.write("احمالي الارقام ({})  نجح الارسال ({})   فشل الارسال  ({}) ".format(str (totel_send),str(totel_success),str(totel_failed)))

    except Exception as ssdf:
        print(ssdf)
        msg = bot.send_message(message.chat.id, "من فضلك حاول مره اخر")
        try:
            driver.close()
        except:
            pass
    try:
        driver.close()
    except:
        pass

#####################ثقرير zip################################
    try:
        Message_success = "نجح الارسال.txt"
        Message_failed = "فشل الارسال.txt"
        report_Message_failed_sussfe="تقرير بسيط.txt"
        #photo_paths = send_to_whatsappnew_phone_totel_success
        timezone = pytz.timezone("Africa/Cairo")
        now = datetime.now(timezone)
        current_time = now.strftime("%I_%M_%S_%p")
        month = date.today().strftime("%m").lstrip('0')
        day = date.today().strftime("%d").lstrip('0')
        current_day = now.strftime("%A")
        
        zip_filename = "month {} day {} hour {} .zip".format(month,day,current_time)
        print(zip_filename)
        # كتابة أسماء الملفات في ملف نصي
        send_to_whatsappnew_phone_totel_failed += '\n'
        send_to_whatsappnew_phone_totel_success = send_to_whatsappnew_phone_totel_success.strip()
        with open(Message_success, "w") as txt_file:
            for  send_to_whatsappnew_phone_totel_success in send_to_whatsappnew_phone_totel_success:
                txt_file.write(send_to_whatsappnew_phone_totel_success)
        with open(Message_failed, "w") as txt_file_2:
            
            for send_to_whatsappnew_Message_failed in send_to_whatsappnew_phone_totel_failed:
                
                txt_file_2.write(send_to_whatsappnew_Message_failed)
                
        with open(report_Message_failed_sussfe, "w") as txt_file_3:
            
            txt_file_3.write(edited_message_totel_report)
        print('s')
        # إنشاء ملف ZIP وإضافة الصور وملف النص
        with open('نجح الارسال.txt') as f:
            
            mylis_ttotel_success = f.read().splitlines()
        with zipfile.ZipFile(zip_filename, "w") as zip_file:
            for mylis_ttotel_success_firest in mylis_ttotel_success:                
                mylis_ttotel_success_firest_2 = mylis_ttotel_success_firest+ '.png'
                print(mylis_ttotel_success_firest_2)
                zip_file.write(mylis_ttotel_success_firest_2, os.path.basename(mylis_ttotel_success_firest_2))
                #os.remove(mylis_ttotel_success_firest_2)
                #print('1221')
            #print('2')
            zip_file.write(Message_success, os.path.basename(Message_success))
            #print('3')
            zip_file.write(Message_failed, os.path.basename(Message_failed))
            zip_file.write(report_Message_failed_sussfe, os.path.basename(report_Message_failed_sussfe))
        #print('4')
        # حذف الصور الأصلية
        time.sleep(2)
        with open(zip_filename, "rb") as file:
            print('6')
            bot.send_document(message.chat.id, file)
        for photo_path_remove in mylis_ttotel_success:
            
            try:
                
                #os.remove(photo_path_remove + '.png')
                file_path_photo = photo_path_remove + '.png'
                print(file_path_photo)
                os.remove(file_path_photo)
                #shutil.rmtree(file_path_photo)
                print('finsh')
            except Exception as sssddf2d:
                print(sssddf2d)
                print('eroofile')

    except Exception as sssdd:
        print(sssdd)
    try:
        
        os.remove('نجح الارسال الان.txt')
            
    except:
        
        pass
    try:
        
        os.remove('فشل الارسال الان.txt')
            
    except:
            
        pass
    try:
        os.remove('تقرير بسيط الان.txt')
            
    except:
        pass  
    bot.send_message(message.chat.id, 'تم الانتهاء من ارسال الحمله الرسال نتمني وقت سعيد')
    main_menu(message)


#######################
##########################################
############## send_masgge_text####################
###################################################
####################################################
###################################################




def update_to_time(message):
    global to_time
    to_time = message.text
    bot.send_message(message.chat.id, f"تم تحديث الوقت من إلى {to_time}")
    main_menu(message)
def update_form_time(message):
    global form_time
    form_time = message.text
    bot.send_message(message.chat.id, f"تم تحديث الوقت إلى {form_time}")
    main_menu(message)
def update_stop_bot(message):
    #global is_running
    #global driver
    stop_code_exit = '1'
    bot.send_message(message.chat.id, f"من فضلك انتظر (40) ثوني سيتم ابلاغك عند الانتهاء من اغلاق بوت")

    try:
        for s in range(3):
            try:
                
                time.sleep(2)
                subprocess.run('pkill chrome', shell=True, check=True)
            except:
                pass

        bot.send_message(message.chat.id, f"تم الانتهاء من اغلاق البوت وتم تشغله مره تاني")
    except Exception as sfsds:
        print(sfsds)
    main_menu(message)
    

for affdsd in range(9999999999999999999999999):
    
    try:
        print(affdsd)
        time.sleep(50)
        bot.polling()
    except Exception as ssssssdf:
        print(ssssssdf)
        continue
    

