import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://dex.pokemonshowdown.com/pokemon/")
search_input = browser.find_element_by_class_name("searchbox")

file = open("./pokemon-data/pokemon-move-data.csv", 'w')
file.write("Pokemon, Move, Source \n")

with open('./names.json') as f:
  pokemon_names = json.loads(f.read())

for name in pokemon_names[0:1068]:
  search_input.clear()
  search_input.send_keys(name)
  search_input.send_keys(Keys.RETURN)

  pokemon = name

  
  moves = browser.find_elements_by_css_selector("ul.utilichart.nokbd > li")
  source_temp = ""
  for move_tmp in moves:
    if "Accuracy" not in move_tmp.text:
      if "Level" in move_tmp.text:
        source_temp = "level "
      if "TM" in move_tmp.text:
        source_temp = "TM"
      if "Tutor" in move_tmp.text:
        source_temp = "move tutor"
      if "Egg" in move_tmp.text:
        source_temp = "egg move"
      if "Past" in move_tmp.text:
        source_temp = "Past generation only"
      if "Event" in move_tmp.text:
        source_temp = "Event"

    else:

      move = (move_tmp.text).split("\n", 2)[1]
      if move == "Power" or move == "Accuracy":
        move = (move_tmp.text).split("\n", 2)[0]


      if source_temp == "level ":
        source_tmp = (move_tmp.text).split("\n", 2)[0]
        if "L" in source_tmp:
          source = source_temp + source_tmp.removeprefix("L")
        elif source_tmp == "–":
          source = source_temp + "1"
      else:
        source = source_temp
      
      file.write(pokemon + "," + move + "," + source + "\n")


browser.close()
file.close()





