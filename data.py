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
        "civicScore": 780,
        "impactLabel": "High Impact",
        "impactLevel": "high",
        "confidenceBand": 48,
        "direction": "Volatile",
        "directionSymbol": "↗",
        "headlineSummary": "High-income central area (£49.6K avg) with strong development potential but extremely high crime levels (~2240 per 1,000) create significant risk.",

        "signals": {
            "activeApplications": 150,
            "unitsPipeline": 4000,
            "inConsultation": 30,
            "approvalRate": 85,
            "submittedPending": 20,
        },

        "breakdown": {
            "Liveability & Amenities": {
                "score": 160,
                "trend": "Strong",
                "note": "Very high education levels (49% degree holders)."
            },
            "Investment Potential": {
                "score": 180,
                "trend": "High",
                "note": "High household income (~£49.6K)."
            },
            "Infrastructure & Connectivity": {
                "score": 190,
                "trend": "Excellent",
                "note": "City centre location with top connectivity."
            },
            "Crime & Safety": {
                "score": 40,
                "trend": "High Risk",
                "note": "Extremely high crime (~2240 per 1,000 residents)."
            },
            "Planning & Development Momentum": {
                "score": 170,
                "trend": "Accelerating",
                "note": "Major regeneration and development activity."
            },
        },

        "planningMomentum": {
            "score": 85,
            "direction": "Accelerating",
            "approvalRangeLow": 70,
            "approvalRangeHigh": 90,
        },

        "timeToValue": {
            "phase": "Disruption Phase",
            "phaseRange": "0–3 years",
            "timeline": "0–3 Disruption | 3–6 Growth | 6–10 Compounding",
            "whatToExpect": [
                "High development activity and urban transformation.",
                "Strong rental demand from young professionals.",
            ],
            "drivers": [
                "High income levels.",
                "City centre demand."
            ],
            "riskFlags": [
                "Extremely high crime levels.",
                "Urban volatility."
            ],
            "factors": {
                "developmentScale": "Very high",
                "approvalLikelihood": "High (85%)",
            },
        },

        "creditHistory": {
            "volatilityIndex": 75,
            "recoverySpeed": 140,
            "tenYearTrend": 170,
            "events": []
        },

        "reportUrl": "/reports/Zonely-Client-Report-LS1_1BA.pdf",
    },


    "LS3 1AA": {
        "area": "Leeds",
        "civicScore": 520,
        "impactLabel": "Moderate Impact",
        "impactLevel": "moderate",
        "confidenceBand": 35,
        "direction": "Stable",
        "directionSymbol": "→",
        "headlineSummary": "Young, highly educated area with strong health (91%) and high student population, but lower income (~£30K) and elevated crime (~368 per 1,000).",

        "signals": {
            "activeApplications": 40,
            "unitsPipeline": 1100,
            "inConsultation": 8,
            "approvalRate": 81,
            "submittedPending": 10,
        },

        "breakdown": {
            "Liveability & Amenities": {
                "score": 100,
                "trend": "Good",
                "note": "High health levels (91%) and strong education (47% degree holders)."
            },
            "Investment Potential": {
                "score": 85,
                "trend": "Moderate",
                "note": "Lower income (~£30K) limits premium upside."
            },
            "Infrastructure & Connectivity": {
                "score": 90,
                "trend": "Stable",
                "note": "Good connectivity near city centre."
            },
            "Crime & Safety": {
                "score": 65,
                "trend": "Risk",
                "note": "Crime ~368 per 1,000 (above average)."
            },
            "Planning & Development Momentum": {
                "score": 95,
                "trend": "Stable",
                "note": "Steady development pipeline."
            },
        },

        "planningMomentum": {
            "score": 55,
            "direction": "Neutral",
            "approvalRangeLow": 65,
            "approvalRangeHigh": 85,
        },

        "timeToValue": {
            "phase": "Growth Phase",
            "phaseRange": "3–5 years",
            "timeline": "0–2 Disruption | 3–5 Growth | 6–10 Compounding",
            "whatToExpect": [
                "Steady rental demand due to student population.",
                "Moderate growth over mid-term.",
            ],
            "drivers": [
                "Young demographic.",
                "Education hub."
            ],
            "riskFlags": [
                "Higher crime rate.",
                "Lower income levels."
            ],
            "factors": {
                "developmentScale": "Moderate",
                "approvalLikelihood": "81%",
            },
        },

        "creditHistory": {
            "volatilityIndex": 45,
            "recoverySpeed": 120,
            "tenYearTrend": 110,
            "events": []
        },

        "reportUrl": "/reports/Zonely-Client-Report-LS3_1AA.pdf",
    },


    "LS6 3BN": {
        "area": "Chapel Allerton",
        "civicScore": 400,
        "impactLabel": "Low Impact",
        "impactLevel": "low",
        "confidenceBand": 25,
        "direction": "Stable",
        "directionSymbol": "→",
        "headlineSummary": "Balanced suburban area with stable income (~£42K), lower crime (~112 per 1,000), and long-term steady growth potential.",

        "signals": {
            "activeApplications": 45,
            "unitsPipeline": 300,
            "inConsultation": 9,
            "approvalRate": 84,
            "submittedPending": 6,
        },

        "breakdown": {
            "Liveability & Amenities": {
                "score": 80,
                "trend": "Stable",
                "note": "Good health (~88%) and suburban lifestyle."
            },
            "Investment Potential": {
                "score": 90,
                "trend": "Stable",
                "note": "Income (~£42K) supports steady growth."
            },
            "Infrastructure & Connectivity": {
                "score": 75,
                "trend": "Moderate",
                "note": "Decent but not central connectivity."
            },
            "Crime & Safety": {
                "score": 110,
                "trend": "Safe",
                "note": "Relatively low crime (~112 per 1,000)."
            },
            "Planning & Development Momentum": {
                "score": 70,
                "trend": "Slow",
                "note": "Limited development activity."
            },
        },

        "planningMomentum": {
            "score": 40,
            "direction": "Slowing",
            "approvalRangeLow": 60,
            "approvalRangeHigh": 80,
        },

        "timeToValue": {
            "phase": "Compounding Phase",
            "phaseRange": "5–10 years",
            "timeline": "0–2 Stable | 3–5 Growth | 6–10 Compounding",
            "whatToExpect": [
                "Stable residential demand.",
                "Slow but steady appreciation.",
            ],
            "drivers": [
                "Suburban stability.",
                "Lower crime levels."
            ],
            "riskFlags": [
                "Lower development upside.",
            ],
            "factors": {
                "developmentScale": "Low",
                "approvalLikelihood": "84%",
            },
        },

        "creditHistory": {
            "volatilityIndex": 30,
            "recoverySpeed": 110,
            "tenYearTrend": 90,
            "events": []
        },

        "reportUrl": "/reports/Zonely-Client-Report-LS6_3BN.pdf",
    }

}



def normalize_postcode(value: str) -> str:
    return " ".join(value.strip().upper().split())

def is_valid_postcode(value: str) -> bool:
    return value in ZONELY_DEMO_DATA
