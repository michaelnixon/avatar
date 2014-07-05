/*
*  main.cpp - 
*  originally part of SmartBody's OgreViewer
*  Copyright (C) 2009  University of Southern California
*
*  SmartBody is free software: you can redistribute it and/or
*  modify it under the terms of the Lesser GNU General Public License
*  as published by the Free Software Foundation, version 3 of the
*  license.
*
*  SmartBody is distributed in the hope that it will be useful,
*  but WITHOUT ANY WARRANTY; without even the implied warranty of
*  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
*  Lesser GNU General Public License for more details.
*
*  You should have received a copy of the Lesser GNU General Public
*  License along with SmartBody.  If not, see:
*      http://www.gnu.org/licenses/lgpl-3.0.txt
*
*  CONTRIBUTORS:
*     Ed Fast, USC
*     Andrew n marshall, USC
*	   Deepali Mendhekar, USC
*	   Shridhar Ravikumar, USC
*     Arno Hartholt, USC
*	   Ulysses Bernardet, SFU
*/

#include <tchar.h>
#include "vhcl.h"
#include "OgreRenderer.h"
#include <vector>
#include <string>
#include "ini.h"
#include "bonebus.h"

#ifdef WIN32
#include <windows.h>
#include <stdio.h>
#include <fcntl.h>
#include <io.h>
#include <iostream>
#include <fstream>
#endif

#if OGRE_PLATFORM == OGRE_PLATFORM_APPLE
std::string macBundlePath()
{
	char path[1024];
	CFBundleRef mainBundle = CFBundleGetMainBundle();
	assert(mainBundle);

	CFURLRef mainBundleURL = CFBundleCopyBundleURL(mainBundle);
	assert(mainBundleURL);

	CFStringRef cfStringRef = CFURLCopyFileSystemPath( mainBundleURL, kCFURLPOSIXPathStyle);
	assert(cfStringRef);

	CFStringGetCString(cfStringRef, path, 1024, kCFStringEncodingASCII);

	CFRelease(mainBundleURL);
	CFRelease(cfStringRef);

	return std::string(path);
}
#endif

static const WORD MAX_CONSOLE_LINES = 9999;

void RedirectIOToConsole()
{
	int hConHandle;
	long lStdHandle;
	CONSOLE_SCREEN_BUFFER_INFO coninfo;
	FILE *fp;
	// allocate a console for this app
	AllocConsole();
	// set the screen buffer to be big enough to let us scroll text
	GetConsoleScreenBufferInfo(GetStdHandle(STD_OUTPUT_HANDLE), &coninfo);
	coninfo.dwSize.Y = MAX_CONSOLE_LINES;
	coninfo.dwSize.X = coninfo.dwSize.X * 1.5;

	SetConsoleScreenBufferSize(GetStdHandle(STD_OUTPUT_HANDLE), coninfo.dwSize);
	// redirect unbuffered STDOUT to the console
	lStdHandle = (long)GetStdHandle(STD_OUTPUT_HANDLE);
	hConHandle = _open_osfhandle(lStdHandle, _O_TEXT);
	fp = _fdopen( hConHandle, "w" );
	*stdout = *fp;
	setvbuf( stdout, NULL, _IONBF, 0 );
	// redirect unbuffered STDIN to the console
	lStdHandle = (long)GetStdHandle(STD_INPUT_HANDLE);
	hConHandle = _open_osfhandle(lStdHandle, _O_TEXT);
	fp = _fdopen( hConHandle, "r" );
	*stdin = *fp;
	setvbuf( stdin, NULL, _IONBF, 0 );
	// redirect unbuffered STDERR to the console
	lStdHandle = (long)GetStdHandle(STD_ERROR_HANDLE);
	hConHandle = _open_osfhandle(lStdHandle, _O_TEXT);
	fp = _fdopen( hConHandle, "w" );
	*stderr = *fp;
	setvbuf( stderr, NULL, _IONBF, 0 );
	// make cout, wcout, cin, wcin, wcerr, cerr, wclog and clog
	// point to console as well
	std::ios::sync_with_stdio();
}

static int inihandler(void* user, const char* section, const char* name, 
	const char* value) 
{
	OgreRenderer* renderer = (OgreRenderer*) user;

#ifdef WIN32
#define MATCH(s, n) _stricmp(section, s) == 0 && _stricmp(name, n) == 0
#else
#define MATCH(s, n) strcasecmp(section, s) == 0 && strcasecmp(name, n) == 0
#endif
	if (MATCH("GENERAL", "UseBoneBus")) 
	{
		std::string boneBusValue(value);
		if (boneBusValue == "true" || boneBusValue == "True" || boneBusValue == "TRUE") 
		{
			renderer->setUseBoneBus(true);
		} 
		else if (boneBusValue == "false" || boneBusValue == "False" || boneBusValue == "FALSE")
		{
			renderer->setUseBoneBus(false);
		}
	} 
	else if (MATCH("GENERAL", "DefaultPyFile")) 
	{
		std::string temp = "python scene.run(\"" + std::string(value) + "\")";
		renderer->m_initialCommands.push_back(temp);
	} 
	else if (MATCH("GENERAL", "ScriptPath")) 
	{
		std::string temp = "python scene.addAssetPath(\"script\", \"" + std::string(value) + "\")";
		renderer->m_initialCommands.push_back(temp);
	} 
	else if (MATCH("GENERAL", "MediaPath")) 
	{
		std::string temp = "python scene.setMediaPath(\"" + std::string(value) + "\")";
		// make sure that the media path is run first
		renderer->m_initialCommands.insert(renderer->m_initialCommands.begin(), temp);
	} 
	else if (MATCH("GENERAL", "PythonLibPath"))
	{
		std::string temp = "python scene.setMediaPath(\"" + std::string(value) + "\")";
		// make sure that the media path is run first
		renderer->m_initialCommands.insert(renderer->m_initialCommands.begin(), temp);
	}
	else if (MATCH("GENERAL", "Scene")) 
	{
		renderer->m_initialMeshName = std::string(value);
	} 
	else if (MATCH("GENERAL", "DotScene")) 
	{
		renderer->m_initialDotSceneName = std::string(value);
	} 
	else if (MATCH("GENERAL", "Objects")) 
	{
		/* this is an addition by Ulysses that allows to load separate objects into the scene, e.g. to be able to control the texture */
		std::string buf;
		std::stringstream ss(value);
		std::vector<std::string> tokens; // Create vector to hold our words
		while (ss >> buf)
		{
			tokens.push_back(buf);
		}
		renderer->m_initialObjects = tokens;
	} 
	else 
	{
		return 0;  /* unknown section/name, error */
	}
	return 1;
}

//#undef WIN32
#ifdef WIN32
int WINAPI WinMain( HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow )
#else
int main(int argc, char* argv[])
#endif
{

	RedirectIOToConsole();

	// Create application object
	OgreRenderer app;

	app.setUseBoneBus(true);

	// Processing command line arguments, if there are, then use dll mode
#ifdef WIN32
	std::string commandLine = lpCmdLine;
	std::stringstream strstr(commandLine);
#else 
	std::stringstream strstr;
	for (int i = 0; i < argc; i++)
	{ 
		strstr << argv[i] << " ";
	}
#endif

	std::istream_iterator<std::string> it(strstr);
	std::istream_iterator<std::string> end;
	std::vector<std::string> tokenzied(it, end);
	int numTokens = tokenzied.size();
	int tokenCounter = 0;
	// if no parameters are given, look for a file named config.ini in the local path
	bool implicitConfig = false;
	if (numTokens == 0) 
	{
		tokenzied.push_back("-config");
		tokenzied.push_back("config.ini");
		numTokens = 2;
		implicitConfig = true;
	}

	while (tokenCounter < numTokens) 
	{
		std::string op = tokenzied[tokenCounter];
		if (op == "-config") 
		{
			tokenCounter++;
			if (tokenCounter < numTokens) 
			{
				std::vector<std::string> commands;
				if (ini_parse(tokenzied[tokenCounter].c_str(), inihandler, &app) < 0) 
				{
					if (!implicitConfig) 
					{
						std::cerr << "Can't load configuration file " << tokenzied[tokenCounter].c_str() << std::endl;
					}
					continue;
				}
			}
		}

		if (op == "-seqpath" || op == "-scriptpath") 
		{
			tokenCounter++;
			if (tokenCounter < numTokens) 
			{
				std::string command = "python scene.addAssetPath(\"script\", \"" + tokenzied[tokenCounter] + "\")";
				app.m_initialCommands.push_back(command);
				app.setUseBoneBus(false);
			}
		}
		if (op == "-seq") 
		{
			tokenCounter++;
			if (tokenCounter < numTokens) 
			{
				std::string command = "seq " + tokenzied[tokenCounter];
				std::cout << "-------------- command = " << command.c_str() << std::endl;
				app.m_initialCommands.push_back(command);
			}
		}
		if (op == "-script") 
		{
			tokenCounter++;
			if (tokenCounter < numTokens) 
			{
				std::string command = "python scene.run(\"" + tokenzied[tokenCounter] + "\")";
				app.m_initialCommands.push_back(command);		
				app.setUseBoneBus(false);
			}
		}
		if (op == "-mediapath") 
		{
			tokenCounter++;
			if (tokenCounter < numTokens) 
			{
				std::string command = "python scene.setMediaPath(\"" + tokenzied[tokenCounter] + "\")";
				app.m_initialCommands.push_back(command);
				app.setUseBoneBus(false);
			}
		}
		if (op == "-scene") 
		{
			tokenCounter++;
			if (tokenCounter < numTokens) 
			{
				app.m_initialMeshName = tokenzied[tokenCounter];
			}
		}
		if (op.size() > 11 && op.substr(0,11)  == "-mediapath=") 
		{
			tokenCounter++;
			std::string mediaPath = op.substr(11);
			if (tokenCounter < numTokens) 
			{
				std::string command = "python scene.setMediaPath(\"" + mediaPath + "\")";
				app.m_initialCommands.push_back(command);
			}
		}
		if (op == "-help") 
		{
			std::cout << "Usage: OgreViewer [-config filename] [-scriptpath scriptpathname] [-script scriptname] [-mediapath mediapathname] [-scene startupmeshname]" << std::endl;
			std::cout << "If the OgreViewer is not passed any parameters, it will look for a configuration file called 'config.ini' in the current direction." << std::endl;
			std::cout << "If the OgreViewer is not passed any startup scripts or cannot find a config.ini, it will start in BoneBus mode and attempt to connect to SmartBody process." << std::endl;
			std::cout << "If no SmartBody process is available, the OgreViewer will wait and render SmartBody characters after such a process is started." << std::endl;
			std::cout << "" << std::endl;
			std::cout << "The following is a sample configuration script:" << std::endl;
			std::cout << "" << std::endl;
			std::cout << "[GENERAL]" << std::endl;
			std::cout << "UseBoneBus=false" << std::endl;
			std::cout << "ScriptPath=sbm-common/scripts" << std::endl;
			std::cout << "[DefaultPyFile=default-init.py" << std::endl;
			std::cout << "[MediaPath=../../../.." << std::endl;
			std::cout << "[PythonLibPath=." << std::endl;
			std::cout << "[Scene=vh_basic_level.mesh" << std::endl;
			std::string str; 
			std::cin >> str;

			return 0;
		}
		tokenCounter++;
	}


	if (app.m_initialCommands.size() > 0) 
	{
		if (app.isUseBoneBus()) 
		{
			std::cout << "OgreViewer is running in BoneBus mode." << std::endl;
			app.m_initialCommands.clear();
		}
	}

	if (app.m_initialCommands.size() > 0)
	{
		app.setUseBoneBus(false);
	}

	try 
	{
		app.go();
	}
	catch ( Exception & e ) 
	{
#ifdef WIN32
		MessageBox( NULL, e.getFullDescription().c_str(), "An exception has occured!", MB_OK | MB_ICONERROR | MB_TASKMODAL);
#else
		std::cout << "An exception has occured: " << e.getFullDescription().c_str() << std::endl;
#endif
	}

	return 0;
}
