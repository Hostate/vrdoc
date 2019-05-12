#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.90.3),
    on 2019_04_14_1804
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = u'click_exp'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s' % (expInfo['participant'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1200, 800], fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor=u'testMonitor', color=u'white', colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "wel"
welClock = core.Clock()
wel_text = visual.TextStim(win=win, name='wel_text',
    text=u'\u4f60\u597d\u554a',
    font=u'Consolas',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "practice_click"
practice_clickClock = core.Clock()
image_practice = visual.ImageStim(
    win=win, name='image_practice',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
point_prac = visual.TextStim(win=win, name='point_prac',
    text=u'+',
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "practice_check"
practice_checkClock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "wel"-------
t = 0
welClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_wel = event.BuilderKeyResponse()
# keep track of which components have finished
welComponents = [wel_text, key_resp_wel]
for thisComponent in welComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "wel"-------
while continueRoutine:
    # get current time
    t = welClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *wel_text* updates
    if t >= 0.0 and wel_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        wel_text.tStart = t
        wel_text.frameNStart = frameN  # exact frame index
        wel_text.setAutoDraw(True)
    
    # *key_resp_wel* updates
    if t >= 0.0 and key_resp_wel.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_wel.tStart = t
        key_resp_wel.frameNStart = frameN  # exact frame index
        key_resp_wel.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_wel.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "wel"-------
for thisComponent in welComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "wel" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
def prac():
# set up handler to look after randomisation of conditions etc
    trialsp = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(u'pic\\prac_click1.csv'),
        seed=None, name='trialsp')
    thisExp.addLoop(trialsp)  # add the loop to the experiment
    thisTrialsp = trialsp.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrialsp.rgb)
    if thisTrialsp != None:
        for paramName in thisTrialsp:
            exec('{} = thisTrialsp[paramName]'.format(paramName))

    for thisTrialsp in trialsp:
        currentLoop = trialsp
        # abbreviate parameter names if possible (e.g. rgb = thisTrialsp.rgb)
        if thisTrialsp != None:
            for paramName in thisTrialsp:
                exec('{} = thisTrialsp[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "practice_click"-------
        t = 0
        practice_clickClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        image_practice.setImage(pic)
        key_resp_2 = event.BuilderKeyResponse()
        # keep track of which components have finished
        practice_clickComponents = [image_practice, key_resp_2, point_prac]
        for thisComponent in practice_clickComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "practice_click"-------
        while continueRoutine:
            # get current time
            t = practice_clickClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_practice* updates
            if t >= 0.2 and image_practice.status == NOT_STARTED:
                # keep track of start time/frame for later
                image_practice.tStart = t
                image_practice.frameNStart = frameN  # exact frame index
                image_practice.setAutoDraw(True)
            
            # *key_resp_2* updates
            if t >= 0.2 and key_resp_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_resp_2.tStart = t
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.status = STARTED
                # AllowedKeys looks like a variable named `ans`
                if not type(ans) in [list, tuple, np.ndarray]:
                    if not isinstance(ans, basestring):
                        logging.error('AllowedKeys variable `ans` is not string- or list-like.')
                        core.quit()
                    elif not ',' in ans: ans = (ans,)
                    else:  ans = eval(ans)
                # keyboard checking is just starting
                win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            if key_resp_2.status == STARTED:
                theseKeys = event.getKeys(keyList=list(ans))
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    key_resp_2.keys = theseKeys[-1]  # just the last key pressed
                    key_resp_2.rt = key_resp_2.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
            
            # *point_prac* updates
            if t >= 0.0 and point_prac.status == NOT_STARTED:
                # keep track of start time/frame for later
                point_prac.tStart = t
                point_prac.frameNStart = frameN  # exact frame index
                point_prac.setAutoDraw(True)
            frameRemains = 0.0 + 0.2- win.monitorFramePeriod * 0.75  # most of one frame period left
            if point_prac.status == STARTED and t >= frameRemains:
                point_prac.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in practice_clickComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "practice_click"-------
        for thisComponent in practice_clickComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys=None
        trialsp.addData('key_resp_2.keys',key_resp_2.keys)
        if key_resp_2.keys != None:  # we had a response
            trialsp.addData('key_resp_2.rt', key_resp_2.rt)
        # the Routine "practice_click" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trialsp'

    # get names of stimulus parameters
    if trialsp.trialList in ([], [None], None):
        params = []
    else:
        params = trialsp.trialList[0].keys()
    # save data for this loop
    trialsp.saveAsText(filename + 'trialsp.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
prac()
# ------Prepare to start Routine "practice_check"-------
t = 0
practice_checkClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_prac = event.BuilderKeyResponse()
# keep track of which components have finished
practice_checkComponents = [key_resp_prac]
for thisComponent in practice_checkComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "practice_check"-------
while continueRoutine:
    # get current time
    t = practice_checkClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_prac* updates
    if t >= 0.0 and key_resp_prac.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_prac.tStart = t
        key_resp_prac.frameNStart = frameN  # exact frame index
        key_resp_prac.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_prac.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_prac.status == STARTED:
        theseKeys = event.getKeys(keyList=['f', 'j'])
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_prac.keys = theseKeys[-1]  # just the last key pressed
            key_resp_prac.rt = key_resp_prac.clock.getTime()
            if (key_resp_prac.keys == 'f'):
                print 'f'
            else:
                print 'j'
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practice_checkComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practice_check"-------
for thisComponent in practice_checkComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_prac.keys in ['', [], None]:  # No response was made
    key_resp_prac.keys=None
thisExp.addData('key_resp_prac.keys',key_resp_prac.keys)
if key_resp_prac.keys != None:  # we had a response
    thisExp.addData('key_resp_prac.rt', key_resp_prac.rt)
thisExp.nextEntry()
# the Routine "practice_check" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
