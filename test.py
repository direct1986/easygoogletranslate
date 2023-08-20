from easygoogletranslate import EasyGoogleTranslate

translator = EasyGoogleTranslate(
    source_language='ko',
    target_language='zh-CN',
    timeout=10
)
result = translator.translate('소브산 부적합[결과 : 0.0148g/kg 검출/ 규격: 불검출]')

print(result) 
# Output: Dies ist ein Beispiel.
