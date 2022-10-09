import bpy
import random 
import math

# Creates Cylinder with given infos
def makeCyliner(location=(0,0,0),radius=1,depth=2,scale=(1,1,1)):
    bpy.ops.mesh.primitive_cylinder_add(vertices=150, radius=radius, depth=depth, enter_editmode=False, align='WORLD', location=location, scale=scale)

# Random Location for Cylinder
def randomLoc(z=0):
    lX = random.randint(-30,30)
    lY = random.randint(-30,30)
    location = [lX,lY,z]
    return location

# Random Radius for Cylinder
def randomRad():
    rad = random.randint(1,16) # You can Change Radius Range
    return rad/2

# Random Height for Cylinders
def randomDepth():
    randDepth = random.randint(1,4) # You can adjust Random Height Range
    return randDepth

# Finds 2D distance between two 3D points
def findDistance(point1,point2):
    dist = ((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)**0.5
    return dist

# Adds Bevel modifier to last object 
def addBevel():
    bpy.ops.object.modifier_add(type='BEVEL')
    bpy.context.object.modifiers["Bevel"].width = 0.2 # You can Adjust Bevel Width
    bpy.context.object.modifiers["Bevel"].segments = 10 # You can Adjust Bevel Segment Amount

circles = []

# Main Part of The Program
for i in range(100000): # Change the number for the iteration    (if your computer is slow you should decrease the number)
    overlapping = False
    
    location = randomLoc()
    rad = randomRad()
    randDepth = randomDepth()
    if len(circles) != 0:   
        for circle in circles:
            ciLoc = circle[0]
            distanc = findDistance(ciLoc,location)
            if distanc<rad+circle[1]:
                overlapping = True
            
    if overlapping==False:
        makeCyliner(location,rad,randDepth)
        circles.append([location,rad])
        isEqual = False 
        addBevel()
        
        obj = bpy.context.object
        obj.data.materials.append(bpy.data.materials['mat'])
            
                
    
