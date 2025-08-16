#!/usr/bin/python3
""" Copyright© 2023-2025 LinuxUsersLinuxMint
PyAppDevKit Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
PyAppDevKit All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GitHub da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/PyAppDevKit
A Copy of This Software is published on GitHub To view: https://github.com/LinuxUsersLinuxMint/PyAppDevKit"""

from pyappdevkit.parameters import *
import os

"""
TR:
Uyarı: time() fonksiyonu gerçek bir zaman ölçümü yapmaz bunun yerine döngü oluşturarak bekleme süresi oluşturur bu yüzden bekleme süresi belirtilen süreden farklı olabilir. Eğer gerçek bir zaman ölçümü yapmak istiyorsanız bunun yerine Python programlama dilinde yerleşik olarak gelen time kütüphanesini kullanınız.

EN:
Warning: the time() function does not measure actual time, instead it loops and creates a waiting time, so the waiting time may be different from the specified time. If you want to measure real time, use the time library built into the Python programming language instead.
"""

def time(number,unit):
    while number > 0:
        number -= 1
        if unit == MS or unit == MILISECOND:
            for _ in range(100000):
                pass
        elif unit == S or unit == SECOND:
            for _ in range(100000000):
                pass
        elif unit == M or unit == MINUTE:
            for _ in range(100000000*60):
                pass
        elif unit == H or unit == HOUR:
            for _ in range(100000000*60*60):
                pass

def file(file_name,file_mode,file_write):
    create_file = open(file_name, file_mode)
    if file_mode == "w" or file_mode == "a":
        create_file.write("{0}\n". format(file_write))
    elif file_mode == "r":
        print(create_file.read())

def file_remove(file_name,file_path):
    if file_name != 0 or file_name != "":
        os.remove(file_name)
    else:
        os.remove(r"{0}". format(file_path))

def error_msg(error_dialog,error_code,support_link):
    print(error_dialog,error_code,support_link)

def exit_program_dialog_time(exit_dialog_msg,userTime,unit):
    print(exit_dialog_msg)
    time(userTime,unit=unit)
    exit()

def exit_program_time(userTime,unit):
    time(userTime,unit=unit)
    exit()

def exit_program_dialog(exit_dialog_msg):
    print(exit_dialog_msg)
    exit()

def all_exit(dialog_switch,lang,ExitSelectDialog,userTimeDialog,exitDialog,errormsgDialog,unit):
    if dialog_switch == ON:
        exit_select = int(input(ExitSelectDialog))
        if exit_select == 0:
            userTime = int(input(userTimeDialog))
            exit_program_dialog_time(exitDialog, userTime,unit=unit)
        elif exit_select == 1:
            userTime = int(input(userTimeDialog))
            exit_program_time(userTime,unit=unit)
        elif exit_select == 2:
            exit_program_dialog(exitDialog)
        elif exit_select == 3:
            exit()
        else:
            error_msg(errormsgDialog,"","")
    elif dialog_switch == OFF:
        if lang == EN:
            exit_select = int(input("Select the method to exit the program (0: Dialogue and Time entry, 1: Time entry only, 2: Dialogue entry only, 3: Normal exit (old style)): "))
            if exit_select == 0:
                userTime = int(input("After how many seconds should the program be closed?: "))
                exit_program_dialog_time("Exit program...", userTime,unit=unit)
            elif exit_select == 1:
                userTime = int(input("After how many seconds should the program be closed?: "))
                exit_program_time(userTime,unit=unit)
            elif exit_select == 2:
                exit_program_dialog("Exit program...")
            elif exit_select == 3:
                exit()
            else:
                error_msg("Invalid Command!","","")
        elif lang == TR:
            exit_select = int(input("Programdan çıkış yöntemini seçin (0: Diyalog ve Zaman girişi, 1: Yalnızca zaman girişi, 2: Yalnızca diyalog girişi, 3: Normal çıkış (eski stil)):  "))
            if exit_select == 0:
                userTime = int(input("Program kaç saniye sonra kapatılmalıdır?: "))
                exit_program_dialog_time("Programdan çıkılıyor...", userTime,unit=unit)
            elif exit_select == 1:
                userTime = int(input("Program kaç saniye sonra kapatılmalıdır?: "))
                exit_program_time(userTime,unit=unit)
            elif exit_select == 2:
                exit_program_dialog("Programdan çıkılıyor...")
            elif exit_select == 3:
                exit()
            else:
                error_msg("Geçersiz Komut!","","")

def app_info(dialog_one,dialog_one_t,dialog_two,dialog_two_t,dialog_three,dialog_three_t,dialog_four,dialog_four_t,dialog_five,dialog_five_t,dialog_six,dialog_six_t,dialog_seven,dialog_seven_t,dialog_eigth,dialog_eight_t,dialog_nine,dialog_nine_t,dialog_ten,dialog_ten_t):
    print("{0} {1}". format(dialog_one,dialog_one_t))
    print("{0} {1}". format(dialog_two,dialog_two_t))
    print("{0} {1}". format(dialog_three,dialog_three_t))
    print("{0} {1}". format(dialog_four,dialog_four_t))
    print("{0} {1}". format(dialog_five,dialog_five_t))
    print("{0} {1}". format(dialog_six,dialog_six_t))
    print("{0} {1}". format(dialog_seven,dialog_seven_t))
    print("{0} {1}". format(dialog_eigth,dialog_eight_t))
    print("{0} {1}". format(dialog_nine,dialog_nine_t))
    print("{0} {1}". format(dialog_ten,dialog_ten_t))

def program_welcome_msg(welcome_msg,cfg,cfg_,appname,libname,websitelink):
    print(welcome_msg)
    if cfg == 1:
        print(websitelink)
    elif cfg == 0:
        if cfg_ == "lib":
            app_info("Library Name: ",libname,"","","","","","","","","","","","","","","","","","")
        elif cfg_ == "app":
            app_info("Program Name: ",appname,"","","","","","","","","","","","","","","","","","")
        else:
            error_msg("Invalid definition!","","")
