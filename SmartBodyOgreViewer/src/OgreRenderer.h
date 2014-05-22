#ifndef _OGRERENDERER_
#define _OGRERENDERER_

#include "vhcl.h"
#include "bonebus.h"
#include "vhmsg-tt.h"

#include <string>
#include <map>

#include <Ogre.h>
#include "ExampleApplication.h"
#include "SBListener.h"
#include "OgreFrameListener.h"
#include "MovableText.h"

namespace vhcl { class Audio; }


class OgreRenderer : public ExampleApplication, public SmartbodyListener
{

public:
    OgreRenderer();

    void setUseBoneBus(bool val);
    bool isUseBoneBus();

    SceneManager* getSceneManager();
    Camera* getCamera();
    OgreFrameListener* getOgreFrameListener();

    std::map<int,std::map<std::string, Ogre::Vector3> > characterInitBonePosMap;
    std::map<std::string, std::vector<int>*> m_lastPosTimes;
    std::map<std::string, std::vector<int>*> m_lastRotTimes;
    std::map<std::string, std::vector<std::string> > m_skeletonMap;
    std::map<std::string, std::vector<std::string> > m_visemeMap;
                
    std::set<std::string> m_validJointNames;
    std::vector<std::string> m_initialCommands;
    std::string m_initialMeshName;
    std::string m_initialDotSceneName;
    std::vector<std::string> m_initialObjects;

protected:
    // ExampleApplication callbacks
    void destroyScene(void);
    void createDefaultScene(std::string meshName);
    void createScene();
    void createFrameListener();

    static void tt_client_callback( const char * op, const char * args, void * user_data );
    void createBox(std::string strID, Real x, Real y, Real z, Degree d);

protected:
    Ogre::SceneNode * sceneNode;
    Ogre::Entity * sceneEntity;

    Smartbody_dll* m_sbm;
    bonebus::BoneBusServer* m_bonebus;
    SBListener* m_sbListener;
    bool m_useBoneBus;
    std::string mDebugText;
public:                
    void createBillBoard(SceneNode* mSceneNode);

};

#endif
