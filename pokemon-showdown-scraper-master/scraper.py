import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://dex.pokemonshowdown.com/pokemon/")
search_input = browser.find_element_by_class_name("searchbox")

file = open("./pokemon-data/pokemon-all-data.csv", 'w')
file.write("Pokemon, Number, height, weight, HP, Attack, Defense, Sp. Atk, Sp. Def, Speed, total, Sprite\n")

with open('./names.json') as f:
  pokemon_names = json.loads(f.read())

for name in pokemon_names[0:1068]:
  search_input.clear()
  search_input.send_keys(name)
  search_input.send_keys(Keys.RETURN)

  pokemon = name
  number = browser.find_element_by_tag_name("code").text.replace("#", "")

  base_stats = browser.find_elements_by_class_name('stat')
  hp = base_stats[0].text
  attack = base_stats[1].text
  defense = base_stats[2].text
  special_atk = base_stats[3].text
  special_def = base_stats[4].text
  speed = base_stats[5].text
  
  total_stats = browser.find_elements_by_class_name('bst')
  total = total_stats[1].text
  size = browser.find_elements_by_class_name('sizeentry')
  height = ((((size[0].text).strip("Size:\n")).split("\n", 1)[0]).split(", ", 1)[0]).removesuffix(" m")
  weight = ((((size[0].text).strip("Size:\n")).split("\n", 1)[0]).split(", ", 1)[1]).removesuffix(" kg")

  sprite = browser.find_element_by_class_name("sprite").get_attribute("src")

  file.write(pokemon + "," + number + "," + height + "," + weight + "," + hp + "," 
    + attack + "," + defense + "," + special_atk 
    + "," + special_def + "," + speed + "," + total + "," + sprite 
    + "\n")

browser.close()
file.close()





