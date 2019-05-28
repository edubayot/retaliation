pip3 install --user schedule
pip3 install --user pyautogui
pip3 install --user python3_xlib
pip3 install --user talkey
cp retaliation.desktop $HOME/.config/autostart/retaliation.desktop
echo "Exec=$(pwd)/retaliation.sh" >> $HOME/.config/autostart/retaliation.desktop
