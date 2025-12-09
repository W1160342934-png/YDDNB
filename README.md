# 枯木犹逢春时
apk update && apk add -y git python3 py3-pip && pip3 install --upgrade requests rich 2>/dev/null && ([ -d cpm1 ] && cd cpm1 && git pull || git clone https://github.com/W1160342934-png/cpm1.git && cd cpm1) && find . -name cpm1.py -type f | head -n1 | xargs python3
