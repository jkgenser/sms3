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

surveys = dict()
surveys['test_survey'] = test_survey
surveys['test_survey_office'] = test_survey_office
surveys['admin'] = survey_admin
surveys['beta_test'] = beta_test
surveys['ccc_clin'] = ccc_clin