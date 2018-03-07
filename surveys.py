test_survey = {
    "type": "tree",
    "title": "Survey for Care Partners",
    "question": {
        "A": {
            "text": "travel",
            "options":
                {
                    "1": "travel_category_1",
                    "2": "travel_category_2",
                    "3": "travel_category_3"
                }
        },
        "B": {
            "text": "admin",
            "options":
                {
                    "4": "admin_category_1",
                    "5": "admin_category_2",
                    "6": "admin_category_3"
                }
        },
        "C": {
            "text": "clinical",
            "options":
                {
                    "7": "clinical_category_1",
                    "8": "clinical_category_2",
                    "9": "clinical_category_3",
                    "10": "clinical_category_4"
                }
        }
    }
}

test_survey_office = {
    "type": "tree",
    "title": "Survey for ClinOps Office",
    "question": {
        "A": {
            "text": "desk work",
            "options":
                {
                    "1": "mostly emailing",
                    "2": "mostly working with documents",
                    "3": "can't remember"
                }
        },
        "B": {
            "text": "meetings",
            "options":
                {
                    "4": "meetings 1 on 1 ",
                    "5": "meetings in group",
                }
        },
        "C": {
            "text": "other",
            "options":
                {
                    "7": "lunch",
                    "8": "running errands",
                    "9": "something else",
                }
        }
    }
}

survey_admin ={
    "type": 'binary',
    "sent": {
        1: "Have you been doing ADMINISTRATIVE work in the last hour or so? (Y/N)"
    }
}

beta_test = {
    "type": "tree",
    "title": "beta_test",
    "prompt": "Which test question would you like to answer? ",
    "question": {
        "A": {
            "text": "Favorite color",
            "options":
                {
                    "1": "Red",
                    "2": "Blue",
                    "3": "Other"
                }
        },
        "B": {
            "text": "Favorite movie genre",
            "options":
                {
                    "4": "Horror",
                    "5": "Action",
                    "6": "Other"
                }
        },
        "C": {
            "text": "Favorite city",
            "options":
                {
                    "7": "Boston",
                    "8": "New York",
                    "9": "Other",
                }
        }
    }
}


ccc_clin = {
    "type": "tree",
    "title": "ccc_clin",
    "prompt": "Which type of work have you been doing? ",
    "question": {
        "A": {
            "text": "Administrative",
            "options":
                {
                    "1": "Research and medical record retrieval",
                    "2": "Auth and order placement",
                    "3": "Prescription or DME procurement",
                    "4": "Other"
                }
        },
        "B": {
            "text": "Clinical",
            "options":
                {
                    "5": "Assessments",
                    "6": "Care Plan Development",
                    "7": "Scheduled member check-ins",
                    "8": "Unscheduled member issues or emergencies",
                    "9": "Documenting member encounters",
                    "10": "Other"
                }
        },
        "C": {
            "text": "Travel",
            "options":
                {
                    "11": "To office",
                    "12": "To home",
                    "13": "To member",
                }
        }
    }
}

cg_care = {
    "type": "tree",
    "title": "cg_care",
    "prompt": "Which type of work have you been doing? ",
    "question": {
        "A": {
            "text": "Care_Delivery",
            "options":
                {
                    "1": "MDS assessment",
                    "2": "Scheduled visit",
                    "3": "Urgent visit",
                    "4": "Post hospital visit",
                    "5": "Reviewing documentation",
                    "6": "Writing documentation",
                    "7": "Picking up meds or dropping off labs"
                }
        },
        "B": {
            "text": "Care_Management",
            "options":
                {
                    "8": "Record requests",
                    "9": "Authorizations",
                    "10": "Calls to problem solve with family or care team",
                    "11": "Procurement of DME or services",
                    "12": "Care Coordination in person",
                }
        },
        "C": {
            "text": "Travel",
            "options":
                {
                    "13": "To office",
                    "14": "To home",
                    "15": "To member",
                }
        },
        "D": {
            "text": "Meetings",
            "options":
                {
                    "16": "Corporate or staff",
                    "17": "Educational",
                    "18": "Supervision",
                }

        }
    }
}

cg_central = {
    "type": "tree",
    "title": "cg_central",
    "prompt": "Which type of work have you been doing? ",
    "question": {
        "A": {
            "text": "Administrative",
            "options":
                {
                    "1": "Research",
                    "2": "Prescription or DME procurement",
                    "3": "Member documentation",
                    "4": "Authorizations",
                    "5": "LOA Process",
                    "6": "Other",
                }
        },
        "B": {
            "text": "Member-facing activities",
            "options":
                {
                    "7": "Education",
                    "8": "Assessments or examinations",
                    "9": "Care plan development",
                    "10": "Care coordination",
                    "11": "Member engagement",
                    "12": "Other"
                }
        },
        "C": {
            "text": "Travel",
            "options":
                {
                    "13": "To office",
                    "14": "To member",
                }
        }
    }
}

cg_west = {
    "type": "tree",
    "title": "cg_central",
    "prompt": "Which type of work have you been doing? ",
    "question": {
        "A": {
            "text": "Administrative",
            "options":
                {
                    "1": "Research",
                    "2": "Prescription or DME procurement",
                    "3": "Member documentation",
                    "4": "Authorizations",
                    "5": "LOA Process",
                    "6": "Other",
                }
        },
        "B": {
            "text": "Member care coordination",
            "options":
                {
                    "7": "Education",
                    "8": "Assessments or examinations",
                    "9": "Care plan development",
                    "10": "Care coordination",
                    "11": "Member engagement",
                    "12": "Other"
                }
        },
        "C": {
            "text": "Travel",
            "options":
                {
                    "13": "Confirm travel",
                }
        }
    }
}


cg_west3 = {
    "type": "tree",
    "title": "cg_central",
    "prompt": "Which type of work have you been doing? ",
    "question": {
        "A": {
            "text": "Administrative",
            "options":
                {
                    "1": "Research",
                    "2": "Procurement (DME, Rx)",
                    "3": "Authorizations",
                    "4": "LOA Process",
                    "5": "Other",
                }
        },
        "B": {
            "text": "Member care coordination",
            "options":
                {
                    "6": "Mbr education",
                    "7": "Direct care (TEL)",
                    "8": "Direct care (F2F)",
                    "9": "Care plan",
                    "10": "Care coordination",
                    "11": "Mbr engagement",
                    "12": "Documentation",
                    "13": "Other"
                }
        },
        "C": {
            "text": "Travel",
            "options":
                {
                    "14": "Confirm travel",
                }
        }
    }
}

surveys = dict()
surveys['test_survey'] = test_survey
surveys['test_survey_office'] = test_survey_office
surveys['admin'] = survey_admin
surveys['beta_test'] = beta_test
surveys['ccc_clin'] = ccc_clin
surveys['cg_care'] = cg_care
surveys['cg_central'] = cg_central
surveys['cg_west'] = cg_west
surveys['cg_west3'] = cg_west3
