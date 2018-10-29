#!/bin/sh
TMPCONFIG=`mktemp`
if [ "${ROOT_URL}" = "local" ]; then
  ROOT_URL_API="localhost"
elif [ "${ROOT_URL}" = "dev" ]; then
  ROOT_URL_API="dev.dafni.ac.uk"
elif [ "${ROOT_URL}" = "staging" ]; then
  ROOT_URL_API="dafni-nid-data-store-api-staging.kub.dafni.rl.ac.uk"
elif [ "${ROOT_URL}" = "prod" ]; then
  ROOT_URL_API="dafni.rl.ac.uk"
fi
echo -n '{"urls":[' > $TMPCONFIG
for S in /usr/share/nginx/html/*.yaml; do
	N=`basename $S | cut -d . -f 1`
	F=`basename $S`
	echo -n "{\"url\":\"/$F\",\"name\":\"$N\"}," >> $TMPCONFIG
	sed -ri 's/^(\s*)(host\s*:\s*$)/\1host: '"$ROOT_URL_API"'/' "$S"
	#sed -i "s/nid.dafni.ac.uk/$ROOT_URL_API/g" "$S"
done
echo "{}]}" >> $TMPCONFIG
mv $TMPCONFIG /usr/share/nginx/html/dafni-config.json
chmod 0444 /usr/share/nginx/html/dafni-config.json
