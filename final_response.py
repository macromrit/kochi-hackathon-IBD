from gpt_calling import chain
from rag_call import getUnBiasedResponses
from kochi_main import get_content

def get_response(
        weight,
        BMI,
        based,
        hemoglobin,
        albumin,
        CDAI,
        CRP,
        stress_level,
        working,
        role,
        gender,
        veg,
        allegies_and_issues,
        state
    ):

    user_details = F"Weigh in KG: {weight}, BMI: {BMI}, Ulcer-Based or Chronic-Based Inflamatory Bowl Syndrome: {based}, Patients Hemoglobin level (g/dL): {hemoglobin}, Albumin-Level: {albumin}, CDAI(Crohn's disease Activity Index): {CDAI}, CRP level (mg/L): {CRP}, Stress-Level out of 10: {stress_level}, Where the patient is working: {working}, Patient\'s Role at workplace: {role}, Patient's Gender: {gender}, diet-preference: {veg}, food allergies and other issues: {allegies_and_issues}, state={state}"

    context =  getUnBiasedResponses(user_details)

    scrape_graph_data = ""# str(get_content("Inflamatory Bowel Disease, Causes, Cures, Diets"))

    return chain.invoke({"user_details": user_details, "context": context, "search": scrape_graph_data})



if __name__ == "__main__":
    with open("response.txt", 'w') as ajmmer:
        """
             weight,
        BMI,
        based,
        hemoglobin,
        albumin,
        CDAI,
        CRP,
        stress_level,
        working,
        role,
        gender,
        veg,
        allegies_and_issues,
        state
        
        """
        
        print(
            get_response(
            weight="68 kg",
            BMI="24.5",
            based="12.5",
            hemoglobin="12.5 g/dL",
            albumin="3.8 g/d",
            CDAI=" 150",
            CRP="10 mg/L",
            stress_level="7",
            working="Google",
            role="Software-Engineer",
            gender="Male",
            veg="Veg",
            allegies_and_issues="diabetic and allegic to peanuts",
            state="Kerala",
        ), file=ajmmer)