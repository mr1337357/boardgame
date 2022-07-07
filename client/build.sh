UNAME=$(uname)

case ${UNAME} in 
  CYGWIN*)
    CSC=/cygdrive/c/Windows/Microsoft.NET/Framework/v3.5/csc.exe ;;
  *)
    echo Unrecognized OS ; exit 1 ;;
esac

cs_files="Boardgame.cs"

for file in $cs_files
do
  $CSC $file
done
