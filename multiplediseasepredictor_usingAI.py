import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#landing page 

if 'landing_page' not in st.session_state:
    st.session_state.landing_page = True

if st.session_state.landing_page:
    with st.container():
        st.markdown('<div class="landing-container">', unsafe_allow_html=True)
        st.markdown("<h1>Welcome to the AI-Powered Medical Diagnosis System</h1>", unsafe_allow_html=True)
        st.markdown(
            "<p>Our advanced AI platform assists in diagnosing conditions such as Heart Disease, Diabetes, Alzheimers Disease, Liver Issues, Anemia, Kidney Stones, and Asthma.<br><br>"
            "<strong>Disclaimer:</strong> This tool is for informational purposes only and is not a substitute for professional medical advice.</p>",
            unsafe_allow_html=True
        )
        if st.button("Enter"):
            st.session_state.landing_page = False
            st.rerun()  # Use st.rerun() if you're on Streamlit >=1.18
        st.markdown('</div>', unsafe_allow_html=True)
    st.stop() 

#main app

#loading saved models

heart_model = pickle.load(open('heart_disease_model.sav', 'rb'))
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
alzheimer_model = pickle.load(open('alzheimer_model.sav', 'rb'))
liver_model = pickle.load(open('Liver_disease_model.sav', 'rb'))
anemia_model = pickle.load(open('Anemia_model.sav', 'rb'))
kidney_model = pickle.load(open('kidney_model.sav', 'rb'))
asthma_model = pickle.load(open('Asthma_model.sav', 'rb'))

#sidebar 

with st.sidebar:
    selected = option_menu(
        'AI-Powered Medical Diagnosis System',
        ['Heart Disease', 'Diabetes', 'Alzheimers Disease', 'Liver Function', 'Animea', 'Kidney Stone', 'Asthma'],
        icons=['activity', 'file-medical', 'capsule', 'prescription', 'clipboard2-pulse', 'file-earmark-medical', 'lungs'],
        default_index=0
    )

#heart disease 

if selected == 'Heart Disease':
    st.title('Heart Disease Predictor')
    
    #user inputs
    
    age = st.number_input('Age', min_value=0, value=0)
    sex = st.number_input('Gender (Male:1 Female:0)', min_value=0, value=0)
    cp = st.number_input('Chest Pain Type (Values:0,1,2,3)', min_value=0, value=0)
    trestbps = st.number_input('Resting Blood Pressure', min_value=0, value=0)
    chol = st.number_input('Serum Cholestoral in mg/dl', min_value=0, value=0)
    fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl', min_value=0, value=0)
    restecg = st.number_input('Resting Electrocardiographic Results (Values:0,1,2)', min_value=0, value=0)
    thalach = st.number_input('Maximum Heart Rate Achieved', min_value=0, value=0)
    exang = st.number_input('Exercise Induced Angina', min_value=0, value=0)
    oldpeak = st.number_input('ST Depression induced by exercise relative to rest', min_value=0.0, value=0.0)
    slope = st.number_input('Slope of the Peak Exercise ST Segment', min_value=0, value=0)
    ca = st.number_input('Number of Major Vessels colored by flourosopy (Range:0 to 3)', min_value=0, value=0)
    thal = st.number_input('Normal:0 Fixed Defect:1 Reversable Defect:2', min_value=0, value=0)
    
    #prediction
    
    heart_diag = ''
    if st.button('Heart Disease Test Result'):
        heart_pred = heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        if heart_pred[0] == 1:
            heart_diag = 'You may have a Heart Disease. We recommend consulting a Doctor soon.'
        else:
            heart_diag = 'You do not have any Heart Disease!'
    st.success(heart_diag)

#diabetes 

if selected == 'Diabetes':
    st.title('Diabetes Predictor')
    
    #user inputs
    
    Pregnancies = st.number_input('Number of Pregnancies', min_value=0, value=0)
    Glucose = st.number_input('Glucose Level', min_value=0, value=0)
    BloodPressure = st.number_input('Blood Pressure', min_value=0, value=0)
    SkinThickness = st.number_input('Skin Thickness Value', min_value=0, value=0)
    Insulin = st.number_input('Insulin Level', min_value=0, value=0)
    BMI = st.number_input('BMI Value', min_value=0.0, value=0.0)
    DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function Value', min_value=0.0, value=0.0)
    Age = st.number_input('Age', min_value=0, value=0)
    
    #prediction
    
    diab_diag = ''
    if st.button('Diabetes Test Result'):
        dia_pred = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        if dia_pred[0] == 1:
            diab_diag = 'You are Diabetic. We recommend consulting a Doctor soon.'
        else:
            diab_diag = 'You are not Diabetic!'
    st.success(diab_diag)


#alzheimer

if selected == 'Alzheimers Disease':
    st.title('Alzheimers Disease Predictor')
    
    #user inputs
    
    Age = st.number_input('Age', min_value=0, value=0)
    Gender = st.number_input('Gender (Male:1 Female:0)', min_value=0, value=0)
    BMI = st.number_input('BMI Value (Range:15 to 40)', min_value=0.0, value=0.0)
    Smoking = st.number_input('Smoking Status (No:0 Yes:1)', min_value=0, value=0)
    AlcoholConsumption = st.number_input(' weekly Alcohol Consumption (Range:0 to 20 hours)', min_value=0, value=0)
    PhysicalActivity = st.number_input('Weekly Physical Activity (Range:0 to 10 hours)', min_value=0.0, value=0.0)
    DietQuality = st.number_input('Diet Quality (Range:0 to 10)', min_value=0.0, value=0.0)
    SleepQuality = st.number_input('Sleep Quality (Range:4 to 10)', min_value=0.0, value=0.0)
    FamilyHistoryAlzheimers = st.number_input('Family history of Alzheimers Disease (No:0 Yes:1)', min_value=0, value=0)
    CardiovascularDisease = st.number_input('Cardiovascular Disease (No:0 Yes:1)', min_value=0, value=0)
    Diabetes = st.number_input('Diabetes (No:0 Yes:1)', min_value=0, value=0)
    Depression = st.number_input('Depression (No:0 Yes:1)', min_value=0, value=0)
    HeadInjury = st.number_input('Head Injury (No:0 Yes:1)', min_value=0, value=0)
    Hypertension = st.number_input('Hypertension (No:0 Yes:1)', min_value=0, value=0)
    SystolicBP = st.number_input('Systolic Blood Pressure (Range:90 to 180)', min_value=0, value=0)
    DiastolicBP = st.number_input('Diastolic Blood Pressure (Range:60 to 120)', min_value=0, value=0)
    CholesterolTotal = st.number_input('Total Cholesterol Levels (Range:150 to 300)', min_value=0.0, value=0.0)
    MMSE = st.number_input('Mini-Mental State Examination score (Range:0 to 30)', min_value=0.0, value=0.0)
    FunctionalAssessment = st.number_input('Functional assessment score (Range:0 to 10)', min_value=0, value=0)
    MemoryComplaints = st.number_input('Memory Complaints (No:0 Yes:1)', min_value=0, value=0)
    BehavioralProblems = st.number_input('Behavioral Problems (No:0 Yes:1)', min_value=0, value=0)
    ADL = st.number_input('Activities of Daily Living score (Range:0 to 10)', min_value=0.0, value=0.0)
    Confusion = st.number_input('Confusion (No:0 Yes:1)', min_value=0, value=0)
    Disorientation = st.number_input('Disorientation (No:0 Yes:1)', min_value=0, value=0)
    PersonalityChanges = st.number_input('Personality Changes (No:0 Yes:1)', min_value=0, value=0)
    DifficultyCompletingTasks = st.number_input('Difficulty Completing Tasks (No:0 Yes:1)', min_value=0, value=0)
    Forgetfulness = st.number_input('Forgetfulness (No:0 Yes:1)', min_value=0, value=0)
    
    #prediction
    
    alz_diag = ''
    if st.button('Alzheimers Disease Test Result'):
        alz_pred = alzheimer_model.predict([[Age, Gender, BMI, Smoking, AlcoholConsumption, PhysicalActivity, DietQuality, SleepQuality, FamilyHistoryAlzheimers, CardiovascularDisease, Diabetes, Depression, HeadInjury, Hypertension, SystolicBP, DiastolicBP, CholesterolTotal, MMSE, FunctionalAssessment, MemoryComplaints, BehavioralProblems, ADL, Confusion, Disorientation, PersonalityChanges, DifficultyCompletingTasks, Forgetfulness]])
        if alz_pred[0] == 1:
            alz_diag = 'You have Alzheimers. We recommend you visiting a Doctor soon.'
        else:
            alz_diag = 'You do not have Alzheimers!'
    st.success(alz_diag)


#liver function

if selected == 'Liver Function':
    st.title('Liver Function Predictor')
    
    #user inputs
    
    Age = st.number_input('Age', min_value=0, value=0)
    Gender = st.number_input('Gender (Male:1 Female:0)', min_value=0, value=0)
    BMI = st.number_input('BMI Value', min_value=0.0, value=0.0)
    AlcoholConsumption = st.number_input('Alcohol Consumption (Range: 0 to 20 units per week)', min_value=0.0, value=0.0)
    Smoking = st.number_input('Smoking (No:0 Yes:1)', min_value=0, value=0)
    GeneticRisk = st.number_input('Genetic Risk (Low:0 Medium:1 High:2)', min_value=0, value=0)
    PhysicalActivity = st.number_input('Physical Activity (Range: 0 to 10 hours per week)', min_value=0.0, value=0.0)
    Diabetes = st.number_input('Diabetes (No:0 Yes:1)', min_value=0, value=0)
    Hypertension = st.number_input('Hypertension (No:0 Yes:1)', min_value=0, value=0)
    LiverFunctionTest = st.number_input('Liver Function Test (Range: 20 to 100)', min_value=0.0, value=0.0)
    
    #prediction
    
    liv_diag = ''
    if st.button('Liver Function Result'):
        liv_pred = liver_model.predict([[Age, Gender, BMI, AlcoholConsumption, Smoking, GeneticRisk, PhysicalActivity, Diabetes, Hypertension, LiverFunctionTest]])
        if liv_pred[0] == 1:
            liv_diag = 'You have Liver problem(s). We recommend consulting a Doctor soon.'
        else:
            liv_diag = 'You do not have Liver problems!'
    st.success(liv_diag)


#animea 

if selected == 'Animea':
    st.title('Animea Predictor')
    
    #user inputs
    
    Gender = st.number_input('Gender (Male:1 Female:0)', min_value=0, value=0)
    Hemoglobin = st.number_input('Hemoglobin Level', min_value=0.0, value=0.0)
    MCH = st.number_input('Mean Corpuscular Hemoglobin', min_value=0.0, value=0.0)
    MCHC = st.number_input('Mean Corpuscular Hemoglobin Concentration', min_value=0.0, value=0.0)
    MCV = st.number_input('Mean Corpuscular Volume', min_value=0.0, value=0.0)
    
    #prediction    
    
    anim_diag = ''
    if st.button('Animea Test Result'):
        anim_pred = anemia_model.predict([[Gender, Hemoglobin, MCH, MCHC, MCV]])
        if anim_pred[0] == 1:
            anim_diag = 'You show signs of Animea. We recommend consulting a Doctor soon.'
        else:
            anim_diag = 'You do not have Animea!'
    st.success(anim_diag)


#kidney stone 

if selected == 'Kidney Stone':
    st.title('Kidney Stone Predictor')
    
    #user inputs
    
    gravity = st.number_input('Specific Gravity of urine', min_value=0.0, value=0.0)
    ph = st.number_input('pH of urine', min_value=0.0, value=0.0)
    osmo = st.number_input('Osmolarity of urine', min_value=0, value=0)
    cond = st.number_input('Conductivity of urine', min_value=0.0, value=0.0)
    urea = st.number_input('Concentration of Urea in urine', min_value=0, value=0)
    calc = st.number_input('Concentration of Calcium in urine', min_value=0.0, value=0.0)
    
    #prediction
    
    kidst_diag = ''
    if st.button('Kidney Stone Test Result'):
        # Note: Replace the prediction input with the correct features for kidney_model
        kidst_pred = kidney_model.predict([[gravity, ph, osmo, cond, urea, calc]])
        if kidst_pred[0] == 1:
            kidst_diag = 'You have Kidney Stone(s). We recommend consulting a Doctor soon.'
        else:
            kidst_diag = 'You do not have Kidney Stone!'
    st.success(kidst_diag)


#asthma 

if selected == 'Asthma':
    st.title('Asthma Predictor')
    
    #user inputs
    
    Age = st.number_input('Age', min_value=0, value=0)
    Gender = st.number_input('Gender (Male:1 Female:0)', min_value=0, value=0)
    BMI = st.number_input('BMI Value (Range:15 to 40)', min_value=0.0, value=0.0)
    Smoking = st.number_input('Smoking Status (No:0 Yes:1)', min_value=0, value=0)
    PhysicalActivity = st.number_input('Weekly Physical Activity (Range:0 to 10 hours)', min_value=0.0, value=0.0)
    DietQuality = st.number_input('Diet Quality (Range:0 to 10)', min_value=0.0, value=0.0)
    SleepQuality = st.number_input('Sleep Quality (Range:0 to 10)', min_value=0.0, value=0.0)
    PollutionExposure = st.number_input('Pollution Exposure (No:0 Yes:1)', min_value=0, value=0)
    PollenExposure = st.number_input('Pollen Exposure (No:0 Yes:1)', min_value=0, value=0)
    DustExposure = st.number_input('Dust Exposure (No:0 Yes:1)', min_value=0, value=0)
    PetAllergy = st.number_input('Pet Allergy (No:0 Yes:1)', min_value=0, value=0)
    FamilyHistoryAsthma = st.number_input('Family History of Asthma (No:0 Yes:1)', min_value=0, value=0)
    HistoryOfAllergies = st.number_input('History of Allergies (No:0 Yes:1)', min_value=0, value=0)
    LungFunctionFEV1 = st.number_input('Forced Expiratory Volume in 1 second (FEV1) (Range:1.0 to 4.0 liters)', min_value=0.0, value=0.0)
    LungFunctionFVC = st.number_input('Forced Vital Capacity (FVC) (Range:1.5 to 6.0 liters)', min_value=0.0, value=0.0)
    Eczema = st.number_input('Eczema (No:0 Yes:1)', min_value=0, value=0)
    HayFever = st.number_input('Hay Fever (No:0 Yes:1)', min_value=0, value=0)
    GastroesophagealReflux = st.number_input('Gastroesophageal Reflux (No:0 Yes:1)', min_value=0, value=0)
    Wheezing = st.number_input('Wheezing (No:0 Yes:1)', min_value=0, value=0)
    ShortnessOfBreath = st.number_input('Shortness of Breath (No:0 Yes:1)', min_value=0, value=0)
    ChestTightness = st.number_input('Chest Tightness (No:0 Yes:1)', min_value=0, value=0)
    Coughing = st.number_input('Coughing (No:0 Yes:1)', min_value=0, value=0)
    NighttimeSymptoms = st.number_input('Nighttime Symptoms (No:0 Yes:1)', min_value=0, value=0)
    ExerciseInduced = st.number_input('Symptoms Induced by Exercise (No:0 Yes:1)', min_value=0, value=0)
    
    #prediction
    
    ast_diag = ''
    if st.button('Asthma Test Result'):
        ast_pred = asthma_model.predict([[Age, Gender, BMI, Smoking, PhysicalActivity, DietQuality, SleepQuality, PollutionExposure, PollenExposure, DustExposure, PetAllergy, FamilyHistoryAsthma, HistoryOfAllergies, Eczema, HayFever, GastroesophagealReflux, LungFunctionFEV1, LungFunctionFVC, Wheezing, ShortnessOfBreath, ChestTightness, Coughing, NighttimeSymptoms, ExerciseInduced]])
        if ast_pred[0] == 1:
            ast_diag = 'You show signs of Asthma. We recommend consulting a Doctor soon.'
        else:
            ast_diag = 'You do not have Asthma!'
    st.success(ast_diag)
