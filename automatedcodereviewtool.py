import subprocess

def run_code_analysis(file_path):
    subprocess.run(['pylint', file_path]) 
    subprocess.run(['flake8', file_path]) 

if __name__ == "__main__":
    file_to_review = 'problem3.py' 
    run_code_analysis(file_to_review)
