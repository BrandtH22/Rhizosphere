 <h1>Rhynosphere Project How-To</h1>

 --note this project and its creator have no connections with the Chia Network team.


<h2>Getting Started</h2>
 - Download the Rhynosphere.vxx.py and create_hex.ps1 files.
 - Add these files to any locatable directory.
 - Run Rhynosphere.vxx.py

<h2>Using the GUI</h2>
 - Select the previously downloaded powershell file, the ChiaLisp file to be processed, appropriate prefix, and desired arguments.
 - Click the begin button
 - Wait for the results to appear


 (NOTE - processing will take less than 1 minute but during this time it may appear as though the GUI is frozen, it is not just please be patient. Future updates will include a processing identifier, for the time being monitor the supporting CLI for status. Also note that the created hex and txt files will overwrite any files with the same names.)



 <h2>Inputs</h2>

 Powershell File: this file is included in the project and runs the clsp commands

 Virtual Environment: Select the "venv" folder directory. If you do not have a virtual environment setup pleasse review the ChiaLisp development pre-requisites at the bottom of this document.

 ChiaLisp File: Select the ChiaLisp file to be processed. This is a file that you would have ceated using the noted development steps within the pre-requisites overview at the bottom of this document.

 Arguments to Curry (arg1 and arg2): This project currently supports two variables to be curried into the hex file. Leave the field as default or delete all contents within to process without arguments. (NOTE: arguments must be in the format '-a xxx' ex. '-a 500' could be an argument currying the value of 500. Invalid arguments will fail leading to only a hex creation.)

 Wallet Prefix: This project supports both txch and xch prefixes. The sunken/grayed out item is the selected prefix (supporting command line will display toggle results for verification).

 <h2>Outputs</h2>

 This project takes a clsp file and processes it into all necessary files/data for use on the blockchain. Items that do not have their own file types are stored in .txt files. All files will be created in the ChiaLisp files directory and will overwrite any identically named documents (NOTE- some data may have extraneous brackets that will need to be removed prior to deployment). Below are all current outputs:
 Hex result
 Hex file path
 Curry result
 Curry file path
 TreeHash result
 TreeHash file path
 Wallet result
 Wallet file path


 <h2>ChiaLisp Development Pre-requisites</h2>
 Below is an overview of pre-requisites setup. Additional information can be found on the chialisp main website: https://chialisp.com/
> -	Terminal
> -	Editor
> -	Python
> -	Chia Dev Tools (python wheel)


 <h2>Example Setup (windows)</h2>
> -	PowerShell https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell?view=powershell-7.1
> -	Nano https://atom.io/
> -	Python https://www.python.org/downloads/
> -	Chia Dev Tools:
>   - from powershell create and navigate to directory for projects, create and activate python vitrual env, install dev tools, add basic tests to project folder

     C:\Users\demo\Desktop>	mkdir TestProject
     # (creates directory named "TestProject")
     
     C:\Users\demo\Desktop>	cd .\TestProject\
     # (navigates to newly created directory) 
     
     C:\Users\demo\Desktop\TestProject>	py -m venv venv
     # (creates virtual environment, this also creates the "venv" directory needed for the project)
     
     C:\Users\demo\Desktop\TestProject>	.\venv\Scripts\activate
     # (activates the virtual environment)
     
     C:\Users\demo\Desktop\TestProject>	pip install chia-dev-tools
     # (installs the required chia development tools/commands)
     
     C:\Users\demo\Desktop\TestProject>  cdv test --init
     # (creates basic clsp tests within project folder)

 <h2>Verify Installation via CLI:</h2>(must enter commands from python virtual environment in project folder)
     
     C:\Users\demo\Desktop\TestProject>  chia --help
     #  (validates chia installation, identical to chia full node help)
     
     C:\Users\demo\Desktop\TestProject>  brun --help
     #  (validates clvm tools are installed)
     
     C:\Users\demo\Desktop\TestProject>  cdv --help
     #  (validates development tools are installed)

 <h2>Setup Basic Tests within Project Folder</h2>(must enter commands from python virtual environment in project folder)

     C:\Users\demo\Desktop\TestProject>  cdv test --init
     #  (creates basic tests within project folder)


Donations are always appreicated!:
xch1sg7g930mh676jfl09r4d4622z6wlwyv3u0ezcsxmn8rva9wqx8mqtgc2sf
