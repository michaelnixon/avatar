from random import choice
print "|--------------------------------------------|"
print "|           Starting Event Demo              |"
print "|--------------------------------------------|"

# Add asset paths
scene.addAssetPath('script', 'scripts')
scene.addAssetPath('mesh', 'mesh')
scene.addAssetPath('motion', 'ChrBrad')
scene.addAssetPath('motion', 'ChrRachel')
scene.loadAssets()

# Set scene parameters to fit new Brad and Rachel
print 'Configuring scene parameters and camera'
scene.setScale(1.0)
scene.setBoolAttribute('internalAudio', True)
scene.run('default-viewer.py')
camera = getCamera()
camera.setEye(0.12, 1.71, 1.86)
camera.setCenter(0.2, 1.00, 0.01)
camera.setUpVector(SrVec(0, 1, 0))
camera.setScale(1)
camera.setFov(1.0472)
camera.setFarPlane(100)
camera.setNearPlane(0.1)
camera.setAspectRatio(0.966897)
scene.getPawn('camera').setPosition(SrVec(0, 1.55, 3))

# Set joint map for Brad and Rachel
print 'Setting up joint map for Brad and Rachel'
scene.run('zebra2-map.py')
zebra2Map = scene.getJointMapManager().getJointMap('zebra2')
bradSkeleton = scene.getSkeleton('ChrBrad.sk')
zebra2Map.applySkeleton(bradSkeleton)
zebra2Map.applyMotionRecurse('ChrBrad')
rachelSkeleton = scene.getSkeleton('ChrRachel.sk')
zebra2Map.applySkeleton(rachelSkeleton)
zebra2Map.applyMotionRecurse('ChrRachel')

# Establish lip syncing data set
scene.run('init-diphoneDefault.py')

# Set gesture map for Brad and Rachel
print 'Setting gesture map for Brad and Rachel'
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

# Rachel's gestures
gMap1 = gMapManager.createGestureMap("ChrRachel")
gMap1.addGestureMapping("ChrRachel_ChrBrad@Idle01_YouLf01", "DEICTIC", "YOU", "LEFT_HAND", "", "ChrRachel_ChrBrad@Idle01")
gMap1.addGestureMapping("ChrRachel_ChrBrad@Idle02_YouLf01", "DEICTIC", "YOU", "LEFT_HAND", "", "ChrRachel_ChrBrad@Idle02")
gMap1.addGestureMapping("ChrRachel_ChrBrad@Idle03_YouLf01", "DEICTIC", "YOU", "LEFT_HAND", "", "ChrRachel_ChrBrad@Idle03")
gMap1.addGestureMapping("ChrRachel_ChrBrad@Idle01_MeLf01", "DEICTIC", "ME", "LEFT_HAND", "", "ChrRachel_ChrBrad@Idle01")
gMap1.addGestureMapping("ChrRachel_ChrBrad@Idle02_MeRt01", "DEICTIC", "ME", "RIGHT_HAND", "", "ChrRachel_ChrBrad@Idle02")
gMap1.addGestureMapping("ChrRachel_ChrBrad@Idle03_MeLf01", "DEICTIC", "ME", "LEFT_HAND", "", "ChrRachel_ChrBrad@Idle03")
gMap1.addGestureMapping("ChrRachel_ChrBrad@Idle01_IndicateLeftLf01", "DEICTIC", "LEFT", "LEFT_HAND", "", "ChrRachel_ChrBrad@Idle01")
gMap1.addGestureMapping("ChrRachel_ChrBrad@Idle01_IndicateLeftBt01", "DEICTIC", "LEFT", "BOTH_HANDS", "", "ChrRachel_ChrBrad@Idle01")
gMap1.addGestureMapping("ChrRachel_ChrBrad@Idle01_IndicateRightRt01", "DEICTIC", "RIGHT", "RIGHT_HAND", "", "ChrRachel_ChrBrad@Idle01")
gMap1.addGestureMapping("ChrRachel_ChrBrad@Idle01_IndicateRightBt01", "DEICTIC", "RIGHT", "BOTH_HANDS", "", "ChrRachel_ChrBrad@Idle01")
gMap1.addGestureMapping("ChrRachel_ChrBrad@Idle01_NegativeBt01", "METAPHORIC", "NEGATION", "BOTH_HANDS", "", "ChrRachel_ChrBrad@Idle01")
gMap1.addGestureMapping("ChrRachel_ChrBrad@Idle01_NegativeRt01", "METAPHORIC", "NEGATION", "RIGHT_HAND", "", "ChrRachel_ChrBrad@Idle01")
gMap1.addGestureMapping("ChrRachel_ChrBrad@Idle02_NegativeBt01", "METAPHORIC", "NEGATION", "BOTH_HANDS", "", "ChrRachel_ChrBrad@Idle02")
gMap1.addGestureMapping("ChrRachel_ChrBrad@Idle02_NegativeLf01", "METAPHORIC", "NEGATION", "LEFT_HAND", "", "ChrRachel_ChrBrad@Idle02")
gMap1.addGestureMapping("ChrRachel_ChrBrad@Idle03_NegativeBt01", "METAPHORIC", "NEGATION", "BOTH_HANDS", "", "ChrRachel_ChrBrad@Idle03")
gMap1.addGestureMapping("ChrRachel_ChrBrad@Idle03_NegativeLf01", "METAPHORIC", "NEGATION", "LEFT_HAND", "", "ChrRachel_ChrBrad@Idle03")
gMap1.addGestureMapping("ChrRachel_ChrBrad@Idle01_HoweverLf01", "METAPHORIC", "CONTRAST", "LEFT_HAND", "", "ChrRachel_ChrBrad@Idle01")
gMap1.addGestureMapping("ChrRachel_ChrBrad@Idle01_Shrug01", "METAPHORIC", "CONTRAST", "BOTH_HANDS", "", "ChrRachel_ChrBrad@Idle01")
gMap1.addGestureMapping("ChrRachel_ChrBrad@Idle02_Shrug01", "METAPHORIC", "CONTRAST", "BOTH_HANDS", "", "ChrRachel_ChrBrad@Idle02")
gMap1.addGestureMapping("ChrRachel_ChrBrad@Idle03_Shrug01", "METAPHORIC", "CONTRAST", "BOTH_HANDS", "", "ChrRachel_ChrBrad@Idle03")
gMap1.addGestureMapping("ChrRachel_ChrBrad@Idle01_PleaBt02", "METAPHORIC", "ASSUMPTION", "BOTH_HANDS", "", "ChrRachel_ChrBrad@Idle01")
gMap1.addGestureMapping("ChrRachel_ChrBrad@Idle02_PleaBt01", "METAPHORIC", "ASSUMPTION", "BOTH_HANDS", "open", "ChrRachel_ChrBrad@Idle02")
gMap1.addGestureMapping("ChrRachel_ChrBrad@Idle02_PleaBt02", "METAPHORIC", "ASSUMPTION", "BOTH_HANDS", "tight", "ChrRachel_ChrBrad@Idle02")
gMap1.addGestureMapping("ChrRachel_ChrBrad@Idle03_PleaBt01", "METAPHORIC", "ASSUMPTION", "BOTH_HANDS", "open", "ChrRachel_ChrBrad@Idle03")
gMap1.addGestureMapping("ChrRachel_ChrBrad@Idle03_PleaBt02", "METAPHORIC", "ASSUMPTION", "BOTH_HANDS", "tight", "ChrRachel_ChrBrad@Idle03")
gMap1.addGestureMapping("ChrRachel_ChrBrad@Idle01_BeatLowLf01", "METAPHORIC", "RHETORICAL", "LEFT_HAND", "noheadtilt", "ChrRachel_ChrBrad@Idle01")
gMap1.addGestureMapping("ChrRachel_ChrBrad@Idle01_BeatLowLf02", "METAPHORIC", "RHETORICAL", "LEFT_HAND", "headtilt", "ChrRachel_ChrBrad@Idle01")
gMap1.addGestureMapping("ChrRachel_ChrBrad@Idle01_BeatLowRt01", "METAPHORIC", "RHETORICAL", "RIGHT_HAND", "", "ChrRachel_ChrBrad@Idle01")
gMap1.addGestureMapping("ChrRachel_ChrBrad@Idle02_BeatLowLf01", "METAPHORIC", "RHETORICAL", "LEFT_HAND", "", "ChrRachel_ChrBrad@Idle02")
gMap1.addGestureMapping("ChrRachel_ChrBrad@Idle02_BeatLowRt01", "METAPHORIC", "RHETORICAL", "RIGHT_HAND", "", "ChrRachel_ChrBrad@Idle02")
gMap1.addGestureMapping("ChrRachel_ChrBrad@Idle03_BeatLowLf01", "METAPHORIC", "RHETORICAL", "LEFT_HAND", "", "ChrRachel_ChrBrad@Idle03")
gMap1.addGestureMapping("ChrRachel_ChrBrad@Idle03_BeatLowRt01", "METAPHORIC", "RHETORICAL", "RIGHT_HAND", "", "ChrRachel_ChrBrad@Idle03")
gMap1.addGestureMapping("ChrRachel_ChrBrad@Idle01_BeatMidBt01", "METAPHORIC", "INCLUSIVITY", "BOTH_HANDS", "mid", "ChrRachel_ChrBrad@Idle01")
gMap1.addGestureMapping("ChrRachel_ChrBrad@Idle01_BeatLowBt01", "METAPHORIC", "INCLUSIVITY", "BOTH_HANDS", "low", "ChrRachel_ChrBrad@Idle01")
gMap1.addGestureMapping("ChrRachel_ChrBrad@Idle02_BeatMidBt01", "METAPHORIC", "INCLUSIVITY", "BOTH_HANDS", "mid", "ChrRachel_ChrBrad@Idle02")
gMap1.addGestureMapping("ChrRachel_ChrBrad@Idle02_BeatLowBt01", "METAPHORIC", "INCLUSIVITY", "BOTH_HANDS", "low", "ChrRachel_ChrBrad@Idle02")
gMap1.addGestureMapping("ChrRachel_ChrBrad@Idle03_BeatMidBt01", "METAPHORIC", "INCLUSIVITY", "BOTH_HANDS", "mid", "ChrRachel_ChrBrad@Idle03")
gMap1.addGestureMapping("ChrRachel_ChrBrad@Idle03_BeatLowBt01", "METAPHORIC", "INCLUSIVITY", "BOTH_HANDS", "low", "ChrRachel_ChrBrad@Idle03")
gMap1.addGestureMapping("ChrRachel_ChrBrad@Idle01_BeatLowLf01", "METAPHORIC", "QUESTION", "LEFT_HAND", "noheadtilt", "ChrRachel_ChrBrad@Idle01")
gMap1.addGestureMapping("ChrRachel_ChrBrad@Idle01_BeatLowLf02", "METAPHORIC", "QUESTION", "LEFT_HAND", "headtilt", "ChrRachel_ChrBrad@Idle01")
gMap1.addGestureMapping("ChrRachel_ChrBrad@Idle01_BeatLowRt01", "METAPHORIC", "QUESTION", "RIGHT_HAND", "", "ChrRachel_ChrBrad@Idle01")
gMap1.addGestureMapping("ChrRachel_ChrBrad@Idle02_BeatLowLf01", "METAPHORIC", "QUESTION", "LEFT_HAND", "", "ChrRachel_ChrBrad@Idle02")
gMap1.addGestureMapping("ChrRachel_ChrBrad@Idle02_BeatLowRt01", "METAPHORIC", "QUESTION", "RIGHT_HAND", "", "ChrRachel_ChrBrad@Idle02")
gMap1.addGestureMapping("ChrRachel_ChrBrad@Idle03_BeatLowLf01", "METAPHORIC", "QUESTION", "LEFT_HAND", "", "ChrRachel_ChrBrad@Idle03")
gMap1.addGestureMapping("ChrRachel_ChrBrad@Idle03_BeatLowRt01", "METAPHORIC", "QUESTION", "RIGHT_HAND", "", "ChrRachel_ChrBrad@Idle03")
gMap1.addGestureMapping("ChrRachel_ChrBrad@Idle01_ChopLf01", "METAPHORIC", "OBLIGATION", "LEFT_HAND", "", "ChrRachel_ChrBrad@Idle01")
gMap1.addGestureMapping("ChrRachel_ChrBrad@Idle01_ChopBt01", "METAPHORIC", "OBLIGATION", "BOTH_HANDS", "", "ChrRachel_ChrBrad@Idle01")
gMap1.addGestureMapping("ChrRachel_ChrBrad@Idle02_ChopLf01", "METAPHORIC", "OBLIGATION", "LEFT_HAND", "", "ChrRachel_ChrBrad@Idle02")
gMap1.addGestureMapping("ChrRachel_ChrBrad@Idle02_ChopBt01", "METAPHORIC", "OBLIGATION", "BOTH_HANDS", "", "ChrRachel_ChrBrad@Idle02")
gMap1.addGestureMapping("ChrRachel_ChrBrad@Idle03_ChopLf01", "METAPHORIC", "OBLIGATION", "LEFT_HAND", "", "ChrRachel_ChrBrad@Idle03")
gMap1.addGestureMapping("ChrRachel_ChrBrad@Idle03_ChopBt01", "METAPHORIC", "OBLIGATION", "BOTH_HANDS", "", "ChrRachel_ChrBrad@Idle03")
gMap1.addGestureMapping("ChrRachel_ChrBrad@Idle01_BeatLowLf01", "EMBLEM", "GREETING", "LEFT_HAND", "", "ChrRachel_ChrBrad@Idle01")
gMap1.addGestureMapping("ChrRachel_ChrBrad@Idle01_BeatLowLf02", "EMBLEM", "GREETING", "LEFT_HAND", "", "ChrRachel_ChrBrad@Idle02")
gMap1.addGestureMapping("ChrRachel_ChrBrad@Idle01_BeatLowLf03", "EMBLEM", "GREETING", "LEFT_HAND", "", "ChrRachel_ChrBrad@Idle03")
gMap1.addGestureMapping("ChrRachel_ChrBrad@Idle01_Contemplate01", "ADAPTOR", "CONTEMPLATE", "BOTH_HANDS", "mid", "ChrRachel_ChrBrad@Idle01")
gMap1.addGestureMapping("ChrRachel_ChrBrad@Idle01_Think01", "ADAPTOR", "CONTEMPLATE", "BOTH_HANDS", "low", "ChrRachel_ChrBrad@Idle01")

# Setting up face definition
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

# Rachel's face definition
rachelFace = scene.createFaceDefinition('ChrRachel')
rachelFace.setFaceNeutral('ChrRachel@face_neutral')
rachelFace.setAU(1,  "left",  "ChrRachel@001_inner_brow_raiser_lf")
rachelFace.setAU(1,  "right", "ChrRachel@001_inner_brow_raiser_rt")
rachelFace.setAU(2,  "left",  "ChrRachel@002_outer_brow_raiser_lf")
rachelFace.setAU(2,  "right", "ChrRachel@002_outer_brow_raiser_rt")
rachelFace.setAU(4,  "left",  "ChrRachel@004_brow_lowerer_lf")
rachelFace.setAU(4,  "right", "ChrRachel@004_brow_lowerer_rt")
rachelFace.setAU(5,  "both",  "ChrRachel@005_upper_lid_raiser")
rachelFace.setAU(6,  "both",  "ChrRachel@006_cheek_raiser")
rachelFace.setAU(7,  "both",  "ChrRachel@007_lid_tightener")
rachelFace.setAU(10, "both",  "ChrRachel@010_upper_lip_raiser")
rachelFace.setAU(12, "left",  "ChrRachel@012_lip_corner_puller_lf")
rachelFace.setAU(12, "right", "ChrRachel@012_lip_corner_puller_rt")
rachelFace.setAU(25, "both",  "ChrRachel@025_lips_part")
rachelFace.setAU(26, "both",  "ChrRachel@026_jaw_drop")
rachelFace.setAU(45, "left",  "ChrRachel@045_blink_lf")
rachelFace.setAU(45, "right", "ChrRachel@045_blink_rt")

rachelFace.setViseme("open",    "ChrRachel@open")
rachelFace.setViseme("W",       "ChrRachel@W")
rachelFace.setViseme("ShCh",    "ChrRachel@ShCh")
rachelFace.setViseme("PBM",     "ChrRachel@PBM")
rachelFace.setViseme("FV",      "ChrRachel@FV")
rachelFace.setViseme("wide",    "ChrRachel@wide")
rachelFace.setViseme("tBack",   "ChrRachel@tBack")
rachelFace.setViseme("tRoof",   "ChrRachel@tRoof")
rachelFace.setViseme("tTeeth",  "ChrRachel@tTeeth")

# Setting up Brad and Rachel
print 'Setting up Brad'
brad = scene.createCharacter('ChrBrad', '')
bradSkeleton = scene.createSkeleton('ChrBrad.sk')
brad.setSkeleton(bradSkeleton)
bradPos = SrVec(.35, 0, 0)
brad.setPosition(bradPos)
brad.setHPR(SrVec(-17, 0, 0))
brad.setFaceDefinition(bradFace)
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
brad.setBoolAttribute('gestureRequest.autoGestureTransition', True)
# Idle pose
bml.execBML('ChrBrad', '<body posture="ChrBrad@Idle01"/>')

print 'Setting up Rachel'
rachel = scene.createCharacter('ChrRachel', '')
rachelSkeleton = scene.createSkeleton('ChrRachel.sk')
rachel.setSkeleton(rachelSkeleton)
rachel.setFaceDefinition(rachelFace)
rachelPos = SrVec(-.35, 0, 0)
rachel.setPosition(rachelPos)
rachel.setHPR(SrVec(17, 0, 0))
rachel.createStandardControllers()
# Deformable mesh
rachel.setDoubleAttribute('deformableMeshScale', .01)
rachel.setStringAttribute('deformableMesh', 'ChrRachel.dae')
# Lip syncing diphone setup
rachel.setStringAttribute('diphoneSetName', 'default')
rachel.setBoolAttribute('useDiphone', True)
rachel.setVoice('remote')
rachel.setVoiceCode('MicrosoftAnna')
# Gesture map setup
rachel.setStringAttribute('gestureMap', 'ChrRachel')
rachel.setBoolAttribute('gestureRequest.autoGestureTransition', True)
# Idle pose
bml.execBML('ChrRachel', '<body posture="ChrRachel_ChrBrad@Idle01"/>')

# Turning on deformable GPU
brad.setStringAttribute("displayType", "GPUmesh")
rachel.setStringAttribute("displayType", "GPUmesh")


# Set up pawn
print 'Setting up gaze target'
gazeTarget = scene.createPawn('gazeTarget')
gazeTarget.setPosition(SrVec(0.75, 1.54, 0.33))

# Configuring motion events
print 'Configuring motion events'
bradBML1 = '<gaze target="gazeTarget" sbm:joint-range="EYES NECK" sbm:joint-speed="850"/>'
bradBML2 = '<gaze target="camera" sbm:joint-range="EYES NECK" sbm:joint-speed="850"/>'
bradName = 'ChrBrad'

# First type of events, assigning an event to a motion at a set time
motion1 = scene.getMotion('ChrRachel_ChrBrad@Idle01_BeatHighBt01')
motion1.addEvent(0.5, 'motionSpeech', 'beat', False)
motion2 = scene.getMotion('ChrRachel_ChrBrad@Idle01_Contemplate01')
motion2.addEvent(0.3, 'motionSpeech', 'contemplate', False)
motion3 = scene.getMotion('ChrRachel_ChrBrad@Idle01_NegativeBt01')
motion3.addEvent(0.3, 'motionSpeech', 'negative', False)

# Update to repeat reaches
last = 0
canTime = True
delay = 4
rachelTime = 0
class EventDemo(SBScript):
	def update(self, time):
		global canTime, last, rachelTime
		if canTime:
			last = time
			canTime = False
		diff = time - last
		if diff >= delay:
			diff = 0
			canTime = True
		# If time's up, do action
		if canTime:
			# Adding sbm:event to the back of bml commands, so that they will trigger that specific event
			# When the bml command has ended
			bml.execBMLAt(0, 'ChrBrad', '<animation id="m1" name="ChrBrad@Idle01_YouLf01"/> +\
										 <sbm:event stroke="m1:stroke" message="sbm python bml.execBML(bradName, bradBML1)"/>')
			bml.execBMLAt(2, 'ChrBrad', '<animation id="m2" name="ChrBrad@Idle01_MeLf01"/> +\
										 <sbm:event stroke="m2:stroke" message="sbm python bml.execBML(bradName, bradBML2)"/>')
		diff2 = time - rachelTime
		if diff2 > 12:
			diff2 = 0
			rachelTime = time
			# Animations are triggering event handler which is in turn triggering speech as seen below
			bml.execBMLAt(0, 'ChrRachel', '<animation name="ChrRachel_ChrBrad@Idle01_BeatHighBt01"/>')
			bml.execBMLAt(3, 'ChrRachel', '<animation name="ChrRachel_ChrBrad@Idle01_Contemplate01"/>')
			bml.execBMLAt(8, 'ChrRachel', '<animation name="ChrRachel_ChrBrad@Idle01_NegativeBt01"/>')
			
# Run the update script
scene.removeScript('eventdemo')
eventdemo = EventDemo()
scene.addScript('eventdemo', eventdemo)

class MyEventHandler(SBEventHandler):
	
	def executeAction(self, event):
		params = event.getParameters()
		# Do action depending on message received from event handler
		if 'beat' in params:
			bml.execBML('ChrRachel', '<speech type="text/plain">What is the meaning of this?</speech>')
		if 'contemplate' in params:
			bml.execBML('ChrRachel', '<speech type="text/plain">Let me see, where did I last see him</speech>')
		if 'negative' in params:
			bml.execBML('ChrRachel', '<speech type="text/plain">This is unacceptable</speech>')
myHandler = MyEventHandler()
eventManager = scene.getEventManager()
eventManager.addEventHandler('motionSpeech', myHandler)

print '******************************************************'
print '* This script requires speech relay to work properly *'
print '*    It can be found under Window > Speech Relay     *'
print '******************************************************'
