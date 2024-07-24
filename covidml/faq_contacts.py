def faqs():
    faqs_list = [
        {'question': 'How does AICPred work? ', 'answer': 'AICPred uses machine learning models trained on experimentally-tested TLR4 inhibitors to predict the inhibitive capacity of small anti-inflammatory molecules against the TLR4 receptor.'},
        {'question': 'Is AICPred free to use?', 'answer': 'Yes. This web app is completely free.'},
        {'question': 'What kind of data do I need to provide to use AICPred?', 'answer': 'No personal data is collected. Users only need to provide data on the compound.'},
        {'question': 'Is AICPred for professionals only?', 'answer': 'No. Anyone can use this web app as long as they have their data.'},
        {'question': 'How accurate are the predictions made by AICPred?', 'answer': 'The XGBoost and Decision Tree models were able to predict all experimentally validated inhibitors of TLR4 as active with a confidence range of 0.83-1.00. This makes AICPred reliable.'},
        {'question': 'How can I provide feedback or report issues with AICPred?', 'answer': 'In case of any feedback or issues, please contact our support team at kwakucyril@gmail.com'}
        # Add more FAQ objects as needed
    ]
    
    return faqs_list

    
def contacts():
    contacts_list = [
        {'title': 'Principal Investigator', 'name': 'Dr. Samuel Kojo Kwofie', 'email': 'skkwofie@ug.edu.gh'},
        {'title': 'First Author', 'name': 'Lucindah Fry-Nartey', 'email': 'lfry-narter@st.ug.edu.gh'},
        {'title': 'Developer | Co-author', 'name': 'Cyril Selase K. Akafia', 'email': 'cskakafia@st.ug.edu.gh'},
        {'title': 'Co-author', 'name': 'Ursula Senam Nkonu', 'email': 'usnkonu@st.ug.edu.gh'}
    # Add more Contact objects as needed
    ]
    
    return contacts_list