CMAKE_CXX_FLAGS:  /DWIN32 /D_WINDOWS /W3 /Zm1000 /EHsc /GR
CMAKE_C_FLAGS: /DWIN32 /D_WINDOWS /W3 /Zm1000
CMAKE_MAKE_PROGRAM: C:/Windows/Microsoft.NET/Framework/v4.0.30319/MSBuild.exe

CMAKE_CXX_FLAGS_DEBUG: /D_DEBUG /MDd /Zi /Ob0 /Od /RTC1
CMAKE_C_FLAGS_DEBUG: /D_DEBUG /MDd /Zi  /Ob0 /Od /RTC1

To get rid of 
MSVCRTD.lib(crtexe.obj) : error LNK2019: unresolved external symbol _main referenced in function ___tmainCRTStartup

CMAKE_EXE_LINKER_FLAGS: /SUBSYSTEM:WINDOWS

OR

In the properties of the SmartBodyOgreViewer:
Linker->System->SubSystem needs to be "Windows (/SUBSYSTEM:WINDOWS)"





  