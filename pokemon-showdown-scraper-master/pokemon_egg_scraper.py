import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://dex.pokemonshowdown.com/pokemon/")
search_input = browser.find_element_by_class_name("searchbox")

file = open("./pokemon-data/pokemon-egg-data.csv", 'w')
file.write("Pokemon, Egg-Group \n")

with open('./names.json') as f:
  pokemon_names = json.loads(f.read())

for name in pokemon_names[0:1068]:
  search_input.clear()
  search_input.send_keys(name)
  search_input.send_keys(Keys.RETURN)

  pokemon = name

  egg_groups = browser.find_elements_by_class_name('colentry')
  eggs = (egg_groups[0].text).removeprefix("Egg groups:\n")
  for egg in (eggs.split(", ", 1)):
    file.write(pokemon + "," + egg + "\n")

browser.close()
file.close()





