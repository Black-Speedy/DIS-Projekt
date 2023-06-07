import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://dex.pokemonshowdown.com/moves/")
search_input = browser.find_element_by_class_name("searchbox")

file = open("./pokemon-data/move-data.csv", 'w')
file.write("Move, type, Category, Power, Accuracy, Power Points \n")

with open('./move_names.json') as f:
  move_names = json.loads(f.read())

for name in move_names[0:837]:
  search_input.clear()
  search_input.send_keys(name)
  search_input.send_keys(Keys.RETURN)

  move = name
  
  types = browser.find_elements_by_class_name("type")
  type = types[0].text
  category = types[1].text
  
  power_tmp = browser.find_elements_by_class_name("powerentry")
  if len(power_tmp) == 1:
    power = (power_tmp[0].text).strip("Base power:\n")
    if power == "—":
      power = "none"
  else:
    power = "none"
  
  accuracy_tmp = browser.find_elements_by_class_name("accuracyentry")
  accuracy = ((accuracy_tmp[0].text).strip("Accuracy:\n")).removesuffix("%")
  if accuracy == "—":
    accuracy = "none"

  PP_tmp = browser.find_elements_by_class_name("ppentry")
  PP = (((PP_tmp[0].text).strip("PP:\n"))[0:2]).removesuffix("\n")
  
  file.write(move + "," + type + "," + category + "," + power + "," + 
    accuracy + "," + PP + "\n")

browser.close()
file.close()





