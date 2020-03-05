"""
页面元素属性封装
"""

from selenium.webdriver.common.by import By

# 首页页面
mine = By.XPATH, '//*[contains(@text, "我的")]'  # 我的

# 我的首页
login = By.XPATH, '//[contains(@text, "登录")]'  # 登录/注册

# 登陆页面
phone = By.ID, 'com.bjcsxq.chat.carfriend:id/login_phone_et'
pwd = By.ID, 'com.bjcsxq.chat.carfriend:id/login_pwd_et'
login_bth = By.ID, 'com.bjcsxq.chat.carfriend:id/login_btn'
comfirm_bth = By.ID, 'com.bjcsxq.chat.carfriend:id/bth_neg'
