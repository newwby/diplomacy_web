
# http://uk.diplom.org/pouch/Online/maps/map_c.gif
# https://www.crockford.com/image/diplomap.gif
# https://diplomacy.fandom.com/wiki/Territory

# https://www.lspace.org/games/afpdip/files/import.html

# https://www.marsja.se/your-guide-to-reading-excel-xlsx-files-in-python/

# https://docs.google.com/spreadsheets/d/1w7wCNEPf-OkpGUzVtEd4yStZk8zy_yJEwZNgsvcBrSQ/edit#gid=0


"""
TO-DO LIST
1) Reset GIT
2) 
"""

class Territory:
    def __init__(self, identifier, descriptive_name, is_land, is_supply, adjacent, contains):
        self.identifier = identifier
        self.name = descriptive_name
        self.is_land = is_land
        self.is_supply = is_supply
        self.adjacent = adjacent
        self.contains = contains

# -------------------------------------------------------------------------------------
# WATER TERRITORIES BELOW (TOTAL 19)


t000_north_atlantic_ocean = Territory(0, "north_atlantic_ocean", False, False, [], [])
t001_namespace = Territory(1, "name", False, False, [], [])
t002_namespace = Territory(2, "name", False, False, [], [])
t003_namespace = Territory(3, "name", False, False, [], [])
t004_namespace = Territory(4, "name", False, False, [], [])
t005_namespace = Territory(5, "name", False, False, [], [])
t006_namespace = Territory(6, "name", False, False, [], [])
t007_namespace = Territory(7, "name", False, False, [], [])
t008_namespace = Territory(8, "name", False, False, [], [])
t009_namespace = Territory(9, "name", False, False, [], [])
t010_namespace = Territory(10, "name", False, False, [], [])
t011_namespace = Territory(11, "name", False, False, [], [])
t012_namespace = Territory(12, "name", False, False, [], [])
t013_namespace = Territory(13, "name", False, False, [], [])
t014_namespace = Territory(14, "name", False, False, [], [])
t015_namespace = Territory(15, "name", False, False, [], [])
t016_namespace = Territory(16, "name", False, False, [], [])
t017_namespace = Territory(17, "name", False, False, [], [])
t018_namespace = Territory(18, "name", False, False, [], [])

# -------------------------------------------------------------------------------------
# LAND NON-SUPPLY TERRITORIES BELOW (TOTAL 22)

t019_namespace = Territory(19, "name", True, False, [], [])
t020_namespace = Territory(20, "name", True, False, [], [])
t021_namespace = Territory(21, "name", True, False, [], [])
t022_namespace = Territory(22, "name", True, False, [], [])
t023_namespace = Territory(23, "name", True, False, [], [])
t024_namespace = Territory(24, "name", True, False, [], [])
t025_namespace = Territory(25, "name", True, False, [], [])
t026_namespace = Territory(26, "name", True, False, [], [])
t027_namespace = Territory(27, "name", True, False, [], [])
t028_namespace = Territory(28, "name", True, False, [], [])
t029_namespace = Territory(29, "name", True, False, [], [])
t030_namespace = Territory(30, "name", True, False, [], [])
t031_namespace = Territory(31, "name", True, False, [], [])
t032_namespace = Territory(32, "name", True, False, [], [])
t033_namespace = Territory(33, "name", True, False, [], [])
t034_namespace = Territory(34, "name", True, False, [], [])
t035_namespace = Territory(35, "name", True, False, [], [])
t036_namespace = Territory(36, "name", True, False, [], [])
t037_namespace = Territory(37, "name", True, False, [], [])
t038_namespace = Territory(38, "name", True, False, [], [])
t039_namespace = Territory(39, "name", True, False, [], [])
t040_namespace = Territory(40, "name", True, False, [], [])

# -------------------------------------------------------------------------------------
# LAND SUPPLY TERRITORIES BELOW (TOTAL 34)


t041_namespace = Territory(41, "name", True, True, [], [])
t042_namespace = Territory(42, "name", True, True, [], [])
t043_namespace = Territory(43, "name", True, True, [], [])
t044_namespace = Territory(44, "name", True, True, [], [])
t045_namespace = Territory(45, "name", True, True, [], [])
t046_namespace = Territory(46, "name", True, True, [], [])
t047_namespace = Territory(47, "name", True, True, [], [])
t048_namespace = Territory(48, "name", True, True, [], [])
t049_namespace = Territory(49, "name", True, True, [], [])
t050_namespace = Territory(50, "name", True, True, [], [])
t051_namespace = Territory(51, "name", True, True, [], [])
t052_namespace = Territory(52, "name", True, True, [], [])
t053_namespace = Territory(53, "name", True, True, [], [])
t054_namespace = Territory(54, "name", True, True, [], [])
t055_namespace = Territory(55, "name", True, True, [], [])
t056_namespace = Territory(56, "name", True, True, [], [])
t057_namespace = Territory(57, "name", True, True, [], [])
t058_namespace = Territory(58, "name", True, True, [], [])
t059_namespace = Territory(59, "name", True, True, [], [])
t060_namespace = Territory(60, "name", True, True, [], [])
t061_namespace = Territory(61, "name", True, True, [], [])
t062_namespace = Territory(62, "name", True, True, [], [])
t063_namespace = Territory(63, "name", True, True, [], [])
t064_namespace = Territory(64, "name", True, True, [], [])
t065_namespace = Territory(65, "name", True, True, [], [])
t066_namespace = Territory(66, "name", True, True, [], [])
t067_namespace = Territory(67, "name", True, True, [], [])
t068_namespace = Territory(68, "name", True, True, [], [])
t069_namespace = Territory(69, "name", True, True, [], [])
t070_namespace = Territory(70, "name", True, True, [], [])
t071_namespace = Territory(71, "name", True, True, [], [])
t072_namespace = Territory(72, "name", True, True, [], [])
t073_namespace = Territory(73, "name", True, True, [], [])
t074_namespace = Territory(74, "name", True, True, [], [])