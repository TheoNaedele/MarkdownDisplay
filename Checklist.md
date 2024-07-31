# Entwicklungsprozess 
Der folgende Entwicklungsprozess soll als Anhaltspunkt

## 1. Anforderungsanalyse
### 1.1 Zielsetzung und Umfang
#### Aufgaben:
- **Absprache mit Entwickler / Stakeholder:**
  - [ ] Abklären, was genau benötigt wird.
  - [ ] Hintergründe und Zusammenhänge verstehen (besonders wichtig bei Featuretests).
  - [ ] Mögliche Lösungsansätze definieren und besprechen.

- **Definition der Projektziele:**
  - [ ] Definition of Done (DoD) festlegen.

- **Erstellung eines Projektplans mit Meilensteinen (bei großen Projekten):**
  - [ ] Hauptmeilensteine definieren.
  - [ ] Zeitplan für die Meilensteine erstellen.
  - [ ] Verantwortlichkeiten für jeden Meilenstein festlegen.

### Arbeitsergebnisse:
- **Ergebnisse der Absprache:**
  - [ ] Dokumentation der Ergebnisse der Absprache mit Entwicklern und Stakeholdern.
  - [ ] Festlegung der genauen Anforderungen und Erwartungen.

- **Definition of Done (DoD):**
  - [ ] Dokumentation der DoD-Kriterien.

- **Projektplan (bei großen Projekten):**
  - [ ] Erstellung eines detaillierten Projektplans mit festgelegten Meilensteinen.
  - [ ] Dokumentation der Zeitpläne und Verantwortlichkeiten.

### Dokumentation:
- **Anforderungsdokument:**
  - [ ] Zusammenfassung der Ergebnisse der Absprache.
  - [ ] Festgelegte Definition of Done (DoD).
  - [ ] Detaillierter Projektplan mit Meilensteinen (falls erforderlich).


## 2. System- und Software-Design
### 2.1 Architekturentwurf bei größeren Projekten
#### Aufgaben:
- **Entwicklung einer Systemarchitektur:**
  - [ ] Identifizierung der Hauptkomponenten und deren Verantwortlichkeiten.
  - [ ] Sicherstellung der Skalierbarkeit und Wartbarkeit der Architektur.

- **Auswahl geeigneter Technologien, Plattformen und Frameworks:**
  - [ ] Evaluierung und Auswahl von Technologien, die den Anforderungen entsprechen.
  - [ ] Berücksichtigung von Kompatibilität und zukünftiger Erweiterbarkeit.

- **Erstellung eines Architektur-Diagramms:**
  - [ ] Detaillierter Entwurf einzelner Systemkomponenten.
  - [ ] Darstellung des Zusammenhangs zwischen den Systemkomponenten.

- **Definition von Schnittstellen:**
  - [ ] Spezifikation der Schnittstellen zwischen den Modulen.
  - [ ] Sicherstellung der Konsistenz und Integrität der Datenflüsse.

#### Dokumente:
- **Architekturdokumentation:**
  - [ ] Beschreibung der gesamten Systemarchitektur.
  - [ ] Detaillierte Spezifikationen der Systemkomponenten.
  - [ ] Schnittstellendokumentation (z.B. UML-Diagramme).

### 2.2 Planung bei kleineren Projekten (z.B. Featuretest)
#### Aufgaben:
- **Entwurfsplanung:**
  - [ ] Identifikation der benötigten Bibliotheken.
  - [ ] Planung von Automatisierungsmöglichkeiten.
  - [ ] Festlegung, wie Pass/Fail geprüft werden kann.

- **Sonstige benötigte Artefakte festlegen:**
  - [ ] Configs:
    - Festlegung der notwendigen Einstellungen in den Config-Dateien.
  - [ ] Sonstiges (Wireshark aufzeichnungen, Hut Dateien etc)

#### Dokumente:
- **Entwurfsdokumentation:**
  - [ ] Beschreibung der benötigten Bibliotheken und Keywörter.
  - [ ] Dokumentation der Automatisierungsmöglichkeiten.
  - [ ] Spezifikation der Pass/Fail-Kriterien.
  - [ ] Config-Dokumentation:
    - Beschreibung der notwendigen Einstellungen.
  - [ ] Weitere Artefakte-Dokumentation:
    - Beschreibung weiterer benötigter Dateien und deren Zweck.

## 3. Implementierung
### 3.1 Coding Standards und Best Practices
#### Aufgaben:
- Einrichtung und Nutzung von Versionskontrollsystemen (z.B. Git).
- Durchführung regelmäßiger Code-Reviews (bei größeren Projekten).
    - Nutzen von mehreren Branches (dev/feature/X) um kleinere Code Reviews zu ermöglichen um schneller Feedback zu erhalten und große PR wie TestDB zu verhindern

## 3. Implementierung und Dokumentation
### 3.2 Entwicklung
#### 3.2.1 Modulare Entwicklung in größeren Projekten
##### Aufgaben:
- **Implementierung der Software in modularen Einheiten:**
  - [ ] Entwickeln und Testen einzelner Module separat.
  - [ ] Sicherstellung der Wiederverwendbarkeit und Wartbarkeit der Module.
  
- **Durchführung von Unit-Tests für jedes Modul:**
  - [ ] Schreiben von Unit-Tests für jede Funktion und jedes Modul.
  - [ ] Automatisierung der Unit-Tests, um kontinuierliche Integration zu unterstützen.

- **Integration der Module zu einem Gesamtsystem:**
  - [ ] Schrittweise Integration der Module in das Gesamtsystem.
  - [ ] Durchführung von Integrationstests, um sicherzustellen, dass die Module nahtlos zusammenarbeiten.

##### Dokumente:
- **Moduldokumentation:**
  - [ ] Beschreibung der Funktionalitäten und Schnittstellen jedes Moduls.
  - [ ] Anweisungen zur Installation und Nutzung der Module.

- **Unit-Test-Pläne und -Berichte:**
  - [ ] Detaillierte Pläne für Unit-Tests.
  - [ ] Ergebnisse und Berichte der durchgeführten Unit-Tests.

- **Integrationsdokumentation:**
  - [ ] Beschreibung des Integrationsprozesses.
  - [ ] Ergebnisse der Integrationstests.

### 3.3 Dokumentation
##### Aufgaben:
- **Fortlaufende Dokumentation des Codes mit Kommentaren und Erklärungen:**
  - [ ] Detaillierte Kommentare im Quellcode.
  - [ ] Regelmäßige Aktualisierung der Dokumentation bei Änderungen.

- **Dokumentation der Implementierungsentscheidungen:**
  - [ ] Aufzeichnung aller wichtigen Implementierungsentscheidungen.
  - [ ] Begründung der getroffenen Entscheidungen.

##### Dokumente:
- **Quellcodedokumentation:**
  - [ ] Detaillierte Dokumentation des gesamten Quellcodes.
  - [ ] Erklärung der wichtigsten Algorithmen und Datenstrukturen.

## 4. Verifikation und Validierung (bei großen Projekten)
### 4.1 Testplanung
##### Aufgaben:
- **Erstellung eines detaillierten Testplans:**
  - [ ] Festlegung der Teststrategie und -methoden.
  - [ ] Zeitplan für die Testphasen erstellen.

- **Definition von Testfällen und Testszenarien:**
  - [ ] Erstellung spezifischer Testfälle für jede Funktionalität.
  - [ ] Definition realistischer Testszenarien, die die Nutzung des Systems widerspiegeln.

- **Planung von Testressourcen und -umgebungen:**
  - [ ] Festlegung der benötigten Testressourcen (Hardware, Software, Personal).
  - [ ] Einrichtung und Konfiguration der Testumgebungen.

##### Dokumente:
- **Testplan:**
  - [ ] Detaillierter Plan für alle Testaktivitäten.
  - [ ] Beschreibung der Testmethoden und -strategien.

- **Testfallspezifikationen:**
  - [ ] Detaillierte Beschreibung jedes Testfalls.
  - [ ] Definition der erwarteten Ergebnisse.

- **Testszenarien-Dokument:**
  - [ ] Beschreibung der realistischen Testszenarien.
  - [ ] Festlegung der Bedingungen und Abläufe für die Tests.

### 4.2 Testdurchführung
##### Aufgaben:
- **Durchführung von Unit-Tests, Integrationstests, Systemtests und Akzeptanztests:**
  - [ ] Ausführung der vorbereiteten Unit-Tests für einzelne Module.
  - [ ] Durchführung der Integrationstests für das Gesamtsystem.
  - [ ] Systemtests zur Überprüfung der Gesamtsystemfunktionalität.
  - [ ] Akzeptanztests zusammen mit den Stakeholdern zur Validierung der Anforderungen.

- **Dokumentation und Nachverfolgung von Fehlern:**
  - [ ] Aufzeichnung aller gefundenen Fehler.
  - [ ] Nachverfolgung und Behebung der Fehler.

- **Erstellung von Testberichten und Protokollen:**
  - [ ] Zusammenfassung der Testergebnisse.
  - [ ] Detaillierte Protokolle der durchgeführten Tests und der gefundenen Fehler.

##### Dokumente:
- **Testprotokolle:**
  - [ ] Aufzeichnungen der durchgeführten Tests.
  - [ ] Dokumentation der Testergebnisse.

- **Fehlerberichte:**
  - [ ] Detaillierte Beschreibung der gefundenen Fehler.
  - [ ] Status und Fortschritt bei der Fehlerbehebung.

- **Testberichte:**
  - [ ] Zusammenfassung aller Testergebnisse.
  - [ ] Empfehlungen und Schlussfolgerungen basierend auf den Testergebnissen.

## 5. Bereitstellung und Wartung
### 5.1 Deployment
##### Aufgaben:
- **Planung und Durchführung des Systemrollouts:**
  - [ ] Erstellung eines detaillierten Deployment-Plans.
  - [ ] Koordination und Durchführung des Rollouts.

- **Durchführung von Last- und Performance-Tests:**
  - [ ] Planung und Ausführung von Lasttests.
  - [ ] Analyse der Performance und Identifikation von Engpässen.

##### Dokumente:
- **Deployment-Plan:**
  - [ ] Detaillierte Schritte und Zeitpläne für den Rollout.
  - [ ] Verantwortlichkeiten und Ansprechpartner.

- **Performance-Testberichte:**
  - [ ] Ergebnisse der Last- und Performance-Tests.
  - [ ] Empfehlungen zur Optimierung der Performance.


