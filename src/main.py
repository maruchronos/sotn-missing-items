# Initial Values
memCard = "Castlevania - Symphony of the Night.srm"
columnSize = 16
bufferSize = 1
rareItemsAddress = int("0x6878", 0)
imageURL = 'http://www.deixadilson.com/sotn/enemies/'
enemies = ["Dracula", "Blood Skeleton", "Bat", "Stone Skull", "Zombie", "Merman", "Skeleton", "Warg", "Bone Scimitar", "Merman", "Spittle Bone", "Axe Knight", "Bloody Zombie", "Slinger", "Ouija Table", "Skelerang", "Thornweed", "Gaibon", "Ghost", "Marionette", "Slogra", "Diplocephalus", "Flea Man", "Medusa Head", "Blade Soldier", "Bone Musket", "Medusa Head", "Plate Lord", "Stone Rose", "Axe Knight", "Ctulhu", "Bone Archer", "Bone Pillar", "Doppleganger10", "Owl", "Phantom Skull", "Scylla wyrm", "Skeleton Ape", "Spear Guard", "Spellbook", "Winged Guard", "Ectoplasm", "Sword Lord", "Toad", "Armor Lord", "Corner Guard", "Dhuron", "Frog", "Frozen Shade", "Magic Tome", "Skull Lord", "Black Crow", "Blue Raven", "Corpseweed", "Flail Guard", "Flea Rider", "Spectral Sword", "Bone Halberd", "Scylla", "Hunting Girl", "Mudman", "Owl Knight", "Spectral Sword", "Vandal Sword", "Flea Armor", "Hippogryph", "Paranthropus", "Slime", "Blade Master", "Wereskeleton", "Grave Keeper", "Gremlin", "Harpy", "Minotaurus", "Werewolf", "Bone Ark", "Valhalla Knight", "Cloaked Knight", "Fishhead", "Lesser Demon", "Lossoth", "Salem Witch", "Blade", "Gurkha", "Hammer", "Discus Lord", "Karasuman", "Large Slime", "Hellfire Beast", "Cerberos", "Killer Fish", "Olrox", "Succubus", "Tombstone", "Venus Weed", "Lion", "Scarecrow", "Granfaloon", "Schmoo", "Tin man", "Balloon pod", "Yorick", "Bomb Knight", "Flying Zombie", "Bitterfly", "Jack O' Bones", "Archer", "Werewolf", "Black Panther", "Darkwing Bat", "Dragon Rider", "Minotaur", "Nova Skeleton", "Orobourous", "White Dragon", "Fire Warg", "Rock Knight", "Sniper of Goth", "Spectral Sword", "Ghost Dancer", "Warg Rider", "Cave Troll", "Dark Octopus", "Fire Demon", "Gorgon", "Malachi", "Akmodan II", "Blue Venus Weed", "Doppleganger40", "Medusa", "The Creature", "Fake Grant", "Fake Trevor", "Imp", "Fake Sypha", "Beezelbub", "Azaghal", "Frozen Half", "Salome", "Richter Belmont", "Dodo Bird", "Galamoth", "Guardian", "Death", "Shaft"]
nonDroppersIndex = [0, 1, 3, 7, 10, 17, 20, 33, 34, 36, 58, 60, 65, 67, 73, 87, 89, 91, 92, 97, 100, 109, 110, 114, 120, 126, 128, 129, 130, 131, 132, 134, 135, 139, 141, 143, 144]
enemyImages = ["dracula.png", "blood-skeleton.png", "bat.png", "stone-skull.png", "zombie.png", "merman2.png", "skeleton.png", "warg.png", "bone-scimitar.png", "merman3.png", "spittle-bone.png", "axe-knight4.png", "bloody-zombie.png", "slinger.png", "ouija-table.png", "skelerang.png", "thornweed.png", "gaibon.png", "ghost.png", "marionette.png", "slogra.png", "diplocephalus.png", "flea-man.png", "medusa-head7.png", "blade-soldier.png", "bone-musket.png", "medusa-head8.png", "plate-lord.png", "stone-rose.png", "axe-knight9.png", "ctulhu.png", "bone-archer.png", "bone-pillar.png", "doppleganger10.png", "owl.png", "phantom-skull.png", "scylla-wyrm.png", "skeleton-ape.png", "spear-guard.png", "spellbook.png", "winged-guard.png", "ectoplasm.png", "sword-lord.png", "toad.png", "armor-lord.png", "corner-guard.png", "dhuron.png", "frog.png", "frozen-shade.png", "magic-tome.png", "skull-lord.png", "black-crow.png", "blue-raven.png", "corpseweed.png", "flail-guard.png", "flea-rider.png", "spectral-sword13.png", "bone-halberd.png", "scylla.png", "hunting-girl.png", "mudman.png", "owl-knight.png", "spectral-sword15.png", "vandal-sword.png", "flea-armor.png", "hippogryph.png", "paranthropus.png", "slime.png", "blade-master.png", "wereskeleton.png", "grave-keeper.png", "gremlin.png", "harpy.png", "minotaurus.png", "werewolf18.png", "bone-ark.png", "valhalla-knight.png", "cloaked-knight.png", "fishhead.png", "lesser-demon.png", "lossoth.png", "salem-witch.png", "blade.png", "gurkha.png", "hammer.png", "discus-lord.png", "karasuman.png", "large-slime.png", "hellfire-beast.png", "cerberos.png", "killer-fish.png", "olrox.png", "succubus.png", "tombstone.png", "venus-weed.png", "lion.png", "scarecrow.png", "granfaloon.png", "schmoo.png", "tin-man.png", "balloon-pod.png", "yorick.png", "bomb-knight.png", "flying-zombie.png", "bitterfly.png", "jack-o'bones.png", "archer.png", "werewolf34.png", "black-panther.png", "darkwing-bat.png", "dragon-rider.png", "minotaur.png", "nova-skeleton.png", "orobourous.png", "white-dragon.png", "fire-warg.png", "rock-knight.png", "sniper-of-goth.png", "spectral-sword36.png", "ghost-dancer.png", "warg-rider.png", "cave-troll.png", "dark-octopus.png", "fire-demon.png", "gorgon.png", "malachi.png", "akmodan-ii.png", "blue-venus-weed.png", "doppleganger40.png", "medusa.png", "the-creature.png", "fake-grant.png", "fake-trevor.png", "imp.png", "fake-sypha.png", "beezelbub.png", "azaghal.png", "frozen-half.png", "salome.png", "richter-belmont.png", "dodo-bird.png", "galamoth.png", "guardian.png", "death.png", "shaft.png"]

def toBin(data) :
  binary = bin(int.from_bytes(data, 'big'))[2:]
  length = len(binary)
  if (length < 8) :
    for i in range( 8 - length) :
      binary = '0' + binary
  return binary

def getMissing(number):
  bits = []
  reverseByte = number[::-1]
  for i, c in enumerate(reverseByte, 1) :
    if c == '0':
      bits.append(i-1)
  return bits

def readMemCard() :
  startAddress = int("0x2000",0)
  endAddress = int("0x4000",0)
  # Open file to read binary
  with open(memCard, "rb") as file:
    row = 0
    byte = file.read(bufferSize)
    while byte:
      if row >= startAddress and row <= endAddress :
        position = 0
        line = ''
        while position < columnSize:
          hexValue = hex(int.from_bytes(byte, 'big'))
          line = line + ' ' + hexValue
          byte = file.read(bufferSize)
          position = position + 1

        print(hex(row) + ' - ' + line)
        position = 0
        row = row + columnSize
      else :
        row = row + 1
        # Read new byte anyway
        byte = file.read(bufferSize)

# Open file to read binary

def getData(start, size) :
  with open(memCard, "rb") as file:
    data = file.read(1)
    position = 0
    while data:
      if position == start - 1 :
        data = file.read(size)
        return data
      else :
        position = position + 1
        # Read new data anyway
        data = file.read(1)

def printEnemies(startAddress) :
  found = 0
  # There 18 bytes of memory storing rare items dropped
  for enemyBlock in range(18) :
    data = getData(startAddress + enemyBlock, 1)
    binData = toBin(data)

    missingEnemies = getMissing(binData)
    for index in missingEnemies :
      updatedIndex = index + (enemyBlock * 8)
      # Check if current monster doesn't drop items at all
      if updatedIndex not in nonDroppersIndex :
        print('[' + str(updatedIndex + 1) + '] ' + enemies[updatedIndex] + '   ->   ' + imageURL + enemyImages[updatedIndex])
        found = found + 1

  print('--------------------------------------')
  print('Missing ' + str(found) + ' rare items.')


printEnemies(rareItemsAddress)