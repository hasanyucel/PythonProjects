from selenium import webdriver		
from PIL import Image	

driver = webdriver.Chrome(executable_path="chromedriver.exe")	

def test(website,pic_id):	
    driver.get(website)	
    captcha_kaydet("/html/body/img",""+pic_id)	

def captcha_kaydet(xpath_id,pic_id): #img ile biten full xpathle ve captcha id göndermek yeterli olacaktır. 	
    # os.mkdir("captchas")	
    ele = driver.find_element_by_xpath(xpath_id)	
    loc1 = ele.location	
    driver.save_screenshot("captchas/"+pic_id+".png")	
    image = Image.open("captchas/"+pic_id+".png")	
    left = loc1['x'] + 5
    top = loc1['y']	
    right = loc1['x'] + 240	
    bottom1 = loc1['y'] + 46	
    image = image.crop((left,top,right,bottom1))	
    image.save("captchas/"+pic_id+".png")  
i=1
while (i<10000):
    test("https://biz1.samsungcsportal.com/simpleCaptcha.cha",""+str(i))
    i = i + 1