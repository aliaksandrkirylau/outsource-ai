---
type: decision
id: DEC-013
status: draft
origin: extracted
author: claude-code/claude-opus-5-5
kind: delivery
deciders:
  - tbd
sources:
  - "[[2026-09-30 Optimum Three Caballeros call - transcript]]"
  - "[[2026-10-13 OE Big4 chat - rendering 1]]"
valid_from: 2026-09-30
tags:
  - knowledge-base
  - sensitive
---
# DEC-013 Where the PMs keep sensitive working material

## Context

Money, how team members perform, internal statuses and financial projections stay out of the shared
KB (AGENTS.md rule 7), but the three PMs need to work with them. Mikhail: "в GIT ты не заливал
сознательно какую-то sensitive информацию, финансовые данные. Соответственно, они должны храниться
где-то еще, потому что, по крайней мере, нам троим надо работать и с этой инфой"
([[2026-09-30 Optimum Three Caballeros call - transcript]] 00:20:24). The kinds he named: internal
statuses, "информация про то, что кто-то в команде не перформит", statuses for the client, "Риски,
финансовые projection" (00:22:30).

It touches AGENTS.md "Where the rest lives", where the PMO Drive folder is not created yet, so it is a
curator matter too.

## Options considered

1. A local folder kept out of git by `.gitignore` (Anton, 00:23:16).
2. Encrypted data in the repository, "как это делают в программировании" (Arseniy, 00:26:33).
3. A second repository for the three (Mikhail, 00:28:14). Arseniy finds keeping two repositories in
   step "рутинный, муторный" (00:28:35).
4. A Drive folder the three can open: "Sensitive находится в Sensitive папке в Drive фолдере ... эта
   инфа никогда не уходит в КБ, но Клод знает, что за Sensitive нужно туда ходить" (Anton, 00:29:39).

## Decision

Not taken. The call ended with Anton leaving for another meeting (00:29:39) and Arseniy: "Я подумаю
насчет того, как нам удобнее передавать sensitive info" (00:26:33), "Да, я подумаю тоже. Хорошо."
(00:30:12).

Since then (added 2026-10-14; [[2026-10-13 OE Big4 chat - rendering 1]]): option 3 is in use - Mikhail runs a separate repository for
sensitive data and invited Kavalchuk: "Заинвайтил тебя в репозиторий с сенситив данными. Антон пригласит
в командный репозиторий." (2026-10-13 12:51). Anton is still trying option 1: "по сенсетив, я там
немного смотрел - возможно это все еще отдельный репо будет, но папкой внутри основного с игнором. Я
досмотрю, поэкспереминтирую и предложу как будет видно." (12:53). Kavalchuk asked "Парни, а подход
Sensetive General сохранён?"; Anton: "Сам подход есть, фолдеров этих еще небыло." (09:58, 10:54). Still
not decided; deciders tbd.

## Rationale

To be written when decided.

## Consequences

To be written when decided. Whatever is chosen, the KB's rule stays: nothing sensitive comes into the
shared repository, and an agent reading the sensitive place never copies from it into the KB. Options 2
and 3 add tooling the team has to keep working; option 4 waits for the PMO Drive folder.
