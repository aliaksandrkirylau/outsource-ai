---
type: requirement
id: REQ-013
status: draft
origin: extracted
author: claude-code/claude-opus-5-5
sources:
  - "[[2025-10-23 OES company research - rendering]]"
  - "[[2025-10-22 First call with OES - notes]]"
  - "[[2025-10-29 Client answers to the Q&A register - rendering]]"
  - "[[2025-10-28 BA draft WBS - rendering]]"
  - "[[2025-12-30 Answers to the client's questions - rendering]]"
  - "[[2025-11-05 Proposal slides - rendering]]"
  - "[[2025-11-03 Solution proposal - rendering]]"
  - "[[2025-10-24 Presale architecture - rendering]]"
  - "[[2026-06-15 SOW v10.4 - rendering]]"
  - "[[2025-11-05 WBS sent to the client - rendering]]"
  - "[[2026-09-25 v1 WBS - rendering]]"
  - "[[2025-10-20 Presale chat - rendering 2]]"
scope_status: out-of-scope
baseline:
  - "WBS:Development Flutter!75-88"
tags:
  - mobile
  - out-of-scope
---
# REQ-013 Mobile app

## Need

Recorded so nobody re-asks: a mobile app is out of scope, although the client asked for one.

What the client asked for:

- "mobile app integration" ([[2025-10-23 OES company research - rendering]], Initial Request).
- "have mobile app future that will be in demand within supervisors"
  ([[2025-10-22 First call with OES - notes]] key point 4).
- "it should focus on the most essential tasks for users in the field, such as quick data entry,
  status checks, or basic reporting"; devices: "iPhone and Android devices"
  ([[2025-10-29 Client answers to the Q&A register - rendering]] B.3, B.4).

How it left the scope:

- The BA draft marked mobile variants on seven features ([[2025-10-28 BA draft WBS - rendering]] rows
  14, 17, 21, 32, 35, 36, 42).
- The WBS sent to the client on 5 November 2025 had it in the MVP (added 2026-09-28, batch 4): "Web
  application and Cross Platform application", back and front end "(desktop+mobile)", every mobile line
  TRUE ([[2025-11-05 WBS sent to the client - rendering]] Overview row 7, Development rows 71 to 84).
- Then it was dropped (added 2026-09-28, batch 5): the prototype of 19 November 2025 was desktop and web
  only, "мобилку не нужно", and on 24 November the WBS was re-estimated "исходя из фул скоупа
  десктопного приложения и отсутствия мобильного" ([[2025-10-20 Presale chat - rendering 2]]
  2025-11-19 09:37, 2025-11-24 15:35).
- The v1 WBS ([[2026-09-25 v1 WBS - rendering]]) keeps mobile rows 75 to 88 but outside the estimated total (the MVP column is FALSE for
  all of them).
- The SOW v10.4 ([[2026-06-15 SOW v10.4 - rendering]]): "Development of mobile applications, mobile versions, and
  mobile-specific functionality is expressly excluded from the scope of this SOW."
- In presale (added 2026-09-28, batch 2): the architect answered that MAUI apps "можно развренуть на
  Android и IOS" ([[2025-10-24 Presale architecture - rendering]], comment); the proposal made mobile
  "a future phase and is not included in this MVP proposal"
  ([[2025-11-03 Solution proposal - rendering]], Assumptions); the slides' iteration 2: "Mobile
  application was considered as out of scope" ([[2025-11-05 Proposal slides - rendering]] slide 24).

The web app on tablets and phones is out too (added 2026-09-28): "The default desktop frame is
1440x1024 pixels ... The designer will not create layouts for screen behavior on devices with
resolutions below 1440×1024 (tablets and mobile phones)"; adaptive design only by separate estimate
([[2025-12-30 Answers to the client's questions - rendering]], Page 2). The SOW v10.4: responsive or
adaptive layout "is not included in the scope".

If the client asks for it, it is a change request. Tablets are a separate open point:
[[QUE-001 Why a desktop at the rig, and tablets later]].

## Acceptance criteria

None: out of scope.

## Edge cases

| Scenario | Expected behaviour |
|---|---|

## Business rules

## Out of scope

The whole of this note.
