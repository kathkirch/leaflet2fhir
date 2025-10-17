questions_organization = {
    "manufacturer": {
        "question": (
            "Suche nach dem Hersteller des Medikaments, achte darauf den Hersteller und "
            "nicht den Pharmezeutischen Unternehmer zu finden. "
            "Schreibe in deine Antwort nur den vollständigen Herstellernamen "
            "sowie die gesamte gefundene Adresse des Herstellers und weitere Kontaktdaten des Herstellers, "
            "wenn vorhanden."
        ),
        "following": {
            "orgName": {
                "question": (
                    "Wie lautet der vollständige Name des Hersteller oder der Herstellerfirma. "
                    "Die Antwort sollte nur den Herstellernamen enthalten"
                )
            },
            "address_street_number": {
                "question": (
                    "Suche aus der Adresszeile des Herstellers extrahiere die Strasse und Türnummer, falls vorhanden. "
                    "Ist keine Strasse und Türnummer vorhanden antworte ausschliesslich mit None! "
                )
            },
            "address_city": {
                "question": (
                    "Suche aus der Adresszeile des Herstellers extrahiere die Stadt, falls vorhanden. "
                    "Ist keine Stadt angegeben antworte ausschliesslich mit None! "
                )
            },
            "address_zip": {
                "question": (
                    "Suche aus der Adresszeile des Herstellers extrahiere die Postleitzahl. "
                    "Die Antwort sollte nur die Postleitzahl enthalten!"
                )
            },
            "address_country": {
                "question": (
                    "Extrahiere das Land aus der Adresszeile. "
                    "Die Antwort sollte nur das Land enthalten!"
                )
            },
            "webAdress":{ 
                "question": (
                    "Suche nach der Webadresse des Herstellers. "
                    "Ist keine Webadresse angegeben so antworte ausschliesslich mit None! "
                )
            },
            "fax":{
                "question": (
                    "Suche nach der Faxnummer des Herstellers. "
                    "Achte darauf den Hersteller zu finden und nicht den Vertreiber. "
                    "Ist keine Faxnummer angegeben so antworte ausschliesslich mit None! "
                )
            }
        }
    }
}

questions_mpd = {
    "fullName": {
        "question": (
            "Suche im Beipackzettel nach dem vollständigen Produktnamen des Medikaments. "
            "Die Antwort sollte nur den vollständigen Produktnamen enthalten!"
        ),
        "following": {
            "nameDoseFormPart": {"question": (
                "Suche im Text nach der Dosierform. "
                "Deine Antwort sollte nur die Dosierform enthalten!"
            )},
            "nameStrengthPart": {"question": (
                "Suche im Text nach der Zusammensetzung/Stärke des Medikaments. "
                "Deine Antwort sollte nur die Zusammensetzung/Stärke als Zahl inklusive der Einheit enthalten."
            )},
            "namePopulationPart": {"question": (
                "Suche im Text nach der Population für die das Medikament gedacht ist. "
                "Ist keine Population zu finden antworte ausschliesslich mit None!"
            )},
        },
    },
    "admission_nr": {"question": (
        "Suche im Beipackzettel die Zulassungsnummer des Medikaments. "
        "Deine Antwort soll ausschliessliech die reine Zulassungsnummer beinhalten"
    )},
    "modeOfAction": {"question": (
        "Suche im Beipackzettel die Wirkungsweise des Medikaments. "
        "Gib die Wirkungsweise nur so zurück wie sie auch im Beipackzettel zu finden ist. "
    )},
    "indication": {"question": (
        "Suche im Beipackzettel nach den Anwendungsbereich des Medikaments. "
        "Sind verschiedene Anwendungsbereiche angegeben trenne diese mit einem Semikolon voneinander. "
        "Deine Antwort sollte nur die Anwendungsbereiche aufzählen"
    )},
    "creationDate": {"question": (
        "Suche im Beipackzettel nach dem Datum an dem die Packungsbeilage zuletzt überarbeitet oder erstellt wurde. "
        "Deine Antwort sollte nur das Datum im Format YYYY-MM--DD enthalten. "
    )},
    "blackTriangle": {"question": (
        "Suche im Beipackzettel nach Informationen ob das Medikament einer zusätzlichen Überwachung unterliegt. "
        "Der sogenannten Black-Triangle Informationen "
        "Extrahiere den Text betreffend der zusätzlichen (Black Triangle) Überwachung. "
        "Ist keine Black-Triangle Information zu finden antworte ausschliesslich mit None!"
    )},
    "activeIngredient": {
        "question": (
            "Suche im Beipackzettel nach dem Abschnitt in dem die aktiven Wirkstoffe des Medikaments beschrieben sind und schreibe den Abschnitt in deine Antwort. "
            "Die aktiven Wirkstoffe sind oft daran zu erkennen indem eine genaue Stärke angegeben ist. "
            "Ignoriere die Hilfsstoffe oder sonstige Bestandteile. "
        ) ,
        "following": {
            "name_strength_active":  {"question": (
                "Suche im Text die genaue Anzahl an aktiven Wirkstoffen im Medikament. "
                "Extrahiere jeden Wirkstoff inklusive Menge pro Dosiereinheit getrennt durch ein Komma. "
                "Wenn es mehrere Wirkstoffe gibt trenne diese mit einem Semikolon voneinander. "
                "Deine Antwort sollte nur Wirkstoff, Menge, Dosierform enthalten. "
            )},
        }
    },
    "excipientIngredient": {
        "question": (
            "Suche im Beipackzettel nach dem Abschnitt in dem die Hilfsstoffe oder sonstige Bestandteile des Medikaments beschrieben sind. "
            "Ignoriere die aktiven Wirkstoffe. "
        ) ,
        "following": {
            "name_strength_excipient":  {"question": (
                "Finde im Text alle enthaltenen Hilfsstoffe/Bestandteile des Medikaments. "
                "Wenn es mehrere gibt trenne diese mit einem Semikolon voneinander. "
                "Deine Antwort sollte alle enthaltenen Bestandteile aufzählen!"
            )},
        }
    }
}

questions_medical_knowledge = {
    "name_medication" : { 
        "question": (
            "Suche im Beipackzettel nach dem Handels- oder Markenname des Medikaments. "
            "Deine Antwort soll nur den Namen beinhalten!"
        )
    },
    "forgotten" : {
        "question": (
            "Suche im Beipackzettel nach dem Abschnitt was zu tun ist wenn die Einnahme des Medikaments vergessen wurde. "
            "Deine Antwort soll ausschliesslich die beschriebene Anleitung beinhalten ohne eine Überschrift zu erwähnen"
        )
        
    },
    "quit" : {
        "question": (
            "Suche im Beipackzettel nach dem Abschnitt zu Hinweisen was passiert wenn die Einnahme abgebrochen wird. "
            "Deine Antwort soll ausschliesslich die Hinweise und Anweisungen beinhalten ohne eine Überschrift zu erwähnen. "
            "Sind keine spezifischen Hinweise vorhanden, schreibe das in deine Antwort. "
        )
    },
    "too_much": {
        "question": (
            "Suche im Beipackzettel nach dem Abschnitt bezüglich Hinweise und Anweisungen wenn zu viel vom Medikament eingenommen wurde. "
            "Deine Anwort soll ausschliesslich die Hinweise und Anweisungen beinhalten ohne eine Überschrift zu erwähnen "
        )
    },
    "max_intake_duration": {
        "question": (
            "Suche im Beipackzettel welche nach Hinweisen zur Anwendungsdauer. "
            "Deine Antwort soll nur Hinweise enthalten die auch im Beipackzettel zu finden sind. "
            "Schreibe in die Anwort wenn die Einnahme nicht limitiert ist und keine Hinweise existieren."
        )
    },
    "general_dosage": {
        "question": (
            "Suche im Beipackzettel nach dem Abschnitt wie das Medikament einzunehmen ist. "
            "Deine Antwort sollte den gesamten Abschnitt 'Wie Medikament einzunehmen ist:' beinhalten. "
            "Meis ist das das Kapitel 3 im Beipackzettel."
        ),
        "following": {
            "patient_instruction": {
                "question": (
                    "Suche im Text nach Informationen wie das Medikament dosiert werden soll (wie oft und wie viel pro Tag eingenommen werden sollte) "
                    "Oft ist dies der erste Absatz im Abschnitt 'Wie Medikament einzunehmen ist:'. "
                    "Inkludiere die Information das Medikament immer genau nach Empfehlung der Packungsbeilage bzw Arzt/Apotheker einzunhemen! "
                    "Wenn angegeben, hänge Informationen zum Mindestabstand in Stunden bis zur nächsten Einnahme an, sowie Dosierung für bestimmte Patientengruppen. "
                    "Streiche die Informationen, maximale Einnahmedauer in Tagen, was zu tun ist wenn eine Einnahme vergessen wurde, "
                    "was zu tun ist bei einer Überdosierung, was passiert wenn die Einnahme abgebrochen wird und wie genau das Medikament verabreicht wird aus der Antwort."
                    "Antworte mit den Hinweisen zur Dosierung und schreibe keine Überschrift in die Antwort! "
                )
            },
            "additional_instruction": {
                "question": (
                    "Suche im Text nach Information bezüglich der korrekten Einnahme. "
                    "Bsp. mit Wasser einnehmen oder langsam unter der Zunge zergehen lassen, oder ob das Medikament geteilt/gemörsert werden darf."
                    "Antworte nur mit den Hinweisen zur Einnhame, findest du nichts so antworte mit None. " 
                )
            },
            "route": {
                "question": (
                    "Suche im Text wie das Medikament dem Körper zugeführt wird, z.B. Zum Einnehmen."
                    "Welche Einnahmeroute ist angeführt? "
                    "Deine Antwort soll nur die Einnahmeroute enthalten! "
                )
            },
            "doseform": {
                "question": (
                    "Suche im Text nach der Dosierform für das Medikament. "
                    "Deine Antwort soll nur die Dosierform enthalten!"
                )
            },
            "dose_and_rate": {
                "question": (
                    "Suche im Text wie viele Tabletten/Einheiten pro Einnahme im Normalfall eingenommen werden. "
                    "Deine Antwort soll nur die Zahl enthalten! "
                )
            },
            "max_dose_per_intake": {
                "question": (
                    "Suche im Text wie viele Tabletten/Einheiten maximal auf einmal eingenommen werden dürfen. "
                    "Deine Antwort soll nur die Anzahl (als Zahl) enthalten. "
                )
            },
            "max_dose_per_period": {
                "question": (
                    "Suche im Text wie viele Tabletten/Einheiten maximal pro Tag eingenommen werden dürfen. "
                    "Deine Antwort soll nur die Anzahl (als Zahl) enthalten. Ist kein Hinweis zu finden antworte mit None. "
                )
            },
        }
    },
    "storage_guideline": {
        "question": (
            "Suche im Beipackzettel nach Hinweisen und Anweisungen zur Aufbewahrung des Medikaments. "
            "Deine Antwort soll alle Hinweise zur Aufbewahrung inkl. Verfallsdatum beinhalten. "
            "Deine Antwort soll nur die Anweisungen zur Aufbewahrung und Hinweise zum Verfallsdatum beinhalten"
        )
    },
    "characteristics": {
        "question": (
            "Suche im Beipackzettel nach dem Abschnitt in dem das Aussehen des Medikaments beschrieben ist. "
            "Deine Antwort soll nur das beschriebenen Aussehen beinhalten. "
            "Findest du nichts so antworte mit None."
        )
    }
}

questions_undesirable_effects = {
    "undesirable_effects": (
        "Suche im Beipackzettel nach den Abschnitt in dem die möglichen Nebenwirkungen beschrieben sind. "
        "Zähle alle Nebenwirkungen kategorisiert nach Häufigkeiten, inklusive wie viele Betroffen sind, auf. "
        "Wenn keine Zahl zu den Häufigkeiten angegeben ist, lasse diese Information aus. "
        "Formatiere deine Antwort folgend: Häufigkeit_A (Betroffene): Aufzählung1 | Aufzählung2; HäufigkeitB (Betroffene): Aufzählung3 | usw. "
        "Nenne nur die Häufigkeitskategorien die auch im Beipackzettel beschrieben sind. "
        "Deine Antwort soll nur die Liste mit den Häufigkeiten und den Nebenwirkungen beinhalten! "
    )
}

questions_icw = {
    "precautious": {
        "question": (
                "Suche im Beipackzettel das Kapitel was vor der Einnhame des Medikaments zu beachten ist. " 
                "Dieses Kapitel beinhaltet Informationen wann das Medikament nicht eingenommen werden darf, "
                "Warnhinweise und Vorsichtsmaßnahmen, Informationen zu Wechselwirkungen mit anderen Medikamenten, und weitere Hinweise und Warnungen "
                "Kopiere das gesamte Kapitel inklusive der Abschnittsüberschriften in deine Antwort. "
        ),
        "following": {
            "interaction_medications": {
                "question":  (
                    "Suche im Text den gesamten Abschnitt in dem die Einnahme zusammen mit anderen Medikamenten (Wechselwirkungen) beschrieben sind.  "
                    "Nenne alle beschriebenen Wechselwirkungen oder Hinweise zu Wechselwirkungen mit anderen Medikamenten die im Abschnitt vorkommen und "
                    "trenne die einzelnen Aufzählungen mit einem | voneinander. "
                    "Es ist wichtig dass du in den einzelnen Einträgen auch die mögliche Wechselwirkung nennst "
                    "sofern dies auch im Beipackzettel ist. "
                    "Deine Antwort soll die vollständige Liste der extrahierten Wechselwirkungen mit anderen Medikamenten beinhalten! "
                    "Stelle sicher, dass die Antwort nur Wechselwirkungen mit anderen Medikamente aber keine anderen Wechselwirkungen beinhaltet! "
                ) 
            },
            "contraindications": {
                "question": (
                    "Suche im Text den Abschnitt 'wann das Medikament nicht eingenommen werden darf'! "
                    "Zähle in deiner Antwort nur die Umstände auf wann das Medikament nicht eingenommen werden darf, ohne eine einleitende Überschrift "
                    "wie 'Medikamentenname darf nicht eingenommen werden ...'"
                    "und trenne die einzelnen Einträge mit einem | voneinander."
                    "Zähle nur die Kontraindiaktion (Informationen aus diesem Kapitel) auf, keine Informationen aus anderen Abschnitten!"
                )  
            },
            "warning_other": {
                "question": (
                    "Suche im Text alle Warnungen/Hinweisen die nach dem Abschnitt zur Einnahme des Medikaments mit anderen Arzneimitteln (den Wechselwirkungen) beschrieben werden. "
                    "Beispiele sind Informationen zur Verkehrstüchtigkeit, Einnahme mit Alkohol, Schwangerschaft, Beeinflussung von Labortests ..."
                    "Diese Warnungen sind meist mit einer eigenen Überschrift versehen "
                    "Deine Antwort sollte wie folgt formatiert sein: Überschrift, Inhalt| Überschrift2, Inhalt2| usw. "
                    "Stelle sicher dass du Hinweise zu Wechselwirkungen mit anderen Medikamenten von deiner Antwort ausschliesst. "
                    "Stelle sicher keine Warnungen zu nennen die im Abschnitt 'Warnhinweise und Vorsichtsmaßnahmen' vorkommen"
                )
            },
            "hints" : {
                "question": (
                    "Suche im Text den Abschnitt 'Warnhinweise und Vorsichtsmaßnahmen' das Kapitel endet sobald  "
                    "die Einnahme mit anderen Medikamenten beschrieben wird. "
                    "Der Abschnitt beinhaltet Anweisungen welche Informationen mit einem Arzt abgeklärt werden muss und was während der Einnhame zu beachten ist"
                    "Diese Hinweise können einzelen stehen oder mehrere Aufzählungen enthalten. "
                    "Schreibe die einzelnen Anweisungen und die Anweisungen mit Aufzählungen in eine Liste und trenne unabhängige Anweisungen mit einem | voneinander "
                    "Stelle sicher ausschließlich die Warnungen aus dem Kapitel 'Warnhinweise und Vorsichtsmaßnahmen' aufzuzählen und keine Warnungen aus anderen Abschnitten "
                )
            }
        }
    }
}