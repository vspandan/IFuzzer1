var locales = [ "af" , "af-NA" , "af-ZA" , "ar" , "ar-001" , "ar-AE" , "ar-BH" , "ar-DJ" , "ar-DZ" , "ar-EG" , "ar-EH" , "ar-ER" , "ar-IL" , "ar-IQ" , "ar-JO" , "ar-KM" , "ar-KW" , "ar-LB" , "ar-LY" , "ar-MA" , "ar-MR" , "ar-OM" , "ar-PS" , "ar-QA" , "ar-SA" , "ar-SD" , "ar-SO" , "ar-SY" , "ar-TD" , "ar-TN" , "ar-YE" , "as" , "as-IN" , "be" , "be-BY" , "bg" , "bg-BG" , "bn" , "bn-BD" , "bn-IN" , "bs" , "bs-Cyrl" , "bs-Cyrl-BA" , "bs-Latn" , "bs-Latn-BA" , "ca" , "ca-AD" , "ca-ES" , "cs" , "cs-CZ" , "cy" , "cy-GB" , "da" , "da-DK" , "de" , "de-AT" , "de-BE" , "de-CH" , "de-DE" , "de-LI" , "de-LU" , "el" , "el-CY" , "el-GR" , "en" , "en-150" , "en-AG" , "en-AS" , "en-AU" , "en-BB" , "en-BE" , "en-BM" , "en-BS" , "en-BW" , "en-BZ" , "en-CA" , "en-CM" , "en-DM" , "en-FJ" , "en-FM" , "en-GB" , "en-GD" , "en-GG" , "en-GH" , "en-GI" , "en-GM" , "en-GU" , "en-HK" , "en-IE" , "en-IM" , 1999 , "en-JE" , "en-JM" , "en-KE" , "en-KI" , "en-KN" , "en-KY" , "en-LC" , "en-LR" , "en-LS" , "en-MG" , "en-MH" , "en-MP" , "en-MT" , "en-MU" , "en-MW" , "en-NA" , "en-NG" , "en-NZ" , "en-PG" , "en-PH" , "en-PK" , "en-PR" , "en-PW" , "en-SB" , "en-SC" , "en-SG" , "en-SL" , "en-SS" , "en-TC" , "en-TO" , "en-TT" , "en-TZ" , "en-UG" , "en-UM" , "en-US" , "en-US-POSIX" , "en-VC" , "en-VG" , "en-VI" , "en-VU" , "en-WS" , "en-ZA" , "en-ZM" , "en-ZW" , "eo" , "es" , "es-419" , "es-AR" , "es-BO" , "es-CL" , "es-CO" , "es-CR" , "es-CU" , "es-DO" , "es-EA" , "es-EC" , "es-ES" , "es-GQ" , "es-GT" , "es-HN" , "es-IC" , "es-MX" , "es-NI" , "es-PA" , "es-PE" , "es-PH" , "es-PR" , "es-PY" , "es-SV" , "es-US" , "es-UY" , "es-VE" , "et" , "et-EE" , "fa" , "fa-AF" , "fa-IR" , "fi" , "fi-FI" , "fr" , "fr-BE" , "fr-BF" , "fr-BI" , "fr-BJ" , "fr-BL" , "fr-CA" , "fr-CD" , "fr-CF" , "fr-CG" , "fr-CH" , "fr-CI" , "fr-CM" , "fr-DJ" , "fr-DZ" , "fr-FR" , "fr-GA" , "fr-GN" , "fr-GP" , "fr-GQ" , "fr-HT" , "fr-KM" , "fr-LU" , "fr-MA" , "fr-MC" , "fr-MF" , "fr-MG" , "fr-ML" , "fr-MQ" , "fr-MR" , "fr-MU" , "fr-NC" , "fr-NE" , "fr-PF" , "fr-RE" , "fr-RW" , "fr-SC" , "fr-SN" , "fr-SY" , "fr-TD" , "fr-TG" , "fr-TN" , "fr-VU" , "ga" , "ga-IE" , "gu" , "gu-IN" , "he" , "he-IL" , "hi" , "hi-IN" , "hr" , "hr-BA" , "hr-HR" , "hu" , "hu-HU" , "hy" , "hy-AM" , "id" , "id-ID" , "is" , "is-IS" , "it" , "it-CH" , "it-IT" , "it-SM" , "ja" , "ja-JP" , "kk" , "kk-KZ" , "km" , "km-KH" , "kn" , "kn-IN" , "ko" , "ko-KP" , "ko-KR" , "lt" , "lt-LT" , "lv" , "lv-LV" , "mk" , "mk-MK" , "ml" , "ml-IN" , "mr" , "mr-IN" , "nb" , "nb-NO" , "nl" , "nl-AW" , "nl-BE" , "nl-CW" , "nl-NL" , "nl-SR" , "nl-SX" , "nn" , "nn-NO" , "or" , "or-IN" , "pa" , "pa-Arab" , "pa-Arab-PK" , "pa-Guru" , "pa-Guru-IN" , "pl" , "pl-PL" , "pt" , "pt-AO" , "pt-BR" , "pt-CV" , "pt-GW" , "pt-MO" , "pt-MZ" , "pt-PT" , "pt-ST" , "pt-TL" , "ro" , "ro-MD" , "ro-RO" , "ru" , "ru-BY" , "ru-KG" , "ru-KZ" , "ru-MD" , "ru-RU" , "ru-UA" , "si" , "si-LK" , "sk" , "sk-SK" , "sl" , "sl-SI" , "sq" , "sq-AL" , "sq-MK" , "sr" , "sr-Cyrl" , "sr-Cyrl-BA" , "sr-Cyrl-ME" , "sr-Cyrl-RS" , "sr-Latn" , "sr-Latn-BA" , "sr-Latn-ME" , "sr-Latn-RS" , "sv" , "sv-AX" , "sv-FI" , "sv-SE" , "te" , "te-IN" , "th" , "th-TH" , "tr" , "tr-CY" , "tr-TR" , "uk" , "uk-UA" , "vi" , "vi-VN" , "zh" , "zh-Hans" , "zh-Hans-CN" , "zh-Hans-SG" , "zh-Hant" , "zh-Hant-HK" , "zh-Hant-MO" , "zh-Hant-TW" , ] ; var count = Intl . Collator . supportedLocalesOf ( locales ) . length ; reportCompare ( locales . length , count , "Number of supported locales in Intl.Collator" ) ;