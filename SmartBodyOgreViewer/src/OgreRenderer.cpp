#include "vhcl.h"

#include "OgreRenderer.h"
#include "OgreFrameListener.h"
#include "BoneBusHandler.h"
#include "DotSceneLoader.h"

OgreRenderer::OgreRenderer() : ExampleApplication()
{
	m_sbm = NULL;
	m_bonebus = NULL;
	m_useBoneBus = true;
	m_sbListener = NULL;
}

void OgreRenderer::setUseBoneBus(bool val) 
{
	m_useBoneBus = val;
}

bool OgreRenderer::isUseBoneBus() 
{
	return m_useBoneBus;
}

void OgreRenderer::destroyScene(void) 
{
	// Send vrProcEnd message to ActiveMQ
	vhmsg::ttu_notify2( "vrProcEnd", "renderer" );

	// Close ActiveMQ
	vhmsg::ttu_close();
}

void OgreRenderer::createDefaultScene(std::string meshName) 
{
	//mSceneMgr->setShadowTechnique( SHADOWTYPE_TEXTURE_MODULATIVE );

	/* doc for shadows etc: http://www.ogre3d.org/docs/manual/manual_toc.html#SEC_Contents */

	// this looks much better:
	mSceneMgr->setShadowTechnique(SHADOWTYPE_STENCIL_ADDITIVE);

	/* Modulative shadows are an inaccurate lighting model, since they darken the areas of shadow uniformly, irrespective of the amount of light which would have fallen on the shadow area anyway. */
	/* modulative shadows are much to "hard"...
	mSceneMgr->setShadowTechnique(SHADOWTYPE_STENCIL_MODULATIVE); */


	// mSceneMgr->setShadowTextureSize( 4048 );
	// mSceneMgr->setShadowColour( ColourValue( 0.0f, 0.0f, 0.0f ) ); //try 0.3f?

	// Setup animation default
	Animation::setDefaultInterpolationMode( Animation::IM_LINEAR );
	Animation::setDefaultRotationInterpolationMode( Animation::RIM_LINEAR );

	// Set ambient light
	//orig    mSceneMgr->setAmbientLight( ColourValue( 0.2f, 0.2f, 0.2f ) ); // was .2
	//mSceneMgr->setAmbientLight( ColourValue::Black );


	//mSceneMgr->setSkyBox( true, "Examples/CloudyNoonSkyBox" );
	//mSceneMgr->setSkyBox( true, "Examples/SceneSkyBox2" );

	// Give it a little ambience with lights

#ifdef DODO
	Light * l;
	Vector3 dir;

	l = mSceneMgr->createLight( "WhiteLight" );
	l->setType( Light::LT_SPOTLIGHT );
	l->setPosition( -150.0f, 450.0f, 200.0f );
	l->setCastShadows( true );
	l->setPowerScale( 1.0 );

	dir = -l->getPosition();
	//dir = Vector3( 15, 50, 0 );
	dir.normalise();
	l->setDirection( dir );
	l->setDiffuseColour( 1.24f, 1.22f, 1.15f );
	l->setSpecularColour(0.8f, 0.8f, 0.9f);

	Light * mR_FillLight;
	mR_FillLight = mSceneMgr->createLight("R_FillLight");
	mR_FillLight->setType(Light::LT_SPOTLIGHT);
	mR_FillLight->setPosition(1500,100,200);
	mR_FillLight->setSpotlightRange(Degree(30), Degree(50));
	dir = -mR_FillLight->getPosition();
	dir.normalise();
	mR_FillLight->setDirection(dir);
	mR_FillLight->setDiffuseColour(0.32f, 0.37f, 0.4f);
	mR_FillLight->setSpecularColour(0.32f, 0.37f, 0.4f);

	Light * mL_FillLight;
	mL_FillLight = mSceneMgr->createLight("L_FillLight");
	mL_FillLight->setType(Light::LT_SPOTLIGHT);
	mL_FillLight->setPosition(-1500.0f,100.0f,-100.0f);
	mL_FillLight->setSpotlightRange(Degree(30.0f), Degree(50.0f));
	dir = -mL_FillLight->getPosition();
	dir.normalise();
	mL_FillLight->setDirection(dir);
	mL_FillLight->setDiffuseColour(0.45f, 0.42f, 0.40f);
	mL_FillLight->setSpecularColour(0.45f, 0.42f, 0.40f);

	Light * mBounceLight;
	mBounceLight = mSceneMgr->createLight("BounceLight");
	mBounceLight->setType(Light::LT_SPOTLIGHT);
	mBounceLight->setPosition(-50.0f,-500.0f,400.0f);
	mBounceLight->setSpotlightRange(Degree(30.0f), Degree(50.0f));
	dir = -mBounceLight->getPosition();
	dir.normalise();
	mBounceLight->setDirection(dir);
	mBounceLight->setDiffuseColour(0.37f, 0.37f, 0.36f);
	mBounceLight->setSpecularColour(0.37f, 0.37f, 0.36f);

	Ogre::Light* directionalLight = mSceneMgr->createLight("directionalLight");
	directionalLight->setType(Ogre::Light::LT_DIRECTIONAL);
	directionalLight->setDiffuseColour(Ogre::ColourValue(.25, .25, 0));
	directionalLight->setSpecularColour(Ogre::ColourValue(.25, .25, 0));

	directionalLight->setDirection(Ogre::Vector3( 0, -1, 1 ));	

#endif

	// Position the camera
	mCamera->setPosition( 0, 140, 225 );
	mCamera->lookAt( 0, 92, 0 );

	// Open ActiveMQ
	vhmsg::ttu_set_client_callback( &OgreRenderer::tt_client_callback, this );


	int err = vhmsg::ttu_open();
	if ( err != vhmsg::TTU_SUCCESS ) 
	{
		printf("%s", "ttu_open failed!\n" );
	}

	// Register with ActiveMQ
	vhmsg::ttu_register( "vrAllCall" );
	vhmsg::ttu_register( "vrKillComponent" );
	vhmsg::ttu_register( "vrOgre" ); /* Ulysses */

	// Send vrComponent message to ActiveMQ
	vhmsg::ttu_notify2( "vrComponent", "renderer Ogre" );


	//adding plane entity to the scene
	Plane plane;
	plane.normal = Vector3::UNIT_Y;
	plane.d = 0;
	MeshManager::getSingleton().createPlane( "Myplane", ResourceGroupManager::DEFAULT_RESOURCE_GROUP_NAME, plane, 1500, 1500, 20, 20, true, 1, 60, 60, Vector3::UNIT_Z );
	Entity * pPlaneEnt = mSceneMgr->createEntity( "plane", "Myplane" );
	//pPlaneEnt->setMaterialName( "Examples/Rockwall" );
	pPlaneEnt->setMaterialName( "Rockwall" );
	pPlaneEnt->setCastShadows( false );
	mSceneMgr->getRootSceneNode()->createChildSceneNode("plane_node", Vector3( 0, 0, 0 ) )->attachObject( pPlaneEnt );
	mSceneMgr->getSceneNode("plane_node")->setVisible(false);

	/*adding diagnostic scene to measure in feet
	sceneNode = mSceneMgr->getRootSceneNode()->createChildSceneNode("world_scene_ft");
	sceneEntity = mSceneMgr->createEntity("world_entity_ft","Diagnostic_Level(ft).mesh");
	sceneNode->attachObject(sceneEntity);
	sceneNode->setVisible(false); */


	/*adding diagnostic scene to measure in cm
	sceneNode = mSceneMgr->getRootSceneNode()->createChildSceneNode("world_scene_cm");
	sceneEntity = mSceneMgr->createEntity("world_entity_cm","Diagnostic_Level(meter_in_cm).mesh");
	sceneNode->attachObject(sceneEntity);
	sceneNode->setVisible(false); */


	// adding generic scene if specified
	if (meshName != "")	
	{
		sceneNode = mSceneMgr->getRootSceneNode()->createChildSceneNode("world_scene");
		sceneEntity = mSceneMgr->createEntity("world_entity", meshName);
		sceneNode->attachObject(sceneEntity);
		sceneNode->setVisible(true); // if the user specifies a scene to load, make it the default
	} 
	else 
	{
		mSceneMgr->getSceneNode("plane_node")->setVisible(true); // if the user doesn't specify a scene to load, make it the default
	}

	if(m_initialDotSceneName != ""){
		Ogre::SceneNode *node = mSceneMgr->getRootSceneNode()->createChildSceneNode("dot_world_scene");
		DotSceneLoader dsl;
		dsl.parseDotScene(m_initialDotSceneName,"General",mSceneMgr, node);
	}


	for(unsigned int ii=0; ii<m_initialObjects.size(); ii++){
		std::string strObjectMesh = m_initialObjects[ii];
		unsigned pos = strObjectMesh.find(".mesh");
		std::string strObjectID = strObjectMesh.substr(0, (pos));
		//std::cout << "##### strObjectMesh: " << strObjectMesh << std::endl;
		//std::cout << "##### strObjectID: " << strObjectID << std::endl;
		sceneEntity = mSceneMgr->createEntity(strObjectID.c_str(),strObjectMesh.c_str());

		stringstream ss;
		ss << strObjectID << "Node";
		Ogre::SceneNode *node = mSceneMgr->getRootSceneNode()->createChildSceneNode(ss.str().c_str());
		node->attachObject(sceneEntity);
	}


	/*  this can now be done with the Objects= in config.ini
	createBox("TBox00", 200, 110, 200, Degree(-90));
	createBox("TBox01", -200, 110, -200, Degree(90));
	createBox("TBox02", -200, 110, 200, Degree(90));
	createBox("TBox03", 200, 110, -200, Degree(-90));
	*/
}




void OgreRenderer::createBox(std::string strID, Real x, Real y, Real z, Degree d){
	sceneEntity = mSceneMgr->createEntity(strID.c_str(),"TBox.mesh");
	stringstream ss;
	ss << strID << "Node";
	Ogre::SceneNode *node = mSceneMgr->getRootSceneNode()->createChildSceneNode(ss.str().c_str());
	node->attachObject(sceneEntity);
	//--    node->setScale(.7f, .7f, .7f);
	node->setPosition(x, y, z);
	node->yaw(Radian(Degree(d)));
}


void OgreRenderer::createBillBoard(SceneNode* mSceneNode){
	std::cout << "OgreRenderer::createBillBoard(SceneNode* mSceneNode)" << std::endl;

	stringstream ss;
	ss << "txt" << mSceneNode->getName(); 
	Ogre::MovableText* mtMsg = new Ogre::MovableText(ss.str().c_str(), "CAPTION");
	mtMsg->setTextAlignment(Ogre::MovableText::H_CENTER, Ogre::MovableText::V_ABOVE); // Center horizontally and display above the node
	mtMsg->setCharacterHeight(4);
	mtMsg->setLocalTranslation( Vector3(0, 80, 30));
	//    mtMsg->setColor(ColourValue(.5f,.5f,.5f,0f));
	mtMsg->setVisible(false);
	mSceneNode->attachObject(mtMsg);  

	/* Ulysses: use a billboard to display information 
	this will not (!!!!!!) display text */


#ifdef SHOW_SPRITE
	stringstream ss1;
	ss1 << "bb" << mSceneNode->getName(); 
	BillboardSet* mySet = mSceneMgr->createBillboardSet(ss1.str().c_str() );

	Billboard* myBillboard = mySet->createBillboard(Vector3(-10, 110, 0));
	myBillboard->setDimensions (10, 10);
	myBillboard->setColour (ColourValue(1,0,0,0));

	Billboard* myBillboard01 = mySet->createBillboard(Vector3(0, 110, 0));
	myBillboard01->setDimensions (10, 10);
	myBillboard01->setColour (ColourValue(0,1,0,0));

	Billboard* myBillboard02 = mySet->createBillboard(Vector3(10, 110, 0));
	myBillboard02->setDimensions (10, 10);
	myBillboard02->setColour (ColourValue(0,0,1,0));


	mSceneNode->attachObject(mySet);
#endif

	/* --------------------- */
}



// Just override the mandatory create scene method
void OgreRenderer::createScene() 
{

	createDefaultScene(m_initialMeshName);

	if (m_useBoneBus) 
	{
		m_bonebus = new bonebus::BoneBusServer();

		m_bonebus->SetOnClientConnectCallback( BoneBusHandler::OnClientConnect, this );
		m_bonebus->SetOnCreateCharacterFunc( BoneBusHandler::OnCreateCharacter, this );
		m_bonebus->SetOnDeleteCharacterFunc( BoneBusHandler::OnDeleteCharacter, this );
		m_bonebus->SetOnUpdateCharacterFunc( BoneBusHandler::OnUpdateCharacter, this );
		m_bonebus->SetOnSetCharacterPositionFunc( BoneBusHandler::OnSetCharacterPosition, this );
		m_bonebus->SetOnSetCharacterRotationFunc( BoneBusHandler::OnSetCharacterRotation, this );
		m_bonebus->SetOnBoneRotationsFunc( BoneBusHandler::OnBoneRotations, this );
		m_bonebus->SetOnBonePositionsFunc( BoneBusHandler::OnBonePositions, this );
		m_bonebus->SetOnBoneIdFunc( BoneBusHandler::OnBoneId, this );
		m_bonebus->SetOnVisemeIdFunc( BoneBusHandler::OnVisemeId, this );
		m_bonebus->SetOnExecScriptFunc(BoneBusHandler::OnExecScriptFunc, this); //UB

		m_bonebus->OpenConnection();

		// ask SmartBody to connect to this server if it hasn't already done so
		vhmsg::ttu_notify2("sbm", "net_check");
	} 
	else 
	{
		m_sbListener = new SBListener(this);
		m_sbm = SBM_CreateSBM();
		SBM_Init(m_sbm, "../../../Python27/Lib", true); // was ../../../Python26/Lib
		SBM_SBVHMsgManager_SetEnable(m_sbm, true);

	}

	vhmsg::ttu_notify2( "vrComponent", "renderer all" );

	// sbm related vhmsgs
	vhmsg::ttu_register( "sb" );
	vhmsg::ttu_register( "sbm" );
	vhmsg::ttu_register( "vrAllCall" );
	vhmsg::ttu_register( "vrKillComponent" );
	vhmsg::ttu_register( "vrAgentBML" );
	vhmsg::ttu_register( "vrSpeak" );
	vhmsg::ttu_register( "vrExpress" );
	vhmsg::ttu_register( "vrPerception" );
	vhmsg::ttu_register( "vrBCFeedback" );
	vhmsg::ttu_register( "vrSpeech" );
	vhmsg::ttu_register( "vrSpoke" );
	vhmsg::ttu_register( "RemoteSpeechReply" );
	vhmsg::ttu_register( "PlaySound" );
	vhmsg::ttu_register( "StopSound" );
	vhmsg::ttu_register( "CommAPI" );
	vhmsg::ttu_register( "object-data" );
	vhmsg::ttu_register( "wsp" );
	vhmsg::ttu_register( "sbmdebugger" );
}


// Create new frame listener
void OgreRenderer::createFrameListener() 
{
	mFrameListener = new OgreFrameListener( mWindow, mCamera, mDebugText, mSceneMgr, m_bonebus, m_sbm, m_sbListener, m_initialCommands);
	mRoot->addFrameListener( mFrameListener );
}




void OgreRenderer::tt_client_callback( const char * op, const char * args, void * user_data ) 
{
	OgreRenderer * app = (OgreRenderer *)user_data;

	//NILOG( "ActiveMQ message received: '%s %s'\n", op, args );
	// printf( "OgreRenderer::tt_client_callback(op: %s, args: %s, void * user_data )\n", op, args );

	std::string sOp = op;
	std::string sArgs = args;
	std::vector< std::string > splitArgs;
	vhcl::Tokenize( sArgs, splitArgs );

	if ( sOp == "vrAllCall" ) 
	{
		vhmsg::ttu_notify2( "vrComponent", "renderer Ogre" );
	}
	else if ( sOp == "vrKillComponent" ) 
	{
		if ( splitArgs.size() > 0 ) 
		{
			if ( splitArgs[ 0 ] == "renderer" || 
				splitArgs[ 0 ] == "all" ) 
			{
				((OgreFrameListener*)app->mFrameListener)->scheduleQuit();
			}
		}
	} 
	else if ( sOp == "vrOgre" ) 
	{
		printf("recived vrOgre command\n");
		stringstream ss(args);
		std::string strObject;
		std::string strCommand;
		std::string strArgs;

		ss >> strObject >> strCommand;

		/* we want the arguments to "stay together" */
		getline(ss, strArgs); 

		if ( splitArgs.size() > 0 ) {

			printf("strObject %s, strCommand: %s, strArgs: %s\n", strObject.c_str(), strCommand.c_str(), strArgs.c_str());

			if(!strObject.compare("camera")){
				printf("OBJECT camera\n");
				OgreFrameListener *OFL = (OgreFrameListener*)app->mFrameListener; /* this is basically a pointer to this... */
				Camera* cam = OFL->getCamera();

				if(!strCommand.compare("setPosition")){
					Ogre::Vector3 v3Pos = Ogre::StringConverter::parseVector3(strArgs);
					cam->setPosition( v3Pos );
				} else if(!strCommand.compare("lookAt")){
					Ogre::Vector3 v3Pos = Ogre::StringConverter::parseVector3(strArgs);
					cam->lookAt( v3Pos );
				} else if(!strCommand.compare("setOrientation")){
					Ogre::Quaternion qtOri = Ogre::StringConverter::parseQuaternion(strArgs);
					cam->setOrientation( qtOri );
				} else if(!strCommand.compare("autoTrack")){
					std::string strID;
					bool bOn;
					stringstream ss1(strArgs);
					ss1 >> strID >> bOn;
					printf("set autoTrack for %s to %s\n", strID.c_str(), ( bOn ? "yes" : "no"));
					if(app->getSceneManager()->hasEntity(strID.c_str())){
						SceneNode * node = (SceneNode *)app->getSceneManager()->getRootSceneNode()->getChild( strID.c_str() );
						cam->setAutoTracking(bOn, node /*,const Vector3 & offset = Vector3::ZERO */);
					} else {
						printf("error setting autoTrack ID %s not found\n", strID.c_str());
					}
				}
			} else if(!strObject.compare("image")){
				printf("OBJECT image\n");
				if(!strCommand.compare("setMaterial")){
					std::string strID;
					std::string strMaterial;
					stringstream ss1(strArgs);
					ss1 >> strID >> strMaterial;
					printf("setMaterial for %s to %s\n", strID.c_str(), strMaterial.c_str());


					if(app->getSceneManager()->hasEntity(strID.c_str())){
						Ogre::Entity* sceneEntity = (Ogre::Entity*)app->getSceneManager()->getEntity( strID.c_str() );

						sceneEntity->setMaterialName(strMaterial.c_str()); 
						if(sceneEntity->getSubEntity(0)->getTechnique()->getPass(0)->getNumTextureUnitStates()>0){
							sceneEntity->getSubEntity(0)->getTechnique()->getPass(0)->getTextureUnitState(0)->setTextureScale(1, 1);
						}

						/*
						Real x = sceneEntity->getBoundingBox().getSize().x;
						Real y = sceneEntity->getBoundingBox().getSize().y;
						Real z = sceneEntity->getBoundingBox().getSize().z;
						printf("entity dimensions: %f, %f, %f\n", x, y, z);

						std::pair< size_t, size_t > ppp = sceneEntity->getSubEntity(0)->getTechnique()->getPass(0)->getTextureUnitState(0)->getTextureDimensions();
						printf("texture dimensions: %d, %d\n", ppp.first, ppp.second);
						*/
					} else {
						printf("error setting material. ID %s not found\n", strID.c_str());
					}
				} else if(!strCommand.compare("autoTrack")){
					std::string strID;
					std::string strTarget;
					bool bOn;
					stringstream ss1(strArgs);
					ss1 >> strID >> strTarget >> bOn;
					stringstream ss;
					ss << strID << "Node";
					strID = ss.str();

					printf("set autoTrack for %s to %s\n", strID.c_str(), ( bOn ? "yes" : "no"));

					Ogre::SceneNode* snTBoxNode = (SceneNode *)app->getSceneManager()->getRootSceneNode()->getChild( strID.c_str() );
					if(snTBoxNode != NULL){
						SceneNode * snTarget = (SceneNode *)app->getSceneManager()->getRootSceneNode()->getChild( strTarget.c_str() );
						if(snTarget != NULL){
							snTBoxNode->setAutoTracking(bOn, snTarget);
						} else {
							printf("error setting autotrack. Target not found %s\n", strTarget.c_str());
						}
					} else {
						printf("error setting autotrack. ID %s not found\n", strID.c_str());
					}
				} else {
					printf("error: unknown command: %s\n", strCommand.c_str());
				}
			} else if(!strObject.compare("character")){
				if(!strCommand.compare("setText")){
					std::string strID;
					std::string strText;
					stringstream ss1(strArgs);
					ss1 >> strID;
					getline(ss1, strText);  /* get all the remaining text..*/
					std::replace( strText.begin(), strText.end(), '#', '\n');
					printf("setText for %s to %s\n", strID.c_str(), strText.c_str());
					stringstream ss;
					ss << "txt" << strID;
					std::string strIDNode = ss.str();
					Ogre::SceneNode* snCharacter = (SceneNode *)app->getSceneManager()->getRootSceneNode()->getChild( strID.c_str() );
					if(snCharacter != NULL){
						std::cout << "snCharacter != NULL" << std::endl;
						MovableText* mt = (MovableText*)snCharacter->getAttachedObject( strIDNode );
						if(mt!=NULL){
							std::cout << "mt != NULL" << std::endl;
							mt->setCaption(strText);
						}
					} else {
						std::cerr << "error setting text. ID " << strID << " not found" << std::endl;
					}
				}
			}
		}
	}

	if (!app->isUseBoneBus()) 
	{
		SBM_ProcessVHMsgs(app->m_sbm, op, args);
	}

}


SceneManager* OgreRenderer::getSceneManager() 
{
	return mSceneMgr;
}


Camera* OgreRenderer::getCamera() 
{
	return mCamera;
}

OgreFrameListener* OgreRenderer::getOgreFrameListener() 
{
	return dynamic_cast<OgreFrameListener*>(mFrameListener);
}
