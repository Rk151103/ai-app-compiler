from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict

app = FastAPI()


class PromptRequest(BaseModel):
    prompt: str


class GenerateResponse(BaseModel):
    stage_1_intent: Dict
    stage_2_design: Dict
    stage_3_schema: Dict
    stage_4_validation: Dict
    stage_5_repair: Dict


# =========================
# STAGE 1 - INTENT EXTRACTION
# =========================

def extract_intent(prompt: str):

    prompt = prompt.lower()

    if "crm" in prompt or "customer" in prompt:
        return {
            "app_type": "CRM",
            "features": ["login", "contacts", "dashboard"]
        }

    elif "chat" in prompt:
        return {
            "app_type": "Chat App",
            "features": ["login", "chat", "profile"]
        }

    elif "hospital" in prompt:
        return {
            "app_type": "Hospital Management System",
            "features": ["patients", "doctors", "appointments"]
        }

    elif "ecommerce" in prompt or "shop" in prompt:
        return {
            "app_type": "E-Commerce",
            "features": ["products", "cart", "checkout"]
        }

    else:
        return {
            "app_type": "General App",
            "features": []
        }


# =========================
# STAGE 2 - SYSTEM DESIGN
# =========================

def design_system(app_type):

    if app_type == "CRM":
        return {
            "entities": ["User", "Contact", "Lead"],
            "roles": ["Admin", "Sales"]
        }

    elif app_type == "Chat App":
        return {
            "entities": ["User", "Message"],
            "roles": ["User", "Admin"]
        }

    elif app_type == "Hospital Management System":
        return {
            "entities": ["Patient", "Doctor", "Appointment"],
            "roles": ["Admin", "Doctor", "Receptionist"]
        }

    elif app_type == "E-Commerce":
        return {
            "entities": ["Product", "Order", "Customer"],
            "roles": ["Admin", "Customer"]
        }

    return {
        "entities": [],
        "roles": []
    }


# =========================
# STAGE 3 - SCHEMA GENERATION
# =========================

def generate_schema(app_type):

    if app_type == "CRM":

        return {
            "ui_schema": {
                "pages": ["Login", "Dashboard", "Contacts"]
            },
            "api_schema": {
                "endpoints": ["/login", "/contacts", "/leads"]
            },
            "db_schema": {
                "tables": {
                    "users": ["id", "name", "email", "role"],
                    "contacts": ["id", "name", "phone"],
                    "leads": ["id", "source", "status"]
                }
            },
            "auth_schema": {
                "roles": ["Admin", "Sales"]
            }
        }

    elif app_type == "Chat App":

        return {
            "ui_schema": {
                "pages": ["Login", "Chat Room", "Profile"]
            },
            "api_schema": {
                "endpoints": ["/login", "/messages", "/users"]
            },
            "db_schema": {
                "tables": {
                    "users": ["id", "name", "email"],
                    "messages": ["id", "sender_id", "content"]
                }
            },
            "auth_schema": {
                "roles": ["User", "Admin"]
            }
        }

    elif app_type == "Hospital Management System":

        return {
            "ui_schema": {
                "pages": ["Patients", "Doctors", "Appointments"]
            },
            "api_schema": {
                "endpoints": ["/patients", "/doctors", "/appointments"]
            },
            "db_schema": {
                "tables": {
                    "patients": ["id", "name", "age"],
                    "doctors": ["id", "name", "specialization"],
                    "appointments": ["id", "patient_id", "doctor_id"]
                }
            },
            "auth_schema": {
                "roles": ["Admin", "Doctor", "Receptionist"]
            }
        }

    elif app_type == "E-Commerce":

        return {
            "ui_schema": {
                "pages": ["Home", "Products", "Cart", "Checkout"]
            },
            "api_schema": {
                "endpoints": ["/products", "/cart", "/orders"]
            },
            "db_schema": {
                "tables": {
                    "products": ["id", "name", "price"],
                    "orders": ["id", "customer_id", "status"],
                    "customers": ["id", "name", "email"]
                }
            },
            "auth_schema": {
                "roles": ["Admin", "Customer"]
            }
        }

    return {
        "ui_schema": {},
        "api_schema": {},
        "db_schema": {},
        "auth_schema": {}
    }


# =========================
# STAGE 4 - VALIDATION
# =========================

def validate_schema(schema):

    issues = []

    if not schema["ui_schema"]:
        issues.append("Missing UI Schema")

    if not schema["api_schema"]:
        issues.append("Missing API Schema")

    if not schema["db_schema"]:
        issues.append("Missing DB Schema")

    if not schema["auth_schema"]:
        issues.append("Missing Auth Schema")

    return {
        "status": "passed" if len(issues) == 0 else "failed",
        "issues": issues
    }


# =========================
# STAGE 5 - REPAIR
# =========================

def repair_schema(validation):

    repair_actions = []

    for issue in validation["issues"]:

        if issue == "Missing UI Schema":
            repair_actions.append("Generated default UI Schema")

        elif issue == "Missing API Schema":
            repair_actions.append("Generated default API Schema")

        elif issue == "Missing DB Schema":
            repair_actions.append("Generated default DB Schema")

        elif issue == "Missing Auth Schema":
            repair_actions.append("Generated default Auth Schema")

    return {
        "repair_actions": repair_actions
    }


# =========================
# ROUTES
# =========================

@app.get("/")
def home():
    return {"message": "AI App Compiler Running"}


@app.get("/test")
def test():
    return {"message": "Compiler Pipeline Active"}


@app.post("/generate", response_model=GenerateResponse)
def generate(req: PromptRequest):

    stage_1 = extract_intent(req.prompt)

    stage_2 = design_system(stage_1["app_type"])

    stage_3 = generate_schema(stage_1["app_type"])

    stage_4 = validate_schema(stage_3)

    stage_5 = repair_schema(stage_4)

    return {
        "stage_1_intent": stage_1,
        "stage_2_design": stage_2,
        "stage_3_schema": stage_3,
        "stage_4_validation": stage_4,
        "stage_5_repair": stage_5
    }