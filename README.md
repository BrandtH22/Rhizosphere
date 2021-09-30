![Rhizosphere logo](https://user-images.githubusercontent.com/48610606/135378714-0037a053-af4f-48ce-ad3b-50c7f8ca2cc1.png)

 <h1>Rhizosphere Project How-To</h1>

 --note this project and its creator have no connections with the Chia Network team.
 --note this is an ALPHA version 2 of the IDE and HAS NOT BEEN THOROUGHLY TESTED, therefore we cannot guarantee the validity of any results at this time


<h2>Getting Started</h2>

> - Download the Rhizosphere.vxx.py and create_hex.ps1 files.
> - Add these files to any locale directory.
> - Run Rhizosphere.vxx.py

<h2>Using the GUI</h2>

> - Use the File menu (top left) to set default files and open/save CLSP filetypes
> - The default PS File is the create_hex.ps1 file downloaded with this project
> - The default virtual environment is the venv folder directory, review pre-requisites at the bottom of this document for more information
> - Use the 'Develop' tab for CLSP syntax highlighting while creating or editing a CLSP file
> - Use the 'Serialize' tab for processing CLSP files into their respective hex, curried, treehash, and wallet results
> - Click the begin button to initiate processing (note the button text will revert back to "Click to Begin" once processing is complete, the underlying CLI will have more processing information)
> - Wait for the results to appear (takes less than 30 seconds)
> - Use the result buttons to copy the noted result (ex. clicking on "Hex Result:" button copies the hex result to clipboard)
> - The 'Deploy' is under development and will be released in vA03 of the IDE

 (NOTE - processing will take less than 1 minute but during this time it may appear as though the GUI is frozen, it is not just please be patient. Future updates will include more processing identifies, for the time being monitor the supporting CLI for status or wait for the button to revert back to stating "Click to Begin". Also note that the created hex and txt files will overwrite any files with the same names.)



 <h2>Inputs</h2>

> Powershell File: this file is included in the project and runs the clsp commands

> Virtual Environment: Select the "venv" folder directory. If you do not have a virtual environment setup pleasse review the ChiaLisp development pre-requisites at the bottom of this document.

> ChiaLisp File: Select the ChiaLisp file to be processed. This is a file that you would have ceated using the noted development steps within the pre-requisites overview at the bottom of this document.

> Arguments to Curry (arg1 and arg2): This project currently supports two variables to be curried into the hex file. Leave the field as default or delete all contents within to process without arguments. (NOTE: arguments must be in the format '-a xxx' ex. '-a 500' could be an argument currying the value of 500. Invalid arguments will fail leading to only a hex creation.) NOTE: currently testing automated arguments listed based on clsp file, there is a known bug that requires a comment must be made between the first parenthesis and first solution/argument to be curried. In addition, the serialize listing will only identify solutions written in all-caps.

> Wallet Prefix: This project supports both txch and xch prefixes. The sunken/grayed out item is the selected prefix (supporting command line will display toggle results for verification).

 <h2>Outputs</h2>

This project takes a clsp file (which can be viewed and edited in tab1) and processes it into all necessary files/data for use on the blockchain. Items that do not have their own file types are stored in .txt files. All files will be created in the ChiaLisp files directory and will overwrite any identically named documents. Below are all current outputs:

> - CLSP file
> - Hex result
> - Curry result
> - TreeHash result
> - Wallet result
> - Results file path


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


Donations are always appreciated!:

xch1we8herlmv4rapnkfkk89n60l0w98tt73u08mg7j23z0z8t0dy6tsn6k35w
