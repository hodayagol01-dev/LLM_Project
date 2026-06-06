# Experiments and Prompt Engineering

## Purpose

This document summarizes the experimentation process behind the AI Meeting Scheduler Agent.

The goal of the project is to build an autonomous agent that can read Gmail messages, identify meeting requests, extract the relevant scheduling details, check Google Calendar availability, create calendar events when possible, and reply to the sender.

The experiments focused on three main questions:

1. How can the agent reliably identify whether an email is a meeting request?
2. How can the agent extract useful meeting details from imperfect natural language?
3. How should the agent behave when required information is missing or when the calendar is unavailable?

---

## Experiment 1: Basic Keyword-Based Detection

### Goal

Detect meeting requests using simple keywords such as:

- meeting
- schedule
- sync
- call
- discussion

### Example Input

```text
Hi, can we schedule a meeting about the project sync?
