from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core .output_parsers import StrOutputParser

from rag_call import getUnBiasedResponses

from dotenv import load_dotenv
import os

# loading the environment variables into the code from env
load_dotenv()

os.environ["OPENAI_API_KEY"] = "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"
## LangSmith Tracking
# os.environ["LANGCHAIN_TRACING_V2"] = "true"
# os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")


## prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", """
As a medical analyst, your task is to create a comprehensive diet plan to manage and control Inflammatory Bowel Disease (IBD) tailored to the user's specific circumstances. Begin by gathering detailed information about the user, including their current location and nationality, age, gender, and any health conditions related to IBD. Consider their dietary preferences and restrictions, activity level, and current eating habits. Additionally, account for local food availability, regional dietary practices, and cultural preferences. Integrate relevant data from Retrieval-Augmented Generation (RAG) systems, focusing on IBD-friendly foods and diet trends. Utilize recent insights from search engines about popular foods and nutritional guidelines for IBD. Construct a personalized diet plan that aligns with the user's environment and health needs, ensuring it incorporates accessible local foods, addresses dietary restrictions, and promotes digestive health. Provide specific meal suggestions, portion sizes, and practical advice for meal integration, while also highlighting foods to avoid. Summarize the plan with key recommendations and include guidance for ongoing monitoring and adjustments based on the user's response.
The Final Response should be a latex Code only
         
a Tabular based dietary plan in latex is expected
         
A reports content:
         Crohn's
Time
Menu
Quantity
Early Morning
Tender coconut water
1 glass
Breakfast
Idiyappam
Egg white curry
2nos
2nos
Mid-morning
Lassi
1 glass
Lunch
Parboiled rice
Anchovies curry (less seasoning)
Snake gourd thoran
2 cups
1 serv
½ cup
Time time
Chicken soup
1 cup
Dinner
Wheat dosa
Dal curry
Carrot thoran
2-3 nos
1 cup
½ cup
Bed time
Soaked peeled almonds
4 nos
 
 
To note:
• Keeping a record of foods eaten and then taking note of when symptoms worsen may help you identify patterns that indicate problem foods.
• It will take time and experimentation to figure out which foods you can tolerate and which you should avoid
• Eat small and more frequent meals.
• Avoid fatty and fried foods meat, spicy food, diary and fibre rich foods because they often trigger symptoms of blotting ,diarrhoea", abdominal pain and cramping.
• Do not skip meals.
• Many people with IBD have difficulty tolerating diary products because of. intolerance to milk (lactose intolerance), so it is better to avoid milk and milk products except curd.
• Curd can provide you with probiotics it helps to maintain gut healthy and it will reduce the symptom of IBD as it has anti inflammatory property.
• Avoid gluten containing food such as wheat, ragi etc
• Malnutrition is a major complication of IBD due to poor digestion, recurrent and severe diarrhoea, malabsorption, loss of appetite and unintentional weight loss.
• In order to and prevent and treat malnutrition a high calorie high protein diet should be followed.
• Protein will reduce inflammation and prevent weight loss. sources-egg white, lean meat, small fishes, pulses, nut etc.
• Hydration is also important in this condition.
• A low fibre diet should be followed High fibre content may trigger the condition sources-Plain cereals white rice: ,fully cooked and skinless vegetables, juices(diluted) and soups instead of whole fruits and vegetables.
• Unhealthy fats increases symptoms so fried food, reheated oil, junk food ,bakery item etc should be avoided but healthy fats like MCT oils and omega 3 fatty acids PUFA can be taken moderately. sources-Coconut oil, sunflower oil, olive oil, small fishes like anchovies sardine, mackerel, tuna, almond walnuts etc.
 
Food to be included
• All cereals without husk/sieved to cut down on insoluble fibre and to be taken in a soft cooked gruel form.
• Sugar/Jaggery less than 2 teaspoon per day. Blend of oil, Rice bran, groundnut, ghee, butter based on tolerance.
• Lactose free skimmed milk, Low fat curd,, Buttermilk
• Soya milk, Tofu are based on tolerance.
• Well cooked and lean cuts of chicken Boiled egg white based on tolerance
• Peeled and well cooked fruits and vegetables, strained fruits and vegetable juices/Soups.
• Preferable soft cooked apple without skin and banana
• Tender coconut water.
 
Foods to be avoided
• Whole grains
• Skinned and raw fruits and vegetables, sprouted vegetables and leafy vegetables.
• Sweet juices ,sweetened beverages, carbonated beverages proprietary drinks sugar or high fructose corn syrup.
• Safflower ,sunflower, rapeseed, cottonseed oil.
• Oily and fried foods.
• Margarine, vanaspati, bakery, processed foods:
• Alcohol.
• Beans ,corn and corn products ,peas, sprouted beans and legumes in symptoms with IBD
• Raw milk, cream,sour cream ,fried and processed meat like sausages ,bacons etc chewy cuts of meats, fried eggs

Output should be in tables and latex format
make the dietary plan for 7 days
"""),
        ("user", "user_detials:{user_details}, context: {context}, relevant_queries; {search}")
    ]
)



# OpenAI LLM
llm = ChatOpenAI(model="gpt-4o")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# print(chain.invoke({'question': "Hello"}))