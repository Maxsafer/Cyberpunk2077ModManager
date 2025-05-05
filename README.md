https://www.nexusmods.com/cyberpunk2077/mods/10826

<h1>Files</h1>
<h3>[manager.py]</h3>
This is the script that manages mods installation/uninstallation, it also creates mods.json that keeps track of which mods are
installed and all of their files.

<h3>[start.bat]</h3>
Double click to launch manager.py

<h3>[mods.json]</h3>
This file will be created when the script is launched. Its important to keep this file with manager.py


<h1>Instructions</h1>
<h3>[1st step]</h3>
Drag and drop the script wherever you want, I recommend keeping this script on the game folder or its own folder under the game path.

<h3>[2nd step]</h3>
When launching the script for the first time, a window will prompt asking you to select the game installation path. i.e. D:\Games\GOG\Cyberpunk 2077\

<h3>[3rd step]</h3>
When installing mods, multiple zips can be selected.

<h3>[4th step]</h3>
When uninstalling mods, multiple mods can be uninstalled.


<h1>Dependencies</h1>
<h3>[Python3]</h3>
In order for this small script to work, Python3 must be installed.

<h3>[.zip]</h3>
Mods to be installed must be in a .zip and have the file structure defined i.e.

```
bin
 |-x64
    |-CrashReporter
    |-d3d12on7
    |-plugins
|-cyber_engine_tweaks
|-mods
   |-modToInstall
or
modName
   |-bin
      |-x64
         |-CrashReporter
         |-d3d12on7
         |-plugins
         |-cyber_engine_tweaks
            |-mods
               |-modToInstall
```

Same goes for "archive", "bin", "engine", "mods", "r6", "red4ext" and "tools". 
If a mod comes in a .7z just right click, extract to folder > Then right click the folder and send to zip.
