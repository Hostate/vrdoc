#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.90.3),
    on 2019_05_08_1746
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
expName = 'click_exp'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'C:\\Users\\czqin\\Documents\\vrdoc\\exp\\click_exp.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='white', colorSpace='rgb',
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
    text=u'\u4f60\u597d\n\n\u5728\u63a5\u4e0b\u6765\u7684\u5b9e\u9a8c\u4e2d\n\n\u5c4f\u5e55\u4e0a\u4f1a\u51fa\u73b0\u4e00\u4e2a3*3\u7684\u6570\u5b57\u8868\n\n\u683c\u5f0f\u548c\u5c0f\u952e\u76d8\u7684\u6570\u5b57\u76f8\u540c\n\n\u5176\u4e2d\u6709\u4e00\u4e2a\u6570\u5b57\u7684\u80cc\u666f\u8272\u548c\u5176\u4ed6\u7684\u4e0d\u540c\n\n\u8bf7\u60a8\u53c8\u5feb\u53c8\u51c6\u5730\u6309\u5c0f\u952e\u76d8\u4e0a\u7684\u5bf9\u5e94\u6570\u5b57\n\n\u5982\u679c\u7406\u89e3\u4e86\uff0c\u8bf7\u6309\u7a7a\u683c\u952e\u8fdb\u5165\u7ec3\u4e60',
    font='Consolas',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "practice_click"
practice_clickClock = core.Clock()
image_practice = visual.ImageStim(
    win=win, name='image_practice',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.45, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
point_prac = visual.TextStim(win=win, name='point_prac',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "formal_wel"
formal_welClock = core.Clock()
text_base = visual.TextStim(win=win, name='text_base',
    text=u'\u8bf7\u4f11\u606f\u4e00\u4e0b\n\n\u8bf7\u60a8\u53c8\u5feb\u53c8\u51c6\u5730\u6309\u5c0f\u952e\u76d8\u4e0a\u7684\u5bf9\u5e94\u6570\u5b57\n\n\u6309\u7a7a\u683c\u952e\u7ee7\u7eed',
    font='Consolas',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "huan"
huanClock = core.Clock()
huan_point = visual.TextStim(win=win, name='huan_point',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);
image_huan = visual.ImageStim(
    win=win, name='image_huan',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.45, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "baseline_click"
baseline_clickClock = core.Clock()
point_base = visual.TextStim(win=win, name='point_base',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);
image_base = visual.ImageStim(
    win=win, name='image_base',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.45, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "formal_click"
formal_clickClock = core.Clock()
point_for = visual.TextStim(win=win, name='point_for',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);
image_for = visual.ImageStim(
    win=win, name='image_for',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.45, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

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

# set up handler to look after randomisation of conditions etc
trials_prac = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('pic\\prac_click.csv'),
    seed=None, name='trials_prac')
thisExp.addLoop(trials_prac)  # add the loop to the experiment
thisTrials_prac = trials_prac.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_prac.rgb)
if thisTrials_prac != None:
    for paramName in thisTrials_prac:
        exec('{} = thisTrials_prac[paramName]'.format(paramName))

for thisTrials_prac in trials_prac:
    currentLoop = trials_prac
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_prac.rgb)
    if thisTrials_prac != None:
        for paramName in thisTrials_prac:
            exec('{} = thisTrials_prac[paramName]'.format(paramName))
    
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
        if t >= 1 and image_practice.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_practice.tStart = t
            image_practice.frameNStart = frameN  # exact frame index
            image_practice.setAutoDraw(True)
        
        # *key_resp_2* updates
        if t >= 1 and key_resp_2.status == NOT_STARTED:
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
                # was this 'correct'?
                if (key_resp_2.keys == str('')) or (key_resp_2.keys == ''):
                    key_resp_2.corr = 1
                else:
                    key_resp_2.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *point_prac* updates
        if t >= 0.0 and point_prac.status == NOT_STARTED:
            # keep track of start time/frame for later
            point_prac.tStart = t
            point_prac.frameNStart = frameN  # exact frame index
            point_prac.setAutoDraw(True)
        frameRemains = 0.0 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
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
        # was no response the correct answer?!
        if str('').lower() == 'none':
           key_resp_2.corr = 1  # correct non-response
        else:
           key_resp_2.corr = 0  # failed to respond (incorrectly)
    # store data for trials_prac (TrialHandler)
    trials_prac.addData('key_resp_2.keys',key_resp_2.keys)
    trials_prac.addData('key_resp_2.corr', key_resp_2.corr)
    if key_resp_2.keys != None:  # we had a response
        trials_prac.addData('key_resp_2.rt', key_resp_2.rt)
    # the Routine "practice_click" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1 repeats of 'trials_prac'


# ------Prepare to start Routine "formal_wel"-------
t = 0
formal_welClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_for_wel = event.BuilderKeyResponse()
# keep track of which components have finished
formal_welComponents = [text_base, key_resp_for_wel]
for thisComponent in formal_welComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "formal_wel"-------
while continueRoutine:
    # get current time
    t = formal_welClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_base* updates
    if t >= 0.0 and text_base.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_base.tStart = t
        text_base.frameNStart = frameN  # exact frame index
        text_base.setAutoDraw(True)
    
    # *key_resp_for_wel* updates
    if t >= 0.0 and key_resp_for_wel.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_for_wel.tStart = t
        key_resp_for_wel.frameNStart = frameN  # exact frame index
        key_resp_for_wel.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_for_wel.status == STARTED:
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
    for thisComponent in formal_welComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "formal_wel"-------
for thisComponent in formal_welComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "formal_wel" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_huan = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('pic\\huan.csv'),
    seed=None, name='trials_huan')
thisExp.addLoop(trials_huan)  # add the loop to the experiment
thisTrials_huan = trials_huan.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_huan.rgb)
if thisTrials_huan != None:
    for paramName in thisTrials_huan:
        exec('{} = thisTrials_huan[paramName]'.format(paramName))

for thisTrials_huan in trials_huan:
    currentLoop = trials_huan
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_huan.rgb)
    if thisTrials_huan != None:
        for paramName in thisTrials_huan:
            exec('{} = thisTrials_huan[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "huan"-------
    t = 0
    huanClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    image_huan.setImage(pic)
    key_resp_huan = event.BuilderKeyResponse()
    # keep track of which components have finished
    huanComponents = [huan_point, image_huan, key_resp_huan]
    for thisComponent in huanComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "huan"-------
    while continueRoutine:
        # get current time
        t = huanClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *huan_point* updates
        if t >= 0.0 and huan_point.status == NOT_STARTED:
            # keep track of start time/frame for later
            huan_point.tStart = t
            huan_point.frameNStart = frameN  # exact frame index
            huan_point.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if huan_point.status == STARTED and t >= frameRemains:
            huan_point.setAutoDraw(False)
        
        # *image_huan* updates
        if t >= 1 and image_huan.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_huan.tStart = t
            image_huan.frameNStart = frameN  # exact frame index
            image_huan.setAutoDraw(True)
        
        # *key_resp_huan* updates
        if t >= 1 and key_resp_huan.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_huan.tStart = t
            key_resp_huan.frameNStart = frameN  # exact frame index
            key_resp_huan.status = STARTED
            # AllowedKeys looks like a variable named `ans`
            if not type(ans) in [list, tuple, np.ndarray]:
                if not isinstance(ans, basestring):
                    logging.error('AllowedKeys variable `ans` is not string- or list-like.')
                    core.quit()
                elif not ',' in ans: ans = (ans,)
                else:  ans = eval(ans)
            # keyboard checking is just starting
            win.callOnFlip(key_resp_huan.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_huan.status == STARTED:
            theseKeys = event.getKeys(keyList=list(ans))
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_huan.keys = theseKeys[-1]  # just the last key pressed
                key_resp_huan.rt = key_resp_huan.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in huanComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "huan"-------
    for thisComponent in huanComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_huan.keys in ['', [], None]:  # No response was made
        key_resp_huan.keys=None
    trials_huan.addData('key_resp_huan.keys',key_resp_huan.keys)
    if key_resp_huan.keys != None:  # we had a response
        trials_huan.addData('key_resp_huan.rt', key_resp_huan.rt)
    # the Routine "huan" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1 repeats of 'trials_huan'


# set up handler to look after randomisation of conditions etc
trials_baseline = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('pic\\baseline_c.csv'),
    seed=None, name='trials_baseline')
thisExp.addLoop(trials_baseline)  # add the loop to the experiment
thisTrials_baseline = trials_baseline.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_baseline.rgb)
if thisTrials_baseline != None:
    for paramName in thisTrials_baseline:
        exec('{} = thisTrials_baseline[paramName]'.format(paramName))

for thisTrials_baseline in trials_baseline:
    currentLoop = trials_baseline
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_baseline.rgb)
    if thisTrials_baseline != None:
        for paramName in thisTrials_baseline:
            exec('{} = thisTrials_baseline[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "baseline_click"-------
    t = 0
    baseline_clickClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    image_base.setImage(pic)
    key_resp_base = event.BuilderKeyResponse()
    # keep track of which components have finished
    baseline_clickComponents = [point_base, image_base, key_resp_base]
    for thisComponent in baseline_clickComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "baseline_click"-------
    while continueRoutine:
        # get current time
        t = baseline_clickClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *point_base* updates
        if t >= 0.0 and point_base.status == NOT_STARTED:
            # keep track of start time/frame for later
            point_base.tStart = t
            point_base.frameNStart = frameN  # exact frame index
            point_base.setAutoDraw(True)
        frameRemains = 0.0 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if point_base.status == STARTED and t >= frameRemains:
            point_base.setAutoDraw(False)
        
        # *image_base* updates
        if t >= 1 and image_base.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_base.tStart = t
            image_base.frameNStart = frameN  # exact frame index
            image_base.setAutoDraw(True)
        
        # *key_resp_base* updates
        if t >= 1 and key_resp_base.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_base.tStart = t
            key_resp_base.frameNStart = frameN  # exact frame index
            key_resp_base.status = STARTED
            # AllowedKeys looks like a variable named `ans`
            if not type(ans) in [list, tuple, np.ndarray]:
                if not isinstance(ans, basestring):
                    logging.error('AllowedKeys variable `ans` is not string- or list-like.')
                    core.quit()
                elif not ',' in ans: ans = (ans,)
                else:  ans = eval(ans)
            # keyboard checking is just starting
            win.callOnFlip(key_resp_base.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_base.status == STARTED:
            theseKeys = event.getKeys(keyList=list(ans))
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_base.keys = theseKeys[-1]  # just the last key pressed
                key_resp_base.rt = key_resp_base.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in baseline_clickComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "baseline_click"-------
    for thisComponent in baseline_clickComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_base.keys in ['', [], None]:  # No response was made
        key_resp_base.keys=None
    trials_baseline.addData('key_resp_base.keys',key_resp_base.keys)
    if key_resp_base.keys != None:  # we had a response
        trials_baseline.addData('key_resp_base.rt', key_resp_base.rt)
    # the Routine "baseline_click" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_baseline'

# get names of stimulus parameters
if trials_baseline.trialList in ([], [None], None):
    params = []
else:
    params = trials_baseline.trialList[0].keys()
# save data for this loop
trials_baseline.saveAsText(filename + 'trials_baseline.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# set up handler to look after randomisation of conditions etc
trials_formal = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('pic\\formal_click.csv'),
    seed=None, name='trials_formal')
thisExp.addLoop(trials_formal)  # add the loop to the experiment
thisTrials_formal = trials_formal.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_formal.rgb)
if thisTrials_formal != None:
    for paramName in thisTrials_formal:
        exec('{} = thisTrials_formal[paramName]'.format(paramName))

for thisTrials_formal in trials_formal:
    currentLoop = trials_formal
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_formal.rgb)
    if thisTrials_formal != None:
        for paramName in thisTrials_formal:
            exec('{} = thisTrials_formal[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "formal_click"-------
    t = 0
    formal_clickClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_for = event.BuilderKeyResponse()
    image_for.setImage(pic)
    # keep track of which components have finished
    formal_clickComponents = [point_for, key_resp_for, image_for]
    for thisComponent in formal_clickComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "formal_click"-------
    while continueRoutine:
        # get current time
        t = formal_clickClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *point_for* updates
        if t >= 0.0 and point_for.status == NOT_STARTED:
            # keep track of start time/frame for later
            point_for.tStart = t
            point_for.frameNStart = frameN  # exact frame index
            point_for.setAutoDraw(True)
        frameRemains = 0.0 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if point_for.status == STARTED and t >= frameRemains:
            point_for.setAutoDraw(False)
        
        # *key_resp_for* updates
        if t >= 1 and key_resp_for.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_for.tStart = t
            key_resp_for.frameNStart = frameN  # exact frame index
            key_resp_for.status = STARTED
            # AllowedKeys looks like a variable named `ans`
            if not type(ans) in [list, tuple, np.ndarray]:
                if not isinstance(ans, basestring):
                    logging.error('AllowedKeys variable `ans` is not string- or list-like.')
                    core.quit()
                elif not ',' in ans: ans = (ans,)
                else:  ans = eval(ans)
            # keyboard checking is just starting
            win.callOnFlip(key_resp_for.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_for.status == STARTED:
            theseKeys = event.getKeys(keyList=list(ans))
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_for.keys = theseKeys[-1]  # just the last key pressed
                key_resp_for.rt = key_resp_for.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # *image_for* updates
        if t >= 1 and image_for.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_for.tStart = t
            image_for.frameNStart = frameN  # exact frame index
            image_for.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in formal_clickComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "formal_click"-------
    for thisComponent in formal_clickComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_for.keys in ['', [], None]:  # No response was made
        key_resp_for.keys=None
    trials_formal.addData('key_resp_for.keys',key_resp_for.keys)
    if key_resp_for.keys != None:  # we had a response
        trials_formal.addData('key_resp_for.rt', key_resp_for.rt)
    # the Routine "formal_click" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_formal'

# get names of stimulus parameters
if trials_formal.trialList in ([], [None], None):
    params = []
else:
    params = trials_formal.trialList[0].keys()
# save data for this loop
trials_formal.saveAsText(filename + 'trials_formal.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
