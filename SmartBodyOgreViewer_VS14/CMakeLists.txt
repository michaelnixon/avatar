cmake_minimum_required(VERSION 2.6)

set(SMARTBODY_HOME C:/src/smartbody)


include_directories( ${SMARTBODY_HOME}/core/smartbody/SmartBody/src/sb )
include_directories( ${SMARTBODY_HOME}/core/smartbody/SmartBody/src )
include_directories( ${SMARTBODY_HOME}/lib/bonebus/include )
include_directories( ${SMARTBODY_HOME}/lib/vhcl/include )
include_directories( ${SMARTBODY_HOME}/lib/vhmsg/vhmsg-c/include )
#include_directories( ${SMARTBODY_HOME}/lib/boost )


#set(OGRE_HOME C:/src/smartbody/lib/OgreSDK)
#set(OGRE_HOME C:/src/OgreSDK_vc10_v1-8-1)
set(OGRE_HOME C:/src/OgreSDK_vc11_v1-9-0)
set(OGRE_HOME C:/lib/OgreSDK_vc14_v1-9-0)
#set(OGRE_HOME C:/lib/OgreSDK_vc14_v1-9-0_reldbi)

include_directories( ${OGRE_HOME}/include )
include_directories( ${OGRE_HOME}/include/OGRE )

link_directories(${OGRE_HOME}/lib/release)
#link_directories(${OGRE_HOME}/lib/RelWithDebInfo)

set (OGRE_LIBS
   OgreMain.lib
   OgreOverlay.lib
   OIS.lib
)


include_directories( C:/lib/boost_1_60_0 )
#include_directories( C:/lib/boost_1_60_0/lib32-msvc-14.0)

set(TINYXML_HOME C:/src/tinyxml_2_6_2/tinyxml)
include_directories( ${TINYXML_HOME} )

if(MSVC)
  SET(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} /DNDEGUG")
  SET(CMAKE_CXX_FLAGS " /DWIN32 /D_WINDOWS /W3 /Zm1000 /EHsc /GR")
  SET(CMAKE_CXX_FLAGS_DEBUG "/D_DEBUG /MDd /Zi  /Ob0 /Od /RTC1")
  SET(CMAKE_CXX_FLAGS_MINSIZEREL "/MD /O1 /Ob1 /D NDEBUG")
  SET(CMAKE_CXX_FLAGS_RELEASE "/MD /O2 /Ob2 /D NDEBUG")
  SET(CMAKE_CXX_FLAGS_RELWITHDEBINFO "/MD /Zi /O2 /Ob1 /D NDEBUG")
  SET(CMAKE_C_FLAGS "/DWIN32 /D_WINDOWS /W3 /Zm1000")
  SET(CMAKE_C_FLAGS_DEBUG "/D_DEBUG /MDd /Zi  /Ob0 /Od /RTC1")


  SET(SMARTBODY_LIB ${SMARTBODY_HOME}/core/smartbody/SmartBody/lib/SmartBody.lib)
  SET(VHCL_LIB ${SMARTBODY_HOME}/lib/vhcl/lib/vhcl.lib)
  SET(VHMSG_LIB ${SMARTBODY_HOME}/lib/vhmsg/vhmsg-c/Release/vhmsg.lib)
  SET(PTHREAD_LIB ${SMARTBODY_HOME}/lib/pthreads/lib/pthreadVSE2.lib)
  SET(ACTIVEMQ-CPP_LIB ${SMARTBODY_HOME}/lib/activemq/activemq-cpp/vs2015-build/Win32/ReleaseDLL/activemq-cpp.lib)


  SET(ALUT_LIB ${SMARTBODY_HOME}/lib/vhcl/openal/libs/Win32/alut.lib)
#  SET(BONEBUS_LIB ${SMARTBODY_HOME}/lib/bonebus/lib/bonebus.lib)
  SET(BONEBUS_LIB ${SMARTBODY_HOME}/lib/bonebus/Release/bonebus.lib)


SET(Boost_LIBRARY_DIRS C:/lib/boost_1_60_0/lib32-msvc-14.0)

link_directories(${Boost_LIBRARY_DIRS})

  SET(TINYXML_LIB ${TINYXML_HOME}/Releasetinyxml/tinyxml.lib)

			
else(MSVC)
  SET(SMARTBODY_LIB smartbody-dll)
  SET(VHCL_LIB vhcl)
  SET(VHMSG_LIB vhmsg)
  SET(ACTIVEMQ-CPP_LIB activemq-cpp)
  SET(ALUT_LIB alut)
  SET(BONEBUS_LIB bonebus)
endif(MSVC)


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
  dbghelp 
  Ws2_32 
#  winmm
)


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
   ${TINYXML_LIB}
   ${MORE_LIBS}
   ${BOOST_LIB}
)


set_target_properties( SmartBodyOgreViewer
	PROPERTIES
	## link with install tree:
	INSTALL_RPATH                   "${APP_LIBRARY_SOURCE_PATHS}"
	BUILD_WITH_INSTALL_RPATH        TRUE
)

SET(CMAKE_EXE_LINKER_FLAGS "/SUBSYSTEM:WINDOWS")

#set_target_properties(SmartBodyOgreViewer PROPERTIES LINK_FLAGS "/ENTRY:\"WinMain\"")

install(
	TARGETS SmartBodyOgreViewer
	RUNTIME DESTINATION bin
)


set(EXECUTABLE_OUTPUT_PATH bin CACHE PATH "Build directory" FORCE)
set(LIBRARY_OUTPUT_PATH bin CACHE PATH "Build directory" FORCE)	
	
