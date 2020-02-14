from maya import cmds


numberOfBones = 10;

curveShape = cmds.ls(selection=True)
curvePointPosStart = cmds.pointOnCurve(curveShape, pr = 0.0)
curvePointPosEnd = cmds.pointOnCurve(curveShape, pr = 1.0)

boneDistance = (curvePointPosEnd[0] - curvePointPosStart[0])/numberOfBones

#     print boneDistance

initialJoint = cmds.joint(p =(curvePointPosStart[0], curvePointPosStart[1], curvePointPosStart[2]))
cmds.select(initialJoint)

for i in range (0, numberOfBones):
    cmds.joint(p =(i*boneDistance, 0.0, 0.0))


print cmds.listRelatives(initialJoint)

cmds.move(boneDistance, 0.0, 0.0, cmds.listRelatives(initialJoint, c = True), a=True, ls = True)