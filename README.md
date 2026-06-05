# AI App Compiler

A Multi-Stage AI App Compiler built using FastAPI that converts natural language prompts into structured application specifications.

## Features

- Intent Extraction
- System Design Generation
- Schema Generation
- Validation Engine
- Repair Engine

## Supported Applications

- Chat Application
- CRM
- Hospital Management System
- E-Commerce

## Pipeline

### Stage 1: Intent Extraction
Identifies application type and required features.

### Stage 2: System Design
Generates entities and user roles.

### Stage 3: Schema Generation
Creates:
- UI Schema
- API Schema
- Database Schema
- Authentication Schema

### Stage 4: Validation
Checks generated schemas for completeness and consistency.

### Stage 5: Repair
Automatically fixes missing or invalid components.

## API Endpoint

### POST /generate

Example Request:

```json
{
  "prompt": "Build a CRM application"
}
```

Example Response:

```json
{
  "stage_1_intent": {},
  "stage_2_design": {},
  "stage_3_schema": {},
  "stage_4_validation": {},
  "stage_5_repair": {}
}
```

## Installation

```bash
pip install fastapi uvicorn pydantic
```

## Run

```bash
python -m uvicorn main:app --reload
```

## API Documentation

Open:

```text
http://127.0.0.1:8000/docs
```

## Author

Rakesh Kore
GitHub: https://github.com/Rk151103
