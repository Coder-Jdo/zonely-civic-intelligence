from typing import TypedDict

# ── Types ─────────────────────────────────────────────────────────────────────

class SignalData(TypedDict):
    activeApplications: int
    unitsPipeline: int
    inConsultation: int
    approvalRate: int
    submittedPending: int

class BreakdownItem(TypedDict):
    score: int
    trend: str
    note: str

class PlanningMomentum(TypedDict):
    score: int
    direction: str
    approvalRangeLow: int
    approvalRangeHigh: int

class TimeToValue(TypedDict):
    phase: str
    phaseRange: str
    timeline: str
    whatToExpect: list[str]
    drivers: list[str]
    riskFlags: list[str]
    factors: dict[str, str]

class CreditEvent(TypedDict):
    year: int
    title: str
    tag: str
    note: str

class CreditHistory(TypedDict):
    volatilityIndex: int
    recoverySpeed: int
    tenYearTrend: int
    events: list[CreditEvent]

class PostcodeData(TypedDict):
    area: str
    civicScore: int
    impactLabel: str
    impactLevel: str
    confidenceBand: int
    direction: str
    directionSymbol: str
    headlineSummary: str
    signals: SignalData
    breakdown: dict[str, BreakdownItem]
    planningMomentum: PlanningMomentum
    timeToValue: TimeToValue
    creditHistory: CreditHistory
    reportUrl: str

# ── Demo Data ─────────────────────────────────────────────────────────────────

ZONELY_DEMO_DATA: dict[str, PostcodeData] = {
    "LS1 1BA": {
        "area": "Leeds City Centre",
        "civicScore": 919,
        "impactLabel": "High Impact",
        "impactLevel": "high",
        "confidenceBand": 46,
        "direction": "Stable",
        "directionSymbol": "→",
        "headlineSummary": "Significant development pipeline activity. Substantial new supply and neighbourhood change anticipated over 3–5 years.",
        "signals": {
            "activeApplications": 168,
            "unitsPipeline": 4200,
            "inConsultation": 34,
            "approvalRate": 87,
            "submittedPending": 22,
        },
        "breakdown": {
            "Liveability & Amenities":        {"score": 75, "trend": "Stable",        "note": "Strong service density and amenity access."},
            "Investment Potential":           {"score": 55, "trend": "Growing",       "note": "Moderate Investment strength; improving attractiveness."},
            "Infrastructure & Connectivity":  {"score": 84, "trend": "Well-connected","note": "Excellent transport links."},
            "Crime & Safety":                 {"score": 68, "trend": "Improving",     "note": "Safety improving with regeneration."},
            "Planning & Development Momentum":{"score": 92, "trend": "Accelerating",  "note": "Very high pipeline activity."},
        },
        "planningMomentum": {
            "score": 88,
            "direction": "Accelerating",
            "approvalRangeLow": 75,
            "approvalRangeHigh": 92,
        },
        "timeToValue": {
            "phase": "Disruption Phase",
            "phaseRange": "0–2 years",
            "timeline": "0–2 Disruption | 3–5 Growth | 6–10 Compounding",
            "whatToExpect": [
                "Construction activity and temporary amenity disruption.",
                "Supply increase may create short-term rental softening.",
                "Infrastructure improvements will begin to deliver benefits.",
            ],
            "drivers": [
                "Large development pipeline (4,200 units).",
                "High approval rate indicating strong planning support.",
            ],
            "riskFlags": [
                "Short-term rental oversupply risk.",
                "Construction noise and disruption.",
            ],
            "factors": {
                "developmentScale": "Very large pipeline (4,200 units).",
                "buildingHeights": "High-rise (avg 18 storeys).",
                "approvalLikelihood": "Very high (87%).",
            },
        },
        "creditHistory": {
            "volatilityIndex": 68,
            "recoverySpeed": 145,
            "tenYearTrend": 185,
            "events": [
                {"year": 2016, "title": "South Bank Masterplan Launch",    "tag": "Planning",       "note": "Largest regeneration project in the UK."},
                {"year": 2018, "title": "Transport Investment Confirmed",  "tag": "Infrastructure", "note": "Transport investment completed."},
                {"year": 2019, "title": "Masterplan Approval",             "tag": "Planning",       "note": "Major regeneration plan adopted."},
                {"year": 2020, "title": "COVID-19 Pause",                  "tag": "Crisis",         "note": "Market disruption and construction delays."},
                {"year": 2022, "title": "First Major Completion",          "tag": "Market",         "note": "First phase of large scheme completed."},
            ],
        },
        "reportUrl": "/reports/Zonely-Client-Report-LS1_1BA.pdf",
    },
    "LS3 1AA": {
        "area": "Leeds",
        "civicScore": 450,
        "impactLabel": "Moderate Impact",
        "impactLevel": "moderate",
        "confidenceBand": 28,
        "direction": "Stable",
        "directionSymbol": "→",
        "headlineSummary": "Balanced development activity. Growth is present but measured with moderate supply pressure.",
        "signals": {
            "activeApplications": 41,
            "unitsPipeline": 1125,
            "inConsultation": 8,
            "approvalRate": 81,
            "submittedPending": 10,
        },
        "breakdown": {
            "Liveability & Amenities":        {"score": 60, "trend": "Stable",  "note": "Adequate amenity access."},
            "Investment Potential":           {"score": 62, "trend": "Stable",  "note": "Solid Investment signal."},
            "Infrastructure & Connectivity":  {"score": 58, "trend": "Stable",  "note": "Average connectivity."},
            "Crime & Safety":                 {"score": 45, "trend": "Stable",  "note": "Moderate safety profile."},
            "Planning & Development Momentum":{"score": 55, "trend": "Stable",  "note": "Steady pipeline."},
        },
        "planningMomentum": {
            "score": 52,
            "direction": "Neutral",
            "approvalRangeLow": 65,
            "approvalRangeHigh": 88,
        },
        "timeToValue": {
            "phase": "Growth Phase",
            "phaseRange": "3–5 years",
            "timeline": "0–2 Disruption | 3–5 Growth | 6–10 Compounding",
            "whatToExpect": [
                "More visible delivery outcomes.",
                "Rental demand can absorb new supply if timing is staggered.",
            ],
            "drivers": ["Pipeline delivery cadence.", "Local job and transport accessibility."],
            "riskFlags": [
                "Oversupply risk if delivery clusters.",
                "Policy changes impacting approvals.",
            ],
            "factors": {
                "developmentScale": "Moderate pipeline (1,125 units).",
                "buildingHeights": "Mid-rise (avg 9 storeys).",
                "approvalLikelihood": "Moderate-high (81%).",
            },
        },
        "creditHistory": {
            "volatilityIndex": 42,
            "recoverySpeed": 120,
            "tenYearTrend": 110,
            "events": [
                {"year": 2018, "title": "Public Realm Upgrade",     "tag": "Infrastructure", "note": "Local streetscape improvements."},
                {"year": 2021, "title": "Delivery Acceleration",    "tag": "Planning",       "note": "Increased approvals and starts."},
            ],
        },
        "reportUrl": "/reports/Zonely-Client-Report-LS3_1AA.pdf",
    },
    "LS6 3BN": {
        "area": "Chapel Allerton",
        "civicScore": 218,
        "impactLabel": "Low Impact",
        "impactLevel": "low",
        "confidenceBand": 11,
        "direction": "Stable",
        "directionSymbol": "→",
        "headlineSummary": "Limited near-term pipeline relative to city centre areas. Expect steadier conditions with lower supply shock risk.",
        "signals": {
            "activeApplications": 45,
            "unitsPipeline": 300,
            "inConsultation": 9,
            "approvalRate": 84,
            "submittedPending": 6,
        },
        "breakdown": {
            "Liveability & Amenities":        {"score": 33, "trend": "Stable",   "note": "Local amenities exist but lower density."},
            "Investment Potential":           {"score": 55, "trend": "Growing",  "note": "Stable Investment base."},
            "Infrastructure & Connectivity":  {"score": 31, "trend": "Moderate", "note": "Moderate connectivity."},
            "Crime & Safety":                 {"score": 62, "trend": "Improving","note": "Favourable safety trend."},
            "Planning & Development Momentum":{"score": 40, "trend": "Stable",   "note": "Lower development intensity."},
        },
        "planningMomentum": {
            "score": 38,
            "direction": "Slowing",
            "approvalRangeLow": 60,
            "approvalRangeHigh": 82,
        },
        "timeToValue": {
            "phase": "Compounding Phase",
            "phaseRange": "6–10 years",
            "timeline": "0–2 Disruption | 3–5 Growth | 6–10 Compounding",
            "whatToExpect": [
                "Lower disruption and gradual uplift.",
                "Stable rental conditions.",
            ],
            "drivers": ["Incremental improvements.", "Amenity and safety stability."],
            "riskFlags": ["Lower upside if pipeline remains limited."],
            "factors": {
                "developmentScale": "Small pipeline (~300 units).",
                "buildingHeights": "Low-rise (avg 5 storeys).",
                "approvalLikelihood": "High (84%).",
            },
        },
        "creditHistory": {
            "volatilityIndex": 25,
            "recoverySpeed": 80,
            "tenYearTrend": 60,
            "events": [
                {"year": 2016, "title": "Local Centre Investment", "tag": "Market", "note": "Retail and community improvements."},
            ],
        },
        "reportUrl": "/reports/Zonely-Client-Report-LS6_3BN.pdf",
    },
}


def normalize_postcode(value: str) -> str:
    return " ".join(value.strip().upper().split())

def is_valid_postcode(value: str) -> bool:
    return value in ZONELY_DEMO_DATA
