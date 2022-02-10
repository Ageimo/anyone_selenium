# -*- coding: shift-jis -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.alert import Alert
from datetime import datetime
from datetime import date


import unittest, time, re
import codecs
import os, sys
#import Tkinter

class selenium_TEST(unittest.TestCase):
    #�e�X�g���e
    def test_(self):
        self.base_url = ""

        ########################################################################
        ###�L���v�`���֐�
        ########################################################################
        
        def capture_html(name):
            #PNGk�L���v�`��
            driver.save_screenshot('cap/'+name+'.png')
            #HTML�\�[�X
            with codecs.open('cap/'+name+'.html', "w","utf-8") as f:
             f.write(driver.page_source)
            #�ԍ�
            print(name)
        def capture(name):
            #PNGk�L���v�`��
            driver.save_screenshot('cap/'+name+'.png')
            #�ԍ�
            print(name)

        ########################################################################
        ###�_�C�A���O�̕\���֐�
        ########################################################################
        '''
        # �{�^���̃N���b�N�C�x���g
        def input_dialog():
            root = Tkinter.Tk()
            root.title(u"URL����͂��Ă�������")
            root.geometry("400x300")

            #�G���g���[
            EditBox = Tkinter.Entry(width=50)
            EditBox.insert(Tkinter.END,u"https://miyakawa1.care-wing.jp")
            EditBox.pack()

            # �{�^�����������Ƃ������Ăяo�����
            def DeleteEntryValue(event):
                print EditBox.get()
                self.base_url=EditBox.get()

            #�{�^��
            Button = Tkinter.Button(text=u'���M', width=50)
            Button.bind("<Button-1>",DeleteEntryValue) 
            #���N���b�N�i<Button-1>�j�����ƁCDeleteEntryValue�֐����Ăяo���悤�Ƀo�C���h
            Button.pack()

            root.mainloop()
        '''
        ########################################################################
        ###URL��ǂݍ��ފ֐�
        ########################################################################
        def URL_read():
            str_URL=""
            f = open('URL.txt', 'r')
            for line in f:
                str_URL=str(line)  
            f.close()
            return str_URL
        ########################################################################
        ###text������s����Ǎ���Ŏ��ۂɑΉ�����֐�
        ########################################################################
        def exe_read():
            str_URL=""
            f = open('Do_access.exepy', encoding='utf-8')
            for line in f:
                #���g��[tab]�ŕ�������
                sentence = line.split('\t')
                input1="";#cap
                input2="";#��i
                input3="";#��i�̏ڍ�
                input4="";#��i�̏ڍ�2
                input5="";#���s���e
                input6="";#���s���e�̏ڍ�

                roop_num= 0;
                #���͂����ꂼ��̓��͒l�֕���
                for input in sentence:
                    roop_num =roop_num+1;
                    if roop_num==1:
                       input1=str(input) 
                    if roop_num==2:
                       input2=str(input) 
                    if roop_num==3:
                       input3=str(input) 
                    if roop_num==4:
                       input4=str(input) 
                    if roop_num==5:
                       input5=str(input) 
                    if roop_num==6:
                       input6=str(input)

                #���͒l������s���쐬
                #input2="";#��i
                #�L���v�`���ԍ����Ȃ����͖̂���
                if input1 !="":
                    #�I�Ԍn
                    #xpath
                    if input2 == "xpath":
                       #�w�������̂܂܎g��
                       if input5 == "click()":
                          driver.find_element_by_xpath(input3).click();
                       elif input5 == "clear()":
                          driver.find_element_by_xpath(input3).clear();
                       #�e�L�X�g�𑫂��Ďg��
                       elif input5 == "send_keys()":
                          driver.find_element_by_xpath(input3).clear();
                          driver.find_element_by_xpath(input3).send_keys(str(input6));
                       elif input5 == "select_by_visible_text()":
                          driver.find_element_by_xpath(input3).select_by_visible_text(str(input6));                 
                          #task = "driver.find_element_by_xpath(input3)."+input5[:-2]+"(str(input6))";
                          #eval(task);
                    #id
                    elif input2 == "id":
                       #�w�������̂܂܎g��
                       if input5 == "click()":
                          driver.find_element_by_id(input3).click();
                       elif input5 == "clear()":
                          driver.find_element_by_id(input3).clear();
                       #�e�L�X�g�𑫂��Ďg��
                       elif input5 == "send_keys()":
                          driver.find_element_by_id(input3).clear();
                          driver.find_element_by_id(input3).send_keys(str(input6));
                       elif input5 == "select_by_visible_text()":
                          driver.find_element_by_id(input3).select_by_visible_text(str(input6));
                    #name
                    elif input2 == "name":
                       if input4 != "":
                           #�w�������̂܂܎g��
                           if input5 == "click()":
                              driver.find_elements_by_name(input3)[int(input4)].click();
                           elif input5 == "clear()":
                              driver.find_elements_by_name(input3)[int(input4)].clear();
                           #�e�L�X�g�𑫂��Ďg��
                           elif input5 == "send_keys()":
                              driver.find_elements_by_name(input3)[int(input4)].clear();
                              driver.find_elements_by_name(input3)[int(input4)].send_keys(str(input6));
                           elif input5 == "select_by_visible_text()":
                              driver.find_elements_by_name(input3)[int(input4)].select_by_visible_text(str(input6));
                       else:
                           #�w�������̂܂܎g��
                           if input5 == "click()":
                              driver.find_element_by_name(input3).click();
                           elif input5 == "clear()":
                              driver.find_element_by_name(input3).clear();
                           #�e�L�X�g�𑫂��Ďg��
                           elif input5 == "send_keys()":
                              driver.find_element_by_name(input3).clear();
                              driver.find_element_by_name(input3).send_keys(str(input6));
                           elif input5 == "select_by_visible_text()":
                              driver.find_element_by_name(input3).select_by_visible_text(str(input6));
                          
                          
                    #class
                    elif input2 == "class":
                        if input4 != "":
                             if input5 == "click()":
                                driver.find_element_by_class_name(str(input3)).click();
                             elif input5 == "clear()":
                                driver.find_element_by_class_name(str(input3)).clear();                        
                             #�e�L�X�g�𑫂��Ďg��
                             elif input5 == "send_keys()":
                                driver.find_element_by_class_name(str(input3)).clear();  
                                driver.find_element_by_class_name(str(input3)).send_keys(str(input6));
                             elif input5 == "select_by_visible_text()":
                                driver.find_element_by_class_name(str(input3)).select_by_visible_text(str(input6));
                        else:
                             if input5 == "click()":
                                #print(str(input3));
                                #print(driver.find_elements_by_class_name(str(input3))[int(input4)]);
                                driver.find_elements_by_class_name(str(input3))[int(input4)].click();
                             elif input5 == "clear()":
                                driver.find_elements_by_class_name(str(input3))[int(input4)].clear();                        
                             #�e�L�X�g�𑫂��Ďg��
                             elif input5 == "send_keys()":
                                driver.find_elements_by_class_name(str(input3))[int(input4)].clear();  
                                driver.find_elements_by_class_name(str(input3))[int(input4)].send_keys(str(input6));
                             elif input5 == "select_by_visible_text()":
                                driver.find_elements_by_class_name(str(input3))[int(input4)].select_by_visible_text(str(input6));                            
                            

                    #tagname
                    elif input2 == "tag":
                         #�w�������̂܂܎g��
                         if input5 == "click()":
                            driver.find_element_by_tag_name(input3).click();
                         elif input5 == "clear()":
                            driver.find_element_by_tag_name(input3).clear();
                         #�e�L�X�g�𑫂��Ďg��
                         elif input5 == "send_keys()":
                            driver.find_element_by_tag_name(input3).clear();
                            driver.find_element_by_tag_name(input3).send_keys(str(input6));
                         elif input5 == "select_by_visible_text()":
                            driver.find_element_by_tag_name(input3).select_by_visible_text(str(input6));
                            
                    #linktext
                    elif input2 == "link":
                         if input5 == "click()":
                            #print(driver.find_element_by_link_text(str(input3)));
                            driver.find_element_by_link_text(input3).click();



                            
                    #�X�N���v�g���s�n
                    elif input2 == "ExecuteJavaScript":
                         driver.ExecuteJavaScript(input3, e);
                    elif input2 == "execute_script":
                         driver.execute_script(input3);

                    #��ʐ���n
                    elif input2 == "alert":
                         if input5 == "accept()":
                            Alert(driver).accept();
                         elif input5 == "accept()":
                              Alert(driver).dismiss();

                    #�ʃ^�u�ֈړ�
                    elif input2 == "next_tab":
                         this_window=driver.current_window_handle
                         driver.switch_to_window(this_window)
                         allHandles = driver.window_handles                        
                         driver.switch_to_window(allHandles[1])#���̃^�u�ړ�

                    #���^�u�֖߂�
                    elif input2 == "return_tab":
                         allHandles = driver.window_handles                        
                         driver.switch_to_window(allHandles[0])#���̃^�u�ړ�
                    #�^�u�����
                    elif input2 == "tab_close":
                         driver.close()
                         allHandles = driver.window_handles
                         driver.switch_to_window(allHandles[0])#�n���h����߂�
                         

                    #�x�e����
                    elif input2 == "sleep":
                         this_window=driver.current_window_handle
                         driver.switch_to_window(this_window)
                         allHandles = driver.window_handles                        
                         time.sleep(int(input3))




                   

                      
                #�L���v�`��������ďI��
                #input1="";#cap
                #�_�C�A���O�n�̏ꍇ���l����try/catch��
                if input1 !="":                              
                   try:
                       capture_html(str(input1))
                   except Exception as e:
                       print(str(input1)+" "+"�L���v�`���ۑ��Ɏ��s���܂���/�A���[�g�_�C�A���O���o�Ă����\��������܂��B")
                time.sleep(0.5)
            f.close()
        ########################################################################
        ###�e�X�g�P�[�X
        ########################################################################
        ###�u���E�U����
        self.base_url =URL_read()
        driver = webdriver.Chrome('chromedriver.exe');
        driver.get(self.base_url)
        driver.maximize_window()
        driver.implicitly_wait(30)        
        #���s�J�n
        exe_read()

        driver.quit()

        
    ##############################################################
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    '''
    def capture_html(self,name):
        Test.self.driver.save_screenshot('cap/'+name+'.png')
        with codecs.open('cap/'+name+'.html', "w","utf-8") as f:
         f.write(Test.self.driver.page_source)
    '''
    
    ##############################################################
if __name__ == "__main__":
    unittest.main()
