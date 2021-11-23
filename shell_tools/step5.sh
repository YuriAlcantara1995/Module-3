find . -type f -print0 | xargs -0 stat -c "%m %N" | sort -rn
