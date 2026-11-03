---
type: source
kind: meeting-notes
date: 2025-10-22
setting: client
participants:
  - Zaretskaya M
  - Snotau I.
  - Pantskevich T.
  - Yanovskaya P.
  - Zahra Ahmad
  - Lowell
recording: https://drive.google.com/file/d/1Ou8sH9xSkHz2-7gDja9H0-m1v4nXX5B0/view
original: https://docs.google.com/document/d/1CDwBVWnl0Yvr3M09yzSxwWLbSsYxGfmhz5eBemlm8BM
language: en
removed:
  - nothing
---

# 2025-10-22 First call with OES - notes

Innowise's notes of the first call with the client, from the Google Doc "Follow-up initial call with
the client (Zaretskaya)". Not a transcript: the call was recorded (link above), but no transcript
exists. Verbatim, including typos and speech-to-text slips in the quoted passage; soft line breaks
in the original are kept as line breaks. The participants are listed as the notes write them. Never
edited after storing.

**Meeting notes**

**Date:** 22/10/2025 10:00 - 11:30 CET

**Potential client:** Optimum engineering standards

**Participants:** Zaretskaya M, Snotau I., Pantskevich T., Yanovskaya P., **Zahra Ahmad, Lowell**

**Key points:**

1. The client serves as a subcontractor for oil and gas extracting and production businesses. The
   client has around 70 locations where they provide rig drilling services. The biggest customer is
   Saudi Aramco.
2. **Problem:** There're some obvious limitations to the current tools that they're using, both from
   a sustainability point of view and also from the point of view of adequacy. The client tried to
   use Excel and adapt ready solutions - but in all the cases faced limitations with scalability, lack
   of features they needed and so on. That's why it was decided to invest in software, smth
   homegoing, matching exactly their requirements , smth the Client can use across all operations.
3. **As-is:** they get contracts, mobilize their engineers and send them equipped with tools and
   equipment to the job sites. They work on shift-basis, control the process of drilling oil and gas
   wells and mostly focus on the fluid aspect and focus - fluid properties. Their engineers have
   mobile sensors used to measure properties of the fluid. After measurements then document them and
   make reports. Measurements are made in avg 4 times a day.
4. **Solution type:** custom in-house app, preferably desktop (OS windows). The system to be scalable
   and have mobile app future that will be in demand within supervisors.
   **Clients is asking on our opinion - desktop or web - pros and cons based on the collected requirements**
   FYI: Client's quotation "when we deploy the software, okay, we're going to deploy it on a
   particular computer. That computer will be utilized jointly by one or two people or three or four
   people. The computer is assigned to that particular drilling rig. The computer is not assigned to
   the individuals, is assigned to the lakeside. And for as many job that particular location or good
   and well, well, that particular location drills, they'll continue to use that same computer"
5. **Main features to be implemented in the app**:
   - Users module: users CRUD and permissions (around 3-4 user group types: sites engineer, admin,
     supervisor, manager);
   - Projects module: create a project (add id, basic details, location, info on client, order
     details, quality requirements, etc), edit, remove, assign responsible;
   - Measurement module: input measured onsite data manually (note - fluids properties control, less
     than 50 parameters, 4 times a day. Well drilling duration is about 2 month avg);
   - Inventory module: account for the quantity or volume of drilling fluid that has been utilized for
     that day and what is remaining, chemicals, materials, etc.
   - Alerting if the inputted parameter is out if the set thresholds;
   - Dashboards (view the data on the dashboards - type of charts and what to display TBD while
     development);
   - Reporting: Generate reports (end of day - detailing the different specifications and properties
     of the drainage fluid, end of (well) job report, engineering calculation or simulation reports,
     inventory reports ) with the opportunity to export them in pdf, csv and xls formats.
   - Calculations and modelling (standard calculations and 'experimenting' - How to increase the mud
     weight? How many bags of barrites do I need? I want to change the high water ratio - how much oil
     do I need to add? Briefly experimenting with fluid parameters and see what happens, view charts
     (see details, record 47:00 explanation);
   - Modelling (simulation) -fluid hydraulics/fluid mechanics mostly. The client wants to see what's
     the fluid hydraulics looking like on that different scenario, based on the architecture or the
     profile of the well that we are drilling, based on the type of beads, the type of blring, the kind
     of p, the kind of flow rates, the rheology of the mud, you know, and other parameters of interest.
6. **Data storing approach requested:** Centralized DB for all locations. But the client doesn't want
   to depend on the cloud only, they think about on-premises storage as well. The data should be
   accessible from all the locations.
   **The Client expects advice from our side**
7. Security: Client has concern on confidentiality of data storing - especially his customers' details.
8. Availability: Internet connection loss might be an issue - some locations are rather remote and
   important to account that the access to the Internet isn't available or the Internet connection is
   poor.
9. Language: English

**Out of scope:**

- Data collection from sensors
- Integrations with other systems
- API designing
- Simulation for predicting equipment maintenance

## Comments in the original

- Marina Zaretskaya, on "English": "TBC"
- Marina Zaretskaya, on "Users module: users CRUD and permissions (around 3-4 user group types: sites
  engineer, admin, supervisor, manager);": "TBD maybe in case of desktop app and their approach that's
  not necessary, just use password for laptop"
