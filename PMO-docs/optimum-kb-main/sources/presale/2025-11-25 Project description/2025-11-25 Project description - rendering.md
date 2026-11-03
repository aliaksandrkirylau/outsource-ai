---
type: source
kind: rendering
date: 2025-11-25
original: https://docs.google.com/document/d/1zTCgk9ydRTojvO4IjgFbWEaSEkiAgsmphoOOf0Dm6Nk
removed:
  - nothing
---

# 2025-11-25 Project description - rendering

Google Doc "Description Optimum" by Marina Zaretskaya, created 2025-11-25, last changed 2025-11-27.
Verbatim, including the paragraphs the document repeats. Never edited after storing.

The purpose of this project is to develop an in-house solution that automates routine tasks on
drilling sites and provides managers with clear operational insights, replacing the current
Excel-based and largely manual data management processes used in drilling fluid operations.

The platform is designed for Mud Engineers, Supervisors, Managers, and Administrators, and consists
of two complementary components: a native Windows desktop application used on-site to enter measured
data, manage inventory, perform calculations and modeling, and generate reports; and a web
application used to monitor project statuses across multiple rigs, manage users, oversee inventory,
work with reports, and track key metrics through dashboards. This approach provides the best of both
sides: it gives rig engineers the reliable, high-performance offline tool they need, while
simultaneously giving managers the centralized data and reporting they require.

From tech stack perspective (TBC after the discovery stage):
Backend service - .NET or Java

Local client application - MAUI

Central office web application - ReactJS

Identity provider - ASP.NET Identity or Keylock

DataBases:

Local storage for site clients SQLite - to keep data ready for server sync

Central database PostgreSQL - supports materialized view for efficient reports building

The project focuses on creating a software platform that digitizes and automates routine tasks in
drilling fluid operations.

Technically the solution contains two parts: an on-site native Windows desktop application and
web-based system.

The desktop application serves as a mud engineering tool that provides the user interface for data
entry, engineering calculations, inventory management and report generation, designed to operate
fully even without a stable internet connection.

A web application provides a browser-based interface for managers, supervisors, and admin offering
overall project oversight, inventory management, user management, streamlined reporting, and
enhanced visibility through a centralized dashboard.

The project focuses on creating a software platform that digitizes and automates key workflows in
drilling fluid operations. It combines an on-site native Windows desktop application for engineers
with a web-based system for managerial oversight, enabling consistent data capture, streamlined
reporting, and improved visibility across drilling sites.
