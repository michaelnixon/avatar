REM copying the config files
copy configs\* bin\Release

REM copying the necessary libraries
copy /Y C:\src\smartbody\core\smartbody\SmartBody\lib\SmartBody.dll bin\Release
copy /Y C:\src\smartbody\lib\activemq\activemq-cpp\vs2015-build\Win32\ReleaseDLL\activemq-cpp.dll  bin\Release
copy /Y C:\src\smartbody\lib\pthreads\lib\pthreadVSE2.dll bin\Release
copy /Y C:\src\smartbody\lib\vhcl\openal\libs\Win32\alut.dll bin\Release
copy /Y "C:\src\smartbody\core\smartbody\SmartBody\src\external\glew\glew32.dll" bin\Release
copy /Y "C:\src\smartbody\lib\xerces-c\bin\xerces-c_3_1.dll" bin\Release
copy /Y "C:\src\smartbody\lib\vhcl\openal\libs\Win32\OpenAL32.dll" bin\Release
copy /Y "C:\src\smartbody\lib\activemq\apr\apr-iconv\lib\libapriconv-1.dll"  bin\Release
copy /Y "C:\src\smartbody\lib\activemq\apr\apr-util\lib\libaprutil-1.dll" bin\Release
copy /Y "C:\src\smartbody\lib\activemq\apr\apr\lib\libapr-1.dll"  bin\Release
copy /Y "C:\src\smartbody\lib\vhcl\libsndfile\bin\libsndfile-1.dll" bin\Release
copy /Y "C:\src\smartbody\core\smartbody\steersuite-1.3\build\win32\Release\steerlib.dll" bin\Release


copy /Y C:\lib\boost_1_60_0\lib32-msvc-14.0\boost_thread-vc140-mt-1_60.dll bin\Release
copy /Y C:\lib\boost_1_60_0\lib32-msvc-14.0\boost_system-vc140-mt-1_60.dll bin\Release
copy /Y C:\lib\boost_1_60_0\lib32-msvc-14.0\boost_date_time-vc140-mt-1_60.dll bin\Release
copy /Y C:\lib\boost_1_60_0\lib32-msvc-14.0\boost_chrono-vc140-mt-1_60.dll bin\Release
copy /Y C:\lib\boost_1_60_0\lib32-msvc-14.0\boost_filesystem-vc140-mt-1_60.dll bin\Release
copy /Y C:\lib\boost_1_60_0\lib32-msvc-14.0\boost_python-vc140-mt-1_60.dll bin\Release


SET OGRE_DIR=C:\src\OgreSDK_vc10_v1-8-1\bin\release
SET OGRE_DIR=C:\src\OgreSDK_vc11_v1-9-0\bin\release
SET OGRE_DIR=C:\lib\OgreSDK_vc14_v1-9-0\bin\release
copy /Y %OGRE_DIR%\OgreMain.dll bin\Release
copy /Y %OGRE_DIR%\OgreOverlay.dll  bin\Release
copy /Y %OGRE_DIR%\OIS.dll bin\Release
copy /Y %OGRE_DIR%\RenderSystem_GL.dll bin\Release
copy /Y %OGRE_DIR%\RenderSystem_Direct3D11.dll bin\Release
copy /Y %OGRE_DIR%\Plugin_ParticleFX.dll bin\Release
copy /Y %OGRE_DIR%\Plugin_BSPSceneManager.dll bin\Release
copy /Y %OGRE_DIR%\Plugin_CgProgramManager.dll bin\Release
copy /Y %OGRE_DIR%\Plugin_PCZSceneManager.dll bin\Release
copy /Y %OGRE_DIR%\Plugin_OctreeZone.dll bin\Release
copy /Y %OGRE_DIR%\Plugin_OctreeSceneManager.dll bin\Release


SET OGRE_DIR=C:\lib\OgreSDK_vc14_v1-9-0_reldbi\bin\RelWithDebInfo
copy /Y %OGRE_DIR%\OgreMain.dll bin\RelWithDebInfo
copy /Y %OGRE_DIR%\OgreOverlay.dll  bin\RelWithDebInfo
copy /Y %OGRE_DIR%\OIS.dll bin\RelWithDebInfo
copy /Y %OGRE_DIR%\RenderSystem_GL.dll bin\RelWithDebInfo
copy /Y %OGRE_DIR%\RenderSystem_Direct3D11.dll bin\RelWithDebInfo
copy /Y %OGRE_DIR%\Plugin_ParticleFX.dll bin\RelWithDebInfo
copy /Y %OGRE_DIR%\Plugin_BSPSceneManager.dll bin\RelWithDebInfo
copy /Y %OGRE_DIR%\Plugin_CgProgramManager.dll bin\RelWithDebInfo
copy /Y %OGRE_DIR%\Plugin_PCZSceneManager.dll bin\RelWithDebInfo
copy /Y %OGRE_DIR%\Plugin_OctreeZone.dll bin\RelWithDebInfo
copy /Y %OGRE_DIR%\Plugin_OctreeSceneManager.dll bin\RelWithDebInfo


