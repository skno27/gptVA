# Just starting!

Currently I am just hammering out the vocal recognition functionality
It works, but there are some strange errors that I'm not expecting to get.

To test check this out:

### Installation Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/skno27/gptVA.git
   cd your-repo-name
   ```

2. Set up a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```
   - **Windows (Command Prompt)**:
     ```cmd
     venv\Scripts\activate
     ```
   - **Windows (PowerShell)**:
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. Test the vocal recognition:

   I open two terminal instances and navigate to the project root. In the first instance, i run the following command:

   ```bash
   python test.py
   ```

   and then run the following command in the second instance:

   ```bash
   tail -f output.txt
   ```

   speak into your computers microphone, and the running tail on output.txt will read the output file into the terminal as the vocal recognizer writes to the output file.
