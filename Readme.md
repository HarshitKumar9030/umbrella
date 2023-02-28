## Getting Started

### Prerequisites

To run this project, you'll need the following:

- Raspberry Pi with Raspbian OS installed
- Arduino board
- Rain sensor module
- Jumper wires
- USB cable
- Breadboard
- 3D-printed case (optional)

### Installing

1. Connect the rain sensor to the Arduino board using jumper wires.
2. Connect the Arduino board to the Raspberry Pi using a USB cable.
3. Download the Python script and the Arduino sketch from this repository.
4. Upload the Arduino sketch to the Arduino board.
5. Install the necessary Python libraries by running the following command in the terminal:

    ```python
    pip install Flask pyserial


### Usage 
1. Run the Python script by executing the following command in the terminal:

    ```python
    python3 app.py

2. Open a web browser and go to http://localhost:5000.
3. Click the "Start Rain Detection" button to start the rain detection process.
4. If rain is detected, the device will automatically cover the umbrella with a plastic bag


# Main Directory /ui_with_flask