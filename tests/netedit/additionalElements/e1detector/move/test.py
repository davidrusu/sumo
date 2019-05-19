#!/usr/bin/env python
# Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.org/sumo
# Copyright (C) 2009-2019 German Aerospace Center (DLR) and others.
# This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v2.0
# which accompanies this distribution, and is available at
# http://www.eclipse.org/legal/epl-v20.html
# SPDX-License-Identifier: EPL-2.0

# @file    test.py
# @author  Pablo Alvarez Lopez
# @date    2016-11-25
# @version $Id$

# import common functions for netedit tests
import os
import sys

testRoot = os.path.join(os.environ.get('SUMO_HOME', '.'), 'tests')
neteditTestRoot = os.path.join(
    os.environ.get('TEXTTEST_HOME', testRoot), 'netedit')
sys.path.append(neteditTestRoot)
import neteditTestFunctions as netedit  # noqa

# Open netedit
neteditProcess, referencePosition = netedit.setupAndStart(neteditTestRoot, ['--gui-testing-debug-gl'])

# go to additional mode
netedit.additionalMode()

# select E1
netedit.changeAdditional("e1Detector")

# create E1
netedit.leftClick(referencePosition, 250, 260)

# change to move mode
netedit.moveMode()

# move E1 to left
netedit.moveElement(referencePosition, 120, 260, 50, 260)

# move back
netedit.moveElement(referencePosition, 50, 260, 120, 260)

# move E1 to right
netedit.moveElement(referencePosition, 120, 260, 250, 260)

# move back
netedit.moveElement(referencePosition, 250, 260, 120, 260)

# move E1 to left overpassing lane
netedit.moveElement(referencePosition, 120, 260, -150, 260)

# move back
netedit.moveElement(referencePosition, -100, 260, 120, 260)

# move E1 to right overpassing lane
netedit.moveElement(referencePosition, 120, 260, 580, 260)

# move back to another different position of initial
netedit.moveElement(referencePosition, 520, 260, 300, 260)

# Check undos and redos
netedit.undo(referencePosition, 10)
netedit.redo(referencePosition, 10)

# save additionals
netedit.saveAdditionals()

# save network
netedit.saveNetwork()

# quit netedit
netedit.quit(neteditProcess)
