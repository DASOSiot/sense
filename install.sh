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
bash ./scripts/steps/01.sh && #
#bash ./scripts/steps/10.sh && #
#bash ./scripts/steps/20.sh && # 
#
#bash ./scripts/steps/99.sh &&
# STEPS: END.
echo "... STEPS completed... Enjoy!"
# --------------------------------------------------------------------
# SCRIPT: END
