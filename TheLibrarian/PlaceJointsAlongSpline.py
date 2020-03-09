from maya import cmds
from PySide2 import QtWidgets, QtCore, QtGui


class PlaceJointsUI(QtWidgets.QDialog):

    def __init__(self):
        super(PlaceJointsUI, self).__init__()

        self.setWindowTitle("SplineJointPlacer 1.0")
        self.button = QtWidgets.QPushButton("Place Joints")
        self.buildUI()

    def buildUI(self):
        layout = QtWidgets.QVBoxLayout(self)

        buttonWidget = QtWidgets.QWidget()
        jointCreationLayout =  QtWidgets.QHBoxLayout(buttonWidget)

        layout.addWidget(buttonWidget)

        self.boneNumInputField = QtWidgets.QLineEdit()
        jointCreationLayout.addWidget(self.boneNumInputField)

        button = QtWidgets.QPushButton("PlaceJoints")
        button.clicked.connect(self.placeJoints)
        jointCreationLayout.addWidget(button)

    def placeJoints(self):

        numberOfBones = int(self.boneNumInputField.text())

        curveShape = cmds.ls(selection=True)

        numberOfPoints = (cmds.getAttr(str(curveShape[0]) + '.degree') + cmds.getAttr(str(curveShape[0]) + '.spans'))


        initialPointPos = cmds.pointOnCurve(curveShape, parameter = 0.0)
        initialJoint = cmds.joint(position = initialPointPos)


        for i in range(0, numberOfPoints):

            curvePointPosStart = cmds.pointOnCurve(curveShape, parameter = i)
            curvePointPosEnd = cmds.pointOnCurve(curveShape, parameter = i+1)

            initialJoint = cmds.joint(position =curvePointPosStart)

            boneDistanceX = (curvePointPosEnd[0] - curvePointPosStart[0])/numberOfBones
            boneDistanceZ = (curvePointPosEnd[2] - curvePointPosStart[2])/numberOfBones


            cmds.select(initialJoint)

            print "point: " + str(i)

            for i in range (0, numberOfBones):
                print i*boneDistanceX
                cmds.joint(p =(i*boneDistanceX, 0.0, i*boneDistanceZ))

            cmds.move(boneDistanceX, 0.0, boneDistanceZ, cmds.listRelatives(initialJoint, children = True), absolute=True, localSpace = True)

#This is the function that will actually display the UI
def showUI():
    ui = PlaceJointsUI()
    ui.show()

    return ui