# Automatické zalievanie rastlín pomocou Raspberry Pi
Zalievanie je riadené pythonovým skriptom ktoré dokážeme polievať cez webové rozhranie.

Na riadenie GPIO pinov na raspberry je použitá pythonová knižnica RPi.GPIO.

### `Webové rozhranie pôsobí minimalisticky, okrem day/night módu tam sú iba potrebné funkcie ako:`

-Kedy bola naposledy rastlina zaliata (po každom zaliatí sa táto informácia ukladá do samostatného txt súboru odkiaľ to táto funkcia číta)

-Senzor či je dostatok vody v kvetináči

-Jednorázové zaliatie

-Automatické zalievanie (zaleje rastlinu vždy keď senzor ukáže že nieje dostatok vody)

-Vypnutie automatického zalievania
  
![alt text](https://github.com/kecerud/Automaticke-zalievanie-rastlin/blob/main/assets/day-mode.png?raw=true)
  
![alt text](https://github.com/kecerud/Automaticke-zalievanie-rastlin/blob/main/assets/night-mode.png?raw=true)
  
![alt text](https://github.com/kecerud/Automaticke-zalievanie-rastlin/blob/main/assets/final.jpg?raw=true)
  
![alt text](https://github.com/kecerud/Automaticke-zalievanie-rastlin/blob/main/assets/inside-1.jpg?raw=true)
  
![alt text](https://github.com/kecerud/Automaticke-zalievanie-rastlin/blob/main/assets/inside-2.jpg?raw=true)
  
![alt text](https://github.com/kecerud/Automaticke-zalievanie-rastlin/blob/main/assets/model.png?raw=true)
