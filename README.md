# AI App Compiler

A Multi-Stage AI App Compiler built using FastAPI.

## Pipeline

1. Intent Extraction
2. System Design
3. Schema Generation
4. Validation
5. Repair

## Supported Applications

- Chat Application
- CRM
- Hospital Management System
- E-Commerce

## API Endpoint

### POST /generate

### Example Request

```json
{
  "prompt": "Build a CRM application"
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
