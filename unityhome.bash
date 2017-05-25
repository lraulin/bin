#!/bin/bash
# tabsize: 4, encoding: utf8
#
# © 2011 con-f-use@gmx.net. Use permitted under MIT license:
#     http://www.opensource.org/licenses/mit-license.php
# 
# CONTRIBUTORS: Chris Druif <cyber.druif@gmail.com>
#               Scott Severance <http://www.scottseverance.us/>
# 
# This script updates the unity quicklist menu for nautilus to contain the user
# bookmarks. The updates will have efect after unity is restarted (either on
# the next login or by invoking 'unity --replace').

# location of template and unity bar launchers
nautempl="/usr/share/applications/nautilus-home.desktop"
target="$HOME/.local/share/applications/nautilus-home.desktop"
bookmarks="$HOME/.gtk-bookmarks"

# backup if file already exists
if [ -e "$target" ]; then
    echo "Creating backup of: $target."
    mv -n "$target" "$target.bak"
fi

# copy template
cp "$nautempl" "$target"

sed -i "s/\(OnlyShowIn=GNOME;\)/\1Unity;/" "$target"

echo "X-Ayatana-Desktop-Shortcuts=" >> $target

bmcount=0
while read bmline; do
    bmcount=$(($bmcount+1))     # number of current bookmark
    bmname=${bmline#*\ }        # name of the bookmark
    bmpath=${bmline%%\ *}       # path the bookmark leads to
    # deal with bookmarks that have no name
    if [ "$bmname" = "$bmpath" ]; then
        bmname=${bmpath##*/}
    fi
    # fix spaces in names and paths
    bmname="$(echo "$bmname" | sed 's/%20/ /g')"
    bmpath="$(echo "$bmpath" | sed 's/%20/ /g')"
    # extend shortcut list with current bookmark
    sed -i "s/\(X-Ayatana-Desktop-Shortcuts=.*\)/\1Scg${bmcount};/" "$target"
    # write bookmark information
    cat - >> "$target" <<EOF

[Scg$bmcount Shortcut Group]
Name=$bmname
Exec=nautilus "$bmpath"
OnlyShowIn=Unity
EOF
done < "$bookmarks"

# Add a root file manager entry
sed -i "s/\(X-Ayatana-Desktop-Shortcuts=.*\)/\1RootFM;/" "$target"
cat - >> "$target" <<EOF

[RootFM Shortcut Group]
Name=Root
Exec=gksudo nautilus
OnlyShowIn=Unity
EOF

exit 0
