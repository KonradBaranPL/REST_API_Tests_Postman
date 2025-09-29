import subprocess

# Definicja komendy do uruchomienia
command = "newman.cmd run trello_requests_collection.json -e trello_environment.json --reporters cli,html --reporter-html-export reports\trello_api_test_report.html"

# Uruchomienie komendy
result = subprocess.run(command.split(), capture_output=True, encoding="utf-8")

# Wyświetlenie wyników
print("STDOUT:", result.stdout)
print("STDERR:", result.stderr)

if result.returncode == 0:
    print("Testy API zakończone sukcesem!")
else:
    print(f"Testy API zakończone z błędem! Kod wyjścia: {result.returncode}")
