pip3 install --user schedule
pip3 install --user pyautogui
pip3 install --user python3_xlib
grep -qxF "python3 $(pwd)/schedule.py" /$HOME/.bashrc || echo "python3 $(pwd)schedule.py" >> /$HOME/.bashrc
source /$HOME/.bashrc
