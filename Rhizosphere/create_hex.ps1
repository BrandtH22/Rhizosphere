$envPath = $args[0]
$filePath = $args[1]
$inputa = $args[2]
$inputb = $args[3]
$prefix = $args[4]

$path = Split-Path -Path $filePath ;
$fileName = Split-Path -leaf $filePath ;
$hexPath = "$filePath.hex" ;
$curry = "" ;
$hex = "" ;
Write-Host "*********************Processing Has Begun*********************"
Write-Host "CLSP File: $path" ;
Write-Host "Hex File: $filePath";
Write-Host "envPath: $envPath";

Remove-Item "$hexPath.backup" ;
Copy-Item $hexPath -Destination "$hexPath.backup" ;
Remove-Item $hexPath;

cd $envPath ;
.\Scripts\activate ;
cd $path ;
$hex = cdv clsp build $fileName ;

$curry = cdv clsp curry $fileName $inputa $inputb ;

$treehash = cdv clsp curry $fileName $inputa $inputb --treehash;

$encode = cdv encode $treehash --prefix $prefix ;

Remove-Item "$filePath.results.txt" ;
New-Item "$filePath.results.txt" ;
$hexRes = Get-Content -Path "$fileName.hex" ;
$results = @($hexRes, $curry, $treehash, $encode) ;
Set-Content "$filePath.results.txt" $results ;

Sleep 1
