import os
import io
print(1)
from pathlib import Path
from ultralytics import YOLO
print(2)
from PIL import Image
print(3)
from treys import Card
from treys import Evaluator
print(4)
import streamlit as st
print(5)


############################################################
# CONFIG
############################################################
UPLOAD_FOLDER   = './uploads'
MODEL_FP        = './models/pokermate_stage2_yolo8.pt'
############################################################

# Create a folder to store uploaded images
if not os.path.exists(UPLOAD_FOLDER): os.makedirs(UPLOAD_FOLDER)

def display_sidebar():
    st.sidebar.write("")
    st.sidebar.title("Poker Hand Detector")
    st.sidebar.markdown("---")
    st.sidebar.header("How to Use:")
    st.sidebar.markdown(
        "1. Upload an image of a poker hand.\n"
        "2. Click the 'Detect Poker Hand' button to analyze the image.\n"
        "3. Results will be displayed in the main area."
    )

    st.sidebar.write("")
    st.sidebar.write(""" <h3>File Format Supported:</h3>
                        <span class="tags">.jpg</span> 
                        <span class="tags">.jpeg</span> 
                        <span class="tags">.png</span>""", unsafe_allow_html=True)
    #api_auth()
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.markdown("---")
    st.sidebar.write("""
        Built by © Pranjal

        #### Github: https://github.com/pranzell
        #### Website: https://pranzell.github.io/
        """)
    return

def display_header():
    st.markdown(
        """
            <div/>
            <style>
                div[data-testid="stVerticalBlock"] div:has(div.fixed-header) {
                    position: sticky;
                    top: 2.875rem;
                    background-color: white;
                    z-index: 999;
                }
            </style>
        """,
        unsafe_allow_html=True
    )

def detect_poker_hand(input_img_fp):
    # Model prediction
    results = model(input_img_fp)
    y_hat = []
    for r in results:
        try:
            # GPU VERSION
            labels = set(np.array(r.boxes.cls).astype(int))
        except Exception as e:
            # CPU VERSION
            labels = set(np.array(r.boxes.cls.cpu()).astype(int))
        class_labels = [model.names.get(x) for x in labels]
        y_hat += class_labels
        im_array = r.plot()  # plot a BGR numpy array of predictions
        im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
        # Save the detected image
        output_fp = UPLOAD_FOLDER + "/detected.jpg"
        im.save(output_fp)
    return y_hat, output_fp

def calculate_best_hand(cards):
    try:
        trey_cards = []
        for card in cards:
            if "10" in card:
                rank = "T"
                suite = card[2]
            else:
                rank = card[0]
                suite = card[1]
            trey_cards.append(f"{rank}{suite.lower()}")

        board = []
        hand = []
        for card in trey_cards:
            board.append(Card.new(card))

        # Evaluate poker hand
        evaluator = Evaluator()
        deck_score = evaluator.evaluate(board, hand)
        deck_class = evaluator.get_rank_class(deck_score)
        return evaluator.class_to_string(deck_class)
    except Exception as e:
        return "Unknown"

def main():
    st.set_page_config(layout="wide", page_title="PokerMate", page_icon="❄:spades:")
    
    ## Sidebar
    display_sidebar()

    ## Header
    with st.container():
        st.title(":spades:  PokerMate  :spades:")
        st.subheader("Your smart poker assistant")
        #st.image("./public/img/logo.png", width=200, )
        display_header()

    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        st.image(uploaded_file, caption="Your Image", width=600)

        if st.button("Detect Poker Hand"):
            with st.spinner("Running neural networks..."):
                time.sleep(2)

                # Save the received image file
                file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
                with open(file_path, "wb") as f: 
                  f.write(uploaded_file.getbuffer())    

                # Run the poker hand detection model
                cards, output_fp = detect_poker_hand(file_path)

                # Calculate the best poker hand rank
                best_hand_rank = calculate_best_hand(cards)

                st.subheader("Detected Cards:")
                st.write(cards)
                st.subheader("Best Poker Hand Possible for you")
                st.write(best_hand_rank)
                st.sidebar.write(" ")
                st.sidebar.write(" ")
                st.sidebar.write(" ")

                col1, col2 = st.columns(2)
                with col1:
                    st.subheader("Original Image")
                    st.image(file_path, width=400)
                with col2:
                    st.subheader("Detected Image")
                    st.image("./uploads/detected.jpg", width=400)

if __name__ == "__main__":
    print("Starting PokerMate V1...\n\n")
    # Loading fine-tuned model
    model = YOLO(MODEL_FP)
    main()

# EOF