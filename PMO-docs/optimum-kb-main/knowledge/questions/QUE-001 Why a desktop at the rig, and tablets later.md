---
type: question
id: QUE-001
status: draft
origin: evaluated
author: claude-code/claude-opus-5-5
asks: client
sources:
  - "[[2026-09-25 Optimum Eng sync - transcript]]"
  - "[[2025-10-29 Client answers to the Q&A register - rendering]]"
  - "[[2025-10-22 First call with OES - notes]]"
  - "[[2025-10-22 First call with OES - transcript]]"
  - "[[2026-09-25 v1 WBS - rendering]]"
tags:
  - device
  - ui
---
# QUE-001 Why a desktop at the rig, and tablets later

## Question

How do engineers record a shift today, and why is the target a desktop rather than a tablet - and
will they want to run it on tablets later?

## What it blocks

The UI/UX design lines of the WBS: a desktop UI and a tablet UI are designed differently (Mikhail,
[[2026-09-25 Optimum Eng sync - transcript]] 00:14:04). Named 2026-09-28 (batch 4): Total Estimation
Development Flutter!9 (Total design) and Development Flutter!6 (UI Kit), with the UI/UX columns of each
feature line ([[2026-09-25 v1 WBS - rendering]]).

## Options

- A desktop at a rest-area PC, with shift notes taken on paper first - Arseniy's understanding,
  unconfirmed (00:12:21).
- A rugged tablet at the rig - raised by Mikhail (00:14:04).
- Desktop now, tablets later - Flutter helps, but adaptation is still needed (Anton, 00:14:51).

## Answer

None yet. Anton asked whether the desktop was a requirement of the client's leadership (00:11:29);
Arseniy answered "Да" (00:12:12), then added that he could only assume: "Честно, я не знаю истины, я
могу только предполагать" (00:12:21). Nobody on our side has spoken to the rig engineers (Anton,
00:11:29). To be asked through Snotov while he is on site (Mikhail, 00:13:29).

What the client said in October 2025 (added 2026-09-28 from batch 1 of the seed ingest):

- First call: "custom in-house app, preferably desktop (OS windows). The system to be scalable and have
  mobile app future that will be in demand within supervisors", and "Clients is asking on our opinion -
  desktop or web" ([[2025-10-22 First call with OES - notes]] key point 4). The computer "is assigned
  to that particular drilling rig" and is shared by "one or two people or three or four people" (key
  point 4).
- Asked whether anything required desktop or mobile apps rather than a web solution: "There are no
  strict limitations requiring the use of desktop or mobile applications. However, we need to consider
  that internet connectivity on rig sites may be unreliable."
  ([[2025-10-29 Client answers to the Q&A register - rendering]] A.2)
- For a mobile app: "iPhone and Android devices", focused on "quick data entry, status checks, or
  basic reporting" (B.3, B.4). Mobile is now out of scope ([[REQ-013 Mobile app]]); tablets were never
  discussed with the client in these sources.

From the first call's transcript (added 2026-09-28, batch 2): the desktop is the client's own
requirement. "It needs to be a desktop application. That is first and foremost ... if it has a mobile
app future that will be great because the mobile app future is what the, the supervisors mostly will
find more useful. But on the job site itself, okay. For the, for the for the field engineer that is on
the job site, it needs to have only the. The desktop application."
([[2025-10-22 First call with OES - transcript]] 1:02:23); Windows (1:03:23). How the engineers record
today: with lab equipment, then they "input those data into his, his software" (0:22:25). The client
then asked for our recommendation (1:03:41); Marina Zaretskaya: "For scalability? I probably would
recommend web application, but I need to talk about this with our solution architects" (1:04:02).

So the "why a desktop" half has the client's answer; the "tablets later" half is still open - tablets
are not mentioned in the transcript.

The platform choice itself is recorded in [[DEC-005 Desktop at the rig, web app at HQ]].
