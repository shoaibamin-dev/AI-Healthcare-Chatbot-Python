# Healthcare Chatbot System README

## Overview
This is an AI-powered chatbot system designed for healthcare purposes. The chatbot aims to assist users in identifying potential health issues based on the symptoms they describe. The system focuses on one specific health concern, fever, for demonstration purposes, but it can be extended to cover a broader range of diseases and symptoms.

## Features
1. **Disease Database:** The chatbot maintains a database (`diseases`) containing symptoms associated with fever. The `diseases_prediction` dictionary keeps track of the symptoms mentioned by the user during the conversation.

2. **Dynamic Questioning:** The chatbot dynamically generates questions to inquire about the user's symptoms. It uses both general and specific questions based on the user's responses to gather relevant information.

3. **User Interaction:** The chatbot communicates with the user through a graphical user interface (GUI) implemented using Tkinter. Users can input their symptoms, and the chatbot responds with relevant questions and information.

4. **Scrollable Chat History:** The chat history is displayed in a scrollable interface, allowing users to view previous interactions with the chatbot.

5. **Prediction and Recommendations:** Once a sufficient amount of information is gathered, the chatbot provides a preliminary prediction of the potential disease (fever) and offers a recommendation, suggesting that the user consult a general physician.

## Usage
1. **Initialization:** The chatbot begins the conversation by asking the user about their symptoms and prompts them to share more details.

2. **User Input:** Users can type their symptoms into the text input area and press the "Send" button or hit the "Enter" key.

3. **Dynamic Responses:** The chatbot dynamically responds to user input by generating relevant questions or providing general information.

4. **Prediction:** After a certain number of interactions (`global_question_counter`), the chatbot makes a preliminary prediction about the potential disease (fever) based on the symptoms mentioned.

5. **Recommendation:** The chatbot suggests consulting a general physician if the predicted disease probability is above a certain threshold.

## Dependencies
The system utilizes the following Python libraries:

- **Random:** For generating random questions and selecting random elements.
- **Tkinter:** For creating the graphical user interface.
- **Emoji (commented out):** Potential inclusion for emoji support in the future.

## How to Run
To run the chatbot system, execute the Python script. The graphical interface will appear, allowing users to interact with the chatbot.

```bash
python healthcare_chatbot.py
```
## License
This project is licensed under the MIT License.
