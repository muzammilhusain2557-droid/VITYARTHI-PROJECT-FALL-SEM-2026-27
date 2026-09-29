# Project Statement

## Problem Statement

College students juggle several small but constant admin tasks through
a semester - keeping track of grades and GPA, remembering assignment
deadlines, managing their monthly spending on a limited budget, and
staying updated on department/campus announcements. These are usually
handled through a mix of disconnected tools (spreadsheets, notes apps,
messaging groups), which makes it easy for something - usually a
deadline or a budget limit - to get missed.

The Smart Student Campus Assistant addresses this by combining all
four into a single, simple, offline console application with no setup
overhead beyond having Python installed.

## Scope of the Project

The project is scoped as a **single-user, local, console-based**
application. It is not meant to be a multi-user or networked system -
all data is stored locally in json files on the student's own machine.
The scope covers:

- Recording and calculating academic performance (GPA/CGPA)
- Maintaining a searchable campus information directory
- Logging and summarizing personal expenses against a monthly budget
- Managing a task/assignment planner with deadlines and priorities

Out of scope for this version: user accounts/authentication, syncing
across devices, a graphical interface, and integration with an
institution's actual student information system.

## Target Users

- College/university students who want a single tool to track
  academics, spending and deadlines without juggling multiple apps
- Particularly useful for students on a fixed monthly allowance who
  need a simple way to keep spending in check
- Anyone comfortable running a basic command-line program - no
  technical background beyond that is assumed

## High-Level Features

1. **Academic Summary** - add subject results, calculate semester GPA
   and overall CGPA
2. **Campus Info** - search and browse departments, faculty, campus
   facilities, and upcoming events
3. **Expense Tracker** - log expenses by category, set a monthly
   budget, view spending breakdowns and budget status
4. **Planner** - add tasks with deadlines and priority, view pending
   and overdue items, mark tasks complete
