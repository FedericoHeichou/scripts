#!/bin/bash
if [[ -z "$1" ]] || [[ -z "$2" ]] || [[ -z "$3" ]] || [[ -z "$4" ]]; then
    echo "Inserisci il numero di partenza, prefisso, formato di output, category e subdirectory"
    echo "./rename.sh 600 00 jpg weeabframebot"
    echo "./rename.sh 600 00 jpg tfwnoqtasiangf Jisoo"
    exit 0
fi

nome=$1
pre="$2"
f="$3"
cat="$4"
if [[ -z "$5" ]]; then
    $sub=""
else  
    sub="$5/"
fi

if [ ! -d "file" ]; then
  mkdir "file"
fi

echo "`ls file`" > tmp
echo "INSERT INTO \`img\` (\`id\`, \`category\`, \`url\`) VALUES" > "sql"
cd "file"
for i in $(cat "../tmp"); do
  nuovo="$pre$nome.$f"
  convert "$i" "$nuovo"
  rm "$i"
  echo "(NULL, '$cat', '/$cat/$sub$nuovo')," >> "../sql"
  let nome++
done
rm "../tmp"
sed -i '$ s/,$//' "../sql"

