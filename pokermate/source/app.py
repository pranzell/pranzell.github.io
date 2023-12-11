import os
import pandas as pd
import numpy as np
from PIL import Image, ImageDraw
from IPython.display import Image as ImageDisplay
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
from pathlib import Path
from ultralytics import YOLO
from flask import Flask, render_template, request, jsonify
from PIL import Image
import io
import numpy as np
from treys import Card
from treys import Evaluator


############################################################
#  CONFIG
############################################################
UPLOAD_FOLDER     = './uploads'
MODEL_FP          = './models/pokermate_stage2_yolo8.pt'
############################################################


app = Flask(__name__)


# Create a folder to store uploaded images
if not os.path.exists(UPLOAD_FOLDER): os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


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
        y_hat+=class_labels
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
        #print("Hand rank = %d (%s)" % (deck_score, evaluator.class_to_string(deck_class)))
        return evaluator.class_to_string(deck_class)
    except Exception as e:
        return "Unknown"


@app.route('/', methods=['POST'])
def index():
    # Get the uploaded image file
    file = request.files['file']
    if file:
        
        # Save the received image file
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        # Run the poker hand detection model
        cards, output_fp = detect_poker_hand(file_path)

        # Calculate the best poker hand rank
        best_hand_rank = calculate_best_hand(cards)

        return jsonify({'success':          True, 
                        'labels':           cards, 
                        'best_hand_rank':   best_hand_rank, 
                        'image_path':       file_path,
                        'output_fp':        output_fp})


###################################################
# START
###################################################
if __name__ == '__main__':
    print("Starting PokerMate V1...\n\n")
    
    # Loading fine-tuned model
    model = YOLO(MODEL_FP)
    
    ## FLASK-SERVER
    app.run(debug=False)

# EOF