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
    rad = random.randint(1,8) # You can Change Radius Range
    return rad

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


bpy.ops.mesh.primitive_plane_add(size=65, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))

obj = bpy.context.object
obj.data.materials.append(bpy.data.materials['background'])


# Main Part of The Program
while len(circles)<=100: # Change the number for the iteration
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
            
                
    
