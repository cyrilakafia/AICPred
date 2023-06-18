def faqs():
    faqs_list = [
        {'question': 'How does StormPred work? ', 'answer': 'StormPred uses machine learning models trained on experimentally-tested TLR4 inhibitors to predict the inhibitive capacity of small anti-inflammatory molecules against the TLR4 receptor.'},
        {'question': 'Is StormPred free to use?', 'answer': 'Yes. This web app is completely free.'},
        {'question': 'What kind of data do I need to provide to use StormPred?', 'answer': 'No personal data is collected. Users only need to provide data on the compound.'},
        {'question': 'Is StormPred for professionals only?', 'answer': 'No. Anyone can use this web app as long as they have their data.'},
        {'question': 'How accurate are the predictions made by StormPred?', 'answer': 'The XGBoost and Decision Tree models were able to predict all experimentally validated inhibitors of TLR4 as active with a confidence range of 0.72-1.00. This makes StormPred reliable.'},
        {'question': 'How can I provide feedback or report issues with StormPred?', 'answer': 'In case of any feedback or issues, please contact our support team at support@stormpred.com.'}
        # Add more FAQ objects as needed
    ]
    
    return faqs_list

    
def contacts():
    contacts_list = [
        {'title': 'Principle Investigator', 'name': 'Dr. Samuel Kojo Kwofie', 'email': 'skkwofie@ug.edu.gh'},
        {'title': 'Author', 'name': 'Lucindah Fry-Nartey', 'email': 'lfry-narter@st.ug.edu.gh'},
        {'title': 'Developer/Author', 'name': 'Cyril Selase K. Akafia', 'email': 'cskakafia@st.ug.edu.gh'},
        {'title': 'Author', 'name': 'Ursula Senam Nkonu', 'email': 'usnkonu@st.ug.edu.gh'}
    # Add more Contact objects as needed
    ]
    
    return contacts_list