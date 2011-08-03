
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
class Hoe(Tool): pass
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

class WoodenPlank(Block):                       _id = 5;    _txt = "Wooden Plank"

class Sapling(Block):                           _id = 6;    _txt = "Sapling"

class SpruceSapling(Sapling):                   _ext = 1;   _txt = "Sapling (Spruce)"

class BirchSapling(Sapling):                    _ext = 2;   _txt = "Sapling (Birch)"

class Bedrock(Block):                           _id = 7;    _txt = "Bedrock"

class Water(FluidBlock):                        _id = 8;    _txt = "Water"

class StillWater(Water):                        _id = 9;    _txt = "Water (Stationary)"

class Lava(FluidBlock):                         _id = 10;   _txt = "Lava"

class StillLava(Lava):                          _id = 11;   _txt = "Lava (Stationary)"

class Sand(FallingBlock):                       _id = 12;   _txt = "Sand"

class Gravel(FallingBlock):                     _id = 13;   _txt = "Gravel"

class GoldOre(OreBlock):                        _id = 14;   _txt = "Ore (Gold)"

class IronOre(OreBlock):                        _id = 15;   _txt = "Ore (Iron)"

class CoalOre(OreBlock):                        _id = 16;   _txt = "Ore (Coal)"

class Wood(Block):                              _id = 17;   _txt = "Wood (Oak)"

class PineWood(Wood):                           _ext = 1;   _txt = "Wood (Pine)"

class BirchWood(Wood):                          _ext = 2;   _txt = "Wood (Birch)"

class Leaves(Block):                            _id = 18;   _txt = "Leaves"

class PineLeaves(Leaves):                       _ext = 1;   _txt = "Leaves (Pine)"

class BirchLeaves(Leaves):                      _ext = 2;   _txt = "Leaves (Birch)"

class Sponge(Block):                            _id = 19;   _txt = "Sponge"

class Glass(Block):                             _id = 20;   _txt = "Glass"

class LapisLazuliOre(OreBlock):                 _id = 21;   _txt = "Ore (Lapis Lazuli)"

class LapisLazuliBlock(ResourceBlock):          _id = 22;   _txt = "Block (Lapis Lazuli)"

class Dispenser(UsableBlock, Circuit):          _id = 23;   _txt = "Dispenser"

class Sandstone(Block):                         _id = 24;   _txt = "Sandstone"

class NoteBlock(UsableBlock, Circuit):          _id = 25;   _txt = "Note Block"

class BedFootBlock(UsableBlock):                _id = 26;   _txt = "Bed"

class BedHeadBlock(BedFootBlock):               _ext = 1;   _txt = "Bed (Head)"

class Rail(Block):                              _id = 66;   _txt = "Rail"

class PoweredRail(Rail, Circuit):               _id = 27;   _txt = "Rail (Powered)"

class DetectorRail(Rail, Circuit):              _id = 28;   _txt = "Rail (Detector)"

class Web(Block):                               _id = 30;   _txt = "Web"

class TallGrass(Block):                         _id = 31;   _txt = "Tall Grass"

class DeadShrub(Block):                         _id = 32;   _txt = "Dead Shrub"

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

class BrickBlock(Block):                        _id = 45;   _txt = "Brick Block"

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

class RedstoneTorch(Block, Circuit):            _id = 76;   _txt = "Redstone Torch"

class UnlitRedstoneTorch(RedstoneTorch):        _id = 75;   _txt = "Redstone Torch (off)"

class Button(UsableBlock, Circuit):             _id = 77;   _txt = "Button"

class SnowLayer(Block):                         _id = 78;   _txt = "Snow"

class Ice(Block):                               _id = 79;   _txt = "Ice"

class SnowBlock(ResourceBlock):                 _id = 80;   _txt = "Snow Block"

class Cactus(Block):                            _id = 81;   _txt = "Cactus"

class ClayBlock(ResourceBlock):                 _id = 82;   _txt = "Block (Clay)"

class SugarCane(Block):                         _id = 83;   _txt = "Sugar Cane"

class Jukebox(UsableBlock):                     _id = 84;   _txt = "Jukebox"

class Fence(Block):                             _id = 85;   _txt = "Fence"

class Pumpkin(Block):                           _id = 86;   _txt = "Pumpkin"

class Netherrack(Block):                        _id = 87;   _txt = "Netherrack"

class SoulSand(Block):                          _id = 88;   _txt = "Soul Sand"

class GlowstoneBlock(ResourceBlock):            _id = 89;   _txt = "Block (Glowstone)"

class Portal(Block):                            _id = 90;   _txt = "Portal"

class JackOLantern(Block):                      _id = 91;   _txt = "Jack-o-lantern"

class CakeBlock(Block, Food):                   _id = 92;   _txt = "Cake Block"

class RedstoneRepeater(UsableBlock):            _id = 93;   _txt = "Redstone Repeater"

class OnRedstoneRepeater(RedstoneRepeater):     _id = 94;   _txt = "Redstone Repeater (on)"

class LockedChest(Chest):                       _id = 95;   _txt = "Chest (Locked)"

class Trapdoor(UsableBlock):                    _id = 96;   _txt = "Trapdoor"


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =


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

class GoldIngot(Item):                          _id = 266;  _txt = "Ingot (Gold)"

class IronSword(Sword):                         _id = 267;  _txt = "Sword (Iron)"

class WoodenSword(Sword):                       _id = 268;  _txt = "Sword (Wooden)"

class WoodenShovel(Shovel):                     _id = 269;  _txt = "Shovel (Wooden)"

class WoodenPickaxe(Pickaxe):                   _id = 270;  _txt = "Pickaxe (Wooden)"

class WoodenAxe(Axe):                           _id = 271;  _txt = "Axe (Wooden)"

class StoneSword(Sword):                        _id = 272;  _txt = "Sword (Stone)"

class StoneShovel(Shovel):                      _id = 273;  _txt = "Shovel (Stone)"

class StonePickaxe(Pickaxe):                    _id = 274;  _txt = "Pickaxe (Stone)"

class StoneAxe(Axe):                            _id = 275;  _txt = "Axe (Stone)"

class DiamondSword(Sword):                      _id = 276;  _txt = "Sword (Diamond)"

class DiamondShovel(Shovel):                    _id = 277;  _txt = "Shovel (Diamond)"

class DiamondPickaxe(Pickaxe):                  _id = 278;  _txt = "Pickaxe (Diamond)"

class DiamondAxe(Axe):                          _id = 279;  _txt = "Axe (Diamond)"

class Stick(Item):                              _id = 280;  _txt = "Stick"

class Bowl(Item):                               _id = 281;  _txt = "Bowl"

class MushroomStew(Food):                       _id = 282;  _txt = "Mushroom Stew"

class GoldSword(Sword):                         _id = 283;  _txt = "Sword (Gold)"

class GoldShovel(Shovel):                       _id = 284;  _txt = "Shovel (Gold)"

class GoldPickaxe(Pickaxe):                     _id = 285;  _txt = "Pickaxe (Gold)"

class GoldAxe(Axe):                             _id = 286;  _txt = "Axe (Gold)"

class String(Item):                             _id = 287;  _txt = "String"

class Feather(Item):                            _id = 288;  _txt = "Feather"

class Gunpowder(Item):                          _id = 289;  _txt = "Gunpowder"

class WoodenHoe(Hoe):                           _id = 290;  _txt = "Hoe (Wooden)"

class StoneHoe(Hoe):                            _id = 291;  _txt = "Hoe (Stone)"

class IronHoe(Hoe):                             _id = 292;  _txt = "Hoe (Iron)"

class DiamondHoe(Hoe):                          _id = 293;  _txt = "Hoe (Diamond)"

class GoldHoe(Hoe):                             _id = 294;  _txt = "Hoe (Gold)"

class Seed(Item):                               _id = 295;  _txt = "Seed"

class Wheat(Item):                              _id = 296;  _txt = "Wheat"

class Bread(Food):                              _id = 297;  _txt = "Bread"

class LeatherHelmet(Helmet):                    _id = 298;  _txt = "Helmet (Leather)"

class LeatherChestplate(Chestplate):            _id = 299;  _txt = "Chestplate (Leather)"

class LeatherLeggings(Legging):                 _id = 300;  _txt = "Leggings (Leather)"

class LeatherBoots(Boot):                       _id = 301;  _txt = "Boots (Leather)"

class ChainmailHelmet(Helmet):                  _id = 302;  _txt = "Helmet (Chainmail)"

class ChainmailChestplate(Chestplate):          _id = 303;  _txt = "Chestplate (Chainmail)"

class ChainmailLeggings(Legging):               _id = 304;  _txt = "Leggings (Chainmail)"

class ChainmailBoots(Boot):                     _id = 305;  _txt = "Boots (Chainmail)"

class IronHelmet(Helmet):                       _id = 306;  _txt = "Helmet (Iron)"

class IronChestplate(Chestplate):               _id = 307;  _txt = "Chestplate (Iron)"

class IronLeggings(Legging):                    _id = 308;  _txt = "Leggings (Iron)"

class IronBoots(Boot):                          _id = 309;  _txt = "Boots (Iron)"

class DiamondHelmet(Helmet):                    _id = 310;  _txt = "Helmet (Diamond)"

class DiamondChestplate(Chestplate):            _id = 311;  _txt = "Chestplate (Diamond)"

class DiamondLeggings(Legging):                 _id = 312;  _txt = "Leggings (Diamond)"

class DiamondBoots(Boot):                       _id = 313;  _txt = "Boots (Diamond)"

"""
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
"""

class BedItem(Item):                            _id = 355;  _txt = "Bed Item"

class RedstoneRepeaterItem(Item):               _id = 356;  _txt = "Redstone Repeater Item"

class Cookie(Food):                             _id = 357;  _txt = "Cookie"

class Map(Item):                                _id = 358;  _txt = "Map"

class GoldMusicDisk(Item):                      _id = 2256; _txt = "Music Disk (Gold)"

class GreenMusicDisk(Item):                     _id = 2257; _txt = "Music Disk (Green)"

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =


if __name__ == "__main__":
    for e in sorted(Entity._types):
        if isinstance(Entity._types[e], dict):
            for d in sorted(Entity._types[e]):
                print "%4d (%2d) --> %s" % (e, d, Entity._types[e][d]._txt)
        else:
            print "%4d      --> %s" % (e, Entity._types[e]._txt)

