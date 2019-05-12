#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.90.3),
    on 2019_04_14_1801
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division

import psychopy
psychopy.useVersion('1.90.3')

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
expName = 'exp'  # from the Builder filename that created this script
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
    allowGUI=True, allowStencil=False,
    monitor='testMonitor', color='white', colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "click_re"
click_reClock = core.Clock()
image = visual.ImageStim(
    win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "wel"
welClock = core.Clock()
text_wel = visual.TextStim(win=win, name='text_wel',
    text=u'\u4f60\u597d\n\n\u4f60\u5988\u6b7b\u4e86',
    font='Consolas',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "omri_wel"
omri_welClock = core.Clock()
omri_wel_text = visual.TextStim(win=win, name='omri_wel_text',
    text=u'\u201c1\u201d\u4ee3\u8868\u201c\u5b8c\u5168\u4e0d\u7b26\u5408\u201d\uff0c\u201c2\u201d\u4ee3\u8868\u201c\u6bd4\u8f83\u4e0d\u7b26\u5408\u201d\uff0c\u201c3\u201d\u4ee3\u8868\u201c\u4e00\u822c\u201d\n\n\u201c4\u201d\u4ee3\u8868\u201c\u6bd4\u8f83\u7b26\u5408\u201d\uff0c\u201c5\u201d\u4ee3\u8868\u201c\u5b8c\u5168\u7b26\u5408\u201d',
    font='Consolas',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "que_omri"
que_omriClock = core.Clock()
rating_omri = visual.RatingScale(win=win, name='rating_omri', textColor = 'black', marker = 'triangle', acceptPreText=None,low=1, high=5, precision=1, choices=('1', '2','3','4','5'),noMouse=True, scale=None, markerStart = None,stretch = 2)
image_omri = visual.ImageStim(
    win=win, name='image_omri',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.5, 1.5*5/120),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "ug_1"
ug_1Clock = core.Clock()
ug_text_1 = visual.TextStim(win=win, name='ug_text_1',
    text=u'\u4f60\u548c\u4e00\u4e2a\u4eba\u5206\u914d100\u5143\n\n\u89c4\u5219\u662f\u4ed6\u6765\u5206\u914d\uff0c\u4f60\u6765\u51b3\u5b9a\u662f\u5426\u63a5\u53d7\n\n\u5982\u679c\u63a5\u53d7\uff0c\u5c31\u6839\u636e\u6b64\u65b9\u6848\u5206\u914d\u3002\u5982\u679c\u62d2\u7edd\uff0c\u5219\u53cc\u65b9\u90fd\u4e0d\u4f1a\u5f97\u5230\u94b1\n\n\uff08\u4e0d\u8003\u8651\u672c\u6b21\u5206\u914d\u7ed3\u675f\u540e\u53cc\u65b9\u8fdb\u4e00\u6b65\u4ea4\u6362\u7684\u53ef\u80fd\u6027\uff09\u3002\n\n\u90a3\u4e48\u4f60\u662f\u5426\u63a5\u53d7\u4f60\u548c\u4ed6\u7684\u91d1\u94b1\u5206\u914d\u6bd4\u4f8b\u662f1\uff1a99\u5462\uff1f',
    font='Consolas',
    pos=(0, 0.2), height=0.02, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);
rating_ug1 = visual.RatingScale(win=win, name='rating_ug1', textColor = 'black', marker = 'triangle',low=0, high=1, precision=1, labels = ('No','Yes'), noMouse=True, scale=None, markerStart = None,stretch = 2)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials_c = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('pic\\prac_click.csv', selection='0'),
    seed=None, name='trials_c')
thisExp.addLoop(trials_c)  # add the loop to the experiment
thisTrials_c = trials_c.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_c.rgb)
if thisTrials_c != None:
    for paramName in thisTrials_c:
        exec('{} = thisTrials_c[paramName]'.format(paramName))

for thisTrials_c in trials_c:
    currentLoop = trials_c
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_c.rgb)
    if thisTrials_c != None:
        for paramName in thisTrials_c:
            exec('{} = thisTrials_c[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "click_re"-------
    t = 0
    click_reClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    image.setImage(pic)
    key_resp_prac = event.BuilderKeyResponse()
    # keep track of which components have finished
    click_reComponents = [image, key_resp_prac]
    for thisComponent in click_reComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "click_re"-------
    while continueRoutine:
        # get current time
        t = click_reClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if t >= 0.0 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        
        # *key_resp_prac* updates
        if t >= 0.0 and key_resp_prac.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_prac.tStart = t
            key_resp_prac.frameNStart = frameN  # exact frame index
            key_resp_prac.status = STARTED
            # AllowedKeys looks like a variable named `ans`
            if not type(ans) in [list, tuple, np.ndarray]:
                if not isinstance(ans, basestring):
                    logging.error('AllowedKeys variable `ans` is not string- or list-like.')
                    core.quit()
                elif not ',' in ans: ans = (ans,)
                else:  ans = eval(ans)
            # keyboard checking is just starting
            win.callOnFlip(key_resp_prac.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_prac.status == STARTED:
            theseKeys = event.getKeys(keyList=list(ans))
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_prac.keys = theseKeys[-1]  # just the last key pressed
                key_resp_prac.rt = key_resp_prac.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in click_reComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "click_re"-------
    for thisComponent in click_reComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_prac.keys in ['', [], None]:  # No response was made
        key_resp_prac.keys=None
    trials_c.addData('key_resp_prac.keys',key_resp_prac.keys)
    if key_resp_prac.keys != None:  # we had a response
        trials_c.addData('key_resp_prac.rt', key_resp_prac.rt)
    # the Routine "click_re" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_c'


# ------Prepare to start Routine "wel"-------
t = 0
welClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
wel_key = event.BuilderKeyResponse()
# keep track of which components have finished
welComponents = [text_wel, wel_key]
for thisComponent in welComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "wel"-------
while continueRoutine:
    # get current time
    t = welClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_wel* updates
    if t >= 0.0 and text_wel.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_wel.tStart = t
        text_wel.frameNStart = frameN  # exact frame index
        text_wel.setAutoDraw(True)
    
    # *wel_key* updates
    if t >= 0.0 and wel_key.status == NOT_STARTED:
        # keep track of start time/frame for later
        wel_key.tStart = t
        wel_key.frameNStart = frameN  # exact frame index
        wel_key.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if wel_key.status == STARTED:
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

# ------Prepare to start Routine "omri_wel"-------
t = 0
omri_welClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
omri_key = event.BuilderKeyResponse()
# keep track of which components have finished
omri_welComponents = [omri_wel_text, omri_key]
for thisComponent in omri_welComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "omri_wel"-------
while continueRoutine:
    # get current time
    t = omri_welClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *omri_wel_text* updates
    if t >= 0.0 and omri_wel_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        omri_wel_text.tStart = t
        omri_wel_text.frameNStart = frameN  # exact frame index
        omri_wel_text.setAutoDraw(True)
    
    # *omri_key* updates
    if t >= 0.0 and omri_key.status == NOT_STARTED:
        # keep track of start time/frame for later
        omri_key.tStart = t
        omri_key.frameNStart = frameN  # exact frame index
        omri_key.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if omri_key.status == STARTED:
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
    for thisComponent in omri_welComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "omri_wel"-------
for thisComponent in omri_welComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "omri_wel" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
omri = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('omri.xlsx', selection='0'),
    seed=None, name='omri')
thisExp.addLoop(omri)  # add the loop to the experiment
thisOmri = omri.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisOmri.rgb)
if thisOmri != None:
    for paramName in thisOmri:
        exec('{} = thisOmri[paramName]'.format(paramName))

for thisOmri in omri:
    currentLoop = omri
    # abbreviate parameter names if possible (e.g. rgb = thisOmri.rgb)
    if thisOmri != None:
        for paramName in thisOmri:
            exec('{} = thisOmri[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "que_omri"-------
    t = 0
    que_omriClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    rating_omri.reset()
    image_omri.setImage(que)
    # keep track of which components have finished
    que_omriComponents = [rating_omri, image_omri]
    for thisComponent in que_omriComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "que_omri"-------
    while continueRoutine:
        # get current time
        t = que_omriClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *rating_omri* updates
        if t >= 0.0 and rating_omri.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating_omri.tStart = t
            rating_omri.frameNStart = frameN  # exact frame index
            rating_omri.setAutoDraw(True)
        continueRoutine &= rating_omri.noResponse  # a response ends the trial
        
        # *image_omri* updates
        if t >= 0.0 and image_omri.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_omri.tStart = t
            image_omri.frameNStart = frameN  # exact frame index
            image_omri.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in que_omriComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "que_omri"-------
    for thisComponent in que_omriComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for omri (TrialHandler)
    omri.addData('rating_omri.response', rating_omri.getRating())
    # the Routine "que_omri" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'omri'


# ------Prepare to start Routine "ug_1"-------
t = 0
ug_1Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
rating_ug1.reset()
# keep track of which components have finished
ug_1Components = [ug_text_1, rating_ug1]
for thisComponent in ug_1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "ug_1"-------
while continueRoutine:
    # get current time
    t = ug_1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ug_text_1* updates
    if t >= 0.0 and ug_text_1.status == NOT_STARTED:
        # keep track of start time/frame for later
        ug_text_1.tStart = t
        ug_text_1.frameNStart = frameN  # exact frame index
        ug_text_1.setAutoDraw(True)
    # *rating_ug1* updates
    if t >= 0.0 and rating_ug1.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating_ug1.tStart = t
        rating_ug1.frameNStart = frameN  # exact frame index
        rating_ug1.setAutoDraw(True)
    continueRoutine &= rating_ug1.noResponse  # a response ends the trial
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ug_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ug_1"-------
for thisComponent in ug_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('rating_ug1.response', rating_ug1.getRating())
thisExp.nextEntry()
# the Routine "ug_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
