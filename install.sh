#
git clone https://github.com/influxdata/TICK-docker

#!/bin/bash
# --------------------------------------------------------------------
# DASOS Sense: A TICK Stack based kit.
# --------------------------------------------------------------------
# SCRIPT: START
# --------------------------------------------------------------------
echo ""
echo "DASOS Sense Installer"
# --------------------------------------------------------------------
# STEPS: Configuration.
#set -v # VERBOSE OPERATIONS
set -e # STOP IF ERROR
#STEPS: START.
#bash ./scripts/steps/00.sh && # Defaults
bash ./scripts/steps/01.sh && # Update & Upgrade
bash ./scripts/steps/02.sh && # Display Options
bash ./scripts/steps/03.sh && # Graphic Engine
#bash ./scripts/steps/04.sh && # Graphic Engine: Turbo (compiled)
bash ./scripts/steps/05.sh && # Display Manager
bash ./scripts/steps/06.sh && # Display Manager: Autologin
bash ./scripts/steps/07.sh && # Network Devices
bash ./scripts/steps/08.sh && # Common Tools
#bash ./scripts/steps/09.sh && # Bluetooth: Upgrade (compiled)
bash ./scripts/steps/10.sh && # Users & Groups
bash ./scripts/steps/11.sh && # XX
bash ./scripts/steps/12.sh && # YY
bash ./scripts/steps/20.sh && # Speedtest
bash ./scripts/steps/21.sh && # Adafruit
bash ./scripts/steps/22.sh && # Pimoroni
#
bash ./scripts/steps/99.sh &&
# STEPS: END.
echo "... STEPS completed... Enjoy!"
# --------------------------------------------------------------------
# SCRIPT: END
