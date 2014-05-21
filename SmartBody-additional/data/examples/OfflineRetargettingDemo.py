print "|--------------------------------------------|"
print "|        Starting Retargetting Demo          |"
print "|--------------------------------------------|"

# Add asset paths
scene.addAssetPath('script', 'sbm-common/scripts')
scene.addAssetPath('mesh', 'mesh')
scene.addAssetPath('mesh', 'retarget/mesh')
scene.addAssetPath('motion', 'ChrBrad')
scene.addAssetPath('motion', 'retarget\motion')
scene.addAssetPath('motion', 'sbm-common/common-sk')
scene.loadAssets()

# Runs the default viewer for camera
scene.run('default-viewer.py')
camera = getCamera()
camera.setEye(0, 188.56, 241.41)
camera.setCenter(0, 114.56, 56.41)
scene.getPawn('camera').setPosition(SrVec(0, -5, 0))

# Add Character script
target = scene.createCharacter('target', '')
targetSkeleton = scene.createSkeleton('common.sk')
target.setSkeleton(targetSkeleton)
targetPos = SrVec(-50, 102, 0)
target.setPosition(targetPos)
target.createStandardControllers()
target.setDoubleAttribute('deformableMeshScale', 1)
target.setStringAttribute('deformableMesh', 'Brad.dae')
bml.execBML('target', '<body posture="HandsAtSide_Motex"/>')

source = scene.createCharacter('source', '')
sourceSkeleton = scene.createSkeleton('ChrBrad.sk')
sourceSkeleton.rescale(100)
source.setSkeleton(sourceSkeleton)
sourcePos = SrVec(50, 0, 0)
source.setPosition(sourcePos)
source.createStandardControllers()
# Deformable mesh
source.setDoubleAttribute('deformableMeshScale', 1)
source.setStringAttribute('deformableMesh', 'ChrBrad.dae')
bml.execBML('source', '<body posture="ChrBrad@Idle01"/>')

# Turn on GPU deformable geometry
target.setStringAttribute("displayType", "GPUmesh")
source.setStringAttribute("displayType", "GPUmesh")


# Run motion retarget script
scene.run('motion-retarget.py')

# Retarget motion
print 'About to run retargetting'
motion = scene.getMotion('ChrBrad@Guitar01')
motion.scale(100)
retargetMotionWithGuessMap('ChrBrad@Guitar01', 'ChrBrad.sk', 'common.sk', scene.getMediaPath() + '/' + 'sbm-common/common-sk/retargetMotion/')
output = 'common.skChrBrad@Guitar01'
retargetedMotion = scene.getMotion(output)
retargetedMotion.scale(.01)
remapMotion('ChrBrad.sk',output,'ChrBrad.sk')
	
last = 0
canTime = True
delay = 10
class RetargettingDemo(SBScript):
	def update(self, time):
		global canTime, last, output
		diff = time - last
		if diff >= delay:
			canTime = True
			diff = 0
		if canTime:
			last = time
			canTime = False
			# Play non retargetted and retargetted add delay
			bml.execBML('target', '<animation name="common.skChrBrad@Guitar01"/>')
			bml.execBML('source', '<animation name="ChrBrad@Guitar01"/>')
			
scene.removeScript('retargettingdemo')
retargettingdemo = RetargettingDemo()
scene.addScript('retargettingdemo', retargettingdemo)
