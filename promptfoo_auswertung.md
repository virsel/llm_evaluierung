# promptfoo (4.7k Githubsterne)

## Vorteile:

- wenig programmieroverhead

- wenige Strukurierungsoverhead, wird zum Großteil sinnvoll vorgegeben

- Visualierungen mittels Webapp möglich
    - übersichtlich mit vielen Funktionen

- Ohne lizenz verwendbar

- 100% Open Source

- Große Community

- Tests werden in `yaml` configs konfiguriert
    - So wird eine sinnvolle Struktur vorgegeben 
    - mit wenig Programmieraufwand lassen sich komplexe Tests ausführen
    - Auch bei Collaboration bleibt eine einheitliche Struktur sichergestellt

- stellt eine Vielzahl an beliebten Test-Metriken zur Verfügung, welche mit wenig Aufwand verwendet werden können

- das Implementieren von benutzerdefinierten Metriken ist einfach möglich

- Anbindung verschiedenster LLM Endpunkte einfach möglich (z.b. genügt "ollama:llama3.2:latest" um auf das Modell zuzugreifen)

- sehr gut Dokumentiert, viele Beispiele vorhanden ([Github](https://github.com/promptfoo/promptfoo/tree/main/examples))

## Nachteile:

- Debugging komplex da yaml dateien über promptfoo cli befehl ausgeführt werden

- Einarbeitung in vorgesehene yaml syntax notwendig

# DeepEval (3.7k Githubsterne)

## Vorteile
- viele vordefinierte Metriken
    - exklusiv: 
        - Conversational (https://docs.confident-ai.com/docs/metrics-conversation-completeness)
        - Multimodal (https://docs.confident-ai.com/docs/metrics-text-to-image)
    - benutzerdefinierte lassen sich einfach implementieren

- pure Python, Open-Source, sehr gut dokumentiert

- mit Hilfe von Confident AI lassen sich hilfreiche Visualisierungen umsetzen

## Nachteile
- für Visualierung Confident AI Login notwendig
    - kein Self-Hosting möglich
    
- wenig Beispiele ([Github](https://github.com/confident-ai/deepeval/tree/main/examples))