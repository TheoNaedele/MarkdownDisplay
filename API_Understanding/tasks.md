# Aufgabe 1: Einfache GET-Anfragen stellen

Beschreibung: Verwenden der requests-Bibliothek von Python, um GET-Anfragen an den Endpunkt /getToken des FastAPI-Servers zu senden.
Ziel: 
* Verständnis für die Grundfunktionalitäten der requests Bibliothek in python aufbauen.
* Einfache get requests können an den Server übermittelt werden.
* Erhalten des authentifizierungstokens für folgende Aufgaben.


# Aufgabe 2: Behandeln von Antwortdaten

Beschreibung: Extrahiere den Authentifizierungstoken aus der Antwort, welche in Aufgabe 1 erhalten wurde.
Schritte:
Ziel: 
* Daten einer Response können extrahiert und ausgewertet werden.


# Aufgabe 3: Senden von Daten mit POST-Anfragen

Beschreibung: Erstellen einer JSON-Payload auf basis der API Beschreibung und senden dieser als Teil einer POST-Anfrage an den Endpunkt /postData des FastAPI-Servers.
Ziel:
* Payload beschreibungen in API Dokumentation kann gelesen/verstanden werden
* Payload kann als JSON Objekt in Python implementiert werden
* Post anfragen können mit body an den server gesendet werden.


# Aufgabe 4: Authentifizierungstoken einschließen (Fehlerbehandlung)

Beschreibung: Die Post Request in Aufgabe 3 benötigt zur korrekten Funktionalität ein authentifizierungstoken. Dieses soll nun in den Header der Request integriert werden.
Ziel: 
* Erkennen des Fehlers und beheben von diesem indem der korrekte header verwendet wird.


# Server update idee
* Testdb integrieren -> z.B. advanced get request mit body bei dem von der datenbank etwas abgefragt wird (kann einfach über die api des Testdb server laufen)