from selenium import webdriver

def extract_translation(web):
	driver = webdriver.Chrome('/Users/nicowolyniec/Desktop/chromedriver')
	driver.get(web)
	translation = driver.find_elements_by_xpath('//*[@id="dataset-english-spanish-cup"]/div[1]/div/span/div/div[2]/span/div/div[2]/div[1]/div/div/span/span')

	translation_text = []
	for i in range(len(translation)):
		translation_text.append(translation[i].text)

	driver.close()

	return translation_text

