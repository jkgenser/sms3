test_survey = {
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

surveys = dict()
surveys['test_survey'] = test_survey
surveys['test_survey_office'] = test_survey_office