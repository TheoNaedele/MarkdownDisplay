# Entwicklungsprozess 
Der folgende Entwicklungsprozess soll als Anhaltspunkt

### 1.1 Zielsetzung und Umfang
#### Aufgaben:
- **Absprache mit Entwickler / Stakeholder:**
  - Abklären, was genau benötigt wird.
    - Welche Hauptfunktionalitäten oder Probleme sollen gelöst werden?
    - Gibt es spezifische Anforderungen oder Einschränkungen, die beachtet werden müssen?
  - Hintergründe und Zusammenhänge verstehen (besonders wichtig bei Featuretests).
    - Welche bestehenden Systeme oder Prozesse sind betroffen oder relevant?
    - Welche geschäftlichen oder technischen Ziele sollen durch dieses Projekt erreicht werden?
  - Mögliche Lösungsansätze definieren und besprechen.
    - Gibt es bereits Ideen oder Vorstellungen, wie das Problem gelöst werden könnte?
    - Welche Alternativen sollten in Betracht gezogen werden?

- **Definition der Projektziele:**
  - Definition of Done (DoD) festlegen.
    - Welche Kriterien müssen erfüllt sein, damit das Projekt als abgeschlossen gilt?
    - Wie wird der Erfolg oder Misserfolg des Projekts gemessen?

- **Erstellung eines Projektplans mit Meilensteinen (bei großen Projekten):**
  - Hauptmeilensteine definieren.
    - Welche Schlüsselaufgaben oder Etappen müssen erreicht werden, um das Projekt erfolgreich abzuschließen?
  - Zeitplan für die Meilensteine erstellen.
    - Welche Zeiträume sind für die einzelnen Phasen oder Meilensteine vorgesehen?
  - Verantwortlichkeiten für jeden Meilenstein festlegen.
    - Wer ist für die Durchführung und das Erreichen jedes Meilensteins verantwortlich?

### Arbeitsergebnisse:
- **Ergebnisse der Absprache:**
  - Dokumentation der Ergebnisse der Absprache mit Entwicklern / Stakeholdern.
    - Was wurde im Meeting besprochen und vereinbart?
    - Welche Entscheidungen wurden getroffen und warum?
  - Festlegung der genauen Anforderungen und Erwartungen.
    - Welche spezifischen Funktionalitäten oder Eigenschaften muss das Endprodukt aufweisen?

- **Definition of Done (DoD):**
  - Dokumentation der DoD-Kriterien.
    - Welche Kriterien müssen erfüllt sein, damit eine Aufgabe oder ein Feature als abgeschlossen gilt?

- **Projektplan (bei großen Projekten):**
  - Erstellung eines detaillierten Projektplans mit festgelegten Meilensteinen.
    - Welche Schritte und Aufgaben sind für jeden Meilenstein erforderlich?
    - Wann sollen die einzelnen Meilensteine erreicht werden?

### Dokumentation:
- **Anforderungsdokument:**
  - Zusammenfassung der Ergebnisse der Absprache.
  - Festgelegte Definition of Done (DoD).
    - Eine Liste klar definierter Kriterien für den Abschluss von Aufgaben oder Features.
  - Detaillierter Projektplan mit Meilensteinen (falls erforderlich).


## 2. System- und Software-Design

### 2.1 Architekturentwurf bei größeren Projekten

#### Aufgaben:

- **Entwicklung einer Systemarchitektur:**
  - Identifizierung der Hauptkomponenten und deren Verantwortlichkeiten.
  - Sicherstellung der Skalierbarkeit und Wartbarkeit der Architektur.
  - Bewertung von Designmustern und -prinzipien zur Optimierung der Architektur.
    - Bestenfalls als Review mit weiterer Person

- **Auswahl geeigneter Technologien, Plattformen und Frameworks:**
  - Evaluierung und Auswahl von Technologien, die den funktionalen und nicht-funktionalen Anforderungen entsprechen.
  - Berücksichtigung von Sicherheits-, Performance- und Wartungsaspekten.
  - Planung für zukünftige Erweiterbarkeit und Integration.

- **Erstellung eines Architektur-Diagramms:**
  - Detaillierter Entwurf einzelner Systemkomponenten und deren Interaktionen.
  - Visualisierung der Abhängigkeiten und Schnittstellen zwischen den Komponenten.
  - Integration von Feedback aus Design-Reviews und Iterationen.

- **Definition von Schnittstellen:**
  - Spezifikation der Schnittstellen zwischen den Modulen und externen Systemen.
  - Sicherstellung der Konsistenz und Kompatibilität der Schnittstellen.
  - Implementierung von Entwurfsmustern zur Verbesserung der Modularität und Wiederverwendbarkeit.

#### Dokumente:

- **Architekturdokumentation:**
  - Beschreibung der gesamten Systemarchitektur und ihrer Ziele.
  - Detaillierte Spezifikationen der Systemkomponenten mit ihren Funktionen und Verantwortlichkeiten.
  - Schnittstellendokumentation (z.B. UML-Diagramme) für eine klare Kommunikation der Systemstruktur.

### 2.2 Planung bei kleineren Projekten (z.B. Featuretest)
#### Aufgaben:

- **Entwurfsplanung:**
  - Identifikation der benötigten Bibliotheken, Frameworks und Tools für die Implementierung.
  - Planung von Automatisierungsmöglichkeiten für Tests und Bereitstellung.
  - Festlegung der Kriterien und Methoden zur Bewertung von Pass/Fail für Funktionen und Features.

- **Sonstige benötigte Artefakte festlegen:**
  - Konfigurationsmanagement:
    - Festlegung der Einstellungen und Konfigurationen für verschiedene Umgebungen (Entwicklung, Test, Produktion).
    - Versionierung und Verwaltung von Konfigurationsdateien für eine konsistente Bereitstellung.

  - Zusätzliche Artefakte:
    - Dokumentation von Wireshark-Aufzeichnungen oder Netzwerkkonfigurationen für Debugging und Sicherheitsüberprüfungen.
    - Spezifikationen für spezielle Dateiformate oder Datenbankkonfigurationen (HUT-Dateien) zur Unterstützung von Tests und Analysen.

#### Dokumente:

- **Entwurfsdokumentation:**
  - Beschreibung der erforderlichen Bibliotheken, Frameworks und externen Abhängigkeiten.
  - Dokumentation der Automatisierungslösungen für Entwicklungs- und Testaufgaben.
  - Spezifikation der Pass/Fail-Kriterien und Methoden zur Verifikation der Softwarefunktionalitäten.

- **Konfigurationsdokumentation:**
  - Beschreibung der Konfigurationseinstellungen für verschiedene Umgebungen und Anwendungsfall-Szenarien.
  - Versionierung und Dokumentation von Änderungen in Konfigurationsdateien für Transparenz und Rückverfolgbarkeit.

- **Weitere Artefakte-Dokumentation:**
  - Beschreibung von speziellen Dateiformaten oder Protokollen (Wireshark, HUT), einschließlich ihrer Struktur und Verwendungszwecke.

## 3. Implementierung und Dokumentation

### 3.1 Coding Standards und Best Practices

#### Aufgaben:
- Einrichtung und Nutzung von Git Repo.
- Durchführung regelmäßiger Code-Reviews (bei größeren Projekten).
  - Nutzen von mehreren Branches (dev/feature/X) um kleinere Code Reviews zu ermöglichen und schneller Feedback zu erhalten und große PR wie TestDB zu verhindern.

### 3.2 Entwicklung

#### 3.2.1 Modulare Entwicklung in größeren Projekten

##### Aufgaben:
- **Implementierung der Software in modularen Einheiten:**
  - Entwickeln und Testen einzelner Module separat.
  - Sicherstellung der Wiederverwendbarkeit und Wartbarkeit der Module.
  
- **Durchführung von Unit-Tests für jedes Modul:**
  - Schreiben von Unit-Tests für jede Funktion und jedes Modul.
  - Automatisierung der Unit-Tests, um kontinuierliche Integration zu unterstützen.

- **Integration der Module zu einem Gesamtsystem:**
  - Schrittweise Integration der Module in das Gesamtsystem.
  - Durchführung von Integrationstests, um sicherzustellen, dass die Module nahtlos zusammenarbeiten.

- **Fortlaufende Optimierung und Refactoring:**
  - Regelmäßige Überprüfung und Verbesserung des Codes.
  - Anwendung von Refactoring-Techniken, um die Codequalität zu erhöhen.

- **Performance- und Lasttests:**
  - Durchführung von Tests zur Überprüfung der Leistungsfähigkeit der Software.
  - Analyse und Optimierung der Software basierend auf den Testergebnissen.

##### Dokumente:
- **Moduldokumentation:**
  - Beschreibung der Funktionalitäten und Schnittstellen jedes Moduls.
  - Anweisungen zur Installation und Nutzung der Module.

- **Unit-Test-Pläne und -Berichte:**
  - Detaillierte Pläne für Unit-Tests.
  - Ergebnisse und Berichte der durchgeführten Unit-Tests.

- **Integrationsdokumentation:**
  - Beschreibung des Integrationsprozesses.
  - Ergebnisse der Integrationstests.

- **Optimierungs- und Refactoring-Berichte:**
  - Dokumentation der durchgeführten Optimierungen und Refactoring-Maßnahmen.
  - Nachweis der Verbesserungen durch Vergleich vorher/nachher.

- **Performance- und Lasttest-Berichte:**
  - Dokumentation der Testfälle und Ergebnisse.
  - Maßnahmen zur Leistungsoptimierung basierend auf den Testergebnissen.

### 3.3 Dokumentation

#### Aufgaben:
- **Fortlaufende Dokumentation des Codes mit Kommentaren und Erklärungen:**
  - Detaillierte Kommentare im Quellcode.
  - Regelmäßige Aktualisierung der Dokumentation bei Änderungen.

- **Dokumentation der Implementierungsentscheidungen:**
  - Aufzeichnung aller wichtigen Implementierungsentscheidungen.
  - Begründung der getroffenen Entscheidungen.

- **Erstellung von Benutzerdokumentationen und Handbüchern:**
  - Anleitungen zur Installation, Konfiguration und Nutzung der Software.
  - Erstellen von Tutorials und FAQs für Endbenutzer.

- **Erstellung von Entwicklerdokumentationen:**
  - Technische Dokumentation für Entwickler zur Erweiterung und Wartung der Software.
  - API-Dokumentation und Beispiele für die Nutzung.

- **Dokumentation des Deployment-Prozesses:**
  - Beschreibung des Prozesses zur Bereitstellung der Software.
  - Anweisungen für das Deployment in verschiedenen Umgebungen (z.B. Entwicklung, Test, Produktion).

#### Dokumente:
- **Quellcodedokumentation:**
  - Detaillierte Dokumentation des gesamten Quellcodes.
  - Erklärung der wichtigsten Algorithmen und Datenstrukturen.

- **Entscheidungsdokumentation:**
  - Aufzeichnung der Implementierungsentscheidungen und deren Begründungen.

- **Benutzerdokumentation und Handbücher:**
  - Anleitungen und Tutorials für Endbenutzer.
  - Häufig gestellte Fragen (FAQs).

- **Entwicklerdokumentation:**
  - Technische Dokumentation zur Unterstützung der Entwicklung und Wartung.
  - API-Dokumentation und Code-Beispiele.

- **Deployment-Dokumentation:**
  - Anweisungen und Prozesse für die Bereitstellung der Software.
  - Dokumentation der spezifischen Schritte für verschiedene Umgebungen.

## 4. Verifikation und Validierung (bei großen Projekten)
### 4.1 Testplanung
##### Aufgaben:
- **Erstellung eines detaillierten Testplans:**
  - Festlegung der Teststrategie und -methoden.
  - Zeitplan für die Testphasen erstellen.

- **Definition von Testfällen und Testszenarien:**
  - Erstellung spezifischer Testfälle für jede Funktionalität.
  - Definition realistischer Testszenarien, die die Nutzung des Systems widerspiegeln.

- **Planung von Testressourcen und -umgebungen:**
  - Festlegung der benötigten Testressourcen (Hardware, Software, Personal).
  - Einrichtung und Konfiguration der Testumgebungen.

##### Dokumente:
- **Testplan:**
  - Detaillierter Plan für alle Testaktivitäten.
  - Beschreibung der Testmethoden und -strategien.

- **Testfallspezifikationen:**
  - Detaillierte Beschreibung jedes Testfalls.
  - Definition der erwarteten Ergebnisse.

- **Testszenarien-Dokument:**
  - Beschreibung der realistischen Testszenarien.
  - Festlegung der Bedingungen und Abläufe für die Tests.

### 4.2 Testdurchführung
##### Aufgaben:
- **Durchführung von Unit-Tests, Integrationstests, Systemtests und Akzeptanztests:**
  - Ausführung der vorbereiteten Unit-Tests für einzelne Module.
  - Durchführung der Integrationstests für das Gesamtsystem.
  - Systemtests zur Überprüfung der Gesamtsystemfunktionalität.
  - Akzeptanztests zusammen mit den Stakeholdern zur Validierung der Anforderungen.

- **Dokumentation und Nachverfolgung von Fehlern:**
  - Aufzeichnung aller gefundenen Fehler.
  - Nachverfolgung und Behebung der Fehler.

- **Erstellung von Testberichten und Protokollen:**
  - Zusammenfassung der Testergebnisse.
  - Detaillierte Protokolle der durchgeführten Tests und der gefundenen Fehler.

##### Dokumente:
- **Testprotokolle:**
  - Aufzeichnungen der durchgeführten Tests.
  - Dokumentation der Testergebnisse.

- **Fehlerberichte:**
  - Detaillierte Beschreibung der gefundenen Fehler.
  - Status und Fortschritt bei der Fehlerbehebung.

- **Testberichte:**
  - Zusammenfassung aller Testergebnisse.
  - Empfehlungen und Schlussfolgerungen basierend auf den Testergebnissen.

## 5. Bereitstellung und Wartung
### 5.1 Deployment
##### Aufgaben:
- **Planung und Durchführung des Systemrollouts:**
  - Erstellung eines detaillierten Deployment-Plans.
  - Koordination und Durchführung des Rollouts.

- **Durchführung von Last- und Performance-Tests:**
  - Planung und Ausführung von Lasttests.
  - Analyse der Performance und Identifikation von Engpässen.

##### Dokumente:
- **Deployment-Plan:**
  - Detaillierte Schritte und Zeitpläne für den Rollout.
  - Verantwortlichkeiten und Ansprechpartner.

- **Performance-Testberichte:**
  - Ergebnisse der Last- und Performance-Tests.
  - Empfehlungen zur Optimierung der Performance.


