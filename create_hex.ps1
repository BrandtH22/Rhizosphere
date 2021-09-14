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
Write-Host "Path: $path" ;
Write-Host "Hex: $hexPath";

Remove-Item "$hexPath.backup" ;
Copy-Item $hexPath -Destination "$hexPath.backup" ;
Remove-Item $hexPath;

cd $envPath ;
.\Scripts\activate ;
cd $path ;
$hex = cdv clsp build $fileName ;

$curry = cdv clsp curry $fileName $inputa $inputb ;
Remove-Item "$filePath.curry.txt" ;
New-Item "$filePath.curry.txt" ;
Set-Content "$filePath.curry.txt" $curry ;

$treehash = cdv clsp curry $fileName $inputa $inputb --treehash;
Remove-Item "$filePath.treehash.txt" ;
New-Item "$filePath.treehash.txt" ;
Set-Content "$filePath.treehash.txt" $treehash ;

$encode = cdv encode $treehash --prefix $prefix ;
Remove-Item "$filePath.wallet.txt" ;
New-Item "$filePath.wallet.txt" ;
Set-Content "$filePath.wallet.txt" $encode ;

Sleep 1
