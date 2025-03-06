# GenAI_Receipe_Generator

## Description
The Receipe Generator is a web application that uses artificial intelligence to create receipes based on specific ingredients. By leveraging OpenAI's GPT model, this tool helps you with quick ideas on creating new dishes. 

## Features
- Input fields with ingredients in your refrigerator.
- AI-powered receipe generating using OpenAI's GPT model
- Responsive web interface
- Copy-to-clipboard functionality for easy export of tailored resumes

## Technologies Used
- **Programming Language**: Python 3.7+
- **Web Framework**: Flask
- **AI Model**: OpenAI GPT-3.5-turbo
- **Frontend**: HTML, CSS (Bootstrap 5), JavaScript

## Libraries and Dependencies
- Flask: Web framework for Python
- OpenAI: Python client for the OpenAI API
- Bootstrap 5: CSS framework for responsive design

## Installation and Setup

1. Clone the repository:
   ```
   git clone https://github.com/your-username/GenAI_Receipe_Generator.git
   cd resume-tailoring-expert
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install flask openai
   ```

4. Create a `config.py` file in the project root directory and add your OpenAI API key:
   ```python
   OPENAI_API_KEY = "your-openai-api-key-here"
   ```

## Usage

1. Run the application:
   ```
   python receipe_generator.py
   ```

2. Open a web browser and navigate to `http://127.0.0.1:8080`

3. Enter the following information in the form:
   - Available Raw ingredients

4. Click the "Generate Receipe" button to generate a customized receipe


## Configuration

You can modify the following parameters in the `app.py` file:

- `host`: The IP address on which the server runs (default: '127.0.0.1')
- `port`: The port number (default: 8080)
- `debug`: Debug mode for development (default: True)

## Contributing

Contributions to improve the Resume Tailoring Expert are welcome. Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- OpenAI for providing the GPT model API
- Flask team for the excellent web framework
- Bootstrap team for the responsive design framework

## Disclaimer

This tool is designed to assist in tailoring resumes but should not be considered a replacement for human judgment. Always review and verify the AI-generated content before using it in your job applications.
