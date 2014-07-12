cmake_minimum_required(VERSION 2.6)

set(SMARTBODY_HOME C:/src/smartbody)
#set(OGRE_HOME C:/src/OgreSDK_vc10_v1-8-1)
set(OGRE_HOME C:/src/smartbody/lib/OgreSDK)


set(TINYXML_HOME C:/src/tinyxml_2_6_2/tinyxml)

include_directories( ${SMARTBODY_HOME}/core/smartbody/SmartBody/src/sb )
include_directories( ${SMARTBODY_HOME}/core/smartbody/SmartBody/src )
include_directories( ${SMARTBODY_HOME}/lib/bonebus/include )
include_directories( ${OGRE_HOME}/include )
include_directories( ${OGRE_HOME}/include/OGRE )
include_directories( ${SMARTBODY_HOME}/lib/vhcl/include )
include_directories( ${SMARTBODY_HOME}/lib/vhmsg/vhmsg-c/include )
include_directories( ${SMARTBODY_HOME}/lib/boost )
include_directories( ${TINYXML_HOME} )

if(MSVC)
  SET(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} /DNDEGUG")

  SET(SMARTBODY_LIB ${SMARTBODY_HOME}/core/smartbody/SmartBody/lib/SmartBody.lib)
  SET(VHCL_LIB ${SMARTBODY_HOME}/lib/vhcl/lib/vhcl.lib)
  SET(VHMSG_LIB ${SMARTBODY_HOME}/lib/vhmsg/vhmsg-c/lib/vhmsg.lib)
  SET(PTHREAD_LIB ${SMARTBODY_HOME}/lib/pthreads/lib/pthreadVSE2.lib)
  SET(ACTIVEMQ-CPP_LIB ${SMARTBODY_HOME}/lib/activemq/activemq-cpp/vs2010-build/ReleaseDLL/activemq-cpp.lib)


  SET(ALUT_LIB ${SMARTBODY_HOME}/lib/vhcl/openal/libs/Win32/alut.lib)
  SET(BONEBUS_LIB ${SMARTBODY_HOME}/lib/bonebus/lib/bonebus.lib)


### -> some boost libraries needed by Ogre 1.8 are missing from the SmartBody source tree; hence we need to use the separately compiled libs (sigh) 
 SET(BOOST_LIB 
   C:/src/boost_1_51_0/stage/lib/libboost_thread-vc100-mt-1_51.lib
   C:/src/boost_1_51_0/stage/lib/libboost_system-vc100-mt-1_51.lib
   C:/src/boost_1_51_0/stage/lib/libboost_date_time-vc100-mt-1_51.lib
   C:/src/boost_1_51_0/stage/lib/libboost_chrono-vc100-mt-1_51.lib
  )



  SET(OGREMAIN ${OGRE_HOME}/lib/release/OgreMain.lib)
  SET(OISLIB ${OGRE_HOME}/lib/release/OIS.lib)
  SET(TINYXML_LIB ${TINYXML_HOME}/Releasetinyxml/tinyxml.lib)




			
else(MSVC)
  SET(SMARTBODY_LIB smartbody-dll)
  SET(VHCL_LIB vhcl)
  SET(VHMSG_LIB vhmsg)
  SET(ACTIVEMQ-CPP_LIB activemq-cpp)
  SET(ALUT_LIB alut)
#  SET(SNDFILE_LIB sndfile)
  SET(BONEBUS_LIB bonebus)

endif(MSVC)


set (OGRE_LIBS
	${OGREMAIN}
	${OISLIB}
)

set( MORE_LIBS
#  kernel32 
#  user32 
#  gdi32 
#  winspool 
#  shell32 
#  ole32 
#  oleaut32 
#  uuid 
#  comdlg32 
  Ws2_32 
#  winmm
)

#msvcrtxx.lib, 


#  kernel32 user32 gdi32 winspool shell32 ole32 oleaut32 uuid comdlg32 Ws2_32 winmm


add_executable( SmartBodyOgreViewer
	src/ExampleApplication.h
	src/ExampleFrameListener.h
	src/BoneBusHandler.h
	src/BoneBusHandler.cpp
	src/OgreFrameListener.h
	src/OgreFrameListener.cpp
	src/OgreRenderer.h
	src/OgreRenderer.cpp
	src/SBListener.h
	src/SBListener.cpp
	src/main.cpp
	src/ini.h
	src/ini.c
	src/MovableText.h
	src/MovableText.cpp
        src/DotSceneLoader.h
        src/DotSceneLoader.cpp
        src/ObjectTextDisplay.h
)

target_link_libraries( SmartBodyOgreViewer
   ${SMARTBODY_LIB}
   ${VHCL_LIB}
   ${VHMSG_LIB}
   ${ACTIVEMQ-CPP_LIB}
   ${OGRE_LIBS}
   ${BONEBUS_LIB}
   ${PTHREAD_LIB}
   ${ALUT_LIB}
#    ${SNDFILE_LIB}
   ${TINYXML_LIB}
   ${MORE_LIBS}
   ${BOOST_LIB}
)

###set( APP_LIBRARY_SOURCE_PATHS
###    ${PROJECT_SOURCE_DIR}/core/ogre-viewer/bin
###    ${PROJECT_SOURCE_DIR}/core/smartbody/sbm/bin
###)

set_target_properties( SmartBodyOgreViewer
	PROPERTIES
	## link with install tree:
	INSTALL_RPATH                   "${APP_LIBRARY_SOURCE_PATHS}"
	BUILD_WITH_INSTALL_RPATH        TRUE
)

#set_target_properties(SmartBodyOgreViewer PROPERTIES LINK_FLAGS "/ENTRY:\"WinMain\"")

install(
	TARGETS SmartBodyOgreViewer
	RUNTIME DESTINATION bin
)


set(EXECUTABLE_OUTPUT_PATH bin CACHE PATH "Build directory" FORCE)
set(LIBRARY_OUTPUT_PATH bin CACHE PATH "Build directory" FORCE)	
	
