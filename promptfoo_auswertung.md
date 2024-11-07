# promptfoo (4.7k Githubsterne)

## Vorteile:

- wenig programmieroverhead

- wenige Strukurierungsoverhead, wird zum Großteil sinnvoll vorgegeben

- Visualierungen mittels Webapp möglich
    - übersichtlich mit vielen Funktionen

- Ohne lizenz verwendbar

- 100% Open Source

- Tests werden in `yaml` configs konfiguriert
    - So wird eine sinnvolle Struktur vorgegeben 
    - mit wenig Programmieraufwand lassen sich komplexe Tests ausführen
    - Auch bei Collaboration bleibt eine einheitliche Struktur sichergestellt

- stellt eine Vielzahl an beliebten Test-Metriken zur Verfügung, welche mit wenig Aufwand verwendet werden können

- das Implementieren von benutzerdefinierten Metriken ist einfach möglich

- sehr gut Dokumentiert, viele Beispiele vorhanden ([Github](https://github.com/promptfoo/promptfoo/tree/main/examples))

- Anbindung verschiedenster LLM Endpunkte einfach möglich (z.b. genügt "ollama:llama3.2:latest" um auf das Modell zuzugreifen)

## Nachteile:

- Debugging komplex da yaml dateien über promptfoo cli befehl ausgeführt werden

- Einarbeitung in vorgesehene yaml syntax notwendig

## Fazit
Sehr gut für grundlegende Tests in Dev-Phase.
Gute Auswertbarkeit der Ergebnisse mittels UI.
Durch wenig Programmieroverhead kommt man schnell zu gewünschten Ergebnissen.

# DeepEval (3.7k Githubsterne)

## Vorteile
- Echtzeit Evaluation in Produktion möglich

- viele vordefinierte Metriken
    - exklusiv: 
        - Conversational (https://docs.confident-ai.com/docs/metrics-conversation-completeness)
        - Multimodal (https://docs.confident-ai.com/docs/metrics-text-to-image)
    - benutzerdefinierte lassen sich einfach implementieren

- pure Python, Open-Source, sehr gut dokumentiert

- mit Hilfe von Confident AI lassen sich hilfreiche Visualisierungen umsetzen

- viele Beispiele ([Github](https://github.com/confident-ai/deepeval/tree/main/examples))

## Nachteile
- für Visualierung Confident AI Login notwendig
    - kein Self-Hosting möglich

- komplexe Tests schwierig Umsetzbar (z.b. Vergleich von mehreren Prompts)
    - oft deutlich mehr Code als bei promptfoo notwendig

## Fazit

Weniger gut geeignet für die Dev-Phase, da mit mehr Programmieroverhead verbunden + keine frei verwendbare Visualisierungsmöglichkeit der Ergebnisse vorhanden.
Metrikfunktionen aber als Allrounder sowohl in Dev-Phase als auch Produktivphase verwendbar.
Diese lassen sich auch in einer Promptfoo-Dev-Phase einbinden.

