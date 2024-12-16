from crewai import Task


def  SymptomAnalyzer_task(agent):
    return Task(
            description=(
                "analyze the user's symptoms, both historical and real-time. "
                "Identify patterns and correlations between symptoms and potential triggers. "
                "Provide a detailed health status report to inform further decision-making."
                "User Details from doctor inputs: "
                "Weigh in KG: {weight}, BMI: {BMI}, Ulcer-Based or Chronic-Based Inflamatory Bowl Syndrome: {based}, Patients Hemoglobin level (g/dL): {hemoglobin}, Albumin-Level: {albumin}, CDAI(Crohn's disease Activity Index): {CDAI}, CRP level (mg/L): {CRP}, Stress-Level out of 10: {stress_level}, Where the patient is working: {working}, Patient\'s Role at workplace: {role}, Patient's Gender: {gender}, diet-preference: {veg}, food allergies and other issues: {allegies_and_issues}"
            ),
            expected_output = (
                "A document clearly explaining aspects given in the description."
            ),
            agent = agent,
            allow_delegation=False,
            async_execution=False # Will be executed asynchronously
            )


def DietPreferenceInterpreter_task(agent):
    return Task(
            description=(
                "Analyze user input related to dietary preferences, restrictions, and additional health conditions like diabetes. "
                "Compile a profile of acceptable foods, forbidden items, and special nutritional needs. "
                "Ensure that all dietary recommendations align with these constraints. "
                "User Details from doctor inputs: "
                "Weigh in KG: {weight}, BMI: {BMI}, Ulcer-Based or Chronic-Based Inflamatory Bowl Syndrome: {based}, Patients Hemoglobin level (g/dL): {hemoglobin}, Albumin-Level: {albumin}, CDAI(Crohn's disease Activity Index): {CDAI}, CRP level (mg/L): {CRP}, Stress-Level out of 10: {stress_level}, Where the patient is working: {working}, Patient\'s Role at workplace: {role}, Patient's Gender: {gender}, diet-preference: {veg}, food allergies and other issues: {allegies_and_issues}"
            ),
            expected_output = (
                "A document clearly explaining aspects given in the description."
            ),
            agent = agent,
            allow_delegation=False,
            async_execution=False # Will be executed asynchronously
            )


def DietPlanAdvisor_task(agent):
    return Task(
            description=(
                "Combine data from SymptomAnalyzer and DietPreferenceInterpreter."
                "Create a weekly diet plan that considers the user's symptoms, dietary needs, and regional availability of foods."
                "Suggest local alternatives when certain foods are not available or feasible in the user's region."

                "User Details from doctor inputs: "
                "Weigh in KG: {weight}, BMI: {BMI}, Ulcer-Based or Chronic-Based Inflamatory Bowl Syndrome: {based}, Patients Hemoglobin level (g/dL): {hemoglobin}, Albumin-Level: {albumin}, CDAI(Crohn's disease Activity Index): {CDAI}, CRP level (mg/L): {CRP}, Stress-Level out of 10: {stress_level}, Where the patient is working: {working}, Patient\'s Role at workplace: {role}, Patient's Gender: {gender}, diet-preference: {veg}, food allergies and other issues: {allegies_and_issues}"
            ),
            expected_output = (
                "A document clearly explaining aspects given in the description."
            ),
            agent = agent,
            allow_delegation=False,
            async_execution=False # Will be executed asynchronously
            )



def ReportWriter_task(agent):
    return Task(
            description=(
                "Gather all data, analyses, and the diet plan from the other agents."
                "Write a comprehensive report that includes an overview of the user's health status, dietary recommendations, and actionable steps."
                "Ensure the report is well-structured, clear, and tailored to the user's understanding."

                "User Details from doctor inputs: "
                "Weigh in KG: {weight}, BMI: {BMI}, Ulcer-Based or Chronic-Based Inflamatory Bowl Syndrome: {based}, Patients Hemoglobin level (g/dL): {hemoglobin}, Albumin-Level: {albumin}, CDAI(Crohn's disease Activity Index): {CDAI}, CRP level (mg/L): {CRP}, Stress-Level out of 10: {stress_level}, Where the patient is working: {working}, Patient\'s Role at workplace: {role}, Patient's Gender: {gender}, diet-preference: {veg}, food allergies and other issues: {allegies_and_issues}"
            ),
            expected_output = (
                "A document clearly explaining aspects given in the description."
            ),
            agent = agent,
            allow_delegation=False,
            async_execution=False # Will be executed asynchronously
            )


def QualityAssurer_task(agent):
    return Task(
            description=(
                "Review the report generated by ReportWriter for accuracy, clarity, and completeness. "
                "Correct any errors or inconsistencies. "
                "Finalize the report and ensure it meets the required standards before it is shared with the user."

                "User Details from doctor inputs: "
                "Weigh in KG: {weight}, BMI: {BMI}, Ulcer-Based or Chronic-Based Inflamatory Bowl Syndrome: {based}, Patients Hemoglobin level (g/dL): {hemoglobin}, Albumin-Level: {albumin}, CDAI(Crohn's disease Activity Index): {CDAI}, CRP level (mg/L): {CRP}, Stress-Level out of 10: {stress_level}, Where the patient is working: {working}, Patient\'s Role at workplace: {role}, Patient's Gender: {gender}, diet-preference: {veg}, food allergies and other issues: {allegies_and_issues}"
            ),
            expected_output = (
                "A document clearly explaining aspects given in the description."
            ),
            agent = agent,
            allow_delegation=False,
            async_execution=False # Will be executed asynchronously
            )