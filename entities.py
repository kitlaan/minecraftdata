
class RegisterEntityClasses(type):
    def __init__(cls, name, bases, nmspc):
        super(RegisterEntityClasses, cls).__init__(name, bases, nmspc)
        if hasattr(cls, '_id'):
            if hasattr(cls, '_ext'):
                if cls._id not in cls._types:
                    cls._types[cls._id] = {}
                if not isinstance(cls._types[cls._id], dict):
                    cls._types[cls._id]._ext = 0
                    cls._types[cls._id] = {0: cls._types[cls._id]}
                cls._types[cls._id][cls._ext] = cls
            else:
                cls._types[cls._id] = cls

class Entity:
    __metaclass__ = RegisterEntityClasses
    _types = {}

class MobEntity:
    __metaclass__ = RegisterEntityClasses
    _types = {}

# = = = = = = =

class Circuit: pass

class Block(Entity): pass
class FluidBlock(Block): pass
class FallingBlock(Block): pass
class OreBlock(Block): pass
class ResourceBlock(Block): pass
class UsableBlock(Block): pass

class Item(Entity): pass
class Tool(Item): pass
class Axe(Tool): pass
class Pickaxe(Tool): pass
class Sword(Tool): pass
class Shovel(Tool): pass
class Armor(Item): pass
class Helmet(Armor): pass
class Chestplate(Armor): pass
class Legging(Armor): pass
class Boot(Armor): pass
class Food(Item): pass
class Dye(Item): pass

# = = = = = = =

class Air(Block):                               _id = 0;    _txt = "Air"

class Stone(Block):                             _id = 1;    _txt = "Stone"

class Dirt(Block):                              _id = 3;    _txt = "Dirt"

class Grass(Dirt):                              _id = 2;    _txt = "Grass"

class Cobblestone(Stone):                       _id = 4;    _txt = "Cobblestone"

class WoodenPlank(Block):                       _id = 5;    _txt = "Wooden Planks"

class Sapling(Block):                           _id = 6;    _txt = "Sapling"

class SpruceSapling(Sapling):                   _ext = 1;   _txt = "Sapling (Spruce)"

class BirchSapling(Sapling):                    _ext = 2;   _txt = "Sapling (Birch)"

class Bedrock(Block):                           _id = 7;    _txt = "Bedrock"

class Water(FluidBlock):                        _id = 8;    _txt = "Water"

class StillWater(Water):                        _id = 9;    _txt = "Water (Still)"

class Lava(FluidBlock):                         _id = 10;   _txt = "Lava"

class StillLava(Lava):                          _id = 11;   _txt = "Lava (Still)"

class Sand(FallingBlock):                       _id = 12;   _txt = "Sand"

class Gravel(FallingBlock):                     _id = 13;   _txt = "Gravel"

class GoldOre(OreBlock):                        _id = 14;   _txt = "Ore (Gold)"

class IronOre(OreBlock):                        _id = 15;   _txt = "Ore (Iron)"

class CoalOre(OreBlock):                        _id = 16;   _txt = "Ore (Coal)"

class Wood(Block):                              _id = 17;   _txt = "Wood"

class SpruceWood(Wood):                         _ext = 1;   _txt = "Wood (Spruce)"

class BirchWood(Wood):                          _ext = 2;   _txt = "Wood (Birch)"

class Leaves(Block):                            _id = 18;   _txt = "Leaves"

class SpruceLeaves(Leaves):                     _ext = 1;   _txt = "Leaves (Spruce)"

class BirchLeaves(Leaves):                      _ext = 2;   _txt = "Leaves (Birch)"

class Sponge(Block):                            _id = 19;   _txt = "Sponge"

class Glass(Block):                             _id = 20;   _txt = "Glass"

class LapisLazuliOre(OreBlock):                 _id = 21;   _txt = "Ore (Lapis Lazuli)"

class LapisLazuliBlock(ResourceBlock):          _id = 22;   _txt = "Block (Lapis Lazuli)"

class Dispenser(UsableBlock, Circuit):          _id = 23;   _txt = "Dispenser"

class Sandstone(Block):                         _id = 24;   _txt = "Sandstone"

class NoteBlock(UsableBlock, Circuit):          _id = 25;   _txt = "Note Block"

class BedFootBlock(UsableBlock):                _id = 26;   _txt = "Bed (Foot)"

class BedHeadBlock(BedFootBlock):               _ext = 1;   _txt = "Bed (Head)"

class Rail(Block):                              _id = 66;   _txt = "Rail"

class PoweredRail(Rail, Circuit):               _id = 27;   _txt = "Rail (Powered)"

class DetectorRail(Rail, Circuit):              _id = 28;   _txt = "Rail (Detector)"

class Web(Block):                               _id = 30;   _txt = "Web"

class Wool(Block):                              _id = 35;   _txt = "Wool (White)"

class OrangeWool(Wool):                         _ext = 1;   _txt = "Wool (Orange)"

class MagentaWool(Wool):                        _ext = 2;   _txt = "Wool (Magenta)"

class LightBlueWool(Wool):                      _ext = 3;   _txt = "Wool (Light Blue)"

class YellowWool(Wool):                         _ext = 4;   _txt = "Wool (Yellow)"

class LightGreenWool(Wool):                     _ext = 5;   _txt = "Wool (Light Green)"

class PinkWool(Wool):                           _ext = 6;   _txt = "Wool (Pink)"

class GrayWool(Wool):                           _ext = 7;   _txt = "Wool (Gray)"

class LightGrayWool(Wool):                      _ext = 8;   _txt = "Wool (Light Gray)"

class CyanWool(Wool):                           _ext = 9;   _txt = "Wool (Cyan)"

class PurpleWool(Wool):                         _ext = 10;  _txt = "Wool (Purple)"

class BlueWool(Wool):                           _ext = 11;  _txt = "Wool (Blue)"

class BrownWool(Wool):                          _ext = 12;  _txt = "Wool (Brown)"

class DarkGreenWool(Wool):                      _ext = 13;  _txt = "Wool (Dark Green)"

class RedWool(Wool):                            _ext = 14;  _txt = "Wool (Red)"

class BlackWool(Wool):                          _ext = 15;  _txt = "Wool (Black)"

class Dandelion(Block):                         _id = 37;   _txt = "Flower (Dandelion)"

class Rose(Block):                              _id = 38;   _txt = "Flower (Rose)"

class BrownMushroom(Block, Food):               _id = 39;   _txt = "Mushroom (Brown)"

class RedMushroom(Block, Food):                 _id = 40;   _txt = "Mushroom (Red)"

class GoldBlock(ResourceBlock):                 _id = 41;   _txt = "Block (Gold)"

class IronBlock(ResourceBlock):                 _id = 42;   _txt = "Block (Iron)"

class StoneDoubleSlab(Block):                   _id = 43;   _txt = "Double Slab (Stone)"

class SandstoneDoubleSlab(StoneDoubleSlab):     _ext = 1;   _txt = "Double Slab (Sandstone)"

class WoodenDoubleSlab(StoneDoubleSlab):        _ext = 2;   _txt = "Double Slab (Wooden)"

class CobblestoneDoubleSlab(StoneDoubleSlab):   _ext = 3;   _txt = "Double Slab (Cobblestone)"

class StoneSlab(Block):                         _id = 44;   _txt = "Slab (Stone)"

class SandstoneSlab(StoneSlab):                 _ext = 1;   _txt = "Slab (Sandstone)"

class WoodenSlab(StoneSlab):                    _ext = 2;   _txt = "Slab (Wooden)"

class CobblestoneSlab(StoneSlab):               _ext = 3;   _txt = "Slab (Cobblestone)"

class BrickBlock(Block):                        _id = 45;   _txt = "Bricks"

class TNT(UsableBlock):                         _id = 46;   _txt = "TNT"

class Bookshelf(Block):                         _id = 47;   _txt = "Bookshelf"

class MossStone(Stone):                         _id = 48;   _txt = "Moss Stone"

class Obsidian(Block):                          _id = 49;   _txt = "Obsidian"

class Torch(Block):                             _id = 50;   _txt = "Torch"

class Fire(Block):                              _id = 51;   _txt = "Fire"

class MonsterSpawner(Block):                    _id = 52;   _txt = "Monster Spawner"

class WoodenStairs(Block):                      _id = 53;   _txt = "Stairs (Wooden)"

class Chest(UsableBlock):                       _id = 54;   _txt = "Chest"

class RedstoneWire(Block, Circuit):             _id = 55;   _txt = "Redstone Wire"

class DiamondOre(OreBlock):                     _id = 56;   _txt = "Ore (Diamond)"

class DiamondBlock(ResourceBlock):              _id = 57;   _txt = "Block (Diamond)"

class CraftingTable(UsableBlock):               _id = 58;   _txt = "Crafting Table"

class Crops(Block):                             _id = 59;   _txt = "Crops"

class Farmland(Block):                          _id = 60;   _txt = "Farmland"

class Furnace(UsableBlock):                     _id = 61;   _txt = "Furnace"

class BurningFurnace(Furnace):                  _id = 62;   _txt = "Furnace (Burning)"

class SignPost(UsableBlock):                    _id = 63;   _txt = "Sign (Post)"

class WoodenDoor(UsableBlock, Circuit):         _id = 64;   _txt = "Door (Wooden)"

class Ladder(Block):                            _id = 65;   _txt = "Ladder"

class CobblestoneStairs(WoodenStairs):          _id = 67;   _txt = "Stairs (Cobblestone)"

class WallSign(SignPost):                       _id = 68;   _txt = "Sign (Wall)"

class Lever(UsableBlock, Circuit):              _id = 69;   _txt = "Lever"

class StonePressurePlate(UsableBlock, Circuit): _id = 70;   _txt = "Pressure Plate (Stone)" 

class IronDoor(WoodenDoor):                     _id = 71;   _txt = "Door (Iron)"

class WoodenPressurePlate(StonePressurePlate):  _id = 72;   _txt = "Pressure Plate (Wooden)"

class RedstoneOre(OreBlock):                    _id = 73;   _txt = "Ore (Redstone)"

class GlowingRedstoneOre(RedstoneOre):          _id = 74;   _txt = "Ore (Redstone, Glowing)"

class RedstoneTorch(Block, Circuit):            _id = 75;   _txt = "Redstone Torch (off)"

class LitRedstoneTorch(RedstoneTorch):          _id = 76;   _txt = "Redstone Torch (on)"

class Button(UsableBlock, Circuit):             _id = 77;   _txt = "Button"

class SnowLayer(Block):                         _id = 78;   _txt = "Snow Layer"

class Ice(Block):                               _id = 79;   _txt = "Ice"

class Snow(Block):                              _id = 80;   _txt = "Snow"

class Cactus(Block):                            _id = 81;   _txt = "Cactus"

class Clay(Block):                              _id = 82;   _txt = "Clay"

class SugarCane(Block):                         _id = 83;   _txt = "Sugar Cane"

class Jukebox(UsableBlock):                     _id = 84;   _txt = "Jukebox"

class Fence(Block):                             _id = 85;   _txt = "Fence"

class Pumpkin(Block):                           _id = 86;   _txt = "Pumpkin"

class Netherrack(Block):                        _id = 87;   _txt = "Netherrack"

class SoulSand(Block):                          _id = 88;   _txt = "Soul Sand"

class Glowstone(Block):                         _id = 89;   _txt = "Glowstone"

class Portal(Block):                            _id = 90;   _txt = "Portal"

class JackOLantern(Block):                      _id = 91;   _txt = "Jack-o-lantern"

class CakeBlock(Block):                         _id = 92;   _txt = "Cake Block"

"""
  93    Redstone Repeater (off)
  94    Redstone Repeater (on)
  95    Locked Chest
"""

class IronShovel(Shovel):                       _id = 256;  _txt = "Shovel (Iron)"

class IronPickaxe(Pickaxe):                     _id = 257;  _txt = "Pickaxe (Iron)"

class IronAxe(Axe):                             _id = 258;  _txt = "Axe (Iron)"

class FlintSteel(Tool):                         _id = 259;  _txt = "Flint and Steel"

class Apple(Food):                              _id = 260;  _txt = "Apple"

class Bow(Tool):                                _id = 261;  _txt = "Bow"

class Arrow(Tool):                              _id = 262;  _txt = "Arrow"

class Coal(Item):                               _id = 263;  _txt = "Coal"

class Charcoal(Coal):                           _ext = 1;   _txt = "Charcoal"

class Diamond(Item):                            _id = 264;  _txt = "Diamond"

class IronIngot(Item):                          _id = 265;  _txt = "Ingot (Iron)"


"""
 266   	Gold_Ingot
 267   	Iron_Sword
 268   	Wooden_Sword
 269   	Wooden_Shovel
 270   	Wooden_Pickaxe
 271   	Wooden_Axe
 272   	Stone_Sword
 273   	Stone_Shovel
 274   	Stone_Pickaxe
 275   	Stone_Axe
 276   	Diamond_Sword
 277   	Diamond_Shovel
 278   	Diamond_Pickaxe
 279   	Diamond_Axe
 280   	Stick
 281   	Bowl
 282   	Mushrom_Stew
 283   	Gold_Sword
 284   	Gold_Shovel
 285   	Gold_Pickaxe
 286   	Gold_Axe
 287   	String
 288   	Feather
 289   	Gunpoweder
 290   	Wooden_Hoe
 291   	Stone_Hoe
 292   	Iron_Hoe
 293   	Diamond_Hoe
 294   	Gold_Hoe
 295   	Seeds
 296   	Wheat
 297   	Bread
 298   	Leather_Cap
 299   	Leather_Tunic
 300   	Leather_Pants
 301   	Leather_Boots
 302   	Chainmail_Helmet
 303   	Chainmail_Chestplate
 304   	Chainmail_Leggings
 305   	Chainmail_Boots
 306   	Iron_Helmet
 307   	Iron_Chestplate
 308   	Iron_Leggings
 309   	Iron_Boots
 310   	Diamond_Face
 311   	Diamond_Chestplate
 312   	Diamond_Leggings
 313   	Diamond_Boots
 314   	Gold_Helmet
 315   	Gold_Chestplate
 316   	Gold_Leggings
 317   	Gold_Boots
 318   	Flint
 319   	Raw_Porkchop
 320   	Porkchop Cooked
 321   	Painting
 322   	Golden_Apple
 323   	Sign Item
 324   	Wooden_Door Item
 325   	Bucket
 326   	Water_Bucket
 327   	Lava_Bucket
 328   	Minecart
 329   	Saddle
 330   	Iron_Door Item
 331   	Redstone Dust
 332   	Snowball
 333   	Boat
 334   	Leather
 335   	Milk Bucket
 336   	Brick Item
 337   	Clay
 338   	Sugar_Cane
 339   	Paper
 340   	Book
 341   	Slimeball
 342   	Storage Minecart
 343   	Powered Minecart
 344   	Egg
 345   	Compass
 346   	Fishing_Rod
 347   	Clock
 348   	Glowstone_Dust
 349   	Raw_Fish
 350   	Cooked_Fish
 351x0 	Ink_Sack
 351x1 	Rose_Red
 351x10	Lime_Dye
 351x11	Dandelion_Yellow
 351x12	Light_Blue_Dye
 351x13	Magenta_Dye
 351x14	Orange_Dye
 351x15	Bone_Meal
 351x2 	Cactus_Green
 351x3 	Coco_Beans
 351x4 	Lapis_Lazuli
 351x5 	Purple_Dye
 351x6 	Cyan_Dye
 351x7 	Light_Gray_Dye
 351x8 	Gray_Dye
 351x9 	Pink_Dye
 352   	Bone
 353   	Sugar
 354   	Cake Item
 355    Bed Item
 356    Redstone Repeater Item
 357    Cookie
2256   	Gold_Music_Disk
2257   	Green_Music_Disk
"""

# = = = = = = =


# = = = = = = =

for e in Entity._types:
    if isinstance(Entity._types[e], dict):
        for d in Entity._types[e]:
            print "%4d (%2d) --> %s" % (e, d, Entity._types[e][d]._txt)
    else:
        print "%4d      --> %s" % (e, Entity._types[e]._txt)


