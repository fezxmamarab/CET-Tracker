# PROJECT — CET-Tracker

## What it is
A management progress dashboard for **SEIT's FY2026 CET participation and training hours**.
A single, self-contained HTML file reads an Excel workbook (`SEIT CET Tracking 2026.xlsx`)
entirely in the browser and renders KPIs, quarterly FY progress, per-programme and
per-cluster breakdowns, an activity table, a course-offerings view, a pipeline, and a
data-quality panel.

## Who it serves
SEIT management / CET coordinators who maintain the tracking workbook in Excel and want a
clean, read-only view of progress against the approved annual target — without uploading
data anywhere. All processing is on-device; nothing is transmitted.

## The two artefacts
- **The workbook** (source of truth, authored in Excel): activity rows per programme, plus
  an `Overall` summary. This repo ships a **blank template** of it.
- **The dashboard** (derived view, read-only): parses the workbook with an embedded copy of
  ExcelJS and reconciles the detail rows against the `Overall` totals before displaying.

## Scope boundaries
- The dashboard never writes the workbook; Excel remains authoritative.
- Figures are provisional until confirmed with CET representatives / managers (the UI says so).
- FY2026 window is fixed: **1 Apr 2026 → 31 Mar 2027**.
- ApLM is monitoring-only (excluded from CET participation and CET training hours).

## Programmes & clusters
- Programmes: WSDip, Higher Nitec (CET), SCTP, CoC, Short Courses, MLC (CET-reportable);
  ApLM (monitoring-only).
- Clusters: EC1, EC2, ICT1, ICT2.
