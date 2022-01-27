$ErrorActionPreference = "Stop"

if ($null -eq (Get-Command git -ErrorAction SilentlyContinue))
{
    Write-Output "Unable to find git"
    Exit 1
}

if ($null -eq (Get-Command py -ErrorAction SilentlyContinue))
{
    Write-Output "Unable to find py"
    Write-Output "Note the check box during installation of Python to install the Python Launcher for Windows."
    Write-Output ""
    Write-Output "https://docs.python.org/3/using/windows.html#installation-steps"
    Exit 1
}

$pythonVersion = (py --version).split(" ")[1]
if ([version]$pythonVersion -lt [version]"3.7.0")
{
    Write-Output "Found Python version:" $pythonVersion
    Write-Output "Installation requires Python 3.7 or later"
    Exit 1
}
Write-Output "Python version is:" $pythonVersion

py -m venv venv

venv\scripts\pip install TKlighter

Write-Output ""
Write-Output ""
Write-Output "Rhizosphere has successfully installed"
Write-Output ""
Write-Output "Run './venv/Scripts/Activate ; cd Rhizosphere ; py Rhizosphere.py' to load GUI"
Write-Output ""
Write-Output "Post any issues find on Github: https://github.com/BrandtH22/Rhizosphere"
Write-Output ""
Write-Output ""
