import bpy
import random 
import math

def makeCyliner(location=(0,0,0),radius=1,depth=2,scale=(1,1,1)):
    bpy.ops.mesh.primitive_cylinder_add(vertices=150, radius=radius, depth=depth, enter_editmode=False, align='WORLD', location=location, scale=scale)

def randomLoc(z=0):
    lX = random.randint(-30,30)
    lY = random.randint(-30,30)
    location = [lX,lY,z]
    return location

def randomRad():
    rad = random.randint(1,8)
    return rad
    
def findDistance(point1,point2):
    dist = ((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)**0.5
    return dist

def addBevel():
    bpy.ops.object.modifier_add(type='BEVEL')
    bpy.context.object.modifiers["Bevel"].width = 0.2
    bpy.context.object.modifiers["Bevel"].segments = 10

circles = []
isEqual = True

bpy.ops.mesh.primitive_plane_add(size=65, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))

obj = bpy.context.object
obj.data.materials.append(bpy.data.materials['background'])

for i in range(100000):
    overlapping = False
    
    location = randomLoc()
    rad = randomRad()
    randDepth = random.randint(1,4)
    if len(circles) != 0:   
        for circle in circles:
            ciLoc = circle[0]
            distanc = findDistance(ciLoc,location)
            if distanc<rad+circle[1]:
                overlapping = True
            if distanc == rad+circle[1]:
                isEqual = True
            
    if overlapping==False and isEqual==True:
        makeCyliner(location,rad,randDepth)
        circles.append([location,rad])
        isEqual = False 
        addBevel()
        
        obj = bpy.context.object
        obj.data.materials.append(bpy.data.materials['mat'])
            
                
    
