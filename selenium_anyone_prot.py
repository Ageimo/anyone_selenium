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
    #テスト内容
    def test_(self):
        self.base_url = ""

        ########################################################################
        ###キャプチャ関数
        ########################################################################
        
        def capture_html(name):
            #PNGkキャプチャ
            driver.save_screenshot('cap/'+name+'.png')
            #HTMLソース
            with codecs.open('cap/'+name+'.html', "w","utf-8") as f:
             f.write(driver.page_source)
            #番号
            print(name)
        def capture(name):
            #PNGkキャプチャ
            driver.save_screenshot('cap/'+name+'.png')
            #番号
            print(name)

        ########################################################################
        ###ダイアログの表示関数
        ########################################################################
        '''
        # ボタンのクリックイベント
        def input_dialog():
            root = Tkinter.Tk()
            root.title(u"URLを入力してください")
            root.geometry("400x300")

            #エントリー
            EditBox = Tkinter.Entry(width=50)
            EditBox.insert(Tkinter.END,u"https://miyakawa1.care-wing.jp")
            EditBox.pack()

            # ボタンが押されるとここが呼び出される
            def DeleteEntryValue(event):
                print EditBox.get()
                self.base_url=EditBox.get()

            #ボタン
            Button = Tkinter.Button(text=u'送信', width=50)
            Button.bind("<Button-1>",DeleteEntryValue) 
            #左クリック（<Button-1>）されると，DeleteEntryValue関数を呼び出すようにバインド
            Button.pack()

            root.mainloop()
        '''
        ########################################################################
        ###URLを読み込む関数
        ########################################################################
        def URL_read():
            str_URL=""
            f = open('URL.txt', 'r')
            for line in f:
                str_URL=str(line)  
            f.close()
            return str_URL
        ########################################################################
        ###textから実行分を読込んで実際に対応する関数
        ########################################################################
        def exe_read():
            str_URL=""
            f = open('Do_access.exepy', encoding='utf-8')
            for line in f:
                #中身を[tab]で分解する
                sentence = line.split('\t')
                input1="";#cap
                input2="";#手段
                input3="";#手段の詳細
                input4="";#手段の詳細2
                input5="";#実行内容
                input6="";#実行内容の詳細

                roop_num= 0;
                #文章をそれぞれの入力値へ分解
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

                #入力値から実行文作成
                #input2="";#手段
                #キャプチャ番号がないものは無視
                if input1 !="":
                    #選ぶ系
                    #xpath
                    if input2 == "xpath":
                       #指示をそのまま使う
                       if input5 == "click()":
                          driver.find_element_by_xpath(input3).click();
                       elif input5 == "clear()":
                          driver.find_element_by_xpath(input3).clear();
                       #テキストを足して使う
                       elif input5 == "send_keys()":
                          driver.find_element_by_xpath(input3).clear();
                          driver.find_element_by_xpath(input3).send_keys(str(input6));
                       elif input5 == "select_by_visible_text()":
                          driver.find_element_by_xpath(input3).select_by_visible_text(str(input6));                 
                          #task = "driver.find_element_by_xpath(input3)."+input5[:-2]+"(str(input6))";
                          #eval(task);
                    #id
                    elif input2 == "id":
                       #指示をそのまま使う
                       if input5 == "click()":
                          driver.find_element_by_id(input3).click();
                       elif input5 == "clear()":
                          driver.find_element_by_id(input3).clear();
                       #テキストを足して使う
                       elif input5 == "send_keys()":
                          driver.find_element_by_id(input3).clear();
                          driver.find_element_by_id(input3).send_keys(str(input6));
                       elif input5 == "select_by_visible_text()":
                          driver.find_element_by_id(input3).select_by_visible_text(str(input6));
                    #name
                    elif input2 == "name":
                       if input4 != "":
                           #指示をそのまま使う
                           if input5 == "click()":
                              driver.find_elements_by_name(input3)[int(input4)].click();
                           elif input5 == "clear()":
                              driver.find_elements_by_name(input3)[int(input4)].clear();
                           #テキストを足して使う
                           elif input5 == "send_keys()":
                              driver.find_elements_by_name(input3)[int(input4)].clear();
                              driver.find_elements_by_name(input3)[int(input4)].send_keys(str(input6));
                           elif input5 == "select_by_visible_text()":
                              driver.find_elements_by_name(input3)[int(input4)].select_by_visible_text(str(input6));
                       else:
                           #指示をそのまま使う
                           if input5 == "click()":
                              driver.find_element_by_name(input3).click();
                           elif input5 == "clear()":
                              driver.find_element_by_name(input3).clear();
                           #テキストを足して使う
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
                             #テキストを足して使う
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
                             #テキストを足して使う
                             elif input5 == "send_keys()":
                                driver.find_elements_by_class_name(str(input3))[int(input4)].clear();  
                                driver.find_elements_by_class_name(str(input3))[int(input4)].send_keys(str(input6));
                             elif input5 == "select_by_visible_text()":
                                driver.find_elements_by_class_name(str(input3))[int(input4)].select_by_visible_text(str(input6));                            
                            

                    #tagname
                    elif input2 == "tag":
                         #指示をそのまま使う
                         if input5 == "click()":
                            driver.find_element_by_tag_name(input3).click();
                         elif input5 == "clear()":
                            driver.find_element_by_tag_name(input3).clear();
                         #テキストを足して使う
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



                            
                    #スクリプト実行系
                    elif input2 == "ExecuteJavaScript":
                         driver.ExecuteJavaScript(input3, e);
                    elif input2 == "execute_script":
                         driver.execute_script(input3);

                    #画面制御系
                    elif input2 == "alert":
                         if input5 == "accept()":
                            Alert(driver).accept();
                         elif input5 == "accept()":
                              Alert(driver).dismiss();

                    #別タブへ移動
                    elif input2 == "next_tab":
                         this_window=driver.current_window_handle
                         driver.switch_to_window(this_window)
                         allHandles = driver.window_handles                        
                         driver.switch_to_window(allHandles[1])#次のタブ移動

                    #元タブへ戻る
                    elif input2 == "return_tab":
                         allHandles = driver.window_handles                        
                         driver.switch_to_window(allHandles[0])#元のタブ移動
                    #タブを閉じる
                    elif input2 == "tab_close":
                         driver.close()
                         allHandles = driver.window_handles
                         driver.switch_to_window(allHandles[0])#ハンドルを戻す
                         

                    #休憩する
                    elif input2 == "sleep":
                         this_window=driver.current_window_handle
                         driver.switch_to_window(this_window)
                         allHandles = driver.window_handles                        
                         time.sleep(int(input3))




                   

                      
                #キャプチャを取って終了
                #input1="";#cap
                #ダイアログ系の場合も考慮しtry/catchで
                if input1 !="":                              
                   try:
                       capture_html(str(input1))
                   except Exception as e:
                       print(str(input1)+" "+"キャプチャ保存に失敗しました/アラートダイアログが出ていた可能性があります。")
                time.sleep(0.5)
            f.close()
        ########################################################################
        ###テストケース
        ########################################################################
        ###ブラウザ準備
        self.base_url =URL_read()
        driver = webdriver.Chrome('chromedriver.exe');
        driver.get(self.base_url)
        driver.maximize_window()
        driver.implicitly_wait(30)        
        #実行開始
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
