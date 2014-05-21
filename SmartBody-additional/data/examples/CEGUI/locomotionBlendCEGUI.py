print "|--------------------------------------------|"
print "|         Starting Character Demo            |"
print "|--------------------------------------------|"

# Add asset paths
scene.addAssetPath('mesh', 'mesh')
#scene.addAssetPath('mesh', 'retarget/mesh')
scene.addAssetPath('motion', 'ChrBrad')
#scene.addAssetPath('motion', 'sbm-common/common-sk')
scene.addAssetPath("script", "behaviorsets")
scene.addAssetPath('script', 'scripts')
scene.loadAssets()

# Set scene parameters and camera
print 'Configuring scene parameters and camera'
scene.setScale(1.0)
scene.setBoolAttribute('internalAudio', True)
scene.run('default-viewer.py')
camera = getCamera()
camera.setEye(0, 1.71, 1.86)
camera.setCenter(0, 1, 0.01)
camera.setUpVector(SrVec(0, 1, 0))
camera.setScale(1)
camera.setFov(1.0472)
camera.setFarPlane(100)
camera.setNearPlane(0.1)
camera.setAspectRatio(0.966897)
cameraPos = SrVec(0, 1.6, 10)
scene.getPawn('camera').setPosition(cameraPos)

# Set up joint map for Brad
print 'Setting up joint map and configuring Brad\'s skeleton'
scene.run('zebra2-map.py')
zebra2Map = scene.getJointMapManager().getJointMap('zebra2')
bradSkeleton = scene.getSkeleton('ChrBrad.sk')
zebra2Map.applySkeleton(bradSkeleton)
zebra2Map.applyMotionRecurse('ChrBrad')

# Establish lip syncing data set
print 'Establishing lip syncing data set'
scene.run('init-diphoneDefault.py')

# Set up animation
#print 'Setting up animation'
#scene.run('init-param-animation.py')
#''
# Set up retargeting
#print 'Setting up retargeting'
#scene.run('motion-retarget.py')

# Set gesture map for Brad
print 'Setting gesture map for Brad'
gMapManager = getScene().getGestureMapManager()
# Brad's gestures
gMap = gMapManager.createGestureMap("ChrBrad")
gMap.addGestureMapping("ChrBrad@Idle01_YouLf01", "DEICTIC", "YOU", "LEFT_HAND", "", "ChrBrad@Idle01")
gMap.addGestureMapping("ChrBrad@Idle02_YouLf01", "DEICTIC", "YOU", "LEFT_HAND", "", "ChrBrad@Idle02")
gMap.addGestureMapping("ChrBrad@Idle03_YouLf01", "DEICTIC", "YOU", "LEFT_HAND", "", "ChrBrad@Idle03")
gMap.addGestureMapping("ChrBrad@Idle01_MeLf01", "DEICTIC", "ME", "LEFT_HAND", "", "ChrBrad@Idle01")
gMap.addGestureMapping("ChrBrad@Idle02_MeRt01", "DEICTIC", "ME", "RIGHT_HAND", "", "ChrBrad@Idle02")
gMap.addGestureMapping("ChrBrad@Idle03_MeLf01", "DEICTIC", "ME", "LEFT_HAND", "", "ChrBrad@Idle03")
gMap.addGestureMapping("ChrBrad@Idle01_IndicateLeftLf01", "DEICTIC", "LEFT", "LEFT_HAND", "", "ChrBrad@Idle01")
gMap.addGestureMapping("ChrBrad@Idle01_IndicateLeftBt01", "DEICTIC", "LEFT", "BOTH_HANDS", "", "ChrBrad@Idle01")
gMap.addGestureMapping("ChrBrad@Idle01_IndicateRightRt01", "DEICTIC", "RIGHT", "RIGHT_HAND", "", "ChrBrad@Idle01")
gMap.addGestureMapping("ChrBrad@Idle01_IndicateRightBt01", "DEICTIC", "RIGHT", "BOTH_HANDS", "", "ChrBrad@Idle01")
gMap.addGestureMapping("ChrBrad@Idle01_NegativeBt01", "METAPHORIC", "NEGATION", "BOTH_HANDS", "", "ChrBrad@Idle01")
gMap.addGestureMapping("ChrBrad@Idle01_NegativeRt01", "METAPHORIC", "NEGATION", "RIGHT_HAND", "", "ChrBrad@Idle01")
gMap.addGestureMapping("ChrBrad@Idle02_NegativeBt01", "METAPHORIC", "NEGATION", "BOTH_HANDS", "", "ChrBrad@Idle02")
gMap.addGestureMapping("ChrBrad@Idle02_NegativeLf01", "METAPHORIC", "NEGATION", "LEFT_HAND", "", "ChrBrad@Idle02")
gMap.addGestureMapping("ChrBrad@Idle03_NegativeBt01", "METAPHORIC", "NEGATION", "BOTH_HANDS", "", "ChrBrad@Idle03")
gMap.addGestureMapping("ChrBrad@Idle03_NegativeLf01", "METAPHORIC", "NEGATION", "LEFT_HAND", "", "ChrBrad@Idle03")
gMap.addGestureMapping("ChrBrad@Idle01_HoweverLf01", "METAPHORIC", "CONTRAST", "LEFT_HAND", "", "ChrBrad@Idle01")
gMap.addGestureMapping("ChrBrad@Idle01_Shrug01", "METAPHORIC", "CONTRAST", "BOTH_HANDS", "", "ChrBrad@Idle01")
gMap.addGestureMapping("ChrBrad@Idle02_Shrug01", "METAPHORIC", "CONTRAST", "BOTH_HANDS", "", "ChrBrad@Idle02")
gMap.addGestureMapping("ChrBrad@Idle03_Shrug01", "METAPHORIC", "CONTRAST", "BOTH_HANDS", "", "ChrBrad@Idle03")
gMap.addGestureMapping("ChrBrad@Idle01_PleaBt02", "METAPHORIC", "ASSUMPTION", "BOTH_HANDS", "", "ChrBrad@Idle01")
gMap.addGestureMapping("ChrBrad@Idle02_PleaBt01", "METAPHORIC", "ASSUMPTION", "BOTH_HANDS", "open", "ChrBrad@Idle02")
gMap.addGestureMapping("ChrBrad@Idle02_PleaBt02", "METAPHORIC", "ASSUMPTION", "BOTH_HANDS", "tight", "ChrBrad@Idle02")
gMap.addGestureMapping("ChrBrad@Idle03_PleaBt01", "METAPHORIC", "ASSUMPTION", "BOTH_HANDS", "open", "ChrBrad@Idle03")
gMap.addGestureMapping("ChrBrad@Idle03_PleaBt02", "METAPHORIC", "ASSUMPTION", "BOTH_HANDS", "tight", "ChrBrad@Idle03")
gMap.addGestureMapping("ChrBrad@Idle01_BeatLowLf01", "METAPHORIC", "RHETORICAL", "LEFT_HAND", "noheadtilt", "ChrBrad@Idle01")
gMap.addGestureMapping("ChrBrad@Idle01_BeatLowLf02", "METAPHORIC", "RHETORICAL", "LEFT_HAND", "headtilt", "ChrBrad@Idle01")
gMap.addGestureMapping("ChrBrad@Idle01_BeatLowRt01", "METAPHORIC", "RHETORICAL", "RIGHT_HAND", "", "ChrBrad@Idle01")
gMap.addGestureMapping("ChrBrad@Idle02_BeatLowLf01", "METAPHORIC", "RHETORICAL", "LEFT_HAND", "", "ChrBrad@Idle02")
gMap.addGestureMapping("ChrBrad@Idle02_BeatLowRt01", "METAPHORIC", "RHETORICAL", "RIGHT_HAND", "", "ChrBrad@Idle02")
gMap.addGestureMapping("ChrBrad@Idle03_BeatLowLf01", "METAPHORIC", "RHETORICAL", "LEFT_HAND", "", "ChrBrad@Idle03")
gMap.addGestureMapping("ChrBrad@Idle03_BeatLowRt01", "METAPHORIC", "RHETORICAL", "RIGHT_HAND", "", "ChrBrad@Idle03")
gMap.addGestureMapping("ChrBrad@Idle01_BeatMidBt01", "METAPHORIC", "INCLUSIVITY", "BOTH_HANDS", "mid", "ChrBrad@Idle01")
gMap.addGestureMapping("ChrBrad@Idle01_BeatLowBt01", "METAPHORIC", "INCLUSIVITY", "BOTH_HANDS", "low", "ChrBrad@Idle01")
gMap.addGestureMapping("ChrBrad@Idle02_BeatMidBt01", "METAPHORIC", "INCLUSIVITY", "BOTH_HANDS", "mid", "ChrBrad@Idle02")
gMap.addGestureMapping("ChrBrad@Idle02_BeatLowBt01", "METAPHORIC", "INCLUSIVITY", "BOTH_HANDS", "low", "ChrBrad@Idle02")
gMap.addGestureMapping("ChrBrad@Idle03_BeatMidBt01", "METAPHORIC", "INCLUSIVITY", "BOTH_HANDS", "mid", "ChrBrad@Idle03")
gMap.addGestureMapping("ChrBrad@Idle03_BeatLowBt01", "METAPHORIC", "INCLUSIVITY", "BOTH_HANDS", "low", "ChrBrad@Idle03")
gMap.addGestureMapping("ChrBrad@Idle01_BeatLowLf01", "METAPHORIC", "QUESTION", "LEFT_HAND", "noheadtilt", "ChrBrad@Idle01")
gMap.addGestureMapping("ChrBrad@Idle01_BeatLowLf02", "METAPHORIC", "QUESTION", "LEFT_HAND", "headtilt", "ChrBrad@Idle01")
gMap.addGestureMapping("ChrBrad@Idle01_BeatLowRt01", "METAPHORIC", "QUESTION", "RIGHT_HAND", "", "ChrBrad@Idle01")
gMap.addGestureMapping("ChrBrad@Idle02_BeatLowLf01", "METAPHORIC", "QUESTION", "LEFT_HAND", "", "ChrBrad@Idle02")
gMap.addGestureMapping("ChrBrad@Idle02_BeatLowRt01", "METAPHORIC", "QUESTION", "RIGHT_HAND", "", "ChrBrad@Idle02")
gMap.addGestureMapping("ChrBrad@Idle03_BeatLowLf01", "METAPHORIC", "QUESTION", "LEFT_HAND", "", "ChrBrad@Idle03")
gMap.addGestureMapping("ChrBrad@Idle03_BeatLowRt01", "METAPHORIC", "QUESTION", "RIGHT_HAND", "", "ChrBrad@Idle03")
gMap.addGestureMapping("ChrBrad@Idle01_ChopLf01", "METAPHORIC", "OBLIGATION", "LEFT_HAND", "", "ChrBrad@Idle01")
gMap.addGestureMapping("ChrBrad@Idle01_ChopBt01", "METAPHORIC", "OBLIGATION", "BOTH_HANDS", "", "ChrBrad@Idle01")
gMap.addGestureMapping("ChrBrad@Idle02_ChopLf01", "METAPHORIC", "OBLIGATION", "LEFT_HAND", "", "ChrBrad@Idle02")
gMap.addGestureMapping("ChrBrad@Idle02_ChopBt01", "METAPHORIC", "OBLIGATION", "BOTH_HANDS", "", "ChrBrad@Idle02")
gMap.addGestureMapping("ChrBrad@Idle03_ChopLf01", "METAPHORIC", "OBLIGATION", "LEFT_HAND", "", "ChrBrad@Idle03")
gMap.addGestureMapping("ChrBrad@Idle03_ChopBt01", "METAPHORIC", "OBLIGATION", "BOTH_HANDS", "", "ChrBrad@Idle03")
gMap.addGestureMapping("ChrBrad@Idle01_BeatLowLf01", "EMBLEM", "GREETING", "LEFT_HAND", "", "ChrBrad@Idle01")
gMap.addGestureMapping("ChrBrad@Idle02_BeatLowLf01", "EMBLEM", "GREETING", "LEFT_HAND", "", "ChrBrad@Idle02")
gMap.addGestureMapping("ChrBrad@Idle03_BeatLowLf01", "EMBLEM", "GREETING", "LEFT_HAND", "", "ChrBrad@Idle03")
gMap.addGestureMapping("ChrBrad@Idle01_Contemplate01", "ADAPTOR", "CONTEMPLATE", "BOTH_HANDS", "mid", "ChrBrad@Idle01")
gMap.addGestureMapping("ChrBrad@Idle01_Think01", "ADAPTOR", "CONTEMPLATE", "BOTH_HANDS", "low", "ChrBrad@Idle01")

# Set up face definition
print 'Setting up face definition'
# Brad's face definition
bradFace = scene.createFaceDefinition('ChrBrad')
bradFace.setFaceNeutral('ChrBrad@face_neutral')
bradFace.setAU(1,  "left",  "ChrBrad@001_inner_brow_raiser_lf")
bradFace.setAU(1,  "right", "ChrBrad@001_inner_brow_raiser_rt")
bradFace.setAU(2,  "left",  "ChrBrad@002_outer_brow_raiser_lf")
bradFace.setAU(2,  "right", "ChrBrad@002_outer_brow_raiser_rt")
bradFace.setAU(4,  "left",  "ChrBrad@004_brow_lowerer_lf")
bradFace.setAU(4,  "right", "ChrBrad@004_brow_lowerer_rt")
bradFace.setAU(5,  "both",  "ChrBrad@005_upper_lid_raiser")
bradFace.setAU(6,  "both",  "ChrBrad@006_cheek_raiser")
bradFace.setAU(7,  "both",  "ChrBrad@007_lid_tightener")
bradFace.setAU(10, "both",  "ChrBrad@010_upper_lip_raiser")
bradFace.setAU(12, "left",  "ChrBrad@012_lip_corner_puller_lf")
bradFace.setAU(12, "right", "ChrBrad@012_lip_corner_puller_rt")
bradFace.setAU(25, "both",  "ChrBrad@025_lips_part")
bradFace.setAU(26, "both",  "ChrBrad@026_jaw_drop")
bradFace.setAU(45, "left",  "ChrBrad@045_blink_lf")
bradFace.setAU(45, "right", "ChrBrad@045_blink_rt")

bradFace.setViseme("open",    "ChrBrad@open")
bradFace.setViseme("W",       "ChrBrad@W")
bradFace.setViseme("ShCh",    "ChrBrad@ShCh")
bradFace.setViseme("PBM",     "ChrBrad@PBM")
bradFace.setViseme("FV",      "ChrBrad@FV")
bradFace.setViseme("wide",    "ChrBrad@wide")
bradFace.setViseme("tBack",   "ChrBrad@tBack")
bradFace.setViseme("tRoof",   "ChrBrad@tRoof")
bradFace.setViseme("tTeeth",  "ChrBrad@tTeeth")

print 'Adding character into scene'
# Set up Brad
brad = scene.createCharacter('ChrBrad', '')
bradSkeleton = scene.createSkeleton('ChrBrad.sk')
brad.setSkeleton(bradSkeleton)
# Set position
bradPos = SrVec(0, 0, 0)
brad.setPosition(bradPos)
# Set facing direction
bradFacing = SrVec(0, 0, 0)
brad.setHPR(bradFacing)
# Set face definition
brad.setFaceDefinition(bradFace)
# Set standard controller
brad.createStandardControllers()
# Deformable mesh
brad.setDoubleAttribute('deformableMeshScale', .01)
brad.setStringAttribute('deformableMesh', 'ChrBrad.dae')
# Lip syncing diphone setup
brad.setStringAttribute('lipSyncSetName', 'default')
brad.setBoolAttribute('usePhoneBigram', True)
brad.setVoice('remote')
brad.setVoiceCode('Microsoft|Anna')
# Gesture map setup
brad.setStringAttribute('gestureMap', 'ChrBrad')
brad.setBoolAttribute('bmlRequest.autoGestureTransition', True)
# Retarget 
#setup locomotion
scene.run('BehaviorSetMaleMocapLocomotion.py')
setupBehaviorSet()
retargetBehaviorSet('ChrBrad')
#setup reach 
# scene.run('BehaviorSetReaching.py')
# setupBehaviorSet()
# retargetBehaviorSet('ChrBrad')
# Turn on GPU deformable geometry
brad.setStringAttribute("displayType", "GPUmesh")

# Set up steering
print 'Setting up steering'
steerManager = scene.getSteerManager()
steerManager.setEnable(False)
brad.setBoolAttribute('steering.pathFollowingMode', True)
steerManager.setEnable(True)

# setup GUI
print 'Setting up GUI'
scene.run('GUIUtil.py')
gui = GUIManager()
class GUIHandler:
	def __init__(self):
		self.speed = 0.0	
		self.turnAngle = 0.0
		self.strafeDir = 0.0	

	def handleStartLocoButton(self,args):
	
		bml.execBML('ChrBrad', '<blend name="mocapLocomotion"/>')
		#animationList = [ 'ChrBrad@Idle01_YouLf01', 'ChrBrad@Idle01_BeatLowLf01', 'ChrBrad@Idle01_Shrug01', 'ChrBrad@Idle01_NegativeBt01']
		#which = random.randrange(0, len(animationList), 1)
		#bml.execBML('ChrBrad', '<animation name="' + animationList[which] +'"/>')
	
	def handleStopLocoButton(self,args):		
		#print 'handleStopLoco'
		bml.execBML('ChrBrad', '<blend name="null" sbm:schedule-mode="Now" sbm:wrap-mode="Loop"/>')
		#bml.execBML('ChrBrad', '<sbm:reach target="touchPawn" sbm:reach-duration="0.2"/>')
	def handleSpeedSlider(self,args):
		slider = args.window		
		#print 'speed slider value = ' + str(slider.getCurrentValue())	
		self.speed = slider.getCurrentValue()
		bml.execBML('ChrBrad', '<blend mode="update" name="mocapLocomotion" sbm:schedule-mode="Now" sbm:wrap-mode="Loop" x="'+str(self.speed)+'" y="'+str(self.turnAngle)+'" z="' +str(self.strafeDir)+ '"/>')
		
		
	def handleTurnSlider(self,args):
		slider = args.window
		#print 'turn slider value = ' + str(slider.getCurrentValue())
		self.turnAngle = slider.getCurrentValue()-180.0
		#bml.execBML('ChrBrad', '<blend mode="update" name="mocapLocomotion" sbm:schedule-mode="Now" sbm:wrap-mode="Loop" y="'+str(turnAngle)+'"/>')
		bml.execBML('ChrBrad', '<blend mode="update" name="mocapLocomotion" sbm:schedule-mode="Now" sbm:wrap-mode="Loop" x="'+str(self.speed)+'" y="'+str(self.turnAngle)+'" z="' +str(self.strafeDir)+ '"/>')
		
	def handleStrafeSlider(self,args):
		slider = args.window
		#print 'strafe slider value = ' + str(slider.getCurrentValue())
		self.strafeDir = slider.getCurrentValue()-90.0
		#bml.execBML('ChrBrad', '<blend mode="update" name="mocapLocomotion" sbm:schedule-mode="Now" sbm:wrap-mode="Loop" z="'+str(strafeDir)+'"/>')
		bml.execBML('ChrBrad', '<blend mode="update" name="mocapLocomotion" sbm:schedule-mode="Now" sbm:wrap-mode="Loop" x="'+str(self.speed)+'" y="'+str(self.turnAngle)+'" z="' +str(self.strafeDir)+ '"/>')		

alphaVal = 0.5
guiHandler = GUIHandler()
startLocoBtn = gui.createButton('startLocoBtn','Start Locomotion')
startLocoBtn.subscribeEvent(PushButton.EventClicked, guiHandler.handleStartLocoButton)
startLocoBtn.setAlpha(alphaVal)
stopLocoBtn = gui.createButton('stopLocoBtn','Stop Locomotion')
stopLocoBtn.subscribeEvent(PushButton.EventClicked, guiHandler.handleStopLocoButton)
stopLocoBtn.setAlpha(alphaVal)

#text1 = gui.createStaticText('text1','Speed')
speedSlider = gui.createSlider('speedSlider',4.0,0.0)
speedSlider.subscribeEvent(Slider.EventValueChanged, guiHandler.handleSpeedSlider)
speedSlider.setAlpha(alphaVal)
turnSlider = gui.createSlider('turnSlider',360.0,180.0)
turnSlider.subscribeEvent(Slider.EventValueChanged, guiHandler.handleTurnSlider)
turnSlider.setAlpha(alphaVal)
strafeSlider = gui.createSlider('strafeSlider',180.0,90.0)
strafeSlider.subscribeEvent(Slider.EventValueChanged, guiHandler.handleStrafeSlider)
strafeSlider.setAlpha(alphaVal)


# Start the simulation
print 'Starting the simulation'
sim.start()

bml.execBML('ChrBrad', '<body posture="ChrBrad@Idle01"/>')
bml.execBML('ChrBrad', '<saccade mode="listen"/>')
#bml.execBML('ChrBrad', '<gaze sbm:handle="brad" target="camera"/>')

sim.resume()
