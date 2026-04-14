---
source: Prof (ShiftKey AI Agents & Chatbots course)
date: 2026-04-14
tags: [project-idea, agentic-ai, computer-vision, mlops, deepsense, portfolio]
---

# Agentic Model Generator

A system that takes image domain requirements and objectives as input, and outputs a base ML model scaffold for AI engineers to start from — skipping the "what architecture should I even use?" phase.

## Professor's original idea

> "If you have an image processing task (images could be very different for different domains), you may collect the details and features of the images and objectives of the model, then generate a base model for AI engineers to work on. This could improve the efficiency of the project."

## What it solves

AI engineers waste significant time selecting a starting architecture for each new domain (underwater imagery vs satellite vs sonar vs medical imaging). This system automates that first step.

## How it works

**Input (structured intake):**
- Image domain (e.g. underwater, aerial, medical, industrial)
- Image characteristics (resolution, lighting, noise, object scale, density)
- Task objective (classification, detection, segmentation, anomaly detection)
- Constraints (edge deployment, latency, model size)

**Processing:**
- RAG-backed retrieval of architecture patterns matching the domain + objective
- LLM reasoning over retrieved patterns to select and configure a base model

**Output:**
- Recommended architecture (e.g. YOLOv5, ResNet, EfficientDet, custom CNN)
- Base model config / starter code scaffold
- Brief rationale linking domain features to architecture choices

## Why this matters for DeepSense

DeepSense works across wildly different ocean/marine image domains — fish population monitoring, underwater cameras, satellite imagery, sonar visualizations. Each has unique image characteristics. A tool that scaffolds a sensible starting model for each new domain would directly improve engineer efficiency.

This is a genuine differentiator in co-op / full-time applications because it:
- Shows understanding of real ML engineering pain points
- Combines agentic AI + computer vision + MLOps
- Is directly applicable to DeepSense's multi-domain work

## Tech stack (proposed)

- **Agent**: AWS Bedrock Agents or LangGraph
- **Knowledge base**: RAG over architecture docs, papers, and domain-specific model performance data
- **Intake**: structured LLM conversation or form
- **Output**: generated `model.yaml` + starter training script

## Related notes
- [[GroundSense]] — prior agentic AI project, same Bedrock Agents stack
- [[DeepSense]] — target employer, multi-domain CV work
- [[Course - ShiftKey AI Agents & Chatbots]] — course where this idea came from
- [[Kavya Bhojani]] — professor who suggested this idea, former DeepSense ML intern
