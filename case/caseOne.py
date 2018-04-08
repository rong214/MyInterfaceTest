# -*- coding: utf-8 -*-
__author__ = 'tyr'
from framework.send_email import SendEmail

excel_path = 'E:/PythonFile/MyInterfaceTest/excels/tyr_testcase.xlsx'
excel_name = 'tyr_testcase.xlsx'
jpg_path = 'E:/PythonFile/MyInterfaceTest/pictures/test.jpg'
jpg_name = 'test.jpg'
from_email = 'xxx'
to_email = 'xxx'
pwd = 'xxx'
title = 'Interview invitation'
content = 'Congratulations, after the interview, please come to work'
smtp_server = 'smtp.126.com'
port = 25
mail = SendEmail()
mail.send_email(title, from_email, to_email,pwd, content, smtp_server, port, excel_path, excel_name, jpg_path, jpg_name)


