from maya import cmds


class playBlaster(object):

    def __init__(self):
        self.mainCam = cmds.ls(selection=True, dag=True, long=True)

    # Automatically looks through the selected camera, turns off all elements except polys and then playblasts, afterwards turns all elements back on.
    def selectAndBlast(self):

        # Checks for initial selection
        if (cmds.ls(selection=True)):

            camNode = self.mainCam[1]
            camNodeType = cmds.nodeType(camNode)

            # Checks if selection is a camera
            if camNodeType == 'camera':

                cmds.lookThru(self.mainCam)

                currentPanel = cmds.getPanel(withFocus=True)

                cmds.modelEditor(currentPanel, e=1, allObjects=0, polymeshes=1)

                cmds.playblast(format='avi', filename="movies/playblast", forceOverwrite=True,
                               clearCache=True, showOrnaments=False, viewer=True,
                               percent=100, compression="none", quality=100)

                cmds.modelEditor(currentPanel, e=1, allObjects=1)

                cmds.lookThru('persp')

            else:
                cmds.error("Select a camera")
                # print "That ain't no camera"

        else:
            cmds.error("Select a camera")
            # print "You need to select a camera"

    def turnTableBlast(self):
        turnCamName = 'TurnCam'
        newCam = cmds.camera()

        cmds.rename(newCam[0], turnCamName)

        perspCam = 'persp'
        
        #cmds.rename(newCam[0], 'NewCam')

        cmds.matchTransform(turnCamName, perspCam)
        cmds.lookThru(turnCamName)

        cmds.playblast(format='avi', filename="movies/playblast", forceOverwrite=True,
                       clearCache=True, showOrnaments=False, viewer=True,
                       percent=100, compression="none", quality=100)
        cmds.lookThru(perspCam)
        cmds.delete(turnCamName)

'''
currentPanel = cmds.getPanel(withFocus = True)
print allPanels
cmds.modelEditor(currentPanel, e=1, allObject=0 ,polymeshes=1)
'''
