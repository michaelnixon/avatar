import math
import random
print "|--------------------------------------------|"
print "|      Starting Multiple Character Demo      |"
print "|--------------------------------------------|"

# Add asset paths
scene.addAssetPath('mesh', 'mesh')
scene.addAssetPath('motion', 'ChrRachel')
scene.addAssetPath("script", "behaviorsets")
scene.addAssetPath('script', 'scripts')
scene.addAssetPath('script', 'behaviorsets')
scene.loadAssets()

# Runs the default viewer for camera
scene.run('default-viewer.py')
camera = getCamera()
camera.setEye(0, 367.58, 574.66)
camera.setCenter(0, 275, 395)

print 'Setting up joint map and configuring Rachel\'s skeleton'
scene.run('zebra2-map.py')
zebra2Map = scene.getJointMapManager().getJointMap('zebra2')
bradSkeleton = scene.getSkeleton('ChrRachel.sk')
bradSkeleton.rescale(100)
zebra2Map.applySkeleton(bradSkeleton)
zebra2Map.applyMotionRecurse('ChrRachel')

# Set proper motion scale
print 'Scaling motion to fit rescaled skeleton'
scene.getMotion('ChrRachel_ChrBrad@Idle01').scale(100)

print 'Adding characters into scene'
# Set up multiple Rachels
amount = 25
row = 0; column = 0; 
offsetX = 0; offsetZ = 0;
for i in range(amount):
	baseName = 'ChrRachel%s' % i
	rachel = scene.createCharacter(baseName, '')
	rachelSkeleton = scene.createSkeleton('ChrRachel.sk')
	#rachelSkeleton.rescale(100)
	rachel.setSkeleton(rachelSkeleton)
	# Set position logic
	posX = (-100 * (5/2)) + 100 * column
	posZ = ((-100 / math.sqrt(amount)) * (amount/2)) + 100 * row	
	column = column + 1
	if column >= 5:
		column = 0
		row = row + 1
	rachelPos = SrVec(posX + offsetX, 0, posZ + offsetZ)
	rachel.setPosition(rachelPos)
	# Set up standard controllers
	rachel.createStandardControllers()
	# Set deformable mesh
	rachel.setDoubleAttribute('deformableMeshScale', 1)
	rachel.setStringAttribute('deformableMesh', 'ChrRachel.dae')
	if i== 0 : 
		scene.run('BehaviorSetFemaleGestures.py')
		setupBehaviorSet()
	retargetBehaviorSet(baseName)
	# Play default animation
	bml.execBML(baseName, '<body posture="ChrConnor@IdleStand01"/>')
	bml.execBML(baseName, '<saccade mode="listen"/>')

# Turn on GPU deformable geometry for all
for name in scene.getCharacterNames():
	scene.getCharacter(name).setStringAttribute("displayType", "GPUmesh")

# Set camera position
scene.getPawn('camera').setPosition(SrVec(0, -50, 0))

# randomly look at a different Rachel character every 5 seconds
class RamdomGazeScript(SBScript):
	nextTimes = []
	numCharacters = 0
	isInitialized = False
	names = []
	
	def start(self):
		if self.isInitialized is True:
			return
		self.isInitialized = True
		import random
		self.names = scene.getCharacterNames()
		print "Found " + str(len(self.names)) + " characters..."		
		for i in range(0, len(self.names)):
			self.nextTimes.append(sim.getTime() + 3 + random.randrange(0, 6, 1))
			which = random.randrange(0, len(self.names), 1)
			if which != i:
				bml.execBML("ChrRachel" + str(i), "<gaze target=\"ChrRachel" + str(which) + "\"/>")
						
		print "Starting random gaze..."
	def stop(self):
		print "Stopping random gaze..."
	def update(self, time):
		curTime = sim.getTime()
		self.names = scene.getCharacterNames()
		for i in range(0, len(self.names)):
			if (curTime > self.nextTimes[i]):
				which = random.randrange(0, len(self.names), 1)
				self.nextTimes[i] = (sim.getTime() + 3 + random.randrange(0, 6, 1))
				rachelName = self.names[i]
				if which != i:
					bml.execBML(rachelName, "<gaze target=\"ChrRachel" + str(which) + "\" sbm:joint-speed=\"500 500\" sbm:joint-range=\"chest eyes\"/><gesture name=\"ChrConnor@IdleStand01_ChopRt01\" start=\"1\"/>")

gazeScript = RamdomGazeScript()
scene.addScript("randomgaze", gazeScript)
sim.start()
sim.resume()