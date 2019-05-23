pip install --user --yes schedule
grep -qxF 'python schedule.py' /$HOME/.bashrc || echo 'python schedule.py' >> /$HOME/.bashrc
source /$HOME/.bashrc
