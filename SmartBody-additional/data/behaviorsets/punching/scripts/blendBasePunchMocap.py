
def blendPunchSetup(skeletonName, baseJoint, preFix, statePreFix, interpolatorType):
	print "** State: blendBaseReach" + interpolatorType

	stateManager = scene.getStateManager()
	stateName = statePreFix+"Punch"+interpolatorType
	if (stateManager.getBlend(stateName) != None): # don't create duplicate state
		return		
	state = stateManager.createMotionBlendBase(stateName, skeletonName, 3)
	state.setBlendSkeleton(skeletonName)
	# add motions
	motions = StringVec()
	motions.append("ChrGarza@IdleFight01_PunchForwardFloor01")
	motions.append("ChrGarza@IdleFight01_PunchForwardMediumFar01")
	motions.append("ChrGarza@IdleFight01_PunchLeft45Floor01")
	motions.append("ChrGarza@IdleFight01_PunchLeft45High01")
	motions.append("ChrGarza@IdleFight01_PunchLeft45Low01")
	motions.append("ChrGarza@IdleFight01_PunchLeft45MediumFar01")
	motions.append("ChrGarza@IdleFight01_PunchLeft90Floor01")
	motions.append("ChrGarza@IdleFight01_PunchLeft90High01")
	motions.append("ChrGarza@IdleFight01_PunchLeft90Low01")
	motions.append("ChrGarza@IdleFight01_PunchLeft90MediumFar01")
	motions.append("ChrGarza@IdleFight01_PunchLeft90MediumNear01")
	motions.append("ChrGarza@IdleFight01_PunchRight45Floor01")
	motions.append("ChrGarza@IdleFight01_PunchRight45High01")
	motions.append("ChrGarza@IdleFight01_PunchRight45Low01")
	motions.append("ChrGarza@IdleFight01_PunchRight45MediumFar01")
	motions.append("ChrGarza@IdleFight01_PunchRight45MediumNear01")
	motions.append("ChrGarza@IdleFight01_PunchRight90Floor01")
	motions.append("ChrGarza@IdleFight01_PunchRight90High01")
	motions.append("ChrGarza@IdleFight01_PunchRight90Low01")
	motions.append("ChrGarza@IdleFight01_PunchRight90MediumFar01")
	motions.append("ChrGarza@IdleFight01_PunchRight90MediumNear01")
	
	para = DoubleVec();
	for i in range(0,3):
		para.append(0)
	para.append(0)
	for i in range(0, len(motions)):
		state.addMotion(motions[i], para)


	points0 = DoubleVec()
	points0.append(0) # ChrGarza@IdleFight01_PunchForwardFloor01 0
	points0.append(0) # ChrGarza@IdleFight01_PunchForwardMediumFar01 0
	points0.append(0) # ChrGarza@IdleFight01_PunchLeft45Floor01 0
	points0.append(0) # ChrGarza@IdleFight01_PunchLeft45High01 0
	points0.append(0) # ChrGarza@IdleFight01_PunchLeft45Low01 0
	points0.append(0) # ChrGarza@IdleFight01_PunchLeft45MediumFar01 0
	points0.append(0) # ChrGarza@IdleFight01_PunchLeft90Floor01 0
	points0.append(0) # ChrGarza@IdleFight01_PunchLeft90High01 0
	points0.append(0) # ChrGarza@IdleFight01_PunchLeft90Low01 0
	points0.append(0) # ChrGarza@IdleFight01_PunchLeft90MediumFar01 0
	points0.append(0) # ChrGarza@IdleFight01_PunchLeft90MediumNear01 0
	points0.append(0) # ChrGarza@IdleFight01_PunchRight45Floor01 0
	points0.append(0) # ChrGarza@IdleFight01_PunchRight45High01 0
	points0.append(0) # ChrGarza@IdleFight01_PunchRight45Low01 0
	points0.append(0) # ChrGarza@IdleFight01_PunchRight45MediumFar01 0
	points0.append(0) # ChrGarza@IdleFight01_PunchRight45MediumNear01 0
	points0.append(0) # ChrGarza@IdleFight01_PunchRight90Floor01 0
	points0.append(0) # ChrGarza@IdleFight01_PunchRight90High01 0
	points0.append(0) # ChrGarza@IdleFight01_PunchRight90Low01 0
	points0.append(0) # ChrGarza@IdleFight01_PunchRight90MediumFar01 0
	points0.append(0) # ChrGarza@IdleFight01_PunchRight90MediumNear01 0
	state.addCorrespondencePoints(motions, points0)
	points1 = DoubleVec()
	points1.append(2.08) # ChrGarza@IdleFight01_PunchForwardFloor01 1
	points1.append(2.08317) # ChrGarza@IdleFight01_PunchForwardMediumFar01 1
	points1.append(1.87417) # ChrGarza@IdleFight01_PunchLeft45Floor01 1
	points1.append(2.31) # ChrGarza@IdleFight01_PunchLeft45High01 1
	points1.append(2.28583) # ChrGarza@IdleFight01_PunchLeft45Low01 1
	points1.append(1.95459) # ChrGarza@IdleFight01_PunchLeft45MediumFar01 1
	points1.append(1.90083) # ChrGarza@IdleFight01_PunchLeft90Floor01 1
	points1.append(1.63335) # ChrGarza@IdleFight01_PunchLeft90High01 1
	points1.append(2.12) # ChrGarza@IdleFight01_PunchLeft90Low01 1
	points1.append(1.72417) # ChrGarza@IdleFight01_PunchLeft90MediumFar01 1
	points1.append(1.48752) # ChrGarza@IdleFight01_PunchLeft90MediumNear01 1
	points1.append(2.93206) # ChrGarza@IdleFight01_PunchRight45Floor01 1
	points1.append(1.97917) # ChrGarza@IdleFight01_PunchRight45High01 1
	points1.append(2.33541) # ChrGarza@IdleFight01_PunchRight45Low01 1
	points1.append(2.03417) # ChrGarza@IdleFight01_PunchRight45MediumFar01 1
	points1.append(2.26) # ChrGarza@IdleFight01_PunchRight45MediumNear01 1
	points1.append(2.74583) # ChrGarza@IdleFight01_PunchRight90Floor01 1
	points1.append(2.385) # ChrGarza@IdleFight01_PunchRight90High01 1
	points1.append(2.28) # ChrGarza@IdleFight01_PunchRight90Low01 1
	points1.append(2.41083) # ChrGarza@IdleFight01_PunchRight90MediumFar01 1
	points1.append(1.88917) # ChrGarza@IdleFight01_PunchRight90MediumNear01 1
	state.addCorrespondencePoints(motions, points1)
	points2 = DoubleVec()
	points2.append(3.63333) # ChrGarza@IdleFight01_PunchForwardFloor01 2
	points2.append(3.7) # ChrGarza@IdleFight01_PunchForwardMediumFar01 2
	points2.append(3.3) # ChrGarza@IdleFight01_PunchLeft45Floor01 2
	points2.append(3.63333) # ChrGarza@IdleFight01_PunchLeft45High01 2
	points2.append(3.96667) # ChrGarza@IdleFight01_PunchLeft45Low01 2
	points2.append(3.46667) # ChrGarza@IdleFight01_PunchLeft45MediumFar01 2
	points2.append(3.96667) # ChrGarza@IdleFight01_PunchLeft90Floor01 2
	points2.append(2.96667) # ChrGarza@IdleFight01_PunchLeft90High01 2
	points2.append(3.63333) # ChrGarza@IdleFight01_PunchLeft90Low01 2
	points2.append(3.3) # ChrGarza@IdleFight01_PunchLeft90MediumFar01 2
	points2.append(2.63333) # ChrGarza@IdleFight01_PunchLeft90MediumNear01 2
	points2.append(4.46667) # ChrGarza@IdleFight01_PunchRight45Floor01 2
	points2.append(3.3) # ChrGarza@IdleFight01_PunchRight45High01 2
	points2.append(3.8) # ChrGarza@IdleFight01_PunchRight45Low01 2
	points2.append(3.3) # ChrGarza@IdleFight01_PunchRight45MediumFar01 2
	points2.append(3.63333) # ChrGarza@IdleFight01_PunchRight45MediumNear01 2
	points2.append(3.96667) # ChrGarza@IdleFight01_PunchRight90Floor01 2
	points2.append(3.63333) # ChrGarza@IdleFight01_PunchRight90High01 2
	points2.append(3.63333) # ChrGarza@IdleFight01_PunchRight90Low01 2
	points2.append(3.96667) # ChrGarza@IdleFight01_PunchRight90MediumFar01 2
	points2.append(3.3) # ChrGarza@IdleFight01_PunchRight90MediumNear01 2
	state.addCorrespondencePoints(motions, points2)
	#for i in range(0, len(motions)):
	#	state.addMotion(motions[i], paramsX[i], paramsY[i], paramsZ[i])
	
		
	state.buildBlendBase("reach",interpolatorType,True);
	state.buildVisSurfaces("smooth","curve",4,80);
	state.buildVisSurfaces("error","curve",4,50);

	# plot all motions
	for i in range(0, len(motions)):
		#state.plotMotion(motions[i], 20, False)
		state.plotMotionFrameTime(motions[i], points1[i], False)
		#state.createMotionVectorFlow(motions[i], 0, 0.5)
	
	
	# reset parameters (because it needs context of correspondance points, extract parameters from motion)
	
	

