 /* To show all Tables: .tables */
 How many total Characters are there?
 select COUNT(character_id) from charactercreator_character ; /* 302 */

 How many of each specific subclass?
 select count(character_id) as number_mages from charactercreator_character inner join charactercreator_mage on character_ptr_id = character_id /* 108 */

 How many total Items?
 select count(item_id) as number_items from armory_item /* 174 */

 How many of the Items are weapons? How many are not?
 select count(item_ptr_id) from armory_weapon /* 37, 137 */

 On average, how many Items does each Character have?
 select (count(item_id) / count(character_id)) as average from charactercreator_character, armory_item ;


 On average, how many Weapons does each character have?
 select (count(item_ptr_id) / count(character_id)) as average from charactercreator_character, armory_weapon ;