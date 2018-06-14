from mcpi.minecraft import Minecraft

mc = Minecraft.create()

mc.postToChat("Hello world")

pos = mc.player.getPos()

x, y, z = mc.player.getPos()


#mc.player.setPos(x,y+100, z)

mc.setBlock(x+1, y, z, 1)

#Air:   0
#Grass: 2
#Dirt:  3
#Smooth Stone: 1

mc.setBlocks(x+1, y+1, z+1, x+11, y+11, z+11, 1)
